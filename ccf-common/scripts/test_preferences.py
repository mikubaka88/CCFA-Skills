#!/usr/bin/env python3
"""Behavior and local HTTP boundary tests; never touch real user preferences."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import http.client
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest import mock

import preferences as prefs


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ccfa-preferences-test-")
        self.root = Path(self.temp.name)
        self.user_path = self.root / "用户偏好" / "ccfa" / "preferences.json"
        self.project = self.root / "论文项目"
        self.store = prefs.PreferenceStore(self.user_path, self.project)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, scope, config):
        path = self.store.paths[scope]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")

    def assert_error(self, code, function, *args):
        with self.assertRaises(prefs.PreferenceError) as caught:
            function(*args)
        self.assertEqual(caught.exception.code, code)

    def test_read_defaults_does_not_create_files(self):
        before = list(self.root.rglob("*"))
        self.assertEqual(self.store.resolve()["effective"], prefs.DEFAULTS)
        self.assertEqual(self.store.snapshot("project")["stored"], None)
        self.assertEqual(self.store.snapshot("user")["revision"], "missing")
        self.assertEqual(list(self.root.rglob("*")), before)

    def test_sparse_layer_precedence_and_ui(self):
        self.write("user", {"version": 1, "preferences": {"independent_review": "on", "extended_search": "off"}, "ui": {"language": "zh-TW"}})
        self.write("project", {"version": 1, "preferences": {"independent_review": "auto"}, "ui": {"theme": "dark"}})
        result = self.store.resolve()
        self.assertEqual(result["effective"]["preferences"]["independent_review"], "auto")
        self.assertEqual(result["effective"]["preferences"]["extended_search"], "off")
        self.assertEqual(result["effective"]["preferences"]["figure_variants"], "off")
        self.assertEqual(result["effective"]["ui"], {"language": "zh-TW", "theme": "dark"})
        self.assertEqual(result["origins"]["preferences"]["independent_review"], "project")
        self.assertEqual(result["origins"]["preferences"]["extended_search"], "user")
        self.assertEqual(result["origins"]["preferences"]["figure_variants"], "default")

    def test_legacy_version_one_omissions_inherit_off_without_rewriting(self):
        legacy = {"version": 1, "preferences": {"independent_review": "on"}, "ui": {"language": "en"}}
        self.write("user", legacy)
        before = self.user_path.read_bytes()
        resolved = self.store.resolve()
        for key in ("alternative_routes", "maintenance_evolution"):
            self.assertEqual(resolved["effective"]["preferences"][key], "off")
            self.assertEqual(resolved["origins"]["preferences"][key], "default")
        self.assertEqual(self.store.snapshot("user")["stored"], legacy)
        self.assertEqual(self.user_path.read_bytes(), before)
        self.assertFalse(self.project.exists())

    def test_route_and_maintenance_preferences_roundtrip_and_restore_inheritance(self):
        config = {"version": 1, "preferences": {"alternative_routes": "on", "maintenance_evolution": "auto"}}
        self.store.save("user", "missing", config)
        self.assertEqual(self.store.snapshot("user")["stored"], config)
        project = self.store.save("project", "missing", {"version": 1, "preferences": {"alternative_routes": "off"}})
        self.assertEqual(project["effective"]["preferences"]["alternative_routes"], "off")
        self.assertEqual(project["effective"]["preferences"]["maintenance_evolution"], "auto")
        restored = self.store.save("project", project["revision"], {"version": 1})
        self.assertEqual(restored["effective"]["preferences"]["alternative_routes"], "on")
        self.assertEqual(restored["origins"]["preferences"]["alternative_routes"], "user")
        self.assertEqual(json.loads(self.store.paths["project"].read_text(encoding="utf-8")), {"version": 1})

    def test_selected_scope_and_inherited_baseline(self):
        self.write("user", {"version": 1, "preferences": {"figure_variants": "on"}})
        self.write("project", {"version": 1, "preferences": {"figure_variants": "off"}})
        user = self.store.snapshot("user")
        project = self.store.snapshot("project")
        self.assertEqual(user["effective"]["preferences"]["figure_variants"], "on")
        self.assertEqual(user["inherited"], prefs.DEFAULTS)
        self.assertEqual(project["inherited"], user["effective"])
        self.assertEqual(project["effective"]["preferences"]["figure_variants"], "off")

    def test_no_implicit_project_discovery(self):
        self.write("project", {"version": 1, "preferences": {"independent_review": "on"}})
        user_only = prefs.PreferenceStore(self.user_path)
        self.assertEqual(user_only.resolve()["effective"], prefs.DEFAULTS)
        self.assert_error("scope_unavailable", user_only.snapshot, "project")
        self.assert_error("scope_unavailable", user_only.save, "project", "missing", {"version": 1})

    def test_strict_config_validation(self):
        invalid = [
            None, [], {}, {"version": True}, {"version": 1.0}, {"version": 2},
            {"version": 1, "path": "somewhere"}, {"version": 1, "preferences": []},
            {"version": 1, "preferences": {"new_mode": "on"}},
            {"version": 1, "preferences": {"independent_review": True}},
            {"version": 1, "preferences": {"independent_review": ["on"]}},
            {"version": 1, "preferences": {"extended_search": "sometimes"}},
            {"version": 1, "ui": {"language": "fr"}},
            {"version": 1, "ui": {"theme": "auto"}},
            {"version": 1, "ui": {"unknown": "system"}},
        ]
        for config in invalid:
            with self.subTest(config=config):
                self.assert_error("invalid_config", prefs.validate_config, config)
        self.assertEqual(prefs.validate_config({"version": 1}), {"version": 1})

    def test_invalid_utf8_duplicate_keys_and_nonfinite_json(self):
        for raw in (b'{"version":1,"version":1}', b'{"ui":{"theme":"dark","theme":"light"}}', b'\xff', b'{"version":NaN}', b'{"version":1,"ui":{"\\ud800":"light"}}', b"[" * 2000 + b"]" * 2000):
            with self.subTest(raw=raw):
                self.assert_error("invalid_json", prefs.decode_json, raw)
        self.assert_error("request_too_large", prefs.decode_json, b" " * (prefs.MAX_BYTES + 1))

    def test_utf8_bom_file_loads_and_saves_without_bom(self):
        original = {"version": 1, "ui": {"language": "zh-TW"}}
        self.user_path.parent.mkdir(parents=True)
        self.user_path.write_text(json.dumps(original), encoding="utf-8-sig")
        loaded = self.store.snapshot()
        self.assertEqual(loaded["stored"], original)
        saved = self.store.save("user", loaded["revision"], original)
        self.assertEqual(saved["stored"], original)
        self.assertFalse(self.user_path.read_bytes().startswith(b"\xef\xbb\xbf"))

    def test_broken_stored_file_is_diagnosed_not_overwritten(self):
        self.user_path.parent.mkdir(parents=True)
        broken = b'{"version":1,"preferences":'
        self.user_path.write_bytes(broken)
        self.assert_error("malformed_stored_config", self.store.resolve)
        self.assert_error("malformed_stored_config", self.store.save, "user", hashlib.sha256(broken).hexdigest(), {"version": 1})
        self.assertEqual(self.user_path.read_bytes(), broken)

    def test_oversize_stored_file_is_bounded(self):
        self.user_path.parent.mkdir(parents=True)
        self.user_path.write_bytes(b" " * (prefs.MAX_BYTES + 1))
        self.assert_error("malformed_stored_config", self.store.resolve)

    def test_directory_at_config_path_reports_storage_error(self):
        self.user_path.mkdir(parents=True)
        self.assert_error("storage_error", self.store.resolve)
        self.assert_error("storage_error", self.store.save, "user", "missing", {"version": 1})

    def test_sparse_save_utf8_path_and_no_temporary_files_left(self):
        config = {"version": 1, "ui": {"language": "zh-CN"}}
        state = self.store.save("user", "missing", config)
        self.assertEqual(state["stored"], config)
        self.assertEqual(json.loads(self.user_path.read_text(encoding="utf-8")), config)
        self.assertEqual(list(self.user_path.parent.iterdir()), [self.user_path])
        self.assertNotEqual(state["revision"], "missing")
        self.assertFalse(self.project.exists())

    def test_stale_revision_protects_existing_contents(self):
        self.store.save("user", "missing", {"version": 1, "ui": {"theme": "dark"}})
        self.assert_error("revision_conflict", self.store.save, "user", "missing", {"version": 1})
        self.assertEqual(self.store.snapshot()["stored"]["ui"]["theme"], "dark")

    def test_project_save_uses_fresh_inheritance_without_persisting_it(self):
        project_revision = self.store.snapshot("project")["revision"]
        self.store.save("user", "missing", {"version": 1, "preferences": {"independent_review": "on"}})
        state = self.store.save("project", project_revision, {"version": 1, "ui": {"theme": "light"}})
        self.assertEqual(state["effective"]["preferences"]["independent_review"], "on")
        self.assertNotIn("preferences", state["stored"])

    def test_atomic_replace_failure_preserves_previous_file(self):
        state = self.store.save("user", "missing", {"version": 1})
        before = self.user_path.read_bytes()
        with mock.patch.object(prefs.os, "replace", side_effect=OSError("simulated failure")):
            self.assert_error("storage_error", self.store.save, "user", state["revision"], {"version": 1, "ui": {"theme": "dark"}})
        self.assertEqual(self.user_path.read_bytes(), before)
        self.assertEqual(list(self.user_path.parent.iterdir()), [self.user_path])

    def test_parallel_store_instances_cannot_silently_overwrite(self):
        first = prefs.PreferenceStore(self.user_path)
        second = prefs.PreferenceStore(self.user_path)
        barrier = threading.Barrier(2)

        def save(store, theme):
            barrier.wait()
            try:
                store.save("user", "missing", {"version": 1, "ui": {"theme": theme}})
                return "saved"
            except prefs.PreferenceError as exc:
                return exc.code

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(save, first, "dark"), pool.submit(save, second, "light")]
            self.assertCountEqual([future.result() for future in futures], ["saved", "revision_conflict"])

    def test_defaults_are_not_shared_mutable_state(self):
        state = self.store.snapshot()
        state["defaults"]["ui"]["theme"] = "dark"
        state["effective"]["ui"]["theme"] = "light"
        self.assertEqual(self.store.snapshot()["effective"]["ui"]["theme"], "system")

    def test_cli_resolve_is_compact_read_only_and_supports_explicit_project(self):
        environment = dict(os.environ, CODEX_HOME=str(self.root / "隔离配置"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, str(Path(prefs.__file__)), "resolve", "--project", str(self.project)]
        result = subprocess.run(command, env=environment, capture_output=True, encoding="utf-8", check=True)
        self.assertEqual(json.loads(result.stdout), prefs.DEFAULTS)
        self.assertEqual(len(result.stdout.strip().splitlines()), 1)
        self.assertFalse((self.root / "隔离配置").exists())
        self.assertFalse(self.project.exists())


class HttpTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ccfa-http-test-")
        self.root = Path(self.temp.name)
        self.ui = self.root / "ui"
        self.ui.mkdir()
        (self.ui / "index.html").write_text("<!doctype html><title>简中 繁中 EN</title>", encoding="utf-8")
        (self.root / "private.html").write_text("private", encoding="utf-8")
        self.store = prefs.PreferenceStore(self.root / "user" / "preferences.json", self.root / "project")
        self.server = prefs.ConfigServer(self.store, ui_root=self.ui, token="test-session-token")
        self.thread = threading.Thread(target=self.server.serve_forever, kwargs={"poll_interval": 0.01}, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)
        self.temp.cleanup()

    def request(self, method="GET", path="/api/preferences?scope=user", payload=None, headers=None, auth=True):
        request_headers = {"X-CCFA-Token": self.server.token} if auth else {}
        if payload is not None:
            request_headers["Content-Type"] = "application/json"
        request_headers.update(headers or {})
        body = json.dumps(payload).encode("utf-8") if isinstance(payload, dict) else payload
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=3)
        try:
            connection.request(method, path, body=body, headers=request_headers)
            response = connection.getresponse()
            data = response.read()
            parsed = json.loads(data) if response.getheader("Content-Type", "").startswith("application/json") else data.decode("utf-8")
            return response.status, parsed, dict(response.getheaders())
        finally:
            connection.close()

    def test_local_static_page_and_security_headers(self):
        status, body, headers = self.request(path="/", auth=False)
        self.assertEqual(status, 200)
        self.assertIn("简中 繁中 EN", body)
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(headers["X-Frame-Options"], "DENY")
        self.assertNotIn("Access-Control-Allow-Origin", headers)

    def test_api_authentication_required_for_reads_and_writes(self):
        for method in ("GET", "POST"):
            status, data, _ = self.request(method, path="/api/preferences", auth=False)
            self.assertEqual((status, data["code"]), (401, "unauthorized"))
        status, data, _ = self.request(headers={"X-CCFA-Token": "wrong"})
        self.assertEqual((status, data["code"]), (401, "unauthorized"))
        status, data, _ = self.request(headers={"X-CCFA-Token": "\xe9"})
        self.assertEqual((status, data["code"]), (401, "unauthorized"))
        self.assertFalse(self.store.paths["user"].parent.exists())

    def test_wrong_host_and_cross_origin_rejected_even_with_token(self):
        for headers, expected in [
            ({"Host": "attacker.invalid"}, "bad_host"),
            ({"Origin": "https://attacker.invalid"}, "bad_origin"),
            ({"Origin": "null"}, "bad_origin"),
        ]:
            status, data, _ = self.request(headers=headers)
            self.assertEqual((status, data["code"]), (403, expected))

    def test_get_and_post_contract_preserves_sparse_config(self):
        status, state, _ = self.request()
        self.assertEqual(status, 200)
        self.assertEqual(state["availableScopes"], ["user", "project"])
        self.assertEqual(state["inherited"], prefs.DEFAULTS)
        config = {"version": 1, "preferences": {"detailed_reports": "on", "alternative_routes": "auto", "maintenance_evolution": "on"}}
        status, saved, _ = self.request("POST", "/api/preferences", {"scope": "user", "revision": state["revision"], "config": config}, {"Origin": self.server.origin})
        self.assertEqual(status, 200)
        self.assertEqual(saved["stored"], config)
        self.assertEqual(saved["effective"]["preferences"]["detailed_reports"], "on")
        self.assertEqual(saved["origins"]["preferences"]["detailed_reports"], "user")
        self.assertEqual(saved["effective"]["preferences"]["alternative_routes"], "auto")
        self.assertEqual(saved["effective"]["preferences"]["maintenance_evolution"], "on")
        self.assertEqual(set(saved), {"version", "scope", "availableScopes", "stored", "effective", "inherited", "origins", "revision", "defaults"})

    def test_http_stale_update_and_bad_schema_cannot_overwrite(self):
        payload = {"scope": "user", "revision": "missing", "config": {"version": 1}}
        self.assertEqual(self.request("POST", "/api/preferences", payload)[0], 200)
        status, data, _ = self.request("POST", "/api/preferences", payload)
        self.assertEqual((status, data["code"]), (409, "revision_conflict"))
        payload["path"] = "arbitrary.json"
        self.assertEqual(self.request("POST", "/api/preferences", payload)[1]["code"], "invalid_config")

    def test_content_type_size_and_duplicate_json_boundaries(self):
        cases = [
            (b"{}", {"Content-Type": "text/plain"}, 415, "bad_content_type"),
            (b" " * (prefs.MAX_BYTES + 1), {}, 413, "request_too_large"),
            (b'{"scope":"user","scope":"project"}', {}, 400, "invalid_json"),
            (b"\xff", {}, 400, "invalid_json"),
            (b'{"scope":"user","revision":"missing","config":{"version":1,"ui":{"\\ud800":"light"}}}', {}, 400, "invalid_json"),
            (b"[" * 2000 + b"]" * 2000, {}, 400, "invalid_json"),
        ]
        for body, headers, expected_status, expected_code in cases:
            status, data, _ = self.request("POST", "/api/preferences", body, headers)
            self.assertEqual((status, data["code"]), (expected_status, expected_code))

    def test_path_traversal_and_unexpected_api_paths_rejected(self):
        for path in ("/../private.html", "/%2e%2e/private.html", "/..%5cprivate.html", "/preferences.json", "/api/preferences?scope=user&scope=project"):
            status, _, _ = self.request(path=path)
            self.assertIn(status, (400, 404))
        self.assertEqual(self.request("DELETE", "/api/preferences")[0], 405)

    def test_invalid_scope_and_malformed_stored_file_errors(self):
        self.assertEqual(self.request(path="/api/preferences?scope=global")[1]["code"], "invalid_scope")
        path = self.store.paths["user"]
        path.parent.mkdir(parents=True)
        path.write_bytes(b"not json")
        status, data, _ = self.request()
        self.assertEqual((status, data["code"]), (422, "malformed_stored_config"))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    unittest.main()
