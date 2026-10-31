#!/usr/bin/env python3
"""Task-local receipts for optional expensive reviews; never calls a model.

This is cooperative call bookkeeping, not an API retry queue or a security
sandbox. A pending receipt is deliberately not a reusable review.
"""
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import secrets
import tempfile
from manuscript_patch import _dependencies, _plain_path


def _digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def review_key(packet, model, options=None):
    if not isinstance(packet, dict) or packet.get("schema_version") != 1:
        raise ValueError("Expected a version-1 writing packet")
    if not isinstance(model, str) or not model.strip():
        raise ValueError("Specify the actual reviewer model/runtime identity")
    if options is not None and not isinstance(options, dict):
        raise ValueError("Review options must be a JSON object")
    view = dict(packet)
    manuscript = Path(packet["manuscript"]["path"]).resolve()
    active = set(path for path, _ in _dependencies(packet, manuscript, packet.get("targets")))
    view["dependencies"] = [item for item in packet.get("dependencies", [])
                            if _plain_path(item["path"], manuscript.parent, require_file=False) in active]
    raw = json.dumps({"packet": view, "model": model, "options": options or {}},
                     ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                     allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _current(packet):
    manuscript = packet["manuscript"]
    entries = [(Path(manuscript["path"]), manuscript["sha256"]),
               *_dependencies(packet, Path(manuscript["path"]), packet.get("targets"))]
    for path, expected in entries:
        if not path.is_file() or _digest(path) != expected:
            raise ValueError("Review inputs changed or disappeared: " + str(path))


def _path(value, forbidden=()):
    path = Path(value).absolute()
    if path.is_symlink() or path.resolve() != path:
        raise ValueError("Use an unambiguous cache/result path without symlinks")
    resolved = path.resolve()
    if any(resolved == Path(other).resolve() for other in forbidden):
        raise ValueError("Cache/result path must not overwrite an input: " + str(path))
    return path


@contextmanager
def _transaction(path):
    if not path.parent.is_dir():
        raise ValueError("Create or reuse the task directory before selecting a cache path")
    lock = path.with_name("." + path.name + ".lock")
    token = secrets.token_hex(16).encode("ascii")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError("Review cache is busy; do not remove a live call's lock") from exc
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(token)
        yield
    finally:
        try:
            if not lock.is_symlink() and lock.read_bytes() == token:
                lock.unlink()
        except FileNotFoundError:
            pass


def _load(path):
    if not path.exists():
        return None
    record = json.loads(path.read_text(encoding="utf-8-sig"))
    if (not isinstance(record, dict) or record.get("schema_version") != 1
            or record.get("record_type") != "ccfa-writing-review"
            or record.get("status") not in {"pending", "complete", "abandoned"}
            or not isinstance(record.get("fingerprint"), str)
            or len(record["fingerprint"]) != 64):
        raise ValueError("Not a writing-review receipt; refusing to replace existing data")
    if record["status"] == "complete":
        result, coverage = record.get("result"), record.get("coverage")
        if (not isinstance(result, dict) or not isinstance(result.get("path"), str)
                or not isinstance(result.get("sha256"), str) or len(result["sha256"]) != 64
                or not isinstance(coverage, dict) or coverage.get("kind") not in {"full", "excerpt"}
                or not isinstance(coverage.get("sections"), list) or not coverage["sections"]):
            raise ValueError("Incomplete completed-review receipt; reconcile the actual report")
    return record


def _save(path, record):
    temp = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=path.parent, prefix="." + path.name + ".",
                                         suffix=".tmp", delete=False) as stream:
            temp = Path(stream.name)
            json.dump(record, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
        temp = None
    finally:
        if temp is not None:
            temp.unlink(missing_ok=True)


def _hit(record, key):
    if record is None or record.get("fingerprint") != key or record["status"] != "complete":
        return False
    result = record.get("result", {})
    path = Path(result.get("path", ""))
    return path.is_file() and _digest(path) == result.get("sha256")


def review_cache(action, packet, cache_path, model, options=None, *,
                 result_path=None, coverage=None, call_stopped=False, forbidden=()):
    """One current receipt per task. Caller retains permissions and spend control.

    Include every actual model parameter, review rubric and applicable policy
    identity in options. Only a completed unchanged result can be reused.
    """
    if action not in {"begin", "lookup", "complete", "abandon"}:
        raise ValueError("Unknown review-cache action")
    key = review_key(packet, model, options)
    manuscript = Path(packet["manuscript"]["path"]).resolve()
    inputs = [manuscript,
              *(_plain_path(item["path"], manuscript.parent, require_file=False)
                for item in packet.get("dependencies", [])), *forbidden]
    cache = _path(cache_path, inputs)
    if action != "abandon":
        _current(packet)
    # Even lookup takes a short file lock, never a long-running model-call lock.
    with _transaction(cache):
        record = _load(cache)
        if action == "lookup":
            return {"hit": _hit(record, key), "fingerprint": key,
                    "record": record if _hit(record, key) else None}
        if action == "begin":
            if record is not None and record["status"] == "pending":
                raise ValueError("An incomplete review is pending; reconcile the actual call before retrying")
            if _hit(record, key):
                return {"hit": True, "fingerprint": key, "record": record}
            record = {"schema_version": 1, "record_type": "ccfa-writing-review",
                      "fingerprint": key, "status": "pending"}
        else:
            if record is None or record["status"] != "pending" or record.get("fingerprint") != key:
                raise ValueError("No matching pending review; do not attach a result to another input")
            if action == "abandon":
                if not call_stopped:
                    raise ValueError("Confirm the actual review call has stopped with --call-stopped")
                record["status"] = "abandoned"
            else:
                if result_path is None:
                    raise ValueError("A completed review requires the actual result file")
                result = _path(result_path, [*inputs, cache])
                raw_result = result.read_bytes() if result.is_file() else b""
                if not raw_result.decode("utf-8-sig").strip():
                    raise ValueError("Review result must be a nonempty UTF-8 text file")
                if not isinstance(coverage, dict) or coverage.get("kind") not in {"full", "excerpt"}:
                    raise ValueError("Declare actual coverage: kind full or excerpt, and sections")
                sections = coverage.get("sections")
                targets = set(packet["targets"])
                if (not isinstance(sections, list) or not sections
                        or any(not isinstance(s, str) or s not in targets for s in sections)
                        or len(set(sections)) != len(sections)):
                    raise ValueError("Coverage sections must be unique IDs from the prepared targets")
                if coverage["kind"] == "full" and set(sections) != targets:
                    raise ValueError("Full scoped coverage must include all prepared targets")
                record.update(status="complete", result={"path": str(result), "sha256": hashlib.sha256(raw_result).hexdigest()},
                              coverage=coverage)
        _save(cache, record)
        return {"hit": False, "fingerprint": key, "record": record}
