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
import ast
import contextlib
import datetime as dt
import hashlib
import importlib.metadata
import importlib.util
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


_CAMPAIGN_SPEC = importlib.util.spec_from_file_location("ccfa_campaign_budget", Path(__file__).with_name("campaign_budget.py"))
CAMPAIGN = importlib.util.module_from_spec(_CAMPAIGN_SPEC)
_CAMPAIGN_SPEC.loader.exec_module(CAMPAIGN)


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
    optional = {"metric_guards", "tie_breaker", "protected_files", "dependency_preflight", "environment", "campaign", "evaluation"}
    if not isinstance(raw, dict) or not required.issubset(raw) or set(raw) - required - optional:
        raise LoopError("Contract requires: " + ", ".join(sorted(required)) + "; optional: " + ", ".join(sorted(optional)))
    for name in ("objective", "scientific_value"):
        if not isinstance(raw[name], str) or not raw[name].strip():
            raise LoopError(f"{name} must be nonempty text")
    if not isinstance(raw["constraints"], list) or not all(isinstance(v, str) and v.strip() for v in raw["constraints"]):
        raise LoopError("constraints must be a list of nonempty strings (an empty list is allowed)")
    all_names = []
    for field in ("editable_files", "evaluator_files", "data_files", "protected_files"):
        names = raw.get(field, [])
        if not isinstance(names, list) or (field in ("editable_files", "evaluator_files") and not names):
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
    guards = raw.get("metric_guards", [])
    if not isinstance(guards, list):
        raise LoopError("metric_guards must be a list")
    seen = set()
    for guard in guards:
        if not isinstance(guard, dict) or set(guard) - {"name", "min", "max"} or not {"name"}.issubset(guard):
            raise LoopError("Each metric guard requires name and min and/or max")
        name = guard["name"]
        bounds = set(guard) - {"name"}
        if not isinstance(name, str) or not name.strip() or name in seen or not bounds:
            raise LoopError("Metric guards need unique names and at least one bound")
        if any(not _finite(guard[key]) for key in bounds) or (bounds == {"min", "max"} and guard["min"] > guard["max"]):
            raise LoopError("Metric guard bounds must be finite and ordered")
        seen.add(name)
    if "tie_breaker" in raw:
        tie = raw["tie_breaker"]
        if not isinstance(tie, dict) or set(tie) != {"name", "direction", "min_delta", "max_primary_loss"}:
            raise LoopError("tie_breaker requires name, direction, min_delta, max_primary_loss")
        if not isinstance(tie["name"], str) or not tie["name"].strip() or tie["name"] == metric["name"] or tie["direction"] not in ("min", "max"):
            raise LoopError("tie_breaker needs a distinct metric name and min|max direction")
        if any(not _finite(tie[key]) or tie[key] < 0 for key in ("min_delta", "max_primary_loss")):
            raise LoopError("tie_breaker tolerances must be finite and nonnegative")
    if raw.get("dependency_preflight", "strict") not in ("strict", "report"):
        raise LoopError("dependency_preflight must be strict or report")
    if "environment" in raw:
        environment = raw["environment"]
        if not isinstance(environment, dict) or set(environment) - {"variables", "packages"}:
            raise LoopError("environment accepts variables and packages name lists")
        for key in ("variables", "packages"):
            values = environment.get(key, [])
            if (not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values)
                    or len(values) != len(set(values))):
                raise LoopError("environment variables/packages require unique nonempty names")
    if "campaign" in raw:
        campaign = raw["campaign"]
        if (not isinstance(campaign, dict) or set(campaign) != {"id", "record"}
                or not isinstance(campaign["id"], str) or not campaign["id"].strip()):
            raise LoopError("campaign requires id and project-relative record")
        _relative(campaign["record"])
    if "evaluation" in raw:
        evaluation = raw["evaluation"]
        if (not isinstance(evaluation, dict) or set(evaluation) - {"split_role", "task_set_id", "frozen_candidate", "task_files", "reused_final"}
                or evaluation.get("split_role") not in ("development", "selection", "final")
                or not isinstance(evaluation.get("task_set_id"), str) or not evaluation["task_set_id"].strip()):
            raise LoopError("evaluation requires split_role and a nonempty task_set_id")
        frozen = evaluation.get("frozen_candidate")
        if evaluation["split_role"] == "final":
            if (not isinstance(frozen, dict) or set(frozen) != {"workdir", "candidate_id"}
                    or not isinstance(frozen["candidate_id"], str) or not frozen["candidate_id"]):
                raise LoopError("final evaluation requires frozen_candidate workdir and candidate_id")
            _relative(frozen["workdir"])
        elif frozen is not None:
            raise LoopError("frozen_candidate is only valid for final evaluation")
        tasks = evaluation.get("task_files", raw["data_files"])
        if (not isinstance(tasks, list) or not tasks or any(not isinstance(name, str) or name not in all_names for name in tasks)
                or len(tasks) != len(set(tasks)) or set(tasks).intersection(raw["editable_files"])):
            raise LoopError("evaluation.task_files must identify nonempty unique protected task/split files; defaults to data_files")
        reuse = evaluation.get("reused_final")
        if reuse is not None:
            if (evaluation["split_role"] == "final" or not isinstance(reuse, dict) or set(reuse) != {"task_set_id", "reason"}
                    or any(not isinstance(v, str) or not v.strip() for v in reuse.values())
                    or reuse["task_set_id"] == evaluation["task_set_id"] or "campaign" not in raw):
                raise LoopError("reused_final requires an explicit reason, new non-final task_set_id and shared campaign record")
    return raw


def _protected(contract):
    return contract["evaluator_files"] + contract["data_files"] + contract.get("protected_files", [])


