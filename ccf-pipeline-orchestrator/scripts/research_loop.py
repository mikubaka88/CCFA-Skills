#!/usr/bin/env python3
"""Bounded, host-agent-driven experiments; stdlib only.

The host edits an explicit file allowlist and chooses hypotheses. This tool
freezes the contract, executes its argv, records evidence, and keeps or restores
managed snapshots. Hash checks are integrity checks, NOT an OS sandbox. The
caller remains responsible for command permissions, environment, and evaluator
independence. No model, network client, GPU job, or background loop is started
except what the caller's explicit command itself requests.

Only foreground commands that wait for all their workers are supported.
Detached/background workers are unsupported. Time meters cover the direct
command's elapsed time, not descendant CPU time; timeout tree termination is
best effort and cannot guarantee orphan cleanup or undo external effects.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import stat
import subprocess
import sys
import time
import uuid


class LoopError(Exception):
    """An actionable contract, integrity, or lifecycle error."""


def _finite(value):
    try:
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    except OverflowError:
        return False


def _pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise LoopError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _json(path):
    try:
        return _parse_json(path.read_bytes())
    except (OSError, UnicodeError, ValueError) as exc:
        raise LoopError(f"Cannot read JSON {path.name}: {exc}") from exc


def _parse_json(data):
    return json.loads(
        data.decode("utf-8-sig"), object_pairs_hook=_pairs,
        parse_constant=lambda value: (_ for _ in ()).throw(LoopError(f"Non-finite JSON value: {value}")),
    )


def _encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _hash(value):
    return hashlib.sha256(_encoded(value)).hexdigest()


def _write(path, data):
    """Atomic replacement of a tool-owned file, or a checked managed file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        with temporary.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _write_json(path, value):
    _write(path, _encoded(value) + b"\n")


