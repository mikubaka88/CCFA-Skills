#!/usr/bin/env python3
"""Read-only validation of a compact task record and a declared transition.

This checks recorded consistency, not evidence truth, scientific acceptance,
semantic goal equivalence, actual execution, or a model's capabilities.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


MAX_BYTES = 64 * 1024
MAX_DEPTH = 32
MODES = {"normal", "focused", "reconciling"}
STATUSES = {"proposed", "executed", "verified"}
BASES = {"user_instruction", "intent_correction", "new_evidence",
         "verified_failure", "comparison", "recovery_check"}
KINDS = {"goal", "route", "recovery", "artifact_retirement"}
_MISSING = object()


def finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message}


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number: {value}")


def _check_tree(value: Any, depth: int = 0) -> None:
    if depth > MAX_DEPTH:
        raise ValueError(f"JSON nesting exceeds {MAX_DEPTH}")
    if isinstance(value, str):
        if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
            raise ValueError("JSON contains an unpaired Unicode surrogate")
    elif isinstance(value, dict):
        for key, item in value.items():
            _check_tree(key, depth + 1)
            _check_tree(item, depth + 1)
    elif isinstance(value, list):
        for item in value:
            _check_tree(item, depth + 1)


def load_record(path: str) -> Any:
    """Read at most MAX_BYTES + 1; never create or modify files."""
    if path == "-":
        data = sys.stdin.buffer.read(MAX_BYTES + 1)
    else:
        with Path(path).open("rb") as stream:
            data = stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError(f"record exceeds {MAX_BYTES} bytes")
    value = json.loads(data.decode("utf-8-sig"), object_pairs_hook=_unique_object,
                       parse_constant=_reject_constant)
    _check_tree(value)
    return value


def validate_record(value: Any, prefix: str = "$") -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []

    def fail(path: str, message: str) -> None:
        issues.append(finding("schema", path, message))

    def obj(item: Any, path: str, required: set[str], optional: set[str] | None = None) -> bool:
        if not isinstance(item, dict):
            fail(path, "expected an object")
            return False
        for key in sorted(required - item.keys()):
            fail(f"{path}.{key}", "required field is missing")
        for key in sorted(item.keys() - required - (optional or set())):
            fail(f"{path}.{key}", "unknown field")
        return True

    def string(item: Any, path: str) -> bool:
        if not isinstance(item, str) or not item.strip():
            fail(path, "expected a nonempty string")
            return False
        return True

    def strings(item: Any, path: str, nonempty: bool = False) -> None:
        if not isinstance(item, list):
            fail(path, "expected a list of nonempty strings")
            return
        if nonempty and not item:
            fail(path, "at least one entry is required")
        for index, entry in enumerate(item):
            string(entry, f"{path}[{index}]")

    def choice(item: Any, path: str, choices: set[str]) -> None:
        if not isinstance(item, str) or item not in choices:
            fail(path, "expected one of: " + ", ".join(sorted(choices)))

    required = {"version", "task_id", "goal", "route", "phase", "mode", "next_action"}
    if not obj(value, prefix, required, {"artifacts", "open_items", "changes"}):
        return issues
    if type(value.get("version")) is not int or value["version"] != 1:
        fail(f"{prefix}.version", "expected integer version 1")
    for field in ("task_id", "phase", "next_action"):
        string(value.get(field), f"{prefix}.{field}")
    choice(value.get("mode"), f"{prefix}.mode", MODES)

    goal = value.get("goal")
    if obj(goal, f"{prefix}.goal", {"revision", "objective", "source", "constraints", "acceptance"}):
        if type(goal.get("revision")) is not int or goal["revision"] < 1:
            fail(f"{prefix}.goal.revision", "expected a positive integer")
        for field in ("objective", "source"):
            string(goal.get(field), f"{prefix}.goal.{field}")
        strings(goal.get("constraints"), f"{prefix}.goal.constraints")
        strings(goal.get("acceptance"), f"{prefix}.goal.acceptance", nonempty=True)

    route = value.get("route")
    if obj(route, f"{prefix}.route", {"id", "summary"}):
        for field in ("id", "summary"):
            string(route.get(field), f"{prefix}.route.{field}")
    if "open_items" in value:
        strings(value["open_items"], f"{prefix}.open_items")

    artifacts = value.get("artifacts", [])
    if not isinstance(artifacts, list):
        fail(f"{prefix}.artifacts", "expected a list")
    else:
        paths: set[str] = set()
        for index, artifact in enumerate(artifacts):
            path = f"{prefix}.artifacts[{index}]"
            if not obj(artifact, path, {"path", "revision", "status", "evidence"}):
                continue
            if string(artifact.get("path"), f"{path}.path"):
                if artifact["path"] in paths:
                    fail(f"{path}.path", "duplicate artifact path")
                paths.add(artifact["path"])
            string(artifact.get("revision"), f"{path}.revision")
            choice(artifact.get("status"), f"{path}.status", STATUSES)
            strings(artifact.get("evidence"), f"{path}.evidence",
                    nonempty=artifact.get("status") == "verified")

    changes = value.get("changes", [])
    if not isinstance(changes, list):
        fail(f"{prefix}.changes", "expected a list")
    else:
        for index, change in enumerate(changes):
            path = f"{prefix}.changes[{index}]"
            if not obj(change, path, {"kind", "reason", "basis", "evidence"}, {"artifact"}):
                continue
            choice(change.get("kind"), f"{path}.kind", KINDS)
            choice(change.get("basis"), f"{path}.basis", BASES)
            string(change.get("reason"), f"{path}.reason")
            strings(change.get("evidence"), f"{path}.evidence", nonempty=True)
            if change.get("kind") == "artifact_retirement":
                string(change.get("artifact"), f"{path}.artifact")
            elif "artifact" in change:
                fail(f"{path}.artifact", "artifact applies only to artifact_retirement")
    return issues


def check_records(current: Any, previous: Any = _MISSING) -> list[dict[str, str]]:
    """Validate declarations; caller remains responsible for checking real evidence."""
    issues = validate_record(current)
    if previous is _MISSING:
        return issues
    issues.extend(validate_record(previous, "$previous"))
    if issues:
        return issues
    if current["task_id"] != previous["task_id"]:
        return [finding("task_mismatch", "$.task_id", "previous record belongs to another task")]

    # A stale declaration cannot justify a later, different transition.
    changes = [change for change in current.get("changes", [])
               if change not in previous.get("changes", [])]

    def declared(kind: str, bases: set[str] | None = None, artifact: str | None = None) -> bool:
        return any(change["kind"] == kind
                   and (bases is None or change["basis"] in bases)
                   and (artifact is None or change.get("artifact") == artifact)
                   for change in changes)

    old_goal, new_goal = previous["goal"], current["goal"]
    goal_changed = any(old_goal[field] != new_goal[field]
                       for field in ("objective", "source", "constraints", "acceptance"))
    if new_goal["revision"] < old_goal["revision"]:
        issues.append(finding("goal_revision", "$.goal.revision", "goal revision cannot decrease"))
    if goal_changed:
        if new_goal["revision"] <= old_goal["revision"]:
            issues.append(finding("goal_revision", "$.goal.revision", "changed goal requires a higher revision"))
        if not declared("goal", {"user_instruction", "intent_correction"}):
            issues.append(finding("goal_change", "$.changes", "changed goal requires a current user_instruction or intent_correction record"))
    if current["route"] != previous["route"] and not declared("route", BASES - {"recovery_check"}):
        issues.append(finding("route_change", "$.changes", "changed route requires a current reason and evidence"))
    if previous["mode"] != "normal" and current["mode"] == "normal":
        if not declared("recovery", {"recovery_check"}):
            issues.append(finding("recovery", "$.changes", "return to normal requires a current recovery_check record"))
    current_artifacts = {artifact["path"]: artifact for artifact in current.get("artifacts", [])}
    for artifact in previous.get("artifacts", []):
        updated = current_artifacts.get(artifact["path"])
        if artifact["status"] == "verified" and updated is None:
            if not declared("artifact_retirement", artifact=artifact["path"]):
                issues.append(finding("artifact_retirement", "$.changes", "removed verified artifact requires a current retirement record: " + artifact["path"]))
        if (updated is not None and updated["revision"] != artifact["revision"]
                and updated["status"] == "verified"
                and not (set(updated["evidence"]) - set(artifact["evidence"]))):
            issues.append(finding("artifact_reverification", "$.artifacts", "changed artifact revision marked verified requires a fresh check reference: " + artifact["path"]))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="validate a record without modifying files")
    check.add_argument("record", help="UTF-8 JSON path, or - for standard input")
    check.add_argument("--previous", help="existing canonical JSON record to compare")
    args = parser.parse_args(argv)
    if args.previous == "-":
        parser.error("--previous must be a file path")
    try:
        current = load_record(args.record)
        previous = load_record(args.previous) if args.previous else _MISSING
        issues = check_records(current, previous)
        status = 1 if issues else 0
    except (OSError, ValueError, RecursionError) as error:
        issues = [finding("input", "$", str(error))]
        status = 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({"ok": not issues, "scope": "recorded_consistency", "findings": issues}, ensure_ascii=False))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