def _task_identity(contract, protected_manifest):
    evaluation = contract.get("evaluation")
    if not evaluation:
        return None
    names = evaluation.get("task_files", contract["data_files"])
    files = {name: protected_manifest[name] for name in names}
    return {"id": evaluation["task_set_id"], "files": files,
            "content_hash": _hash(sorted(info["sha256"] for info in files.values())),
            "scope": "declared task/split content identity only; not a proof of semantic non-overlap"}


def _environment_identity(project, contract):
    specification = contract.get("environment")
    if specification is None:
        return None
    command = contract["command"][0]
    executable = str(project / command) if any(separator in command for separator in ("/", "\\")) and not Path(command).is_absolute() else shutil.which(command)
    if executable is None or not Path(executable).is_file():
        raise LoopError("Cannot identify the declared command executable for environment checks")
    executable = Path(executable).resolve()
    packages = {}
    if specification.get("packages") and executable != Path(sys.executable).resolve():
        raise LoopError("Package identity checks require the controller's Python executable; use an environment lockfile otherwise")
    for name in specification.get("packages", []):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError as exc:
            raise LoopError(f"Declared environment package is not installed: {name}") from exc
    return {"executable": str(executable), "executable_sha256": _file_info(executable)["sha256"],
            "controller_python": sys.version.split()[0], "platform": sys.platform, "packages": packages,
            "variables": {name: _hash(os.environ.get(name)) for name in specification.get("variables", [])}}


def _dependency_preflight(project, contract):
    """Diagnose literal local inputs/imports; never claim dynamic dependency closure."""
    declared = set(contract["editable_files"] + _protected(contract))
    missing = set()

    def record(path, owner):
        try:
            path = path.resolve()
            if path.is_relative_to(project) and path.is_file():
                relative = path.relative_to(project).as_posix()
                if relative not in declared:
                    missing.add((owner, relative))
        except OSError:
            pass

    def literal(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "Path" and node.args:
            return literal(node.args[0])
        return None

    for name in sorted(declared):
        path = _file(project, name)
        if path.suffix != ".py" or not path.is_file():
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=name)
        except (SyntaxError, UnicodeError):
            continue  # The real evaluator reports invalid source; do not execute it here.
        assigned = {node.targets[0].id: literal(node.value) for node in ast.walk(tree)
                    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)}
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                modules = ([alias.name for alias in node.names] if isinstance(node, ast.Import)
                           else [node.module] if node.module else [alias.name for alias in node.names])
                base = path.parent if isinstance(node, ast.ImportFrom) and node.level else project
                if isinstance(node, ast.ImportFrom):
                    for _ in range(max(0, node.level - 1)):
                        base = base.parent
                for module in modules:
                    bases = [base] if isinstance(node, ast.ImportFrom) and node.level else [path.parent, project]
                    for origin in bases:
                        local = origin.joinpath(*module.split("."))
                        record(local.with_suffix(".py"), name)
                        record(local / "__init__.py", name)
                        if isinstance(node, ast.ImportFrom) and node.module:
                            for alias in node.names:
                                if alias.name != "*":
                                    record((local / alias.name).with_suffix(".py"), name)
                                    record(local / alias.name / "__init__.py", name)
                        for depth in range(1, len(module.split("."))):
                            record(origin.joinpath(*module.split(".")[:depth]) / "__init__.py", name)
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name) and node.func.id == "open" and node.args:
                mode = literal(node.args[1]) if len(node.args) > 1 else next((literal(k.value) for k in node.keywords if k.arg == "mode"), "r")
                value = literal(node.args[0])
            elif isinstance(node.func, ast.Attribute) and node.func.attr in ("read_text", "read_bytes", "open"):
                mode = literal(node.args[0]) if node.func.attr == "open" and node.args else "r"
                receiver = node.func.value
                value = assigned.get(receiver.id) if isinstance(receiver, ast.Name) else literal(receiver)
            else:
                continue
            if value and mode and "r" in mode:
                record(project / value, name)
    for argument in contract["command"][1:]:
        if "{" not in argument:
            record(project / argument, "command")
    result = {"method": "existing literal local reads/imports and argv files only; dynamic access is not inferred",
              "unlisted_local_inputs": [{"source": owner, "path": name} for owner, name in sorted(missing)],
              "mode": contract.get("dependency_preflight", "strict")}
    if missing and result["mode"] == "strict":
        raise LoopError("Unlisted local dependencies; declare them as editable/data/protected files before comparison: "
                        + ", ".join(sorted({name for _, name in missing})))
    return result


def _campaign(project, contract):
    specification = contract.get("campaign")
    if specification is None:
        return None
    return _file(project, specification["record"]), specification["id"], project


def _campaign_call(name, binding, *args):
    try:
        return getattr(CAMPAIGN, name)(*binding, *args)
    except CAMPAIGN.CampaignError as exc:
        raise LoopError(str(exc)) from exc


def _reservation_key(project, workdir, run_id):
    return workdir.relative_to(project).as_posix() + ":" + run_id


def _settle_shared(workdir, state, contract, attempt, unknown=False):
    binding = _campaign(Path(state["project"]), contract)
    if binding and attempt.get("campaign_reservation"):
        return _campaign_call("settle", binding, attempt["campaign_reservation"],
                              None if unknown else attempt["budget_charge_seconds"], attempt.get("outcome"))


def _campaign_evaluation(contract, task_identity):
    evaluation = contract.get("evaluation")
    return None if not evaluation else dict(evaluation, task_content_hash=task_identity["content_hash"])


def _final_use(contract, state, manifest):
    if contract.get("evaluation", {}).get("split_role") != "final":
        return None
    return {
        "task_content_hash": state["task_set_identity"]["content_hash"],
        "candidate_id": contract["evaluation"]["frozen_candidate"]["candidate_id"],
        "candidate_hash": _hash(manifest),
        "protocol_hash": _hash({
            "command": contract["command"], "locked_files": state["locked_files"],
            "environment": state.get("environment_identity"),
            **{name: contract.get(name) for name in ("metric", "metric_guards", "tie_breaker")},
        }),
    }