def _now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _relative(value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise LoopError("File paths must be nonempty, project-relative paths using forward slashes")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != value or value == ".":
        raise LoopError(f"Unsafe or noncanonical relative file path: {value}")
    return value


def _file(root, relative):
    path = root / _relative(relative)
    for part in (path, *path.parents):
        if part == root:
            break
        if part.is_symlink() or (hasattr(part, "is_junction") and part.is_junction()):
            raise LoopError(f"Linked managed/locked path is unsupported: {relative}")
    if not path.resolve().is_relative_to(root):
        raise LoopError(f"Path escapes project: {relative}")
    if path.exists() and not path.is_file():
        raise LoopError(f"Expected a regular file: {relative}")
    return path


def _file_info(path):
    if not path.exists():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return {"sha256": digest.hexdigest(), "mode": stat.S_IMODE(path.stat().st_mode)}


def _manifest(project, names, required=False):
    result = {}
    for name in names:
        result[name] = _file_info(_file(project, name))
        if required and result[name] is None:
            raise LoopError(f"Locked file is missing: {name}")
    return result


def _snapshot(project, names, destination):
    manifest = _manifest(project, names)
    destination.mkdir(parents=True, exist_ok=False)
    for name, info in manifest.items():
        if info is not None:
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(_file(project, name), target)
            if _file_info(target)["sha256"] != info["sha256"]:
                raise LoopError(f"File changed while snapshotting: {name}")
    _write_json(destination.parent / "manifest.json", manifest)
    return manifest


def _contract(raw):
    required = {
        "objective", "constraints", "scientific_value", "editable_files",
        "evaluator_files", "data_files", "command", "metric", "budgets",
    }
    if not isinstance(raw, dict) or set(raw) != required:
        raise LoopError("Contract requires exactly: " + ", ".join(sorted(required)))
    for name in ("objective", "scientific_value"):
        if not isinstance(raw[name], str) or not raw[name].strip():
            raise LoopError(f"{name} must be nonempty text")
    if not isinstance(raw["constraints"], list) or not all(isinstance(v, str) and v.strip() for v in raw["constraints"]):
        raise LoopError("constraints must be a list of nonempty strings (an empty list is allowed)")
    all_names = []
    for field in ("editable_files", "evaluator_files", "data_files"):
        names = raw[field]
        if not isinstance(names, list) or (field != "data_files" and not names):
            raise LoopError(f"{field} must be a list; editable/evaluator files cannot be empty")
        all_names.extend(_relative(v) for v in names)
    if len(all_names) != len(set(all_names)):
        raise LoopError("Editable, evaluator, and data paths must be unique and disjoint")
    for name in all_names:
        if any(other != name and other.startswith(name + "/") for other in all_names):
            raise LoopError("A declared file cannot be another declared file's directory")
    command = raw["command"]
    if not isinstance(command, list) or not command or not all(isinstance(v, str) and v and "\0" not in v for v in command):
        raise LoopError("command must be a nonempty argv list, never a shell string")
    if not any("{metrics}" in arg for arg in command):
        raise LoopError("command must contain {metrics}, the evaluator's fresh JSON result path")
    if Path(command[0]).suffix.lower() in (".bat", ".cmd"):
        raise LoopError("Use a direct executable/interpreter, not a Windows batch file")
    metric = raw["metric"]
    if not isinstance(metric, dict) or set(metric) != {"name", "direction", "min_delta"}:
        raise LoopError("metric requires name, direction, min_delta")
    if not isinstance(metric["name"], str) or not metric["name"].strip() or metric["direction"] not in ("min", "max"):
        raise LoopError("metric needs a nonempty name and min|max direction")
    if not _finite(metric["min_delta"]) or metric["min_delta"] < 0:
        raise LoopError("min_delta must be finite and nonnegative; keep requires strictly greater improvement")
    budgets = raw["budgets"]
    if not isinstance(budgets, dict) or set(budgets) != {"max_attempts", "max_seconds", "timeout_seconds"}:
        raise LoopError("budgets requires max_attempts, max_seconds, timeout_seconds")
    if type(budgets["max_attempts"]) is not int or budgets["max_attempts"] < 1:
        raise LoopError("max_attempts must be a positive integer and includes baseline runs")
    for key in ("max_seconds", "timeout_seconds"):
        if not _finite(budgets[key]) or budgets[key] <= 0:
            raise LoopError(f"{key} must be positive and finite")
    return raw


@contextlib.contextmanager
def _lock(workdir):
    """OS lock: released on process death; never steal a lock by its age."""
    lock_path = workdir / ".lock"
    if lock_path.is_symlink():
        raise LoopError("Lock path cannot be a symlink")
    with lock_path.open("a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise LoopError("Another process owns this experiment; use status without starting a second run") from exc
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _apply(state, event):
    state.update(event.get("update", {}))
    if "attempt" in event:
        state.setdefault("attempts", {})[event["attempt"]["id"]] = event["attempt"]
    state["seq"] = event["seq"]
    return state


def _load(workdir):
    """The fsynced append log is authoritative; state.json is only a cache."""
    state = {"seq": 0, "attempts": {}}
    try:
        raw = (workdir / "events.jsonl").read_bytes()
        if not raw.endswith(b"\n"):
            raise LoopError("Incomplete audit tail: preserve it and reconcile manually; no command was replayed")
        for line in raw.splitlines():
            event = json.loads(line.decode("utf-8"), object_pairs_hook=_pairs)
            if event["seq"] != state["seq"] + 1:
                raise LoopError("Audit sequence is inconsistent; no command was replayed")
            _apply(state, event)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        raise LoopError(f"Cannot reconstruct experiment audit: {exc}") from exc
    if "project" not in state:
        raise LoopError("Experiment was not initialized")
    return state


def _event(workdir, state, kind, *, update=None, attempt=None, details=None):
    event = {"seq": state["seq"] + 1, "time": _now(), "event": kind}
    if update is not None:
        event["update"] = update
    if attempt is not None:
        event["attempt"] = dict(attempt)
    if details is not None:
        event["details"] = details
    with (workdir / "events.jsonl").open("ab") as stream:
        stream.write(_encoded(event) + b"\n")
        stream.flush()
        os.fsync(stream.fileno())
    _apply(state, event)
    _write_json(workdir / "state.json", state)


def _integrity(workdir, state):
    contract = _contract(_json(workdir / "contract.json"))
    if _hash(contract) != state["contract_hash"]:
        raise LoopError("Frozen contract changed; start a new experiment for a different protocol")
    actual = _manifest(Path(state["project"]), contract["evaluator_files"] + contract["data_files"], required=True)
    if actual != state["locked_files"]:
        raise LoopError("Frozen evaluator/data changed; restore the known version or start a new experiment")
    return contract


def _checked(workdir, state):
    try:
        return _integrity(workdir, state)
    except LoopError as exc:
        _event(workdir, state, "integrity_error", details={"error": str(exc)})
        raise


def _attempt_dir(workdir, run_id):
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}", run_id):
        raise LoopError("Run id must be 1-64 ASCII letters, digits, underscores, or hyphens")
    if run_id.upper() in {"CON", "PRN", "AUX", "NUL", *[f"COM{i}" for i in range(1, 10)], *[f"LPT{i}" for i in range(1, 10)]}:
        raise LoopError("Run id is reserved on Windows")
    return workdir / "attempts" / run_id


def _target(state):
    return state["attempts"][state["best"]] if state["best"] is not None else state["initial"]


def _restore(workdir, state, attempt):
    """Restore only submitted bytes; preserve concurrent edits, including deletion."""
    target = _target(state)
    project = Path(state["project"])
    conflicts = []
    for name, expected in attempt["manifest"].items():
        desired = target["manifest"][name]
        path = _file(project, name)
        actual = _file_info(path)
        if actual != expected and actual != desired:
            conflicts.append(name)
    if conflicts:
        return conflicts
    for name, expected in attempt["manifest"].items():
        desired = target["manifest"][name]
        path = _file(project, name)
        if _file_info(path) == desired:
            continue
        # Check again immediately before each write; an external editor is not
        # serialized by our lock, so callers must keep these paths exclusive.
        if _file_info(path) != expected:
            conflicts.append(name)
            continue
        if desired is None:
            path.unlink()
        else:
            source = workdir / target["snapshot"] / name
            if _file_info(source) is None or _file_info(source)["sha256"] != desired["sha256"]:
                raise LoopError(f"Stored parent snapshot changed: {name}")
            _write(path, source.read_bytes())
            os.chmod(path, desired["mode"])
    return conflicts


def _discard(workdir, state, attempt, reason):
    attempt = dict(attempt, decision="discard", reason=reason, status="deciding")
    _event(workdir, state, "discard_started", attempt=attempt)
    conflicts = _restore(workdir, state, attempt)
    if conflicts:
        attempt.update(status="rollback_conflict", conflicts=conflicts)
        _event(workdir, state, "rollback_conflict", attempt=attempt)
    else:
        attempt.update(status="discarded", conflicts=[])
        _event(workdir, state, "discard", attempt=attempt, update={"pending": None})
    return attempt


def initialize(project, workdir, contract_path):
    project = project.resolve(strict=True)
    workdir = workdir.resolve()
    if not project.is_dir() or not workdir.is_relative_to(project) or workdir == project:
        raise LoopError("Experiment directory must be a dedicated descendant of the project")
    # Explicit caller-specified task paths are supported; no generic output
    # directory is chosen by the script.
    contract = _contract(_json(contract_path))
    resolved = []
    for name in contract["editable_files"] + contract["evaluator_files"] + contract["data_files"]:
        path = _file(project, name)
        if path.is_relative_to(workdir):
            raise LoopError("Declared input files cannot live in the experiment evidence directory")
        for previous in resolved:
            if os.path.normcase(str(path.resolve())) == os.path.normcase(str(previous.resolve())) or (
                path.exists() and previous.exists() and os.path.samefile(path, previous)
            ):
                raise LoopError("Declared paths must identify different files, including case aliases and hardlinks")
        resolved.append(path)
    locked = _manifest(project, contract["evaluator_files"] + contract["data_files"], required=True)
    if workdir.exists() and any(workdir.iterdir()):
        raise LoopError("Experiment directory is not empty; use status to resume, never reinitialize")
    workdir.mkdir(parents=True, exist_ok=True)
    with _lock(workdir):
        manifest = _snapshot(project, contract["editable_files"], workdir / "initial" / "snapshot")
        _write_json(workdir / "contract.json", contract)
        state = {"seq": 0, "attempts": {}}
        _event(workdir, state, "initialized", update={
            "schema": 1, "project": str(project), "contract_hash": _hash(contract),
            "locked_files": locked, "objective": contract["objective"],
            "initial": {"manifest": manifest, "snapshot": "initial/snapshot"},
            "best": None, "pending": None, "attempt_count": 0, "charged_seconds": 0.0,
            "budgets": contract["budgets"],
        })
        return _summary(workdir, state, contract)


def _read_metric(path, name):
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 1024 * 1024:
        raise LoopError("Evaluator must write a fresh regular metrics JSON file (at most 1 MiB)")
    raw = path.read_bytes()
    try:
        result = _parse_json(raw)
    except (UnicodeError, ValueError) as exc:
        raise LoopError(f"Cannot read metrics JSON: {exc}") from exc
    if not isinstance(result, dict) or name not in result or not _finite(result[name]):
        raise LoopError(f"Metric {name!r} must be one finite JSON number, not bool or text")
    # Preserve exact integer metrics (e.g. counts above 2**53).
    return result[name], hashlib.sha256(raw).hexdigest()


def _metric_evidence(workdir, attempt):
    path = workdir / attempt["metrics"]
    if not path.is_file() or path.is_symlink() or _file_info(path)["sha256"] != attempt.get("metrics_sha256"):
        raise LoopError("Raw metrics evidence changed or is missing; cannot promote this evaluation")


def _stop(process):
    """Best-effort process-tree termination; this cannot undo external effects."""
    if os.name == "nt":
        try:
            stopped = subprocess.run(
                ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5,
            )
            tree_result = f"taskkill_exit_{stopped.returncode}"
        except (OSError, subprocess.TimeoutExpired):
            tree_result = "tree_termination_unconfirmed"
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
            tree_result = "process_group_killed"
        except ProcessLookupError:
            tree_result = "process_group_already_exited"
    try:
        if process.poll() is None:
            process.kill()
        process.wait(timeout=5)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise LoopError("Evaluator termination is unconfirmed; inspect surviving processes, then recover explicitly") from exc
    return tree_result


def _wait(process, seconds):
    # Avoid platform wait-API integer overflow for large but finite budgets.
    deadline = time.monotonic() + seconds
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise subprocess.TimeoutExpired(process.args, seconds)
        try:
            return process.wait(timeout=min(remaining, 60))
        except subprocess.TimeoutExpired:
            if time.monotonic() >= deadline:
                raise


def run(workdir, run_id, hypothesis=""):
    with _lock(workdir):
        state = _load(workdir)
        # Repeating a completed or started ID never repeats the subprocess.
        if run_id in state["attempts"]:
            return {"replayed": False, "already_recorded": True, "attempt": state["attempts"][run_id]}
        contract = _checked(workdir, state)
        if state["pending"] is not None:
            raise LoopError(f"Resolve pending run {state['pending']} with decide/recover before another run")
        budgets = contract["budgets"]
        remaining = budgets["max_seconds"] - state["charged_seconds"]
        if state["attempt_count"] >= budgets["max_attempts"] or remaining <= 0:
            raise LoopError("Experiment attempt or execution-time budget is exhausted")
        project = Path(state["project"])
        current = _manifest(project, contract["editable_files"])
        baseline = state["best"] is None
        if baseline and current != state["initial"]["manifest"]:
            raise LoopError("Run the initial snapshot as baseline before editing a candidate")
        if not baseline:
            if not isinstance(hypothesis, str) or not hypothesis.strip():
                raise LoopError("A candidate needs --hypothesis describing the proposed mechanism/change")
            if current == _target(state)["manifest"]:
                raise LoopError("Candidate is unchanged from its parent; no subprocess was started")
        destination = _attempt_dir(workdir, run_id)
        if destination.exists():
            raise LoopError("Unrecorded attempt directory exists; inspect it instead of overwriting evidence")
        destination.mkdir(parents=True)
        manifest = _snapshot(project, contract["editable_files"], destination / "snapshot")
        parent_id = state["best"]
        candidate_id = _hash({
            "contract": state["contract_hash"], "parent": parent_id,
            "parent_candidate": None if baseline else _target(state)["candidate_id"], "manifest": manifest,
        })
        metrics_path = destination / "metrics.json"
        argv = [
            arg.replace("{metrics}", str(metrics_path)).replace("{attempt_dir}", str(destination))
            for arg in contract["command"]
        ]
        limit = min(budgets["timeout_seconds"], remaining)
        attempt = {
            "id": run_id, "kind": "baseline" if baseline else "candidate",
            "candidate_id": candidate_id, "parent": parent_id, "hypothesis": hypothesis,
            "manifest": manifest, "snapshot": str((destination / "snapshot").relative_to(workdir)).replace("\\", "/"),
            "status": "running", "outcome": None, "started_at": _now(), "pid": None,
            "reserved_seconds": limit, "argv": argv, "metric": None,
            "stdout": f"attempts/{run_id}/stdout.log", "stderr": f"attempts/{run_id}/stderr.log",
            "metrics": f"attempts/{run_id}/metrics.json",
            "environment": {"python": sys.version.split()[0], "platform": sys.platform,
                            "executable": shutil.which(argv[0])},
        }
        _event(workdir, state, "run_started", attempt=attempt, update={
            "pending": run_id, "attempt_count": state["attempt_count"] + 1,
        })
        start = time.monotonic()
        outcome, error, process = "ok", None, None
        try:
            with (destination / "stdout.log").open("xb") as stdout, (destination / "stderr.log").open("xb") as stderr:
                options = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" else {"start_new_session": True}
                process = subprocess.Popen(
                    argv, cwd=project, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                    shell=False, **options,
                )
                attempt["pid"] = process.pid
                _event(workdir, state, "process_started", attempt=attempt)
                try:
                    attempt["returncode"] = _wait(process, limit)
                    if attempt["returncode"] != 0:
                        outcome, error = "crash", f"Evaluator exited with code {attempt['returncode']}"
                except subprocess.TimeoutExpired:
                    outcome, error = "timeout", f"Execution exceeded {limit:g} seconds"
                    attempt["termination"] = _stop(process)
                    attempt["returncode"] = process.returncode
        except OSError as exc:
            if process is None:
                outcome, error = "crash", str(exc)
            else:
                # A controller/cache failure after Popen must not abandon a
                # live evaluator and then restore files underneath it.
                outcome, error = "controller_error", f"Controller I/O failed: {exc}"
                try:
                    attempt["termination"] = _stop(process)
                    attempt["returncode"] = process.returncode
                except (LoopError, OSError) as stop_exc:
                    raise LoopError(
                        f"{error}; evaluator termination is unconfirmed; pending run retained. "
                        "Inspect its process and children, then recover explicitly"
                    ) from stop_exc
                # The event may have committed before its cache write failed.
                # Reload the authoritative sequence; never append from possibly
                # stale memory or silently continue past an incomplete log.
                try:
                    state = _load(workdir)
                except LoopError as audit_exc:
                    raise LoopError(
                        f"{error}; evaluator stopped, but the audit requires reconciliation "
                        "before recovery; no files were restored"
                    ) from audit_exc
        except KeyboardInterrupt:
            outcome, error = "interrupted", "Host interrupted this evaluator"
            if process is not None:
                attempt["termination"] = _stop(process)
                attempt["returncode"] = process.returncode
        elapsed = time.monotonic() - start
        try:
            _integrity(workdir, state)
            if _manifest(project, contract["editable_files"]) != manifest:
                raise LoopError("Managed inputs changed during execution; preserve them for reconciliation")
        except LoopError as exc:
            attempt["execution_outcome"] = outcome
            outcome, error = "integrity_error", str(exc)
        if outcome == "ok":
            try:
                attempt["metric"], attempt["metrics_sha256"] = _read_metric(metrics_path, contract["metric"]["name"])
            except (LoopError, OSError) as exc:
                outcome, error = "invalid_metric", str(exc)
        attempt.update(outcome=outcome, status="evaluated", error=error, elapsed_seconds=elapsed, budget_charge_seconds=elapsed)
        _event(workdir, state, "run_finished", attempt=attempt, update={
            "charged_seconds": state["charged_seconds"] + elapsed,
        })
        if outcome != "ok":
            attempt = _discard(workdir, state, attempt, error or outcome)
        elif baseline:
            attempt.update(status="kept", decision="keep", reason="Initial measured baseline")
            _event(workdir, state, "baseline_kept", attempt=attempt, update={"best": run_id, "pending": None})
        else:
            parent_metric = state["attempts"][parent_id]["metric"]
            gain = attempt["metric"] - parent_metric
            if contract["metric"]["direction"] == "min":
                gain = -gain
            if not _finite(gain):
                attempt.update(outcome="invalid_metric", error="Metric delta exceeds the supported finite numeric range")
                _event(workdir, state, "invalid_metric", attempt=attempt)
                return {"attempt": _discard(workdir, state, attempt, attempt["error"])}
            attempt.update(improvement=gain, eligible=gain > contract["metric"]["min_delta"], status="awaiting_decision")
            _event(workdir, state, "awaiting_decision", attempt=attempt)
        return {"attempt": attempt}


def decide(workdir, run_id, action, reason):
    if not reason.strip():
        raise LoopError("Decision requires a concrete reason; metric improvement alone is not novelty evidence")
    with _lock(workdir):
        state = _load(workdir)
        attempt = state["attempts"].get(run_id)
        if attempt is None:
            raise LoopError("Unknown run id")
        if attempt["status"] in ("kept", "discarded"):
            if attempt.get("decision") != action:
                raise LoopError("Completed decisions are immutable")
            return {"already_recorded": True, "attempt": attempt}
        if state["pending"] != run_id or attempt["status"] not in ("awaiting_decision", "deciding", "rollback_conflict"):
            raise LoopError("Run has not finished; inspect status and use recover if its process has stopped")
        if action == "discard":
            return {"attempt": _discard(workdir, state, attempt, reason)}
        contract = _checked(workdir, state)
        if attempt["outcome"] != "ok" or not attempt.get("eligible"):
            raise LoopError("Keep requires a valid metric improving strictly beyond the frozen min_delta")
        _metric_evidence(workdir, attempt)
        if _manifest(Path(state["project"]), contract["editable_files"]) != attempt["manifest"]:
            raise LoopError("Candidate changed after evaluation; cannot keep unmeasured bytes")
        attempt = dict(attempt, decision="keep", reason=reason, status="kept")
        _event(workdir, state, "keep", attempt=attempt, update={"best": run_id, "pending": None})
        return {"attempt": attempt}


def recover(workdir, run_id, reason, confirm_stopped=False):
    if not confirm_stopped or not reason.strip():
        raise LoopError("Recovery requires --confirm-stopped and a reason after checking any surviving evaluator/children")
    with _lock(workdir):
        state = _load(workdir)
        attempt = state["attempts"].get(run_id)
        if attempt is None or state["pending"] != run_id:
            raise LoopError("No matching pending attempt")
        if attempt["status"] in ("deciding", "rollback_conflict"):
            return {"attempt": _discard(workdir, state, attempt, reason)}
        if attempt["status"] == "running":
            # Parent death removes timeout supervision: a surviving child can
            # exceed the reserved duration. Close the remaining budget rather
            # than pretending the reservation bounds actual execution time.
            remaining = max(0, state["budgets"]["max_seconds"] - state["charged_seconds"])
            attempt = dict(
                attempt, status="evaluated", outcome="interrupted", error=reason,
                elapsed_seconds=None, duration_unknown=True, budget_charge_seconds=remaining,
                budget_note="Remaining execution budget closed because duration is unknown; charge is not measured runtime",
            )
            _event(workdir, state, "interrupted", attempt=attempt, update={
                "charged_seconds": max(state["charged_seconds"], state["budgets"]["max_seconds"]),
                "duration_unknown": True,
                "budget_stop_reason": "Controller lost timeout supervision; reconcile actual costs before any new experiment",
            })
        elif attempt["status"] != "evaluated":
            raise LoopError("Completed evaluation requires decide, not recovery")
        # An interrupted transaction is never silently promoted, even if a
        # metrics file happens to exist.
        return {"attempt": _discard(workdir, state, attempt, reason)}


def _summary(workdir, state, contract):
    pending = state["attempts"].get(state["pending"])
    reserved = pending["reserved_seconds"] if pending and pending["status"] == "running" else 0
    best = state["attempts"].get(state["best"])
    if pending:
        next_action = "inspect process; recover only after it and its children stop" if pending["status"] == "running" else "decide or resolve rollback conflict"
    elif state["attempt_count"] >= state["budgets"]["max_attempts"] or state["charged_seconds"] >= state["budgets"]["max_seconds"]:
        next_action = "stop: experiment budget exhausted"
    elif best is None:
        next_action = "run unchanged initial files as baseline"
    else:
        next_action = "host proposes and edits one allowed candidate, then run with a new id"
    return {
        "objective": state["objective"], "constraints": contract["constraints"],
        "scientific_value": contract["scientific_value"], "contract_hash": state["contract_hash"],
        "best": None if best is None else {key: best[key] for key in ("id", "candidate_id", "metric", "hypothesis")},
        "pending": None if pending is None else {key: pending.get(key) for key in ("id", "status", "outcome", "pid", "error")},
        "budget": {
            "attempts_used": state["attempt_count"],
            "attempts_remaining": max(0, state["budgets"]["max_attempts"] - state["attempt_count"]),
            "execution_seconds_charged": state["charged_seconds"],
            "execution_seconds_reserved": reserved,
            "execution_seconds_remaining": max(0, state["budgets"]["max_seconds"] - state["charged_seconds"] - reserved),
            "duration_unknown": state.get("duration_unknown", False),
            "stop_reason": state.get("budget_stop_reason"),
            "meter_scope": "foreground command elapsed time only; host planning time, model tokens, and descendant CPU time are not measured; detached workers are unsupported",
        },
        "recent_failures": [
            {"id": item["id"], "outcome": item["outcome"], "error": item.get("error")}
            for item in list(state["attempts"].values()) if item["outcome"] not in (None, "ok")
        ][-3:],
        "recent_decisions": [
            {key: item.get(key) for key in ("id", "parent", "hypothesis", "metric", "decision", "reason")}
            for item in state["attempts"].values() if item.get("decision")
        ][-3:],
        "next_action": next_action,
        "paths": {"workdir": str(workdir), "events": str(workdir / "events.jsonl"),
                  "contract": str(workdir / "contract.json"), "attempts": str(workdir / "attempts")},
    }


def status(workdir):
    # Reads can observe an active run without taking its exclusive writer lock.
    state = _load(workdir)
    contract = _contract(_json(workdir / "contract.json"))
    result = _summary(workdir, state, contract)
    try:
        _integrity(workdir, state)
        result["integrity"] = "ok"
    except LoopError as exc:
        result["integrity"] = str(exc)
        result["next_action"] = "resolve frozen protocol integrity before another execution"
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    init_parser = commands.add_parser("init", help="Freeze a supplied contract and current managed bytes; do not execute")
    init_parser.add_argument("--project", type=Path, default=Path.cwd())
    init_parser.add_argument("--workdir", type=Path, required=True)
    init_parser.add_argument("--contract", type=Path, required=True)
    status_parser = commands.add_parser("status", help="Compact state; safe to inspect while a run is executing")
    status_parser.add_argument("--workdir", type=Path, required=True)
    run_parser = commands.add_parser("run", help="Execute once per unique id; first valid run establishes the baseline")
    run_parser.add_argument("--workdir", type=Path, required=True)
    run_parser.add_argument("--id", required=True)
    run_parser.add_argument("--hypothesis", default="")
    decision_parser = commands.add_parser("decide", help="Keep an eligible candidate or restore only its managed files")
    decision_parser.add_argument("--workdir", type=Path, required=True)
    decision_parser.add_argument("--id", required=True)
    decision_parser.add_argument("--action", choices=("keep", "discard"), required=True)
    decision_parser.add_argument("--reason", required=True)
    recovery_parser = commands.add_parser("recover", help="Record an interrupted run without rerunning it")
    recovery_parser.add_argument("--workdir", type=Path, required=True)
    recovery_parser.add_argument("--id", required=True)
    recovery_parser.add_argument("--reason", required=True)
    recovery_parser.add_argument("--confirm-stopped", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.operation == "init":
            workdir = args.workdir if args.workdir.is_absolute() else args.project / args.workdir
            result = initialize(args.project, workdir, args.contract)
        else:
            workdir = args.workdir.resolve(strict=True)
            if args.operation == "status":
                result = status(workdir)
            elif args.operation == "run":
                result = run(workdir, args.id, args.hypothesis)
            elif args.operation == "decide":
                result = decide(workdir, args.id, args.action, args.reason)
            else:
                result = recover(workdir, args.id, args.reason, args.confirm_stopped)
        print(_encoded(result).decode("utf-8"))
        attempt = result.get("attempt", {})
        return 2 if attempt.get("outcome") not in (None, "ok") or attempt.get("status") == "rollback_conflict" else 0
    except (LoopError, OSError) as exc:
        print(_encoded({"error": str(exc)}).decode("utf-8"))
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
