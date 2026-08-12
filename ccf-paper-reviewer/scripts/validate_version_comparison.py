#!/usr/bin/env python3
"""Validate a structured manuscript version comparison without writing files."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


ORIGINS = {
    "inherited",
    "revision_regression",
    "previously_undetected",
    "newly_revealed_by_evidence",
    "external_standard_change",
}
STATUSES = {"unresolved", "partially_resolved", "resolved", "not_applicable"}
CURRENT_NEGATIVE_ORIGINS = {"revision_regression", "newly_revealed_by_evidence"}
PROGRESS_CLASSES = {"regressed", "unchanged", "improved"}


def _read(path: str | None) -> dict:
    raw = Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()
    return json.loads(raw)


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    contract = data.get("contract") or {}
    dimensions = contract.get("dimensions") or []
    weights = contract.get("weights") or {}

    for field in ("id", "venue", "scale", "dimensions", "weights", "reviewer_roles", "thresholds", "evidence_standard"):
        if not contract.get(field):
            errors.append(f"contract.{field} is required")
    if not isinstance(dimensions, list) or not all(_nonempty(item) for item in dimensions):
        errors.append("contract.dimensions must be a nonempty list of names")
        dimensions = []
    if dimensions:
        missing_weights = [dim for dim in dimensions if dim not in weights]
        if missing_weights:
            errors.append(f"contract.weights missing dimensions: {', '.join(missing_weights)}")
        numeric_weights = [weights.get(dim) for dim in dimensions]
        if not all(isinstance(value, (int, float)) and value >= 0 for value in numeric_weights):
            errors.append("contract.weights must contain nonnegative numbers")
        elif not math.isclose(sum(numeric_weights), 1.0, rel_tol=1e-6, abs_tol=1e-6):
            errors.append("contract.weights must sum to 1")

    progress = data.get("relative_progress_scorecard") or {}
    historical = progress.get("historical") or {}
    current = progress.get("current") or {}
    deltas = progress.get("deltas") or {}
    for version_name, version_scores in (("historical", historical), ("current", current)):
        for dim in dimensions:
            if not isinstance(version_scores.get(dim), (int, float)):
                errors.append(f"relative_progress_scorecard.{version_name}.{dim} must be numeric")

    expected_weighted_delta = 0.0
    comparable_deltas = True
    for dim in dimensions:
        old = historical.get(dim)
        new = current.get(dim)
        delta = deltas.get(dim)
        if not isinstance(delta, (int, float)):
            errors.append(f"relative_progress_scorecard.deltas.{dim} must be numeric")
            comparable_deltas = False
            continue
        if isinstance(old, (int, float)) and isinstance(new, (int, float)):
            if not math.isclose(delta, new - old, rel_tol=1e-6, abs_tol=1e-6):
                errors.append(f"relative_progress_scorecard.deltas.{dim} must equal current - historical")
        else:
            comparable_deltas = False
        weight = weights.get(dim)
        if isinstance(weight, (int, float)):
            expected_weighted_delta += delta * weight

    weighted_delta = progress.get("weighted_delta")
    if not isinstance(weighted_delta, (int, float)):
        errors.append("relative_progress_scorecard.weighted_delta must be numeric")
    elif comparable_deltas and not math.isclose(weighted_delta, expected_weighted_delta, rel_tol=1e-6, abs_tol=1e-6):
        errors.append("relative_progress_scorecard.weighted_delta does not match the frozen weights and deltas")
    if progress.get("classification") not in PROGRESS_CLASSES:
        errors.append("relative_progress_scorecard.classification must be regressed, unchanged, or improved")

    readiness = data.get("absolute_readiness_scorecard") or {}
    readiness_dimensions = readiness.get("current_dimension_scores") or {}
    for dim in dimensions:
        if not isinstance(readiness_dimensions.get(dim), (int, float)):
            errors.append(f"absolute_readiness_scorecard.current_dimension_scores.{dim} must be numeric")
    for field in ("scale", "stance", "threshold", "evidence_standard"):
        if not _nonempty(readiness.get(field)):
            errors.append(f"absolute_readiness_scorecard.{field} is required")
    if not isinstance(readiness.get("overall_score"), (int, float)):
        errors.append("absolute_readiness_scorecard.overall_score must be numeric")

    if not _nonempty(data.get("confidence_and_comparability")):
        errors.append("confidence_and_comparability is required and must be reported separately")

    issues = data.get("issues")
    if not isinstance(issues, list):
        errors.append("issues must be a list")
        issues = []

    valid_issues = []
    for index, issue in enumerate(issues):
        label = issue.get("id") or f"issue[{index}]"
        origin = issue.get("origin")
        applies_to = issue.get("applies_to")
        status = issue.get("status")
        affected = issue.get("affected_dimensions") or []
        if origin not in ORIGINS:
            errors.append(f"{label}: invalid origin {origin!r}")
        if applies_to not in {"historical", "current", "both"}:
            errors.append(f"{label}: applies_to must be historical, current, or both")
        if status not in STATUSES:
            errors.append(f"{label}: invalid comparative status {status!r}")
        if not affected or any(dim not in dimensions for dim in affected):
            errors.append(f"{label}: affected_dimensions must use the frozen contract")
        if not _nonempty(issue.get("evidence")):
            errors.append(f"{label}: evidence anchor is required")
        if origin == "previously_undetected" and applies_to != "both":
            errors.append(f"{label}: a previously undetected latent issue must apply to both versions")
        effect = issue.get("score_effect") or {}
        if origin == "external_standard_change" and any(effect.get(key, 0) for key in ("historical", "current")):
            errors.append(f"{label}: an external standard change cannot alter the frozen comparison scores")
        valid_issues.append(issue)

    for dim in dimensions:
        old = historical.get(dim)
        new = current.get(dim)
        if not isinstance(old, (int, float)) or not isinstance(new, (int, float)) or new >= old:
            continue
        traced = []
        for issue in valid_issues:
            effect = issue.get("score_effect") or {}
            if (
                issue.get("origin") in CURRENT_NEGATIVE_ORIGINS
                and issue.get("applies_to") in {"current", "both"}
                and dim in (issue.get("affected_dimensions") or [])
                and isinstance(effect.get("current"), (int, float))
                and effect["current"] < 0
                and _nonempty(issue.get("evidence"))
            ):
                traced.append(issue.get("id", "unknown"))
        if not traced:
            errors.append(f"relative_progress_scorecard.current.{dim} decreased without a traceable current-version regression or newly revealed evidence")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="JSON path; omit to read stdin")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        data = _read(args.path)
        errors = validate(data)
    except (OSError, json.JSONDecodeError) as exc:
        errors = [f"input error: {exc}"]

    result = {"valid": not errors, "error_count": len(errors), "errors": errors}
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS: version comparison is internally consistent." if not errors else "FAIL: version comparison is inconsistent.")
        for error in errors:
            print(f"- {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