def _final_source(project, workdir, contract, manifest):
    evaluation = contract.get("evaluation", {})
    if evaluation.get("split_role") != "final":
        return
    reference = evaluation["frozen_candidate"]
    source_dir = project / reference["workdir"]
    if source_dir.resolve() == workdir.resolve():
        raise LoopError("Final evaluation must reference a separate selection record")
    _file(project, reference["workdir"] + "/contract.json")
    source = _load(source_dir)
    source_contract = _integrity(source_dir, source)
    source_evaluation = source_contract.get("evaluation", {})
    if source_evaluation.get("split_role") != "selection" or source_evaluation.get("task_set_id") == evaluation["task_set_id"]:
        raise LoopError("Final evaluation needs a distinct task-set identity and a selection-stage source")
    identity = _task_identity(contract, _manifest(project, _protected(contract), required=True))
    previous_identity = source.get("task_set_identity")
    if previous_identity is None or previous_identity["content_hash"] == identity["content_hash"]:
        raise LoopError("Final task/split content matches selection; a different display name is not held-out identity")
    selected = next((attempt for attempt in source["attempts"].values()
                     if attempt.get("status") == "kept" and attempt.get("candidate_id") == reference["candidate_id"]), None)
    if selected is not None:
        _metric_evidence(source_dir, selected)
    if selected is None or _invalid_observation(selected) or selected["manifest"] != manifest:
        raise LoopError("Final evaluation bytes must match the referenced retained selection candidate")


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
    project = Path(state["project"])
    actual = _manifest(project, _protected(contract), required=True)
    if actual != state["locked_files"]:
        raise LoopError("Frozen evaluator/data changed; restore the known version or start a new experiment")
    if _environment_identity(project, contract) != state.get("environment_identity"):
        raise LoopError("Frozen environment identity changed; restore it or establish a corrected comparison")
    state["dependency_preflight"] = _dependency_preflight(project, contract)
    if state["best"] is not None:
        anchors = ([item for item in state["attempts"].values() if item["status"] == "kept"]
                   if "tie_breaker" in contract else [state["attempts"][state["best"]]])
        for anchor in anchors:
            _metric_evidence(workdir, anchor)
            if _invalid_observation(anchor):
                raise LoopError("Retained comparison evidence was marked invalid; correct the interpretation explicitly or establish a corrected protocol")
    return contract


def _checked(workdir, state):
    try:
        contract = _integrity(workdir, state)
        verification = {"checked_at": _now(), "contract_hash": state["contract_hash"],
                        "protected_manifest_hash": _hash(state["locked_files"]),
                        "environment_identity_hash": _hash(state.get("environment_identity")),
                        "scope": "declared files and selected environment identities; not an OS sandbox or dynamic dependency closure"}
        _event(workdir, state, "integrity_checked", update={"last_verified": verification,
                                                          "dependency_preflight": state["dependency_preflight"]})
        return contract
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
    if workdir.exists() and (not workdir.is_dir() or any(workdir.iterdir())):
        raise LoopError("Experiment directory is not empty; use status to resume, never reinitialize")
    # Explicit caller-specified task paths are supported; no generic output
    # directory is chosen by the script.
    contract = _contract(_json(contract_path))
    resolved = []
    for name in contract["editable_files"] + _protected(contract):
        path = _file(project, name)
        if path.is_relative_to(workdir):
            raise LoopError("Declared input files cannot live in the experiment evidence directory")
        for previous in resolved:
            if os.path.normcase(str(path.resolve())) == os.path.normcase(str(previous.resolve())) or (
                path.exists() and previous.exists() and os.path.samefile(path, previous)
            ):
                raise LoopError("Declared paths must identify different files, including case aliases and hardlinks")
        resolved.append(path)
    locked = _manifest(project, _protected(contract), required=True)
    environment = _environment_identity(project, contract)
    preflight = _dependency_preflight(project, contract)
    task_identity = _task_identity(contract, locked)
    current = _manifest(project, contract["editable_files"])
    _final_source(project, workdir, contract, current)
    binding = _campaign(project, contract)
    if binding:
        if contract["campaign"]["record"] in contract["editable_files"] + _protected(contract):
            raise LoopError("The shared budget record cannot be an editable or frozen experiment input")
        _campaign_call("register", binding, workdir, _campaign_evaluation(contract, task_identity), True)
    workdir.mkdir(parents=True, exist_ok=True)
    with _lock(workdir):
        if any(item.name != ".lock" for item in workdir.iterdir()):
            raise LoopError("Experiment directory is not empty; use status to resume, never reinitialize")
        manifest = _snapshot(project, contract["editable_files"], workdir / "initial" / "snapshot")
        _write_json(workdir / "contract.json", contract)
        state = {"seq": 0, "attempts": {}}
        _event(workdir, state, "initialized", update={
            "schema": 1, "project": str(project), "contract_hash": _hash(contract),
            "locked_files": locked, "objective": contract["objective"],
            "initial": {"manifest": manifest, "snapshot": "initial/snapshot"},
            "best": None, "pending": None, "attempt_count": 0, "charged_seconds": 0.0,
            "budgets": contract["budgets"],
            "environment_identity": environment, "dependency_preflight": preflight,
            "evaluation": contract.get("evaluation"), "finalized": None,
            "task_set_identity": task_identity,
            "last_verified": {"checked_at": _now(), "contract_hash": _hash(contract),
                              "protected_manifest_hash": _hash(locked), "environment_identity_hash": _hash(environment),
                              "scope": "declared files and selected environment identities; not an OS sandbox or dynamic dependency closure"},
        })
        # Local evidence commits first. Registration is idempotent and run()
        # completes it after interruption; a failed snapshot creates no shared
        # task identity. Neither retry path replays an evaluator.
        if binding:
            _campaign_call("register", binding, workdir, _campaign_evaluation(contract, task_identity))
        return _summary(workdir, state, contract)


