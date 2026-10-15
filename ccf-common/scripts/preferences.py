#!/usr/bin/env python3
"""Resolve CCFA preferences or serve the optional, local-only configurator.

Python standard library only. Reads never create files. Persistent preferences
live outside installed skills; project preferences require an explicit root.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import copy
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import os
from pathlib import Path
import secrets
import sys
import tempfile
import threading
import time
from urllib.parse import parse_qs, unquote, urlsplit
import webbrowser


MAX_BYTES = 64 * 1024
DEFAULTS = {
    "version": 1,
    "preferences": {
        "independent_review": "off",
        "extended_search": "auto",
        "enhanced_document_parsing": "auto",
        "figure_variants": "off",
        "detailed_reports": "off",
        "alternative_routes": "off",
        "maintenance_evolution": "off",
    },
    "ui": {"language": "zh-CN", "theme": "system"},
}
MODES = {"off", "auto", "on"}
LANGUAGES = {"zh-CN", "zh-TW", "en"}
THEMES = {"system", "light", "dark"}


class PreferenceError(Exception):
    """A user-readable failure with a stable code for localized clients."""

    def __init__(self, code: str, message: str, status: int = 400):
        super().__init__(message)
        self.code = code
        self.status = status


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def decode_json(data: bytes):
    if len(data) > MAX_BYTES:
        raise PreferenceError("request_too_large", "JSON exceeds the 64 KiB limit.", 413)
    try:
        decoded = json.loads(
            data.decode("utf-8-sig"),
            object_pairs_hook=_unique_object,
            parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)),
        )
        # JSON permits escaped lone surrogates; reject those before they can
        # break UTF-8 response serialization (including in an error message).
        pending = [(decoded, 0)]
        while pending:
            value, depth = pending.pop()
            if depth > 32:
                raise ValueError("JSON nesting exceeds the configuration limit")
            if isinstance(value, str):
                value.encode("utf-8")
            elif isinstance(value, dict):
                pending.extend((item, depth + 1) for item in value.keys())
                pending.extend((item, depth + 1) for item in value.values())
            elif isinstance(value, list):
                pending.extend((item, depth + 1) for item in value)
        return decoded
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise PreferenceError("invalid_json", "Expected UTF-8 JSON without duplicate keys.") from exc


def validate_config(config):
    if type(config) is not dict:
        raise PreferenceError("invalid_config", "Configuration must be a JSON object.")
    if set(config) - {"version", "preferences", "ui"}:
        raise PreferenceError("invalid_config", "Unknown top-level configuration field.")
    if type(config.get("version")) is not int or config["version"] != 1:
        raise PreferenceError("invalid_config", "Configuration version must be the integer 1.")
    for section in ("preferences", "ui"):
        values = config.get(section, {})
        if type(values) is not dict:
            raise PreferenceError("invalid_config", section + " must be an object.")
        for key, value in values.items():
            if key not in DEFAULTS[section]:
                raise PreferenceError("invalid_config", "Unknown field: " + section + "." + key)
            allowed = MODES if section == "preferences" else (LANGUAGES if key == "language" else THEMES)
            if type(value) is not str or value not in allowed:
                raise PreferenceError("invalid_config", "Unsupported value for " + section + "." + key)
    return copy.deepcopy(config)


def _apply(effective, origins, config, scope):
    if config is not None:
        for section in ("preferences", "ui"):
            for key, value in config.get(section, {}).items():
                effective[section][key] = value
                origins[section][key] = scope


def _initial():
    return copy.deepcopy(DEFAULTS), {
        section: {key: "default" for key in DEFAULTS[section]}
        for section in ("preferences", "ui")
    }


def user_config_path() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    base = Path(codex_home).expanduser() if codex_home else Path.home() / ".codex"
    return base / "ccfa" / "preferences.json"


class PreferenceStore:
    def __init__(self, user_path: Path | None = None, project_root: Path | None = None):
        self.paths = {"user": Path(user_path) if user_path is not None else user_config_path()}
        if project_root is not None:
            self.paths["project"] = Path(project_root).expanduser().resolve() / ".ccfa" / "preferences.json"
        self.lock = threading.RLock()

    def _path(self, scope):
        if scope not in ("user", "project"):
            raise PreferenceError("invalid_scope", "Scope must be user or project.")
        if scope not in self.paths:
            raise PreferenceError("scope_unavailable", "Start with --project to use project preferences.")
        return self.paths[scope]

    def _read(self, scope):
        path = self._path(scope)
        try:
            with path.open("rb") as stream:
                data = stream.read(MAX_BYTES + 1)
        except FileNotFoundError:
            return None, "missing"
        except OSError as exc:
            raise PreferenceError("storage_error", "Cannot read " + str(path) + ": " + str(exc), 500) from exc
        try:
            config = validate_config(decode_json(data))
        except PreferenceError as exc:
            raise PreferenceError(
                "malformed_stored_config", "Invalid stored configuration at " + str(path) + ": " + str(exc), 422
            ) from exc
        return config, hashlib.sha256(data).hexdigest()

    def _snapshot(self, scope):
        self._path(scope)
        effective, origins = _initial()
        inherited = copy.deepcopy(effective)
        stored = None
        revision = "missing"
        for layer in ("user", "project"):
            if layer not in self.paths:
                continue
            config, current_revision = self._read(layer)
            if layer == scope:
                inherited = copy.deepcopy(effective)
                stored, revision = config, current_revision
            _apply(effective, origins, config, layer)
            if layer == scope:
                break
        return {
            "version": 1,
            "scope": scope,
            "availableScopes": list(self.paths),
            "stored": stored,
            "effective": effective,
            "inherited": inherited,
            "origins": origins,
            "revision": revision,
            "defaults": copy.deepcopy(DEFAULTS),
        }

    def snapshot(self, scope="user"):
        with self.lock:
            return self._snapshot(scope)

    def resolve(self):
        state = self.snapshot("project" if "project" in self.paths else "user")
        return {"effective": state["effective"], "origins": state["origins"], "warnings": []}

    @contextmanager
    def _file_lock(self, path):
        # An exclusive sidecar coordinates different configurator processes as
        # well as threads. Do not delete another process's lock on a timeout.
        lock_path = path.with_name(".preferences.lock")
        deadline = time.monotonic() + 2
        while True:
            try:
                descriptor = os.open(lock_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                break
            except FileExistsError:
                if time.monotonic() >= deadline:
                    raise PreferenceError(
                        "storage_error",
                        "Preferences are locked by another save. Retry after it finishes. "
                        "If no configurator is running, inspect and remove the stale lock at " + str(lock_path) + ".",
                        409,
                    )
                time.sleep(0.025)
        try:
            os.close(descriptor)
            yield
        finally:
            lock_path.unlink(missing_ok=True)

    def save(self, scope, revision, config):
        path = self._path(scope)
        config = validate_config(config)
        if type(revision) is not str or not (revision == "missing" or (
            len(revision) == 64 and all(char in "0123456789abcdef" for char in revision)
        )):
            raise PreferenceError("invalid_config", "A valid revision from the last read is required.")
        encoded = (json.dumps(config, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        with self.lock:
            try:
                path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
                with self._file_lock(path):
                    # Read and validate ALL inherited inputs before committing.
                    # Corrupt existing files are never silently overwritten.
                    current = self._snapshot(scope)
                    if current["revision"] != revision:
                        raise PreferenceError("revision_conflict", "Preferences changed since this page loaded. Reload before saving.", 409)
                    temporary = None
                    try:
                        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".preferences-", suffix=".tmp", delete=False) as stream:
                            temporary = Path(stream.name)
                            stream.write(encoded)
                            stream.flush()
                            os.fsync(stream.fileno())
                        os.replace(temporary, path)
                    finally:
                        if temporary is not None:
                            temporary.unlink(missing_ok=True)
                    return self._snapshot(scope)
            except PreferenceError:
                raise
            except OSError as exc:
                raise PreferenceError("storage_error", "Cannot save preferences: " + str(exc), 500) from exc


class ConfigServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, store: PreferenceStore, port=0, ui_root: Path | None = None, token=None):
        self.store = store
        self.ui_root = (ui_root or Path(__file__).resolve().parents[1] / "assets" / "configurator").resolve()
        self.token = token or secrets.token_urlsafe(32)
        super().__init__(("127.0.0.1", port), ConfigHandler)
        self.authority = "127.0.0.1:" + str(self.server_port)
        self.origin = "http://" + self.authority


class ConfigHandler(BaseHTTPRequestHandler):
    server_version = "CCFA-Local"

    def setup(self):
        super().setup()
        self.connection.settimeout(5)

    def log_message(self, format, *args):
        # In particular, do not log auth headers or configuration contents.
        return

    def _respond(self, status, body: bytes, content_type, head=False):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        if not head:
            self.wfile.write(body)

    def _json(self, status, value):
        body = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self._respond(status, body, "application/json; charset=utf-8")

    def _check_request(self, authenticated=False):
        if self.headers.get_all("Host", []) != [self.server.authority]:
            raise PreferenceError("bad_host", "Only the configurator's loopback host is accepted.", 403)
        origins = self.headers.get_all("Origin", [])
        if origins and origins != [self.server.origin]:
            raise PreferenceError("bad_origin", "Cross-origin requests are not accepted.", 403)
        if authenticated:
            tokens = self.headers.get_all("X-CCFA-Token", [])
            if len(tokens) != 1 or not secrets.compare_digest(tokens[0].encode("utf-8"), self.server.token.encode("utf-8")):
                raise PreferenceError("unauthorized", "Open the launch URL to authenticate this browser session.", 401)

    def _get(self, head=False):
        self._check_request()
        try:
            parsed = urlsplit(self.path)
        except ValueError as exc:
            raise PreferenceError("not_found", "Unknown path.", 404) from exc
        if parsed.scheme or parsed.netloc:
            raise PreferenceError("not_found", "Unknown path.", 404)
        if parsed.path == "/api/preferences":
            self._check_request(authenticated=True)
            if head:
                raise PreferenceError("method_not_allowed", "Use GET or POST for preferences.", 405)
            try:
                params = parse_qs(parsed.query, keep_blank_values=True, max_num_fields=8)
            except ValueError as exc:
                raise PreferenceError("invalid_scope", "Invalid scope query.") from exc
            if set(params) - {"scope"} or len(params.get("scope", ["user"])) != 1:
                raise PreferenceError("invalid_scope", "Supply exactly one scope.")
            self._json(200, self.server.store.snapshot(params.get("scope", ["user"])[0]))
            return
        try:
            relative = unquote(parsed.path, errors="strict").lstrip("/") or "index.html"
            if "\\" in relative or "\x00" in relative:
                raise ValueError("Invalid path")
            candidate = (self.server.ui_root / relative).resolve()
            if not candidate.is_relative_to(self.server.ui_root):
                raise ValueError("Outside UI directory")
            if candidate.suffix.lower() not in {".html", ".css", ".js", ".svg", ".png", ".ico", ".woff2"}:
                raise ValueError("Not a UI asset")
            body = candidate.read_bytes()
        except (OSError, ValueError, UnicodeError) as exc:
            raise PreferenceError("not_found", "UI asset not found.", 404) from exc
        content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        if candidate.suffix.lower() in {".html", ".css", ".js", ".svg"}:
            content_type += "; charset=utf-8"
        self._respond(200, body, content_type, head=head)

    def _post(self):
        self._check_request(authenticated=True)
        if self.path != "/api/preferences":
            raise PreferenceError("not_found", "Unknown API path.", 404)
        content_types = self.headers.get_all("Content-Type", [])
        if len(content_types) != 1 or content_types[0].split(";", 1)[0].strip().lower() != "application/json":
            raise PreferenceError("bad_content_type", "Content-Type must be application/json.", 415)
        lengths = self.headers.get_all("Content-Length", [])
        if self.headers.get_all("Transfer-Encoding", []) or len(lengths) != 1:
            raise PreferenceError("invalid_json", "One Content-Length and no transfer encoding are required.")
        try:
            size = int(lengths[0])
        except ValueError as exc:
            raise PreferenceError("invalid_json", "Invalid Content-Length.") from exc
        if size < 0 or size > MAX_BYTES:
            raise PreferenceError("request_too_large", "Request exceeds the 64 KiB limit.", 413)
        try:
            body = self.rfile.read(size)
        except OSError as exc:
            raise PreferenceError("invalid_json", "Request body was not received in time.", 408) from exc
        if len(body) != size:
            raise PreferenceError("invalid_json", "Incomplete request body.")
        request = decode_json(body)
        if type(request) is not dict or set(request) != {"scope", "revision", "config"}:
            raise PreferenceError("invalid_config", "Expected scope, revision, and config only.")
        if type(request["scope"]) is not str:
            raise PreferenceError("invalid_scope", "Scope must be user or project.")
        self._json(200, self.server.store.save(request["scope"], request["revision"], request["config"]))

    def _handle(self, action):
        try:
            action()
        except PreferenceError as exc:
            self._json(exc.status, {"error": str(exc), "code": exc.code})
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self):
        self._handle(self._get)

    def do_HEAD(self):
        self._handle(lambda: self._get(head=True))

    def do_POST(self):
        self._handle(self._post)

    def _unsupported(self):
        self._handle(lambda: self._reject_method())

    def _reject_method(self):
        self._check_request()
        raise PreferenceError("method_not_allowed", "Use GET or POST.", 405)

    do_PUT = do_DELETE = do_PATCH = do_OPTIONS = _unsupported


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    resolve_parser = commands.add_parser("resolve", help="Read effective preferences without creating files")
    resolve_parser.add_argument("--project", type=Path, help="Explicit project root; never inferred from the working directory")
    resolve_parser.add_argument("--details", action="store_true", help="Include value origins and warnings")
    serve_parser = commands.add_parser("serve", help="Launch the optional local configurator")
    serve_parser.add_argument("--project", type=Path, help="Enable project-scoped settings for this explicit root")
    serve_parser.add_argument("--port", type=int, default=0, help="Loopback port, or 0 to select an available port")
    serve_parser.add_argument("--no-browser", action="store_true", help="Print the URL without opening a browser")
    args = parser.parse_args(argv)
    # UTF-8 also works when redirected from legacy Windows console code pages.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    try:
        store = PreferenceStore(project_root=args.project)
        if args.command == "resolve":
            state = store.resolve()
            print(json.dumps(state if args.details else state["effective"], ensure_ascii=False, separators=(",", ":")))
            return 0
        if not 0 <= args.port <= 65535:
            raise PreferenceError("invalid_config", "Port must be between 0 and 65535.")
        with ConfigServer(store, port=args.port) as server:
            url = server.origin + "/#token=" + server.token
            print(url, flush=True)
            if not args.no_browser:
                webbrowser.open(url, new=2)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
        return 0
    except (PreferenceError, OSError) as exc:
        print(json.dumps({"error": str(exc), "code": getattr(exc, "code", "storage_error")}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
