#!/usr/bin/env python3
"""Validate current CCFA structure without rewriting files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_SKILLS = {
    "ccf-humanization",
    "ccf-common",
    "ccf-experiment-designer",
    "ccf-idea-optimizer",
    "ccf-idea-reviewer",
    "ccf-integrity-auditor",
    "ccf-literature-monitor",
    "ccf-literature-searcher",
    "ccf-visual-composer",
    "ccf-paper-reviewer",
    "ccf-paper-writer",
    "ccf-pipeline-orchestrator",
    "ccf-project-scaffolder",
    "ccf-rebuttal-writer",
    "ccf-skill-forger",
    "ccf-submission-checker",
    "ccf-paper-to-exemplar",
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
    # Runtime skills are repository-root ccf-* packages. Experiment outputs may
    # contain temporary Codex homes and third-party plugin caches; those are
    # evidence artifacts rather than members of the CCFA family.
    for directory in sorted(ROOT.glob("ccf-*")):
        path = directory / "SKILL.md"
        if not path.is_file():
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
    registered_order = re.findall(r"^\s*-\s+name:\s*(ccf-[a-z0-9-]+)\s*$", text, flags=re.MULTILINE)
    registered = set(registered_order)
    missing = sorted(set(skill_names) - registered)
    if missing:
        fail(errors, "registry missing skills: " + ", ".join(missing))
    if not registered_order or registered_order[0] != "ccf-humanization":
        fail(errors, "ccf-humanization must be the first registry entry")
    if "runtime_skill_count: 17" not in text:
        fail(errors, "skill-trigger-registry runtime_skill_count must be 17")


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
        "demo/attention-is-all-you-need/visual-composer/README.md",
        "demo/attention-is-all-you-need/visual-composer/plot_demo.py",
        "demo/attention-is-all-you-need/visual-composer/figures/translation_bleu_lollipop.svg",
        "demo/attention-is-all-you-need/visual-composer/figures/training_schedule_slopegraph.svg",
        "demo/attention-is-all-you-need/visual-composer/figures/configuration_ratio_heatmap.svg",
        "demo/attention-is-all-you-need/visual-composer/figures/base_big_small_multiples.svg",
        "demo/attention-is-all-you-need/paper/attention_iclr_submission.tex",
        "demo/attention-is-all-you-need/paper/iclr2026_conference.sty",
        "ccf-common/references/artifact-contracts.md",
        "ccf-common/references/ccfa-yaml-contract.md",
        "ccf-visual-composer/resources/python/ccfa_plot_recipes.py",
        "ccf-visual-composer/references/python-plot-recipes.md",
        "ccf-visual-composer/references/plot-inspiration-map.md",
        "ccf-visual-composer/references/architecture-diagram-generation.md",
        "ccf-humanization/references/humanization-policy.md",
        "ccf-humanization/references/experiment-discipline.md",
        "ccf-paper-writer/references/output-style-policy.md",
        "ccf-paper-writer/references/research-writing-patterns.md",
        "ccf-paper-writer/references/prose-quality-guardrails.md",
        "ccf-paper-writer/scripts/check_prose_quality.py",
        "ccf-paper-reviewer/references/version-comparison.md",
        "ccf-paper-reviewer/scripts/validate_version_comparison.py",
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


def check_visual_generation_contract(errors: list[str]) -> None:
    skill_path = ROOT / "ccf-visual-composer" / "SKILL.md"
    reference_path = ROOT / "ccf-visual-composer" / "references" / "architecture-diagram-generation.md"
    if not skill_path.is_file() or not reference_path.is_file():
        return
    skill_text = read(skill_path)
    reference_text = read(reference_path)
    required_skill_terms = (
        "architecture-generation",
        "editable-reconstruction",
        "icon-system",
        "reference-layout-blueprint",
        "use GPT Image 2 as the default first-pass renderer unless the user explicitly says not to use it",
        "pure-SVG-first route only when the user explicitly rejects GPT Image 2",
        "ask the mandatory editable-deliverable question",
        "Acronyms such as `CCF`, `AI`, `GPT`, `QA`, `SVG`, `PDF`, `PPTX`, and `PNG` remain uppercase",
    )
    for term in required_skill_terms:
        if term not in skill_text:
            fail(errors, f"ccf-visual-composer missing visual generation contract term: {term}")
    required_reference_terms = (
        "a user request to create the diagram selects GPT Image 2 as the default first-pass renderer",
        "Use pure SVG/code-first generation only when the user explicitly says not to use GPT Image 2",
        "是否需要我将它重建为可编辑的 SVG、矢量 PDF 或可编辑 PPTX？",
        "Do not begin reconstruction until the user agrees.",
        "Do not embed the whole raster in an SVG or use it as a full-slide PowerPoint background and call it editable.",
        "preserve canonical uppercase acronyms and initialisms",
    )
    for term in required_reference_terms:
        if term not in reference_text:
            fail(errors, f"architecture diagram reference missing required gate: {term}")
    for rel in (
        "references/icon-system.md",
        "references/reference-layout-blueprint.md",
        "references/editable-pptx.md",
    ):
        if not (ROOT / "ccf-visual-composer" / rel).is_file():
            fail(errors, f"ccf-visual-composer missing visual reference: {rel}")


def check_humanization_contract(errors: list[str]) -> None:
    paths = {
        "skill": ROOT / "ccf-humanization" / "SKILL.md",
        "policy": ROOT / "ccf-humanization" / "references" / "humanization-policy.md",
        "experiment": ROOT / "ccf-humanization" / "references" / "experiment-discipline.md",
        "writer": ROOT / "ccf-paper-writer" / "SKILL.md",
        "designer": ROOT / "ccf-experiment-designer" / "SKILL.md",
        "claude": ROOT / ".claude-plugin" / "plugin.json",
    }
    if any(not path.is_file() for path in paths.values()):
        return
    checks = {
        "skill": (
            "highest-priority preflight",
            "warning-only",
            "Do not edit a source file merely to encode a warning.",
            "verified identity and full configuration in the internal gate",
            "Keep method confirmation and version-gate status internal.",
        ),
        "policy": (
            "## SHA-256 And Checksum Rule",
            "do not conceal it",
            "Make no source edit",
            "## Method Status Versus Academic Description",
        ),
        "experiment": (
            "Only `confirmed` methods may enter publication artifacts.",
            "Smoke tests are engineering checks, not paper evidence.",
            "do not silently substitute a simplified version",
            "The `confirmed` label is internal metadata.",
        ),
        "writer": (
            "Run `ccf-humanization` as the first manuscript-facing preflight",
            "do not write that it is confirmed, approved, or publication-ready",
        ),
        "designer": ("Run `ccf-humanization` as the first publication-facing experiment preflight",),
    }
    for key, terms in checks.items():
        content = read(paths[key])
        for term in terms:
            if term not in content:
                fail(errors, f"{paths[key].relative_to(ROOT).as_posix()} missing humanization contract term: {term}")
    try:
        claude_manifest = json.loads(read(paths["claude"]))
    except json.JSONDecodeError:
        return
    if claude_manifest.get("entrypoints", [None])[0] != "ccf-humanization":
        fail(errors, "ccf-humanization must be the first Claude plugin entrypoint")


def check_issue_regression_contract(errors: list[str]) -> None:
    paths = {
        "artifacts": ROOT / "ccf-common" / "references" / "artifact-contracts.md",
        "humanization_policy": ROOT / "ccf-humanization" / "references" / "humanization-policy.md",
        "writer": ROOT / "ccf-paper-writer" / "SKILL.md",
        "prose": ROOT / "ccf-paper-writer" / "references" / "prose-quality-guardrails.md",
        "prose_checker": ROOT / "ccf-paper-writer" / "scripts" / "check_prose_quality.py",
        "reviewer": ROOT / "ccf-paper-reviewer" / "SKILL.md",
        "comparison": ROOT / "ccf-paper-reviewer" / "references" / "version-comparison.md",
        "comparison_checker": ROOT / "ccf-paper-reviewer" / "scripts" / "validate_version_comparison.py",
        "ledger": ROOT / "ccf-rebuttal-writer" / "references" / "revision-ledger.md",
    }
    if any(not path.is_file() for path in paths.values()):
        return
    checks = {
        "artifacts": (
            "## Canonical Artifact And Overwrite Policy",
            "one canonical path",
            "repository history",
        ),
        "writer": (
            "single source for punctuation and pattern thresholds",
            "scripts/check_prose_quality.py",
            "revise that file in place",
        ),
        "humanization_policy": (
            "allow at most three in a full paper",
            "Remove throat-clearing openers",
            "Do not force every argument into exactly three items",
            "Keep one canonical technical term",
        ),
        "prose": (
            "not detector-evasion",
            "authoritative punctuation limits",
            "do not restate or locally override",
            "scripts/check_prose_quality.py",
        ),
        "prose_checker": (
            "PRECISION_TERMS",
            '"delve"',
            '"groundbreaking"',
            '"em_dash_limit"',
            '"opening_filler"',
            '"uniform_sentence_run"',
        ),
        "reviewer": (
            "version-comparison",
            "relative progress, absolute readiness, and confidence",
            "do not make a dated report per iteration",
        ),
        "comparison": (
            "## Frozen Comparison Contract",
            "revision_regression",
            "previously_undetected",
            "newly_revealed_by_evidence",
            "external_standard_change",
            "Relative progress",
            "Absolute readiness",
        ),
        "comparison_checker": (
            '"revision_regression"',
            '"previously_undetected"',
            '"newly_revealed_by_evidence"',
            '"external_standard_change"',
            "decreased without a traceable current-version regression",
        ),
        "ledger": (
            "one canonical ledger",
            "comparative_score_effect",
        ),
    }
    for key, terms in checks.items():
        content = read(paths[key])
        for term in terms:
            if term not in content:
                fail(errors, f"{paths[key].relative_to(ROOT).as_posix()} missing issue-regression contract term: {term}")


def main() -> int:
    errors: list[str] = []
    names = check_skills(errors)
    check_registry(names, errors)
    check_venue_guides(errors)
    check_required_files(errors)
    check_visual_generation_contract(errors)
    check_humanization_contract(errors)
    check_issue_regression_contract(errors)
    if errors:
        print("CCFA validation failed:")
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print(f"CCFA validation passed. Skills: {len(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