def _read_measurements(path, contract):
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 1024 * 1024:
        raise LoopError("Evaluator must write a fresh regular metrics JSON file (at most 1 MiB)")
    raw = path.read_bytes()
    try:
        result = _parse_json(raw)
    except (UnicodeError, ValueError) as exc:
        raise LoopError(f"Cannot read metrics JSON: {exc}") from exc
    names = {contract["metric"]["name"]}
    names.update(guard["name"] for guard in contract.get("metric_guards", []))
    if "tie_breaker" in contract:
        names.add(contract["tie_breaker"]["name"])
    for name in names:
        if not isinstance(result, dict) or name not in result or not _finite(result[name]):
            raise LoopError(f"Metric {name!r} must be one finite JSON number, not bool or text")
    # Preserve exact integer metrics (e.g. counts above 2**53).
    return {name: result[name] for name in sorted(names)}, hashlib.sha256(raw).hexdigest()


def _guard_failures(measurements, contract):
    return [guard["name"] for guard in contract.get("metric_guards", [])
            if ("min" in guard and measurements[guard["name"]] < guard["min"])
            or ("max" in guard and measurements[guard["name"]] > guard["max"])]


def _selection(attempt, parent, state, contract):
    direction = 1 if contract["metric"]["direction"] == "max" else -1
    gain = direction * (attempt["metric"] - parent["metric"])
    if not _finite(gain):
        raise LoopError("Metric delta exceeds the supported finite numeric range")
    failures = _guard_failures(attempt["measurements"], contract)
    result = {"improvement": gain, "guard_failures": failures, "eligible": False,
              "selection_reason": "metric_guard_failed" if failures else "insufficient_improvement"}
    if failures:
        return result
    if gain > contract["metric"]["min_delta"]:
        return dict(result, eligible=True, selection_reason="primary_improvement")
    tie = contract.get("tie_breaker")
    if tie:
        # Anchor tolerable loss to the best accepted primary value, not the
        # latest cost-saving candidate: repeated small losses cannot drift.
        anchor = max(direction * item["metric"] for item in state["attempts"].values()
                     if item["status"] == "kept")
        loss = anchor - direction * attempt["metric"]
        change = attempt["measurements"][tie["name"]] - parent["measurements"][tie["name"]]
        improvement = change if tie["direction"] == "max" else -change
        if not _finite(loss) or not _finite(improvement):
            raise LoopError("Tie-break comparison exceeds the supported finite numeric range")
        if loss <= tie["max_primary_loss"] and improvement > tie["min_delta"]:
            result.update(eligible=True, selection_reason="bounded_quality_cost_improvement")
    return result


def _metric_evidence(workdir, attempt):
    path = workdir / attempt["metrics"]
    if not path.is_file() or path.is_symlink() or _file_info(path)["sha256"] != attempt.get("metrics_sha256"):
        raise LoopError(f"Raw metrics evidence changed or is missing for {attempt['id']}; cannot use this evaluation")


def _stop(process):
    """Best-effort process-tree termination; this cannot undo external effects."""
    tree_confirmed = True
    if os.name == "nt":
        try:
            stopped = subprocess.run(
                ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5,
            )
            tree_result = f"taskkill_exit_{stopped.returncode}"
            tree_confirmed = stopped.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            tree_result = "tree_termination_unconfirmed"
            tree_confirmed = False
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
    if not tree_confirmed:
        raise LoopError(
            f"Evaluator process-tree termination is unconfirmed ({tree_result}); "
            "pending run retained. Inspect surviving workers, then recover explicitly"
        )
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


def _check_recorded_attempt(workdir, state, attempt):
    """Idempotent reuse must still reject stale or invalid recorded evidence."""
    _checked(workdir, state)
    if attempt["outcome"] == "ok":
        _metric_evidence(workdir, attempt)
        if _invalid_observation(attempt):
            raise LoopError("Recorded evaluation was marked invalid; inspect or correct its interpretation before reuse")


