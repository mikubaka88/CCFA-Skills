#!/usr/bin/env python3
"""Real filesystem and command checks for optional temporary-output ownership."""
import json
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from artifact_scope import Scope, main, validate_inventory


class ArtifactScopeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ccfa-artifacts-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.record = "source/artifact-state.json"

    def scope(self):
        return Scope(self.root, self.record)

    def command(self, name="preview.txt", text="figure"):
        return [sys.executable, "-c", "from pathlib import Path; import sys; Path(sys.argv[1]).write_text(sys.argv[2], encoding='utf-8')", str(self.root / name), text]

    def produce(self, name="preview.txt", text="figure"):
        with self.scope().transaction(create=True) as scope:
            self.assertEqual(scope.run([name], self.command(name, text)), 0)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(Path(__file__).with_name("artifact_scope.py")),
                               "--root", str(self.root), *args],
                              capture_output=True, text=True, encoding="utf-8", timeout=15)

    def test_release_preview_and_delete_only_declared_file(self):
        self.produce()
        other = self.root / "important.txt"
        other.write_text("retain", encoding="utf-8")
        with self.scope().transaction() as scope:
            self.assertEqual(scope.clean(True), [])
            scope.release(["preview.txt"], "verified export no longer needs preview")
            self.assertEqual(scope.clean()[0]["action"], "would_delete")
            self.assertTrue((self.root / "preview.txt").exists())
            self.assertEqual(scope.clean(True)[0]["action"], "delete")
            self.assertEqual(scope.clean(True), [])
        self.assertTrue(other.exists())

    def test_existing_file_never_adopted(self):
        (self.root / "preview.txt").write_text("user input", encoding="utf-8")
        with patch("artifact_scope.subprocess.run") as run:
            with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
                self.produce()
            run.assert_not_called()
        self.assertEqual((self.root / "preview.txt").read_text(encoding="utf-8"), "user input")
        self.assertFalse((self.root / self.record).exists())

    def test_changed_file_preserved_after_release(self):
        self.produce()
        with self.scope().transaction() as scope:
            scope.release(["preview.txt"], "done")
        (self.root / "preview.txt").write_text("user change", encoding="utf-8")
        with self.scope().transaction() as scope:
            self.assertEqual(scope.clean(True)[0]["action"], "preserve_changed")

    def test_rebuild_reuses_record_and_revokes_release(self):
        self.produce()
        with self.scope().transaction() as scope:
            scope.release(["preview.txt"], "done")
        self.produce(text="updated")
        with self.scope().transaction() as scope:
            self.assertEqual(len(scope.inventory["files"]), 1)
            self.assertFalse(scope.inventory["files"]["preview.txt"]["released"])
            self.assertEqual(scope.clean(True), [])

    def test_external_edit_before_rebuild_revokes_ownership(self):
        self.produce()
        (self.root / "preview.txt").write_text("user edit", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            self.produce(text="next build")
        self.assertEqual((self.root / "preview.txt").read_text(encoding="utf-8"), "user edit")
        with self.scope().transaction() as scope:
            self.assertEqual(scope.inventory["files"], {})

    def test_failure_keeps_diagnostics_until_released(self):
        with self.scope().transaction(create=True) as scope:
            command = self.command()
            command[2] += "; sys.exit(7)"
            self.assertEqual(scope.run(["preview.txt"], command), 7)
            self.assertEqual(scope.clean(True), [])
            self.assertTrue((self.root / "preview.txt").exists())

    def test_interruption_blocks_cleanup_and_recovery_disowns_outputs(self):
        with self.scope().transaction(create=True) as scope:
            with patch("artifact_scope.subprocess.run", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    scope.run(["preview.txt"], self.command())
        (self.root / "preview.txt").write_text("partial", encoding="utf-8")
        with self.scope().transaction() as scope:
            with self.assertRaises(ValueError):
                scope.clean(True)
            scope.recover()
            self.assertEqual(scope.inventory["files"], {})
        self.assertTrue((self.root / "preview.txt").exists())

    def test_reject_escaping_and_state_paths_before_command(self):
        with self.scope().transaction(create=True) as scope:
            for name in ("../outside.txt", str(self.root / "absolute.txt"), self.record,
                         ".", "NUL", "build/CON.txt", "build/preview.txt:stream",
                         "preview.txt.", "preview.txt ", "C:relative.txt"):
                with self.subTest(name=name), patch("artifact_scope.subprocess.run") as run:
                    with self.assertRaises(ValueError):
                        scope.run([name], self.command())
                    run.assert_not_called()

    def test_lock_rejects_concurrent_writer(self):
        with self.scope().transaction(create=True):
            with self.assertRaises(FileExistsError):
                with self.scope().transaction():
                    pass

    def test_existing_json_and_unicode_round_trip(self):
        self.record = "source/task-state.json"
        state = self.root / self.record
        state.parent.mkdir()
        state.write_text(json.dumps({"goal": "保留原始目标"}, ensure_ascii=False), encoding="utf-8-sig")
        self.produce("预览.txt", "中文内容")
        data = json.loads(state.read_text(encoding="utf-8"))
        self.assertEqual(data["goal"], "保留原始目标")
        self.assertIn("预览.txt", data["file_lifecycle"]["files"])
        self.assertEqual(list(state.parent.glob("*.json")), [state])

    def test_link_and_hardlink_not_managed(self):
        target = self.root / "original.txt"
        target.write_text("retain", encoding="utf-8")
        link = self.root / "preview.txt"
        os.link(target, link)
        with self.scope().transaction(create=True) as scope:
            # Even a forged claim to a hard-linked file must not permit cleanup.
            from artifact_scope import fingerprint
            with self.assertRaises(ValueError):
                fingerprint(link)
        link.unlink()
        try:
            link.symlink_to(target)
        except OSError:
            return  # Windows may not permit creating symlinks without developer mode.
        with self.assertRaises(ValueError):
            self.scope().output("preview.txt")

    def test_duplicate_json_rejected(self):
        state = self.root / self.record
        state.parent.mkdir()
        state.write_text('{"goal":1,"goal":2}', encoding="utf-8")
        with self.assertRaises(ValueError):
            with self.scope().transaction():
                pass

    def test_cli_default_and_stale_lock_recovery(self):
        self.assertEqual(main(["--root", str(self.root), "run", "--temporary", "preview.txt", "--", *self.command()]), 0)
        scope = self.scope()
        process = subprocess.Popen([sys.executable, "-c", "pass"])
        process.wait(timeout=10)
        scope.lock.write_text(str(process.pid), encoding="ascii")
        self.assertEqual(main(["--root", str(self.root), "recover", "--writers-stopped"]), 0)
        self.assertFalse(scope.lock.exists())

    def test_preview_without_record_creates_nothing(self):
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(main(["--root", str(self.root), "clean"]), 0)
        self.assertEqual(json.loads(output.getvalue()), [])
        self.assertEqual(list(self.root.iterdir()), [])

    def test_cli_keeps_inventory_when_continuity_record_appears(self):
        self.assertEqual(self.cli("run", "--temporary", "preview.txt", "--", *self.command()).returncode, 0)
        task = self.root / "source/task-state.json"
        task.write_text('{"goal":"preserve this later continuity record"}', encoding="utf-8")
        before = task.read_bytes()
        released = self.cli("release", "--path", "preview.txt", "--reason", "finished")
        self.assertEqual(released.returncode, 0, released.stderr)
        cleaned = self.cli("clean", "--apply")
        self.assertEqual(cleaned.returncode, 0, cleaned.stderr)
        self.assertEqual(json.loads(cleaned.stdout)[0]["action"], "delete")
        self.assertFalse((self.root / "preview.txt").exists())
        self.assertEqual(task.read_bytes(), before)
        self.assertIn("file_lifecycle", json.loads((self.root / self.record).read_text(encoding="utf-8")))

    def test_cli_two_inventories_require_explicit_record(self):
        self.produce()
        task = Scope(self.root, "source/task-state.json")
        with task.transaction(create=True):
            self.assertEqual(task.run(["second.txt"], self.command("second.txt")), 0)
        before = {p: p.read_bytes() for p in (self.root / self.record, task.record)}
        failed = self.cli("release", "--path", "preview.txt", "--reason", "finished")
        self.assertEqual(failed.returncode, 2)
        self.assertIn("--record", failed.stderr)
        self.assertEqual({p: p.read_bytes() for p in before}, before)
        released = self.cli("--record", self.record, "release", "--path", "preview.txt", "--reason", "finished")
        self.assertEqual(released.returncode, 0, released.stderr)
        cleaned = self.cli("--record", self.record, "clean", "--apply")
        self.assertEqual(cleaned.returncode, 0, cleaned.stderr)
        self.assertTrue((self.root / "second.txt").exists())
        self.assertEqual(task.record.read_bytes(), before[task.record])

    def test_cli_existing_task_record_is_reused_for_first_build(self):
        task = self.root / "source/task-state.json"
        task.parent.mkdir()
        task.write_text('{"goal":"existing task"}', encoding="utf-8")
        built = self.cli("run", "--temporary", "preview.txt", "--", *self.command())
        self.assertEqual(built.returncode, 0, built.stderr)
        self.assertFalse((self.root / self.record).exists())
        data = json.loads(task.read_text(encoding="utf-8"))
        self.assertEqual(data["goal"], "existing task")
        self.assertIn("preview.txt", data["file_lifecycle"]["files"])

    def test_later_continuity_does_not_bypass_pending_inventory_or_lock(self):
        with self.scope().transaction(create=True) as scope:
            with patch("artifact_scope.subprocess.run", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    scope.run(["preview.txt"], self.command())
        task = self.root / "source/task-state.json"
        task.write_text('{"goal":"continue"}', encoding="utf-8")
        before = task.read_bytes()
        with redirect_stderr(io.StringIO()), patch("artifact_scope.subprocess.run") as run:
            self.assertEqual(main(["--root", str(self.root), "run", "--temporary", "other.txt", "--", *self.command("other.txt")]), 2)
            run.assert_not_called()
        scope = self.scope()
        scope.lock.write_text(str(os.getpid()), encoding="ascii")
        locked = self.cli("recover", "--writers-stopped")
        self.assertEqual(locked.returncode, 2)
        self.assertIn("may still be running", locked.stderr)
        self.assertTrue(scope.lock.exists())
        self.assertEqual(task.read_bytes(), before)

    def test_preview_does_not_write_lock_or_state(self):
        self.produce()
        with self.scope().transaction() as scope:
            scope.release(["preview.txt"], "done")
        before = {p.relative_to(self.root): (p.read_bytes(), p.stat().st_mtime_ns)
                  for p in self.root.rglob("*") if p.is_file()}
        with patch("artifact_scope.os.open", side_effect=AssertionError("preview wrote a file")), redirect_stdout(io.StringIO()):
            self.assertEqual(main(["--root", str(self.root), "clean"]), 0)
        after = {p.relative_to(self.root): (p.read_bytes(), p.stat().st_mtime_ns)
                 for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_recovery_cannot_break_a_live_process_lock(self):
        self.produce()
        process = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
        try:
            scope = self.scope()
            scope.lock.write_text(str(process.pid), encoding="ascii")
            with redirect_stderr(io.StringIO()):
                self.assertEqual(main(["--root", str(self.root), "recover", "--writers-stopped"]), 2)
            self.assertEqual(scope.lock.read_text(encoding="ascii"), str(process.pid))
        finally:
            process.terminate()
            process.wait(timeout=10)

    def test_recovery_preserves_unreadable_lock(self):
        self.produce()
        scope = self.scope()
        scope.lock.write_text("unknown", encoding="ascii")
        with redirect_stderr(io.StringIO()):
            self.assertEqual(main(["--root", str(self.root), "recover", "--writers-stopped"]), 2)
        self.assertTrue(scope.lock.exists())

    def test_shared_record_external_update_is_not_overwritten(self):
        self.produce()
        state = self.root / self.record
        with self.scope().transaction() as scope:
            data = json.loads(state.read_text(encoding="utf-8"))
            data["goal"] = "new owner decision"
            state.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "changed outside"):
                scope.release(["preview.txt"], "done")
        self.assertEqual(json.loads(state.read_text(encoding="utf-8"))["goal"], "new owner decision")

    def test_state_change_before_cleanup_preserves_output(self):
        self.produce()
        with self.scope().transaction() as scope:
            scope.release(["preview.txt"], "done")
            (self.root / self.record).write_text('{"goal":"updated"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "changed outside"):
                scope.clean(True)
        self.assertTrue((self.root / "preview.txt").exists())

    def test_record_edit_by_command_preserved_and_unresolved(self):
        state = self.root / self.record
        command = [sys.executable, "-c", "import json,sys; from pathlib import Path; p=Path(sys.argv[1]); d=json.loads(p.read_text()); d['goal']='changed'; p.write_text(json.dumps(d))", str(state)]
        with self.scope().transaction(create=True) as scope:
            with self.assertRaisesRegex(ValueError, "changed outside"):
                scope.run(["preview.txt"], command)
        data = json.loads(state.read_text(encoding="utf-8"))
        self.assertEqual(data["goal"], "changed")
        self.assertEqual(data["file_lifecycle"]["pending"], ["preview.txt"])

    def test_failed_publication_preserves_state_and_blocks_cleanup(self):
        self.produce()
        state = self.root / self.record
        before = state.read_bytes()
        with self.scope().transaction() as scope:
            with patch("artifact_scope.os.replace", side_effect=OSError("publication failed")):
                with self.assertRaises(OSError):
                    scope.release(["preview.txt"], "done")
        self.assertEqual(state.read_bytes(), before)
        self.assertEqual(list(state.parent.glob(".artifact-*.json")), [])
        with self.scope().transaction() as scope:
            self.assertEqual(scope.clean(True), [])

    def test_command_waits_for_child_writer_before_recording(self):
        child = "import time,sys; from pathlib import Path; time.sleep(.1); Path(sys.argv[1]).write_text('complete')"
        command = [sys.executable, "-c", "import subprocess,sys; subprocess.run([sys.executable,'-c',sys.argv[1],sys.argv[2]],check=True)", child, str(self.root / "preview.txt")]
        with self.scope().transaction(create=True) as scope:
            self.assertEqual(scope.run(["preview.txt"], command), 0)
            self.assertEqual(scope.inventory["files"]["preview.txt"]["fingerprint"]["size"], len("complete"))

    def test_schema_rejects_ambiguous_paths_and_boolean_version(self):
        for value in ({"version": True, "files": {}, "pending": []},
                      {"version": 1, "files": {}, "pending": ["../outside"]},
                      {"version": 1, "files": {}, "pending": ["preview.txt", "preview.txt"]}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_inventory(value)

    def test_replaced_output_with_identical_bytes_is_preserved(self):
        self.produce()
        with self.scope().transaction() as scope:
            scope.release(["preview.txt"], "done")
        replacement = self.root / "new.txt"
        replacement.write_text("figure", encoding="utf-8")
        os.replace(replacement, self.root / "preview.txt")
        with self.scope().transaction() as scope:
            self.assertEqual(scope.clean(True)[0]["action"], "preserve_changed")

    def test_complete_continuity_record_stays_valid_after_file_tracking(self):
        from continuity import load_record, validate_record
        self.record = "source/task-state.json"
        state = self.root / self.record
        state.parent.mkdir()
        data = {"version": 1, "task_id": "figure", "goal": {
            "revision": 1, "objective": "Draw the supplied method", "source": "user:request",
            "constraints": ["Preserve topology"], "acceptance": ["Verified figure"]},
            "route": {"id": "draw", "summary": "Use supplied content"},
            "phase": "render", "mode": "normal", "next_action": "Inspect preview"}
        state.write_text(json.dumps(data), encoding="utf-8")
        self.produce()
        current = load_record(str(state))
        self.assertEqual(validate_record(current), [])
        self.assertEqual({key: value for key, value in current.items() if key != "file_lifecycle"}, data)
        current["file_lifecycle"]["pending"] = ["../unsafe"]
        self.assertTrue(any(issue["path"] == "$.file_lifecycle" for issue in validate_record(current)))

    def test_symlinked_task_root_is_rejected(self):
        directory = self.root / "real"
        directory.mkdir()
        redirect = self.root / "redirect"
        try:
            redirect.symlink_to(directory, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"symlink creation unavailable: {exc}")
        with self.assertRaisesRegex(ValueError, "link or reparse"):
            Scope(redirect, self.record)

    def test_command_cannot_adopt_a_symlink_output(self):
        target = self.root / "input.txt"
        target.write_text("input", encoding="utf-8")
        probe = self.root / "probe.txt"
        try:
            probe.symlink_to(target)
        except OSError as exc:
            self.skipTest(f"symlink creation unavailable: {exc}")
        probe.unlink()
        command = [sys.executable, "-c", "from pathlib import Path; import sys; Path(sys.argv[1]).symlink_to(sys.argv[2])", str(self.root / "preview.txt"), str(target)]
        with self.scope().transaction(create=True) as scope:
            with self.assertRaises(ValueError):
                scope.run(["preview.txt"], command)
        with self.scope().transaction() as scope:
            self.assertEqual(scope.inventory["pending"], ["preview.txt"])
            with self.assertRaises(ValueError):
                scope.clean(True)
            scope.recover()
            self.assertEqual(scope.inventory["files"], {})
        self.assertEqual(target.read_text(encoding="utf-8"), "input")


if __name__ == "__main__":
    unittest.main()
