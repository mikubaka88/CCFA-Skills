#!/usr/bin/env python3
"""Validate CCFA v0.4 structure without rewriting files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_SKILLS = {
    "ccf-common",
    "ccf-experiment-designer",
    "ccf-idea-optimizer",
    "ccf-idea-reviewer",
    "ccf-integrity-auditor",
    "ccf-literature-searcher",
    "ccf-paper-reviewer",
    "ccf-paper-writer",
    "ccf-pipeline-orchestrator",
    "ccf-project-scaffolder",
    "ccf-rebuttal-writer",
    "ccf-skill-forger",
    "ccf-submission-checker",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(path: Path) -> dict[str, str]:
    text = read(path)
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter")
    fm = text[4:end]
    result: dict[str, str] = {}
    for key in ("name", "description"):
        match = re.search(rf"^{key}:\s*(.+)$", fm, flags=re.MULTILINE)
        if not match:
            raise ValueError(f"missing {key}")
        value = match.group(1).strip().strip('"').strip("'")
        if not value:
            raise ValueError(f"empty {key}")
        result[key] = value
    shared = re.search(r"shared_controls:\s*(.+)$", fm, flags=re.MULTILINE)
    if shared:
        result["shared_controls"] = shared.group(1).strip().strip('"').strip("'")
    return result


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_skills(errors: list[str]) -> list[str]:
    names: list[str] = []
    for path in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            fm = frontmatter(path)
        except ValueError as exc:
            fail(errors, f"{rel}: {exc}")
            continue
        name = fm["name"]
        names.append(name)
        if not name.startswith("ccf-"):
            fail(errors, f"{rel}: skill name must start with ccf-, got {name}")
        shared = fm.get("shared_controls")
        if shared:
            target = (path.parent / shared).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"{rel}: shared_controls points outside repo: {shared}")
            if not target.exists():
                fail(errors, f"{rel}: shared_controls target missing: {shared}")
    if len(names) != len(set(names)):
        seen = set()
        dupes = sorted({name for name in names if name in seen or seen.add(name)})
        fail(errors, f"duplicate skill names: {', '.join(dupes)}")
    actual = set(names)
    if actual != EXPECTED_SKILLS:
        extra = sorted(actual - EXPECTED_SKILLS)
        missing = sorted(EXPECTED_SKILLS - actual)
        if extra:
            fail(errors, "unexpected runtime skills: " + ", ".join(extra))
        if missing:
            fail(errors, "missing expected runtime skills: " + ", ".join(missing))
    return names


def check_registry(skill_names: list[str], errors: list[str]) -> None:
    registry = ROOT / "ccf-common" / "references" / "skill-trigger-registry.yaml"
    if not registry.is_file():
        fail(errors, "missing skill-trigger-registry.yaml")
        return
    text = read(registry)
    registered = set(re.findall(r"^\s*-\s+name:\s*(ccf-[a-z0-9-]+)\s*$", text, flags=re.MULTILINE))
    missing = sorted(set(skill_names) - registered)
    if missing:
        fail(errors, "registry missing skills: " + ", ".join(missing))


def check_venue_guides(errors: list[str]) -> None:
    legacy = ROOT / "ccf-conference-skills"
    if legacy.exists() and list(legacy.rglob("SKILL.md")):
        fail(errors, "legacy ccf-conference-skills/**/SKILL.md still exists")
    guide_root = ROOT / "ccf-paper-writer" / "references" / "venue-guides"
    index = guide_root / "index.md"
    if not index.is_file():
        fail(errors, "missing venue-guides/index.md")
        return
    text = read(index)
    rows = [line for line in text.splitlines() if line.startswith("| [")]
    if len(rows) < 100:
        fail(errors, f"venue index too small: {len(rows)} rows")
    for slug in ("cvpr", "neurips", "sigmod"):
        guide = guide_root / f"{slug}.md"
        if not guide.is_file():
            fail(errors, f"missing venue guide: {slug}")
            continue
        guide_text = read(guide)
        if "ccf-latex-templates" not in guide_text:
            fail(errors, f"{slug} guide lacks template path")
    for match in re.findall(r"`(ccf-latex-templates/[^`]+)`", text):
        candidate = ROOT / match
        if not candidate.exists():
            fail(errors, f"template path missing: {match}")


def check_required_files(errors: list[str]) -> None:
    required = [
        "docs/SKILLS_CATALOG.md",
        "docs/ARCHITECTURE.md",
        "docs/INSTALLATION_MATRIX.md",
        "docs/INSTALLATION_MATRIX.zh-CN.md",
        "docs/INSTALLATION_MATRIX.zh-TW.md",
        "AGENT_GUIDE.md",
        "CHANGELOG.md",
        "demo/attention-is-all-you-need/README.md",
        "demo/attention-is-all-you-need/ccfa.yaml",
        "demo/attention-is-all-you-need/skill-self-tests.md",
        "demo/attention-is-all-you-need/artifacts/00-original-paper-reading.md",
        "demo/attention-is-all-you-need/artifacts/01-idea-document.md",
        "demo/attention-is-all-you-need/artifacts/02-iclr-closed-loop-skill-run.md",
        "demo/attention-is-all-you-need/artifacts/03-idea-review.md",
        "demo/attention-is-all-you-need/artifacts/03-writing-draft.md",
        "demo/attention-is-all-you-need/artifacts/04-review-and-rebuttal.md",
        "demo/attention-is-all-you-need/artifacts/05-submission-check.md",
        "demo/attention-is-all-you-need/artifacts/06-family-self-audit.md",
        "demo/attention-is-all-you-need/artifacts/official-data.md",
        "demo/attention-is-all-you-need/artifacts/result-tables.md",
        "demo/attention-is-all-you-need/paper/attention_iclr_submission.tex",
        "demo/attention-is-all-you-need/paper/iclr2026_conference.sty",
        "ccf-common/references/artifact-contracts.md",
        "ccf-common/references/ccfa-yaml-contract.md",
        "ccf-paper-writer/references/output-style-policy.md",
        "ccf-paper-writer/references/research-writing-patterns.md",
        "ccf-project-scaffolder/assets/ccfa.yaml",
        ".codex-plugin/plugin.json",
        ".claude-plugin/plugin.json",
        ".github/workflows/validate.yml",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(errors, f"missing required file: {rel}")
    for rel in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        path = ROOT / rel
        if path.exists():
            try:
                json.loads(read(path))
            except json.JSONDecodeError as exc:
                fail(errors, f"{rel}: invalid JSON: {exc}")
    for key in (
        "architecture",
        "workflow",
        "review-boundaries",
        "catalog",
        "routing",
        "artifacts",
        "installation",
        "demo-attention",
    ):
        for suffix in ("", ".zh-CN", ".zh-TW"):
            rel = f"assets/ccfa-skills-{key}{suffix}.svg"
            path = ROOT / rel
            if not path.is_file() or "<svg" not in read(path):
                fail(errors, f"missing or invalid SVG: {rel}")


def main() -> int:
    errors: list[str] = []
    names = check_skills(errors)
    check_registry(names, errors)
    check_venue_guides(errors)
    check_required_files(errors)
    if errors:
        print("CCFA v0.4 validation failed:")
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print(f"CCFA v0.4 validation passed. Skills: {len(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