def run(workdir, run_id, hypothesis="", replicate_of=None):
    with _lock(workdir):
        state = _load(workdir)
        # Repeating a completed or started ID never repeats the subprocess.
        if run_id in state["attempts"]:
            attempt = state["attempts"][run_id]
            _check_recorded_attempt(workdir, state, attempt)
            return {"replayed": False, "already_recorded": True, "attempt": attempt}
        contract = _checked(workdir, state)
        if state["pending"] is not None:
            raise LoopError(f"Resolve pending run {state['pending']} with decide/recover before another run")
        budgets = contract["budgets"]
        remaining = budgets["max_seconds"] - state["charged_seconds"]
        if state["attempt_count"] >= budgets["max_attempts"] or remaining <= 0:
            raise LoopError("Experiment attempt or execution-time budget is exhausted")
        project = Path(state["project"])
        current = _manifest(project, contract["editable_files"])
        final = contract.get("evaluation", {}).get("split_role") == "final"
        if final:
            if state.get("finalized") is not None:
                raise LoopError("Final evaluation is report-only and already completed; do not reuse it for tuning")
            if replicate_of is not None:
                raise LoopError("A final task set does not accept adaptive replication; freeze repeated measurements inside its evaluator protocol")
            if current != state["initial"]["manifest"]:
                raise LoopError("Final evaluation candidate is frozen; edits cannot be evaluated on final tasks")
            _final_source(project, workdir, contract, current)
        source = None
        if replicate_of is not None:
            if not isinstance(hypothesis, str) or not hypothesis.strip():
                raise LoopError("Replication requires a reason describing the repeated measurement")
            source_id = state["best"] if replicate_of == "best" else replicate_of
            source = state["attempts"].get(source_id)
            if source is None or source["outcome"] != "ok" or _invalid_observation(source):
                raise LoopError("Replication requires an existing valid measured candidate")
            _metric_evidence(workdir, source)
            if current != source["manifest"]:
                raise LoopError("Replication must use the source candidate's identical managed bytes")
        baseline = state["best"] is None
        if baseline and current != state["initial"]["manifest"]:
            raise LoopError("Run the initial snapshot as baseline before editing a candidate")
        if not baseline and source is None:
            if not isinstance(hypothesis, str) or not hypothesis.strip():
                raise LoopError("A candidate needs --hypothesis describing the proposed mechanism/change")
            if current == _target(state)["manifest"]:
                raise LoopError("Candidate is unchanged from its parent; no subprocess was started")
        previous_evaluations = [
            previous["id"] for previous in state["attempts"].values()
            if previous["outcome"] == "ok" and current == previous["manifest"]
        ]
        destination = _attempt_dir(workdir, run_id)
        if destination.exists():
            raise LoopError("Unrecorded attempt directory exists; inspect it instead of overwriting evidence")
        limit = min(budgets["timeout_seconds"], remaining)
        binding = _campaign(project, contract)
        reservation = _reservation_key(project, workdir, run_id) if binding else None
        if binding:
            _campaign_call("register", binding, workdir, _campaign_evaluation(contract, state.get("task_set_identity")))
            limit = _campaign_call("reserve", binding, reservation, limit, workdir, run_id,
                                   _final_use(contract, state, current))
        try:
            destination.mkdir(parents=True)
            manifest = _snapshot(project, contract["editable_files"], destination / "snapshot")
        except (OSError, LoopError):
            if binding:
                _campaign_call("settle", binding, reservation, 0.0, "not_started")
            raise
        parent_id = state["best"]
        candidate_id = (contract["evaluation"]["frozen_candidate"]["candidate_id"] if final else
                        source["candidate_id"] if source else _hash({
            "contract": state["contract_hash"], "parent": parent_id,
            "parent_candidate": None if baseline else _target(state)["candidate_id"], "manifest": manifest,
        }))
        metrics_path = destination / "metrics.json"
        argv = [
            arg.replace("{metrics}", str(metrics_path)).replace("{attempt_dir}", str(destination))
            for arg in contract["command"]
        ]
        if state.get("environment_identity") is not None:
            argv[0] = state["environment_identity"]["executable"]
        attempt = {
            "id": run_id, "kind": "final" if final else "replication" if source else "baseline" if baseline else "candidate",
            "candidate_id": candidate_id, "parent": parent_id, "hypothesis": hypothesis,
            "previous_evaluations": previous_evaluations,
            "manifest": manifest, "snapshot": str((destination / "snapshot").relative_to(workdir)).replace("\\", "/"),
            "status": "running", "outcome": None, "started_at": _now(), "pid": None,
            "reserved_seconds": limit, "argv": argv, "metric": None,
            "stdout": f"attempts/{run_id}/stdout.log", "stderr": f"attempts/{run_id}/stderr.log",
            "metrics": f"attempts/{run_id}/metrics.json",
            "environment": {"python": sys.version.split()[0], "platform": sys.platform,
                            "executable": shutil.which(argv[0])},
        }
        if source:
            attempt["replicate_of"] = source["id"]
            attempt["measurement_parent"] = source["id"]
        if "evaluation" in contract:
            attempt["evaluation"] = contract["evaluation"]
        if binding:
            attempt["campaign_reservation"] = reservation
        try:
            _event(workdir, state, "run_started", attempt=attempt, update={
                "pending": run_id, "attempt_count": state["attempt_count"] + 1,
            })
        except (OSError, LoopError):
            if binding:
                _campaign_call("settle", binding, reservation, 0.0, "not_started")
            raise
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
                attempt["measurements"], attempt["metrics_sha256"] = _read_measurements(metrics_path, contract)
                attempt["metric"] = attempt["measurements"][contract["metric"]["name"]]
                if baseline and not final and _guard_failures(attempt["measurements"], contract):
                    outcome, error = "constraint_violation", "Initial baseline violates frozen metric guards"
            except (LoopError, OSError) as exc:
                outcome, error = "invalid_metric", str(exc)
        attempt.update(outcome=outcome, status="evaluated", error=error, elapsed_seconds=elapsed, budget_charge_seconds=elapsed)
        _event(workdir, state, "run_finished", attempt=attempt, update={
            "charged_seconds": state["charged_seconds"] + elapsed,
        })
        _settle_shared(workdir, state, contract, attempt)
        if outcome != "ok":
            attempt = _discard(workdir, state, attempt, error or outcome)
        elif source or final:
            attempt.update(status="reporting", eligible=False, decision="report",
                           guard_failures=_guard_failures(attempt["measurements"], contract),
                           selection_reason="final_report_only" if final else "replication_report_only")
            _event(workdir, state, "report_started", attempt=attempt)
            conflicts = [] if final else _restore(workdir, state, attempt)
            if conflicts:
                attempt.update(status="rollback_conflict", conflicts=conflicts)
                _event(workdir, state, "rollback_conflict", attempt=attempt)
            else:
                attempt.update(status="reported", conflicts=[])
                update = {"pending": None}
                if final:
                    update["finalized"] = run_id
                _event(workdir, state, "measurement_reported", attempt=attempt, update=update)
        elif baseline:
            attempt.update(status="kept", decision="keep", reason="Initial measured baseline")
            _event(workdir, state, "baseline_kept", attempt=attempt, update={"best": run_id, "pending": None})
        else:
            try:
                selection = _selection(attempt, state["attempts"][parent_id], state, contract)
            except LoopError as exc:
                attempt.update(outcome="invalid_metric", error=str(exc))
                _event(workdir, state, "invalid_metric", attempt=attempt)
                return {"attempt": _discard(workdir, state, attempt, attempt["error"])}
            attempt.update(selection, status="awaiting_decision")
            _event(workdir, state, "awaiting_decision", attempt=attempt)
        return {"attempt": attempt}


