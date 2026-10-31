#!/usr/bin/env python3
"""Track declared temporary outputs of foreground commands; never sweep a directory.

Optional for repeated builds. The caller owns the command and must finish using an
output before releasing it. This is a cooperative file tool, not a process sandbox.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import stat
import subprocess
import sys
import tempfile


KEY = "file_lifecycle"
MAX_BYTES = 64 * 1024
RESERVED = {"CON", "PRN", "AUX", "NUL", "CLOCK$", "CONIN$", "CONOUT$"} | {
    prefix + suffix for prefix in ("COM", "LPT") for suffix in "123456789¹²³"
}


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def reject_constant(value):
    raise ValueError(f"non-finite JSON value: {value}")


def relative_path(name: str) -> Path:
    if not isinstance(name, str) or not name or "\x00" in name:
        raise ValueError("use a nonempty relative path")
    rel = Path(name)
    windows = PureWindowsPath(name)
    if rel.is_absolute() or rel.drive or windows.drive or windows.root or ".." in windows.parts or not rel.parts:
        raise ValueError("use a relative path inside the task directory")
    # Avoid Windows aliases, alternate streams, and device files on every host.
    if any(part.endswith((".", " ")) or any(c in part for c in ':<>"|?*') or
           any(ord(c) < 32 for c in part) or part.split(".", 1)[0].rstrip(" ").upper() in RESERVED
           for part in windows.parts):
        raise ValueError("path contains a reserved or ambiguous component")
    if os.name != "nt" and "\\" in name:
        raise ValueError("use forward slashes for portable paths")
    return rel


def plain_path(root: Path, name: str) -> Path:
    rel = relative_path(name)
    path = root / rel
    if path == root or not path.resolve().is_relative_to(root):
        raise ValueError("path escapes the task directory")
    for item in (path, *path.parents):
        if item == root.parent:
            break
        if item.is_symlink() or (item.exists() and getattr(item.lstat(), "st_file_attributes", 0) & 0x400):
            raise ValueError("links and reparse points are not managed")
    return path


def fingerprint(path: Path) -> dict:
    info = path.stat(follow_symlinks=False)
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError("only regular, unshared files can be managed")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    after = path.stat(follow_symlinks=False)
    if (info.st_ino, info.st_size, info.st_mtime_ns) != (after.st_ino, after.st_size, after.st_mtime_ns):
        raise ValueError("file changed while it was being inspected")
    return {"sha256": digest.hexdigest(), "size": info.st_size,
            "device": info.st_dev, "inode": info.st_ino, "mtime_ns": info.st_mtime_ns}


def validate_inventory(value: object) -> None:
    if not isinstance(value, dict) or set(value) != {"version", "files", "pending"} or type(value["version"]) is not int or value["version"] != 1:
        raise ValueError("invalid file lifecycle record")
    if not isinstance(value["files"], dict) or not isinstance(value["pending"], list):
        raise ValueError("invalid file lifecycle entries")
    if any(not isinstance(p, str) for p in value["pending"]):
        raise ValueError("invalid pending output")
    for name in [*value["files"], *value["pending"]]:
        relative_path(name)
    if len(set(value["pending"])) != len(value["pending"]):
        raise ValueError("duplicate pending output")
    for name, item in value["files"].items():
        if not isinstance(name, str) or not isinstance(item, dict) or set(item) != {"fingerprint", "released", "reason"}:
            raise ValueError("invalid managed output")
        fp = item["fingerprint"]
        if not isinstance(fp, dict) or set(fp) != {"sha256", "size", "device", "inode", "mtime_ns"}:
            raise ValueError("invalid file fingerprint")
        if not isinstance(fp["sha256"], str) or len(fp["sha256"]) != 64 or any(c not in "0123456789abcdef" for c in fp["sha256"]):
            raise ValueError("invalid content digest")
        if any(type(fp[k]) is not int or fp[k] < 0 for k in ("size", "device", "inode", "mtime_ns")):
            raise ValueError("invalid file metadata")
        if type(item["released"]) is not bool or not isinstance(item["reason"], str):
            raise ValueError("invalid release status")
        if item["released"] and not item["reason"].strip():
            raise ValueError("released output needs a reason")


def process_alive(pid: int) -> bool:
    """Conservatively check lock ownership without signalling Windows processes."""
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        kernel.OpenProcess.restype = wintypes.HANDLE
        kernel.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
        kernel.WaitForSingleObject.restype = wintypes.DWORD
        kernel.CloseHandle.argtypes = [wintypes.HANDLE]
        handle = kernel.OpenProcess(0x100000, False, pid)  # SYNCHRONIZE
        if not handle:
            if ctypes.get_last_error() == 87:  # ERROR_INVALID_PARAMETER: no such PID
                return False
            return True  # Access denial or an unknown error cannot prove death.
        try:
            return kernel.WaitForSingleObject(handle, 0) != 0
        finally:
            kernel.CloseHandle(handle)
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


class Scope:
    def __init__(self, root: Path, record: str):
        self.root = root.absolute()
        if not self.root.is_dir() or self.root.parent == self.root:
            raise ValueError("use an existing task directory")
        # Reject redirected roots and their ancestors before resolving them.
        for item in (self.root, *self.root.parents):
            if item.is_symlink() or getattr(item.lstat(), "st_file_attributes", 0) & 0x400:
                raise ValueError("task root must not pass through a link or reparse point")
        plain_path(self.root, ".scope-check")
        self.root = self.root.resolve()
        self.record = plain_path(self.root, record)
        self.lock = self.record.with_name(self.record.name + ".lock")
        self.data = {}
        self.inventory = {"version": 1, "files": {}, "pending": []}
        self._record_bytes = None
        self._readonly = False

    def read_record(self, missing_ok=False):
        plain_path(self.root, self.record.relative_to(self.root).as_posix())
        self.data = {}
        self.inventory = {"version": 1, "files": {}, "pending": []}
        if not self.record.exists():
            if not missing_ok:
                raise ValueError("no artifact record exists")
            self._record_bytes = None
            return
        if not self.record.is_file() or self.record.stat().st_size > MAX_BYTES:
            raise ValueError("record must be a regular JSON file of at most 64 KiB")
        self._record_bytes = self.record.read_bytes()
        self.data = json.loads(self._record_bytes.decode("utf-8-sig"), object_pairs_hook=unique_object, parse_constant=reject_constant)
        if not isinstance(self.data, dict):
            raise ValueError("record must be a JSON object")
        self.inventory = self.data.get(KEY, {"version": 1, "files": {}, "pending": []})
        validate_inventory(self.inventory)

    def check_record_unchanged(self):
        plain_path(self.root, self.record.relative_to(self.root).as_posix())
        current = self.record.read_bytes() if self.record.exists() else None
        if current != self._record_bytes:
            raise ValueError("state record changed outside this transaction; preserve it and reconcile before retrying")

    @contextmanager
    def transaction(self, create: bool = False, readonly: bool = False):
        plain_path(self.root, self.record.relative_to(self.root).as_posix())
        plain_path(self.root, self.lock.relative_to(self.root).as_posix())
        if self.lock.exists():
            raise FileExistsError("an artifact transaction is active or needs recovery")
        if readonly:
            self.read_record(missing_ok=True)
            self._readonly = True
            try:
                yield self
            finally:
                self._readonly = False
            return
        if not create and not self.record.exists():
            raise ValueError("no artifact record exists")
        self.record.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(self.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(str(os.getpid()).encode("ascii"))
            self.read_record(missing_ok=create)
            yield self
        finally:
            self.lock.unlink(missing_ok=True)

    def save(self):
        if self._readonly:
            raise ValueError("preview transactions cannot write")
        validate_inventory(self.inventory)
        self.data[KEY] = self.inventory
        payload = (json.dumps(self.data, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
        if len(payload) > MAX_BYTES:
            raise ValueError("record exceeds 64 KiB; finish the current batch first")
        self.check_record_unchanged()
        fd, tmp = tempfile.mkstemp(prefix=".artifact-", suffix=".json", dir=self.record.parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            self.check_record_unchanged()
            os.replace(tmp, self.record)
            self._record_bytes = payload
        finally:
            Path(tmp).unlink(missing_ok=True)

    def output(self, name: str) -> Path:
        path = plain_path(self.root, name)
        if path in (self.record, self.lock):
            raise ValueError("the state record cannot be a temporary output")
        return path

    def run(self, names: list[str], command: list[str]) -> int:
        if self.inventory["pending"]:
            raise ValueError("an earlier command is unresolved; inspect it before recovery")
        if not command:
            raise ValueError("a foreground command is required")
        paths = {self.output(name).relative_to(self.root).as_posix(): self.output(name) for name in names}
        if not paths:
            raise ValueError("declare at least one temporary output")
        owned = []
        protected = []
        for name, path in paths.items():
            prior = self.inventory["files"].get(name)
            if not path.exists():
                owned.append(name)
            elif prior and fingerprint(path) == prior["fingerprint"]:
                owned.append(name)
            else:
                # Declared temporary outputs may never overwrite unowned inputs.
                self.inventory["files"].pop(name, None)
                protected.append(name)
        if protected:
            if self._record_bytes is not None:
                self.save()
            raise ValueError("refusing to overwrite unowned or changed output: " + ", ".join(protected))
        self.inventory["pending"] = list(paths)
        self.save()
        # Inherit the caller's cwd and streams. The command must wait for all writers.
        result = subprocess.run(command, check=False)
        for name in owned:
            path = self.output(name)
            if path.exists():
                self.inventory["files"][name] = {"fingerprint": fingerprint(path), "released": False, "reason": ""}
            else:
                self.inventory["files"].pop(name, None)
        self.inventory["pending"] = []
        self.save()
        return result.returncode

    def release(self, names: list[str], reason: str):
        if self.inventory["pending"] or not reason.strip():
            raise ValueError("finish all writers and give a disposal reason")
        for raw in names:
            path = self.output(raw)
            name = path.relative_to(self.root).as_posix()
            entry = self.inventory["files"].get(name)
            if not entry or not path.exists() or fingerprint(path) != entry["fingerprint"]:
                raise ValueError(f"output is unowned, missing, or changed: {name}")
            entry.update(released=True, reason=reason)
        self.save()

    def clean(self, apply: bool = False) -> list[dict]:
        if self.inventory["pending"]:
            raise ValueError("an unresolved writer prevents cleanup")
        if apply:
            if self._readonly:
                raise ValueError("preview transactions cannot delete")
            self.check_record_unchanged()
        rows = []
        for name, entry in list(self.inventory["files"].items()):
            if not entry["released"]:
                continue
            path = self.output(name)
            if not path.exists():
                if apply:
                    del self.inventory["files"][name]
                continue
            if fingerprint(path) != entry["fingerprint"]:
                rows.append({"path": name, "action": "preserve_changed"})
                continue
            rows.append({"path": name, "action": "delete" if apply else "would_delete", "bytes": entry["fingerprint"]["size"]})
            if apply:
                # One checked file at a time; no recursive directory removal.
                path.unlink()
                del self.inventory["files"][name]
        if apply:
            self.save()
        return rows

    def recover(self):
        # Caller first confirms the old process and descendants have stopped.
        # Interrupted outputs are never adopted for automatic deletion.
        for name in self.inventory["pending"]:
            self.inventory["files"].pop(name, None)
        self.inventory["pending"] = []
        self.save()

    def clear_stale_lock(self):
        plain_path(self.root, self.lock.relative_to(self.root).as_posix())
        fingerprint(self.lock)
        try:
            pid = int(self.lock.read_text(encoding="ascii"))
        except (ValueError, UnicodeError):
            raise ValueError("lock owner is unreadable; inspect it manually before recovery") from None
        if pid <= 0 or pid > 0xFFFFFFFF or process_alive(pid):
            raise ValueError("lock owner may still be running; recovery cannot remove its lock")
        self.lock.unlink()


def default_scope(root: Path) -> Scope:
    """Keep the established inventory when continuity is introduced later."""
    scopes = [Scope(root, name) for name in
              ("source/artifact-state.json", "source/task-state.json")]
    managed = []
    locked = []
    for scope in scopes:
        if scope.record.exists():
            scope.read_record()
            if KEY in scope.data:
                managed.append(scope)
        if scope.lock.exists():
            locked.append(scope)
    if len(managed) > 1 or len(locked) > 1 or (
            managed and locked and managed[0] is not locked[0]):
        raise ValueError("multiple lifecycle records or locks; inspect them and select --record explicitly")
    if locked:
        return locked[0]
    if managed:
        return managed[0]
    return next((scope for scope in reversed(scopes) if scope.record.exists()), scopes[0])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="existing task working directory")
    parser.add_argument("--record", help="relative JSON state; default reuses the existing lifecycle record")
    subs = parser.add_subparsers(dest="action", required=True)
    run = subs.add_parser("run")
    run.add_argument("--temporary", action="append", required=True)
    run.add_argument("command", nargs=argparse.REMAINDER)
    release = subs.add_parser("release")
    release.add_argument("--path", action="append", required=True)
    release.add_argument("--reason", required=True)
    clean = subs.add_parser("clean")
    clean.add_argument("--apply", action="store_true", help="delete released unchanged files; default is preview")
    recover = subs.add_parser("recover")
    recover.add_argument("--writers-stopped", action="store_true", required=True)
    args = parser.parse_args(argv)
    try:
        scope = Scope(args.root, args.record) if args.record else default_scope(args.root)
        if args.action == "recover" and scope.lock.exists():
            scope.clear_stale_lock()
        with scope.transaction(create=args.action == "run", readonly=args.action == "clean" and not args.apply):
            if args.action == "run":
                command = args.command[1:] if args.command[:1] == ["--"] else args.command
                return scope.run(args.temporary, command)
            if args.action == "release":
                scope.release(args.path, args.reason)
            elif args.action == "clean":
                print(json.dumps(scope.clean(args.apply), ensure_ascii=False))
            else:
                scope.recover()
        return 0
    except (OSError, ValueError, RecursionError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
