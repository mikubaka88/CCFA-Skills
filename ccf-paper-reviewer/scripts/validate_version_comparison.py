#!/usr/bin/env python3
"""Validate a JSON version comparison or a default-format Markdown review; write no files."""

from __future__ import annotations

import argparse
import json
import math
import re
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
REFERENCES = Path(__file__).resolve().parents[1] / "references"
FINDING_TYPES = {"confirmed_flaw", "unsupported_claim", "clarification"}
SEVERITIES = {"critical", "major", "minor"}
SCORE_STATUSES = {"N/A", "not assessed", "不适用", "未评估"}
FINDING_FIELDS = {
    "type": "类型", "severity": "严重程度", "location": "位置",
    "evidence": "证据", "countercheck": "反证复核", "judgment": "判断",
    "criterion": "维度", "resolution": "解决或改判条件", "status": "状态",
}
ISSUE_ID = r"[A-Z]{1,4}-?\d{1,6}"


def _reference_section(filename: str, heading: str) -> str:
    text = (REFERENCES / filename).read_text(encoding="utf-8")
    marker = f"## {heading}\n"
    if marker not in text:
        raise ValueError(f"missing canonical section: {filename}: {heading}")
    return text.split(marker, 1)[1].split("\n## ", 1)[0]


def _cells(line: str) -> list[str]:
    return [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def _plain(text: str) -> str:
    return text.replace("**", "").strip().strip("`*").strip()


def _canonical_criteria() -> list[tuple[str, str, str]]:
    """Read the one rubric definition rather than duplicating its dimension list."""
    section = _reference_section("calibration-and-rank.md", "Canonical Scientific Criteria")
    rows = [_cells(line) for line in section.splitlines() if re.match(r"^\| [a-z_]+ \|", line)]
    criteria = [(row[0], row[1], row[2]) for row in rows]
    if len(criteria) != 7 or len({row[0] for row in criteria}) != 7:
        raise ValueError("canonical scientific rubric must define seven unique criteria")
    return criteria


def _profile_headings(mode: str, detail: str) -> list[tuple[int, set[str]]]:
    section_name = ("Brief Version — Explicit Request" if detail == "brief" else
                    "Writing Detailed Profile" if mode == "writing" else "Detailed Version — Default")
    section = _reference_section("fixed-output-format.md", section_name)
    result = []
    for number, title in re.findall(r"^### (\d+)\. (.+)$", section, re.MULTILINE):
        result.append((int(number), {title, *title.split(" / ", 1)}))
    expected_count = 5 if detail == "brief" else 9 if mode == "writing" else 14
    if len(result) != expected_count or [number for number, _ in result] != list(range(1, expected_count + 1)):
        raise ValueError(f"invalid canonical heading profile: {section_name}")
    return result


def _visible_markdown(text: str) -> str:
    """Ignore quoted material and fenced examples without hiding real report text."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    result = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            result.append("")
        elif marker:
            fence = marker[1]
            result.append("")
        elif re.match(r"^\s*>", line):
            result.append("")
        else:
            result.append(line)
    return "\n".join(result)


def _valid_score(value: object, maximum: int) -> bool:
    if isinstance(value, str):
        value = _plain(value)
        if value in SCORE_STATUSES:
            return True
        match = re.fullmatch(r"(\d+)(?:/(\d+))?", value)
        return bool(match and 1 <= int(match[1]) <= maximum and (match[2] is None or int(match[2]) == maximum))
    return type(value) is int and 1 <= value <= maximum


def _column(headers: list[str], *names: str) -> int | None:
    for index, header in enumerate(headers):
        label = _plain(header).casefold()
        if any(re.match(rf"^{re.escape(name.casefold())}(?:$|[\s/（(])", label) for name in names):
            return index
    return None


def _metric_values(text: str, *labels: str) -> list[str]:
    """Read labeled scalar fields, including bold and bilingual inline fields."""
    aliases = {label.casefold() for label in labels}
    values = []
    for line in text.splitlines():
        for part in re.split(r"(?<!\\)\|", line.replace("**", "")):
            if not re.search(r"[:：]", part):
                continue
            label, value = re.split(r"[:：]", part, maxsplit=1)
            label = re.sub(r"^\s*[-*]\s+", "", label)
            names = [_plain(name).casefold() for name in label.split(" / ")]
            if names and all(name in aliases for name in names):
                values.append(_plain(value))
    return values


def _check_scorecards(text: str, errors: list[str], required: bool, no_scores: bool) -> None:
    criteria = _canonical_criteria()
    aliases = {}
    for key, english, chinese in criteria:
        for label in (key, english, chinese, f"{english} / {chinese}", f"{chinese} / {english}"):
            aliases[label.casefold()] = key
    expected = [row[0] for row in criteria]
    tables = []
    for block in re.findall(r"(?:^\|[^\n]*\n?)+", text, flags=re.MULTILINE):
        rows = [_cells(line) for line in block.splitlines()]
        if len(rows) < 2 or _column(rows[0], "Dimension", "维度") != 0:
            continue
        if len(rows[1]) != len(rows[0]) or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1]):
            errors.append("scorecard must have a Markdown separator row")
            continue
        tables.append(rows)
    if required and len(tables) != 1:
        errors.append("generic detailed ratings require exactly one canonical seven-dimension scorecard")
    for rows in tables:
        headers, _, *body = rows
        score = _column(headers, "Judgment", "判断", "评价") if no_scores else _column(headers, "Score", "评分", "得分")
        confidence = _column(headers, "Confidence", "置信度")
        evidence = _column(headers, "Evidence", "证据")
        condition = _column(headers, "Deduction", "扣分", "改判条件", "解决或改判条件")
        if score is None or confidence is None or evidence is None or condition is None:
            errors.append("scorecard requires dimension, score/judgment, confidence, evidence, and deduction/change-condition columns")
            continue
        keys = []
        for row in body:
            if len(row) != len(headers):
                errors.append("scorecard row width differs from its header")
                continue
            key = aliases.get(_plain(row[0]).casefold())
            keys.append(key)
            if key is None:
                errors.append(f"unknown generic dimension: {row[0]}")
            if not row[score]:
                errors.append(f"{row[0]}: score/judgment is empty")
            elif no_scores:
                if re.fullmatch(r"\d+(?:\.\d+)?(?:/\d+)?", _plain(row[score])):
                    errors.append(f"{row[0]}: numeric quality rating in a no-score report")
            elif not _valid_score(row[score], 5):
                errors.append(f"{row[0]}: criterion score must be an integer 1-5, N/A, or not assessed; never zero")
            if not row[confidence] or (not no_scores and not _valid_score(row[confidence], 5)):
                errors.append(f"{row[0]}: confidence must be 1-5 or an unassessed/inapplicable status")
            elif no_scores and re.fullmatch(r"\d+(?:\.\d+)?(?:/\d+)?", _plain(row[confidence])) and not _valid_score(row[confidence], 5):
                errors.append(f"{row[0]}: invalid numeric confidence")
            if not row[evidence] or not row[condition]:
                errors.append(f"{row[0]}: evidence and deduction/change-condition cells must be nonempty")
        if len(keys) != len(set(keys)):
            errors.append("generic scorecard repeats a dimension")
        if required and keys != expected:
            errors.append("generic detailed scorecard must use all seven canonical dimensions in order")
        elif not required and any(key is None for key in keys):
            errors.append("brief scorecard may only summarize canonical generic dimensions")


def validate_report(markdown: str, *, mode: str = "scientific", detail: str = "detailed",
                    no_scores: bool = False, rubric: str = "generic-7") -> list[str]:
    """Check the default Markdown contract, not scientific quality or custom venue forms."""
    if mode not in {"scientific", "full", "writing", "version-comparison"} or detail not in {"detailed", "brief"}:
        return ["unknown report mode or detail profile"]
    if rubric not in {"generic-7", "external"}:
        return ["unknown report rubric"]
    errors: list[str] = []
    text = _visible_markdown(markdown)
    expected = _profile_headings(mode, detail)
    headings = list(re.finditer(r"^## (.+)$", text, re.MULTILINE))
    sections = {}
    if len(headings) != len(expected):
        errors.append(f"{mode}/{detail} requires exactly {len(expected)} numbered report sections")
    for index, match in enumerate(headings):
        title = _plain(re.sub(r"\s+#+$", "", match[1]))
        numbered = re.fullmatch(r"(\d+)\.\s+(.+)", title)
        if index >= len(expected) or numbered is None or int(numbered[1]) != expected[index][0] or numbered[2] not in expected[index][1]:
            errors.append(f"unexpected section name/order: {title}")
        if numbered:
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            sections[int(numbered[1])] = (match.end(), end, text[match.end():end])
            if not text[match.end():end].strip():
                errors.append(f"empty report section: {title}; state an inapplicable/unassessed reason when needed")

    finding_sections = {3} if detail == "brief" else {5} if mode == "writing" else {6, 7}
    definitions = list(re.finditer(rf"^### ({ISSUE_ID})\s*[:：—-]\s*\S.*$", text, re.MULTILINE))
    defined = set()
    for match in definitions:
        identity = match[1]
        if identity in defined:
            errors.append(f"duplicate finding definition: {identity}")
        defined.add(identity)
        if not any(start <= match.start() < end for number, (start, end, _) in sections.items() if number in finding_sections):
            errors.append(f"{identity}: define findings only in the selected concerns section")
        remainder = text[match.end():]
        block = re.split(r"^#{2,3} ", remainder, maxsplit=1, flags=re.MULTILINE)[0]
        fields = {}
        for line in block.splitlines():
            line = _plain(re.sub(r"^\s*[-*]\s+", "", line))
            if not re.search(r"[:：]", line):
                continue
            label, value = re.split(r"[:：]", line, maxsplit=1)
            for key, chinese in FINDING_FIELDS.items():
                names = [name.casefold().strip() for name in label.split("/")]
                if names in ([key], [chinese], [key, chinese], [chinese, key]):
                    if key in fields:
                        errors.append(f"{identity}: duplicate {key} field")
                    fields[key] = _plain(value)
        for key in FINDING_FIELDS:
            if not fields.get(key):
                errors.append(f"{identity}: missing/nonempty finding field required: {key}")
        for key, allowed in (("type", FINDING_TYPES), ("severity", SEVERITIES), ("status", STATUSES)):
            if fields.get(key) and fields[key] not in allowed:
                errors.append(f"{identity}: invalid {key}: {fields[key]}")
    references = set(re.findall(rf"(?<![!\\])\[({ISSUE_ID})\]", text))
    for identity in sorted(references - defined):
        errors.append(f"undefined finding reference: [{identity}]")

    ratings_number = 4 if detail == "brief" else 7 if mode == "writing" else 12
    ratings = sections.get(ratings_number, (0, 0, ""))[2]
    confidence_scope = ratings
    if mode == "version-comparison":
        comparison_titles = ["Relative Progress / 相对进步", "Absolute Readiness / 绝对成熟度", "Confidence And Comparability / 置信度与可比性"]
        matches = list(re.finditer(r"^### (.+)$", ratings, re.MULTILINE))
        titles = [_plain(item[1]) for item in matches]
        if titles != comparison_titles:
            errors.append("version comparison requires separate relative-progress, absolute-readiness, and confidence subheadings in order")
        else:
            confidence_scope = ratings[matches[1].end():]
            ratings = ratings[matches[1].end():matches[2].start()]
    if mode != "writing" and rubric == "generic-7":
        _check_scorecards(ratings, errors, required=detail == "detailed", no_scores=no_scores)
        overall = _metric_values(ratings, "Overall", "总分", "总体评分")
        if detail == "detailed" and len(overall) != 1:
            errors.append("generic detailed ratings require one Overall field (use not assessed when needed)")
        for value in overall:
            if not value:
                errors.append("Overall field cannot be empty; use not assessed when needed")
            elif no_scores and re.fullmatch(r"\d+(?:\.\d+)?(?:/\d+)?", _plain(value)):
                errors.append("numeric overall rating in a no-score report")
            elif not no_scores and not _valid_score(value, 10):
                errors.append("Overall must be an integer 1-10, N/A, or not assessed")
        confidence = _metric_values(confidence_scope, "Scholarly Confidence", "Confidence", "总体置信度", "置信度")
        if detail == "detailed" and len(confidence) != 1:
            errors.append("generic detailed ratings require one Scholarly Confidence field, separate from quality and coverage")
        for value in confidence:
            if not value or (not no_scores and not _valid_score(value, 5)) or (no_scores and re.fullmatch(r"\d+(?:\.\d+)?(?:/\d+)?", value) and not _valid_score(value, 5)):
                errors.append("overall confidence must be an integer 1-5 or an unassessed/inapplicable status")
    return errors


def _read_utf8(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8-sig")
    if hasattr(sys.stdin, "buffer"):
        return sys.stdin.buffer.read().decode("utf-8-sig")
    return sys.stdin.read().removeprefix("\ufeff")


def _read(path: str | None) -> dict:
    return json.loads(_read_utf8(path))


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
    readiness_scores = readiness.get("current_dimension_scores") or {}
    readiness_rubric = readiness.get("rubric")
    readiness_dimensions = dimensions
    if readiness_rubric == "generic-7":
        readiness_dimensions = [row[0] for row in _canonical_criteria()]
        if set(readiness_scores) != set(readiness_dimensions):
            errors.append("generic-7 readiness must use exactly the canonical keys; historical dimensions stay frozen")
    elif readiness_rubric == "external":
        readiness_dimensions = readiness.get("dimensions") or []
        if not isinstance(readiness_dimensions, list) or not readiness_dimensions or not all(_nonempty(item) for item in readiness_dimensions):
            errors.append("external readiness requires its own nonempty dimensions list")
            readiness_dimensions = []
    elif readiness_rubric is not None:
        errors.append("absolute_readiness_scorecard.rubric must be generic-7 or external when supplied")
    for dim in readiness_dimensions:
        value = readiness_scores.get(dim)
        if readiness_rubric == "generic-7":
            if not _valid_score(value, 5):
                errors.append(f"absolute_readiness_scorecard.current_dimension_scores.{dim} must be 1-5, N/A, or not assessed")
        elif not isinstance(value, (int, float)):
            errors.append(f"absolute_readiness_scorecard.current_dimension_scores.{dim} must be numeric")
    for field in ("scale", "stance", "threshold", "evidence_standard"):
        if not _nonempty(readiness.get(field)):
            errors.append(f"absolute_readiness_scorecard.{field} is required")
    if readiness_rubric == "generic-7" and not _valid_score(readiness.get("overall_score"), 10):
        errors.append("generic-7 readiness overall_score must be an integer 1-10, N/A, or not assessed")
    elif readiness_rubric != "generic-7" and not isinstance(readiness.get("overall_score"), (int, float)):
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
    # Standalone reports and redirected diagnostics use UTF-8 on every platform.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="JSON comparison path, or Markdown with --report; omit to read stdin")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--report", action="store_true", help="validate a default-format Markdown review instead of JSON comparison data")
    parser.add_argument("--mode", choices=("scientific", "full", "writing", "version-comparison"), default="scientific")
    parser.add_argument("--detail", choices=("detailed", "brief"), default="detailed")
    parser.add_argument("--no-scores", action="store_true", help="expect qualitative generic judgments instead of numeric quality ratings")
    parser.add_argument("--rubric", choices=("generic-7", "external"), default="generic-7", help="external retains heading/finding checks but skips generic rating checks")
    args = parser.parse_args()
    try:
        if args.report:
            markdown = _read_utf8(args.path)
            errors = validate_report(markdown, mode=args.mode, detail=args.detail, no_scores=args.no_scores, rubric=args.rubric)
        else:
            data = _read(args.path)
            errors = validate(data)
    except (OSError, ValueError) as exc:
        errors = [f"input error: {exc}"]

    result = {"valid": not errors, "error_count": len(errors), "errors": errors}
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if args.report:
            print("PASS: checked report structure is consistent (scientific quality not verified)." if not errors else "FAIL: report structure is inconsistent.")
        else:
            print("PASS: version comparison is internally consistent." if not errors else "FAIL: version comparison is inconsistent.")
        for error in errors:
            print(f"- {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