def replicate(workdir, run_id, source_id, reason):
    """Measure identical bytes again without using noise to promote a candidate."""
    return run(workdir, run_id, reason, replicate_of=source_id)


def decide(workdir, run_id, action, reason):
    if action not in ("keep", "discard"):
        raise LoopError("Decision action must be keep or discard")
    if not reason.strip():
        raise LoopError("Decision requires a concrete reason; metric improvement alone is not novelty evidence")
    with _lock(workdir):
        state = _load(workdir)
        attempt = state["attempts"].get(run_id)
        if attempt is None:
            raise LoopError("Unknown run id")
        if attempt.get("kind") in ("final", "replication"):
            raise LoopError("Final and replication measurements are report-only; they cannot be promoted")
        if attempt["status"] in ("kept", "discarded"):
            if attempt.get("decision") != action:
                raise LoopError("Completed decisions are immutable")
            if action == "keep":
                _check_recorded_attempt(workdir, state, attempt)
            return {"already_recorded": True, "attempt": attempt}
        if state["pending"] != run_id or attempt["status"] not in ("awaiting_decision", "deciding", "rollback_conflict"):
            raise LoopError("Run is not ready for decide; inspect status and use recover after its process and workers have stopped")
        if action == "discard":
            return {"attempt": _discard(workdir, state, attempt, reason)}
        contract = _checked(workdir, state)
        if (attempt["outcome"] != "ok" or not attempt.get("eligible")
                or _invalid_observation(attempt)):
            raise LoopError("Keep requires valid measurements satisfying the frozen selection rule and metric guards")
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
        contract = _checked(workdir, state)
        attempt = state["attempts"].get(run_id)
        if attempt is None or state["pending"] != run_id:
            raise LoopError("No matching pending attempt")
        if (attempt["status"] in ("deciding", "reporting", "rollback_conflict") or
                (attempt["status"] == "evaluated" and attempt.get("kind") in ("final", "replication")
                 and attempt["outcome"] == "ok")):
            if attempt.get("kind") in ("final", "replication") and attempt["outcome"] == "ok":
                _metric_evidence(workdir, attempt)
                if _invalid_observation(attempt):
                    raise LoopError("Recorded evaluation was marked invalid; resolve it before completing its report")
                conflicts = [] if attempt["kind"] == "final" else _restore(workdir, state, attempt)
                if conflicts:
                    raise LoopError("Reconcile managed-file conflicts before completing the measurement report")
                attempt = dict(attempt, status="reported", conflicts=[], eligible=False, decision="report",
                               guard_failures=_guard_failures(attempt["measurements"], contract),
                               selection_reason="final_report_only" if attempt["kind"] == "final" else "replication_report_only")
                update = {"pending": None}
                if attempt["kind"] == "final":
                    update["finalized"] = run_id
                _settle_shared(workdir, state, contract, attempt)
                _event(workdir, state, "measurement_reported", attempt=attempt, update=update)
                return {"attempt": attempt}
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
            _settle_shared(workdir, state, contract, attempt, unknown=True)
        elif attempt["status"] != "evaluated":
            raise LoopError("Completed evaluation requires decide, not recovery")
        else:
            _settle_shared(workdir, state, contract, attempt)
        # An interrupted transaction is never silently promoted, even if a
        # metrics file happens to exist.
        return {"attempt": _discard(workdir, state, attempt, reason)}


def recover_reservation(workdir, run_id, reason, confirm_stopped=False):
    """Close an orphan shared reservation without guessing or replaying work."""
    if not confirm_stopped or not isinstance(reason, str) or not reason.strip():
        raise LoopError("Reservation recovery requires --confirm-stopped and a reason after checking workers")
    with _lock(workdir):
        state = _load(workdir)
        contract = _checked(workdir, state)
        if run_id in state["attempts"]:
            raise LoopError("A recorded attempt exists; use its normal recover/decide workflow")
        project = Path(state["project"])
        binding = _campaign(project, contract)
        if binding is None:
            raise LoopError("No shared campaign budget is attached")
        key = _reservation_key(project, workdir, run_id)
        result = _campaign_call("settle", binding, key, None)
        _event(workdir, state, "orphan_reservation_closed", details={"reservation": key, "reason": reason})
        return {"campaign_budget": result, "replayed": False,
                "note": "Unknown duration closes remaining shared allowance; managed inputs and partial evidence were preserved"}


OBSERVATION_CATEGORIES = (
    "environment_error", "implementation_error", "invalid_comparison",
    "negative_result", "supports_prediction", "inconclusive",
)
INVALID_OBSERVATIONS = {"environment_error", "implementation_error", "invalid_comparison"}


def _invalid_observation(attempt):
    return (attempt.get("invalidated_by") is not None
            or attempt.get("observation", {}).get("category") in INVALID_OBSERVATIONS)


def note(workdir, run_id, category, finding, next_action, evidence, corrects=None):
    """Record a host interpretation separately from immutable measurements."""
    if category not in OBSERVATION_CATEGORIES:
        raise LoopError("Unknown observation category")
    for value in (finding, next_action):
        if not isinstance(value, str) or not value.strip() or len(value) > 4000:
            raise LoopError("Finding and next action must contain 1-4000 characters")
    if not evidence or len(evidence) > 8 or len(set(evidence)) != len(evidence):
        raise LoopError("Provide 1-8 distinct task-relative evidence paths")
    if corrects is not None and (type(corrects) is not int or corrects < 1):
        raise LoopError("corrects must identify the invalidation event sequence")
    with _lock(workdir):
        state = _load(workdir)
        attempt = state["attempts"].get(run_id)
        if attempt is None or attempt["status"] not in ("kept", "discarded", "awaiting_decision", "reported"):
            raise LoopError("Interpret only a completed measurement or recorded failure")
        if category in ("negative_result", "supports_prediction", "inconclusive") and attempt["outcome"] != "ok":
            raise LoopError("An execution failure is not a scientific result")
        if attempt["outcome"] == "ok":
            _metric_evidence(workdir, attempt)
        anchors = {}
        for relative in evidence:
            path = _file(workdir, relative)
            if not path.is_file():
                raise LoopError("Observation evidence must be an existing task file")
            anchors[relative] = _file_info(path)["sha256"]
        observation = {"category": category, "finding": finding, "next_action": next_action,
                       "evidence": anchors, "origin": "host_interpretation"}
        if corrects is not None:
            observation["corrects"] = corrects
        if attempt.get("observation") == observation:
            return {"already_recorded": True, "attempt": attempt}
        invalidated_by = attempt.get("invalidated_by")
        if corrects is not None:
            if corrects != invalidated_by or category in INVALID_OBSERVATIONS:
                raise LoopError("Correction must name the active invalidation and explain its resolved interpretation")
            invalidated_by = None
        elif category in INVALID_OBSERVATIONS:
            invalidated_by = state["seq"] + 1
        attempt = dict(attempt, observation=observation, invalidated_by=invalidated_by,
                       observation_event_seq=state["seq"] + 1)
        _event(workdir, state, "observation", attempt=attempt)
        return {"attempt": attempt}


def context(workdir, query="", limit=3, fast=False):
    """Return matching past attempts without loading raw logs into a prompt."""
    if type(limit) is not int or not 1 <= limit <= 20 or not isinstance(query, str) or len(query) > 500:
        raise LoopError("Context needs a query of at most 500 characters and limit 1-20")
    state = _load(workdir)
    result = _status_from_state(workdir, state, fast=fast)
    terms = query.casefold().split()
    ranked = []
    for index, attempt in enumerate(state["attempts"].values()):
        text = " ".join(str(attempt.get(key, "")) for key in ("id", "hypothesis", "reason", "observation")).casefold()
        hits = sum(term in text for term in terms)
        if terms and not hits:
            continue
        ranked.append((hits, index, attempt))
    cards = []
    for _, _, attempt in sorted(ranked, key=lambda item: (item[0], item[1]), reverse=True)[:limit]:
        card = {key: attempt.get(key) for key in (
            "id", "kind", "candidate_id", "parent", "replicate_of", "measurement_parent", "evaluation",
            "hypothesis", "outcome", "decision", "metric", "measurements",
            "elapsed_seconds", "reason", "observation", "invalidated_by", "observation_event_seq",
            "snapshot", "stdout", "stderr", "metrics")}
        issues = []
        if attempt["outcome"] == "ok" and not fast:
            try:
                _metric_evidence(workdir, attempt)
            except LoopError as exc:
                issues.append(str(exc))
        for relative, expected in (() if fast else attempt.get("observation", {}).get("evidence", {}).items()):
            try:
                actual = _file_info(_file(workdir, relative))
                if actual is None or actual["sha256"] != expected:
                    issues.append("Observation evidence changed: " + relative)
            except (LoopError, OSError) as exc:
                issues.append(str(exc))
        card["evidence_issues"] = issues
        card["evidence_rechecked"] = not fast
        cards.append(card)
    result["related_attempts"] = cards
    result["retrieval"] = {"query": query, "limit": limit, "matching_attempts": len(ranked),
                           "method": "literal term matching; not semantic or scientific ranking"}
    return result


def _summary(workdir, state, contract):
    pending = state["attempts"].get(state["pending"])
    reserved = pending["reserved_seconds"] if pending and pending["status"] == "running" else 0
    best = state["attempts"].get(state["best"])
    if pending:
        if pending["status"] == "running":
            next_action = "inspect process; recover only after it and its children stop"
        elif pending["status"] == "evaluated":
            next_action = "inspect completed evidence and confirm workers stopped; recover the unfinished transaction without rerunning"
        elif pending["status"] in ("deciding", "rollback_conflict"):
            next_action = "reconcile managed-file conflicts, then retry decide --action discard"
        else:
            next_action = "inspect measured evidence, then decide keep or discard"
    elif state["attempt_count"] >= state["budgets"]["max_attempts"] or state["charged_seconds"] >= state["budgets"]["max_seconds"]:
        next_action = "stop: experiment budget exhausted"
    elif best is None:
        next_action = ("final evaluation completed; report frozen candidate results without selection or tuning"
                       if state.get("finalized") else "run unchanged frozen candidate for final report"
                       if contract.get("evaluation", {}).get("split_role") == "final"
                       else "run unchanged initial files as baseline")
    else:
        next_action = "host proposes and edits one allowed candidate, then run with a new id"
    result = {
        "event_seq": state["seq"],
        "objective": state["objective"], "constraints": contract["constraints"],
        "scientific_value": contract["scientific_value"], "contract_hash": state["contract_hash"],
        "best": None if best is None else {key: best.get(key) for key in ("id", "candidate_id", "metric", "measurements", "hypothesis", "elapsed_seconds")},
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
            {key: item.get(key) for key in ("id", "parent", "hypothesis", "outcome", "error", "snapshot", "stdout", "stderr", "metrics")}
            for item in list(state["attempts"].values()) if item["outcome"] not in (None, "ok")
        ][-3:],
        "recent_decisions": [
            {key: item.get(key) for key in ("id", "parent", "hypothesis", "outcome", "metric", "decision", "reason", "snapshot", "metrics")}
            for item in state["attempts"].values() if item.get("decision")
        ][-3:],
        "next_action": next_action,
        "paths": {"workdir": str(workdir), "events": str(workdir / "events.jsonl"),
                  "contract": str(workdir / "contract.json"), "attempts": str(workdir / "attempts")},
    }
    result["declared_integrity"] = {"protected_files": _protected(contract),
                                    "dynamic_dependency_closure": False,
                                    "dependency_preflight": state.get("dependency_preflight")}
    result["last_verified"] = state.get("last_verified")
    if "evaluation" in contract:
        result["evaluation"] = contract["evaluation"]
        result["task_set_identity"] = state.get("task_set_identity")
        result["finalized"] = state.get("finalized")
    binding = _campaign(Path(state["project"]), contract)
    if binding:
        result["campaign_budget"] = _campaign_call("status", binding)
    return result


def status(workdir, fast=False):
    # Reads can observe an active run without taking its exclusive writer lock.
    return _status_from_state(workdir, _load(workdir), fast=fast)


def _status_from_state(workdir, state, fast=False):
    contract = _contract(_json(workdir / "contract.json"))
    result = _summary(workdir, state, contract)
    if fast:
        result["integrity"] = "not_rechecked"
        result["verification"] = {"rechecked": False, "basis": "last_verified is a prior receipt, not current file validation"}
        return result
    try:
        _integrity(workdir, state)
        result["integrity"] = "ok"
        result["declared_integrity"]["dependency_preflight"] = state.get("dependency_preflight")
        result["verification"] = {"rechecked": True, "passed": True, "checked_at": _now(), "contract_hash": state["contract_hash"]}
    except LoopError as exc:
        result["integrity"] = str(exc)
        result["verification"] = {"rechecked": True, "passed": False, "checked_at": _now()}
        resolution = "resolve recorded protocol or evidence integrity before another execution"
        result["next_action"] = result["next_action"] + "; " + resolution if state["pending"] else resolution
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    init_parser = commands.add_parser("init", help="Freeze a supplied contract and current managed bytes; do not execute")
    init_parser.add_argument("--project", type=Path, default=Path.cwd())
    init_parser.add_argument("--workdir", type=Path, required=True)
    init_parser.add_argument("--contract", type=Path, required=True)
    campaign_parser = commands.add_parser("campaign-init", help="Create one opt-in shared campaign allowance; never reset an existing record")
    campaign_parser.add_argument("--project", type=Path, default=Path.cwd())
    campaign_parser.add_argument("--record", type=Path, required=True)
    campaign_parser.add_argument("--id", required=True)
    campaign_parser.add_argument("--max-attempts", type=int, required=True)
    campaign_parser.add_argument("--max-seconds", type=float, required=True)
    status_parser = commands.add_parser("status", help="Compact state; safe to inspect while a run is executing")
    status_parser.add_argument("--workdir", type=Path, required=True)
    status_parser.add_argument("--fast", action="store_true", help="Read last verified identity without rehashing protected inputs")
    context_parser = commands.add_parser("context", help="Retrieve compact matching experiments and recovery state")
    context_parser.add_argument("--workdir", type=Path, required=True)
    context_parser.add_argument("--query", default="")
    context_parser.add_argument("--limit", type=int, default=3)
    context_parser.add_argument("--fast", action="store_true", help="Retrieve records without rechecking files or evidence")
    note_parser = commands.add_parser("note", help="Record an evidence-linked interpretation without changing a measurement")
    note_parser.add_argument("--workdir", type=Path, required=True)
    note_parser.add_argument("--id", required=True)
    note_parser.add_argument("--category", choices=OBSERVATION_CATEGORIES, required=True)
    note_parser.add_argument("--finding", required=True)
    note_parser.add_argument("--next-action", required=True)
    note_parser.add_argument("--evidence", action="append", required=True)
    note_parser.add_argument("--corrects", type=int, help="Explicitly correct the active invalidation event after reinspection; finding must explain why")
    run_parser = commands.add_parser("run", help="Execute once per unique id; first valid run establishes the baseline")
    run_parser.add_argument("--workdir", type=Path, required=True)
    run_parser.add_argument("--id", required=True)
    run_parser.add_argument("--hypothesis", default="")
    replicate_parser = commands.add_parser("replicate", help="Re-measure identical candidate bytes without promotion")
    replicate_parser.add_argument("--workdir", type=Path, required=True)
    replicate_parser.add_argument("--id", required=True)
    replicate_parser.add_argument("--of", dest="source_id", required=True, help="A valid measured attempt ID, or best")
    replicate_parser.add_argument("--reason", required=True)
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
    reservation_parser = commands.add_parser("recover-reservation", help="Close an orphan shared reservation without replaying a command")
    reservation_parser.add_argument("--workdir", type=Path, required=True)
    reservation_parser.add_argument("--id", required=True)
    reservation_parser.add_argument("--reason", required=True)
    reservation_parser.add_argument("--confirm-stopped", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.operation == "campaign-init":
            record = args.record if args.record.is_absolute() else args.project / args.record
            try:
                result = CAMPAIGN.initialize(record, args.project, args.id, args.max_attempts, args.max_seconds)
            except CAMPAIGN.CampaignError as exc:
                raise LoopError(str(exc)) from exc
        elif args.operation == "init":
            workdir = args.workdir if args.workdir.is_absolute() else args.project / args.workdir
            result = initialize(args.project, workdir, args.contract)
        else:
            workdir = args.workdir.resolve(strict=True)
            if args.operation == "status":
                result = status(workdir, fast=args.fast)
            elif args.operation == "context":
                result = context(workdir, args.query, args.limit, fast=args.fast)
            elif args.operation == "note":
                result = note(workdir, args.id, args.category, args.finding, args.next_action, args.evidence, args.corrects)
            elif args.operation == "run":
                result = run(workdir, args.id, args.hypothesis)
            elif args.operation == "replicate":
                result = replicate(workdir, args.id, args.source_id, args.reason)
            elif args.operation == "decide":
                result = decide(workdir, args.id, args.action, args.reason)
            elif args.operation == "recover-reservation":
                result = recover_reservation(workdir, args.id, args.reason, args.confirm_stopped)
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
