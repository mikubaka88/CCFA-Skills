#!/usr/bin/env python3
"""Validate current CCFA structure without rewriting files."""

from __future__ import annotations

import ast
import contextlib
import copy
import io
import json
import os
import re
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import yaml


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
    return path.read_text(encoding="utf-8-sig")


def frontmatter(path: Path) -> dict:
    text = read(path)
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter")
    try:
        result = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML: {exc}") from exc
    if not isinstance(result, dict):
        raise ValueError("frontmatter must be a mapping")
    for key in ("name", "description"):
        if not isinstance(result.get(key), str) or not result[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    metadata = result.get("metadata")
    controls = metadata.get("ccf_skill_controls") if isinstance(metadata, dict) else None
    required = {"handoff_question_mode", "respect_session_denylists", "protect_idea_scope_in_writing", "private_material_safety", "shared_controls"}
    if not isinstance(controls, dict) or not required.issubset(controls):
        raise ValueError("missing shared ccf_skill_controls fields")
    if controls["handoff_question_mode"] not in {"partial", "full", "off"}:
        raise ValueError("invalid handoff_question_mode")
    for key in ("respect_session_denylists", "protect_idea_scope_in_writing"):
        if not isinstance(controls[key], bool):
            raise ValueError(f"{key} must be a YAML boolean")
    for key in ("private_material_safety", "shared_controls"):
        if not isinstance(controls[key], str) or not controls[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    result["shared_controls"] = controls["shared_controls"]
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
        if not re.fullmatch(r"ccf-[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != directory.name:
            fail(errors, f"{rel}: invalid skill name or directory mismatch: {name}")
        shared = fm.get("shared_controls")
        if shared:
            target = (path.parent / shared).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"{rel}: shared_controls points outside repo: {shared}")
            if not target.exists():
                fail(errors, f"{rel}: shared_controls target missing: {shared}")
        agent = directory / "agents" / "openai.yaml"
        if agent.is_file():
            try:
                config = yaml.safe_load(read(agent))
                interface = config.get("interface", {}) if isinstance(config, dict) else {}
                prompt = interface.get("default_prompt", "")
                if not isinstance(prompt, str) or f"${name}" not in prompt:
                    fail(errors, f"{agent.relative_to(ROOT)}: missing own skill in default_prompt")
                for sibling in re.findall(r"\$(ccf-[a-z0-9-]+)", prompt if isinstance(prompt, str) else ""):
                    if sibling not in EXPECTED_SKILLS:
                        fail(errors, f"{agent.relative_to(ROOT)}: unknown skill {sibling}")
            except yaml.YAMLError as exc:
                fail(errors, f"{agent.relative_to(ROOT)}: invalid YAML: {exc}")
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
    try:
        data = yaml.safe_load(read(registry))
        entries = data["skills"]
        registered_order = [entry["name"] for entry in entries]
    except (yaml.YAMLError, KeyError, TypeError) as exc:
        fail(errors, f"invalid trigger registry: {exc}")
        return
    registered = set(registered_order)
    missing = sorted(set(skill_names) - registered)
    if missing:
        fail(errors, "registry missing skills: " + ", ".join(missing))
    if registered - set(skill_names) or len(registered_order) != len(registered):
        fail(errors, "registry contains unknown or duplicate skills")
    for entry in entries:
        for key in ("trigger", "exclude", "handoff"):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                fail(errors, f"{entry['name']}: missing registry {key}")
        for sibling in re.findall(r"ccf-[a-z0-9-]+", entry.get("handoff", "")):
            if sibling not in EXPECTED_SKILLS:
                fail(errors, f"{entry['name']}: unknown handoff {sibling}")
    if not registered_order or registered_order[0] != "ccf-humanization":
        fail(errors, "ccf-humanization must be the first registry entry")
    if data.get("runtime_skill_count") != len(EXPECTED_SKILLS):
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


def check_resources_and_scripts(errors: list[str]) -> None:
    """Check executable syntax and concrete resource links, not prose wording."""
    scripts = set(ROOT.glob("ccf-*/scripts/*.py")) | set(ROOT.glob("ccf-*/resources/python/*.py")) | set(ROOT.glob("tools/*.py"))
    for path in sorted(scripts):
        try:
            ast.parse(read(path), filename=str(path.relative_to(ROOT)))
        except (SyntaxError, UnicodeError) as exc:
            fail(errors, f"{path.relative_to(ROOT)}: invalid Python: {exc}")
    for path in sorted(ROOT.glob("ccf-*/SKILL.md")):
        for token in re.findall(r"`([^`\n]+)`", read(path)):
            if any(char in token for char in "*<> |"):
                continue
            if not token.startswith(("references/", "scripts/", "assets/", "resources/", "../")):
                continue
            if not token.endswith((".md", ".py", ".yaml", ".json")):
                continue
            target = (path.parent / token).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
                fail(errors, f"{path.relative_to(ROOT)}: missing or external resource: {token}")


def check_text_encodings(errors: list[str]) -> None:
    """Reject damaged maintained text without guessing or rewriting its encoding."""
    suffixes = {".md", ".py", ".yaml", ".yml", ".json", ".svg", ".tex", ".bib", ".cls", ".sty", ".txt", ".rst", ".bst", ".csv", ".toml", ".ps1", ".sh", ".cfg", ".def", ".dtx", ".bbx", ".cbx", ".xml", ".html", ".css", ".js", ".ts", ".lua", ".ist", ".bbl", ".latex"}
    excluded = {".git", "output", "ccfa-workfiles", "__pycache__", ".pytest_cache", "node_modules", ".venv", "venv"}
    for directory, children, filenames in os.walk(ROOT):
        children[:] = [name for name in children if name not in excluded]
        for filename in filenames:
            path = Path(directory) / filename
            if path.suffix.lower() not in suffixes:
                continue
            try:
                text = read(path)
            except UnicodeError as exc:
                fail(errors, f"{path.relative_to(ROOT)}: invalid UTF-8: {exc}")
                continue
            if "\ufffd" in text:
                fail(errors, f"{path.relative_to(ROOT)}: contains U+FFFD replacement characters; inspect the source")


def check_encoding_regressions(errors: list[str]) -> None:
    """Exercise actual UTF-8 pipes/files under legacy standard-stream encodings."""
    try:
        prose = ROOT / "ccf-paper-writer/scripts/check_prose_quality.py"
        review = ROOT / "ccf-paper-reviewer/scripts/validate_version_comparison.py"
        phrase = "为避免审稿人对中文𠮷🔬的质疑"
        payload = (phrase + "，我们核对了繁體中文与简体中文。\n").encode("utf-8")
        with tempfile.TemporaryDirectory(prefix="ccfa-encoding-") as temporary:
            work = Path(temporary).resolve()
            if not work.is_relative_to(Path(tempfile.gettempdir()).resolve()):
                raise ValueError("encoding fixture escaped the managed temporary root")
            source = work / "中文稿件𠮷.md"
            source.write_bytes(b"\xef\xbb\xbf" + payload)

            def run(script, arguments=(), data=None, legacy="gbk"):
                env = dict(os.environ, PYTHONIOENCODING=legacy, PYTHONUTF8="0")
                result = subprocess.run([sys.executable, str(script), *map(str, arguments)], input=data, capture_output=True, env=env, timeout=30)
                return result.returncode, result.stdout.decode("utf-8"), result.stderr.decode("utf-8")

            for legacy in ("ascii", "gbk"):
                for arguments, data in ((("--format", "json"), payload), ((source, "--format", "json"), None)):
                    code, out, err = run(prose, arguments, data, legacy)
                    if code or err or not any(item.get("text") == phrase for item in json.loads(out)["issues"]):
                        raise AssertionError(f"Chinese prose changed through {legacy} file/pipe I/O")
            code, _, err = run(prose, ("--format", "json"), "中文".encode("gbk"))
            if code != 2 or "Cannot read UTF-8 input" not in err:
                raise AssertionError("invalid UTF-8 input was silently accepted or replaced")

            # A BOM must not turn a valid JSON document into an input error.
            comparison = work / "复审输入𠮷.json"
            comparison.write_bytes(b"\xef\xbb\xbf{}")
            for arguments, data in (((comparison, "--format", "json"), None), (("--format", "json"), comparison.read_bytes())):
                code, out, err = run(review, arguments, data)
                findings = json.loads(out)["errors"]
                if code != 1 or err or not findings or any(item.startswith("input error:") for item in findings):
                    raise AssertionError("UTF-8 BOM JSON did not reach comparison validation")
            code, out, err = run(review, ("--report", "--format", "json"), ("## 1. 错误标题𠮷🔬\n中文内容\n").encode("utf-8"), "ascii")
            if code != 1 or err or "错误标题𠮷🔬" not in out:
                raise AssertionError("Chinese review diagnostics did not survive redirected UTF-8 output")

            registry = work / "中文来源𠮷.yaml"
            registry.write_bytes(b"\xef\xbb\xbf" + "sources: []\n".encode("utf-8"))
            code, out, err = run(ROOT / "ccf-common/scripts/check_sources.py", (registry,), legacy="ascii")
            if code or err or registry.name not in out:
                raise AssertionError("registry CLI lost a Chinese path or rejected a UTF-8 BOM")

            # The repository checker must catch both invalid bytes and already-lost text.
            source.write_bytes(b"\xff")
            replacement = work / "lost.md"
            replacement.write_bytes("lost \ufffd text".encode("utf-8"))
            cache = work / "ccfa-workfiles" / "literature" / "fixture" / "cache"
            cache.mkdir(parents=True)
            (cache / "raw-extraction.md").write_bytes(b"\xff")
            detected = []
            with patch.dict(check_text_encodings.__globals__, {"ROOT": work}):
                check_text_encodings(detected)
            if not any("invalid UTF-8" in item for item in detected) or not any("U+FFFD" in item for item in detected):
                raise AssertionError("encoding checker missed a damaged text fixture")
            if any("raw-extraction.md" in item for item in detected):
                raise AssertionError("working cache was treated as maintained skill text")
    except Exception as exc:
        fail(errors, f"encoding regression failed: {type(exc).__name__}: {exc}")


def check_project_and_plugins(errors: list[str]) -> None:
    required = {"version", "project", "target_venue", "stage", "artifacts", "claims", "experiments", "reviews", "revision_ledger", "submission_checks"}
    for rel in ("ccf-project-scaffolder/assets/ccfa.yaml", "demo/attention-is-all-you-need/ccfa.yaml"):
        try:
            state = yaml.safe_load(read(ROOT / rel))
            if not isinstance(state, dict) or not required.issubset(state):
                fail(errors, f"{rel}: missing ccfa.yaml contract fields")
        except (OSError, yaml.YAMLError) as exc:
            fail(errors, f"{rel}: {exc}")
    versions = []
    for rel, root_key in ((".codex-plugin/plugin.json", "skills"), (".claude-plugin/plugin.json", "skills_root")):
        try:
            manifest = json.loads(read(ROOT / rel))
            versions.append(manifest.get("version"))
            location = manifest.get(root_key)
            if not isinstance(location, str) or not location:
                fail(errors, f"{rel}: missing explicit {root_key} path")
                continue
            base = (ROOT / location).resolve()
            if not base.is_relative_to(ROOT.resolve()) or not base.is_dir():
                fail(errors, f"{rel}: invalid skill root {location}")
                continue
            discovered = {path.parent.name for path in base.glob("*/SKILL.md")}
            if discovered != EXPECTED_SKILLS:
                fail(errors, f"{rel}: skill root does not expose the 17 family packages")
            if rel.startswith(".claude-plugin"):
                entries = manifest.get("entrypoints", [])
                if not entries or entries[0] != "ccf-humanization" or set(entries) - EXPECTED_SKILLS:
                    fail(errors, f"{rel}: invalid declared entrypoints")
        except (OSError, json.JSONDecodeError, TypeError) as exc:
            fail(errors, f"{rel}: {exc}")
    if len(versions) == 2 and (not versions[0] or versions[0] != versions[1]):
        fail(errors, "plugin release versions disagree")


def check_prose_regressions(errors: list[str]) -> None:
    """Exercise humanization signals and scientific-language exclusions in memory."""
    path = ROOT / "ccf-paper-writer/scripts/check_prose_quality.py"
    try:
        inspect = runpy.run_path(str(path), run_name="ccfa_prose_check")["inspect"]
        candidates = [
            "To address potential reviewer concerns, we include an ablation.",
            "We do not claim to solve every task.",
            "The result might potentially suggest a useful relation.",
            "为避免审稿人质疑，我们加入消融实验。",
            "我们并不试图解决所有问题。",
        ]
        for text in candidates:
            result = inspect(text, "paragraph")
            if not any(item["code"] == "defensive_framing" for item in result["issues"]):
                fail(errors, "prose checker missed a defensive-language regression case")
        factual = "We use only training labels. The bound does not hold when the stated assumption fails. The observations suggest a relation; causality remains untested. Robust optimization minimizes the worst-case loss."
        if any(item["code"] == "defensive_framing" for item in inspect(factual, "paper")["issues"]):
            fail(errors, "prose checker treats legitimate scientific scope or uncertainty as defensive")
        quoted = '```text\nWe do not claim to solve every task.\n```\n> We do not claim to solve every task.\n\\begin{equation}a---b\\end{equation}\n% We do not claim to solve every task.\nWe do not claim to solve every task.'
        findings = [item for item in inspect(quoted, "paper")["issues"] if item["code"] == "defensive_framing"]
        if len(findings) != 1 or findings[0].get("line") != 7:
            fail(errors, "prose checker lost source line locations or scanned code/math/quotes/comments")
        if inspect(quoted, "paper")["em_dash_count"]:
            fail(errors, "prose checker counts equation dashes as authored prose")
        percentage = "Accuracy is 90%. We do not claim to solve every task."
        if not any(item["code"] == "defensive_framing" for item in inspect(percentage, "paragraph")["issues"]):
            fail(errors, "prose checker mistakes a Markdown percentage for a TeX comment")
        if not any(item["code"] == "em_dash_limit" for item in inspect("A — B — C — D — E.", "paper")["issues"]):
            fail(errors, "prose checker lost the full-paper punctuation preference")
    except Exception as exc:
        fail(errors, f"prose checker could not run regression cases: {type(exc).__name__}: {exc}")


def check_review_regressions(errors: list[str]) -> None:
    """Keep progress, readiness, and attributable regressions separate."""
    try:
        review_tools = runpy.run_path(str(ROOT / "ccf-paper-reviewer/scripts/validate_version_comparison.py"), run_name="ccfa_review_check")
        validate = review_tools["validate"]
        sample = {
            "contract": {"id": "frozen", "venue": "test", "scale": "1-10", "dimensions": ["soundness"], "weights": {"soundness": 1}, "reviewer_roles": ["method"], "thresholds": {"ready": 6}, "evidence_standard": "supplied evidence"},
            "relative_progress_scorecard": {"historical": {"soundness": 2}, "current": {"soundness": 3}, "deltas": {"soundness": 1}, "weighted_delta": 1, "classification": "improved"},
            "absolute_readiness_scorecard": {"current_dimension_scores": {"soundness": 3}, "scale": "1-10", "stance": "not ready", "threshold": "6", "evidence_standard": "supplied evidence", "overall_score": 3},
            "confidence_and_comparability": "Same contract; limited evidence.", "issues": [],
        }
        if validate(sample):
            fail(errors, "review validator rejects progress that remains below readiness")
        missing = copy.deepcopy(sample)
        del missing["absolute_readiness_scorecard"]
        if not validate(missing):
            fail(errors, "review validator accepts missing absolute readiness")
        regression = copy.deepcopy(sample)
        regression["relative_progress_scorecard"].update(historical={"soundness": 3}, current={"soundness": 2}, deltas={"soundness": -1}, weighted_delta=-1, classification="regressed")
        if not validate(regression):
            fail(errors, "review validator accepts an untraceable score decrease")
        issue = {"id": "R1", "origin": "revision_regression", "applies_to": "current", "status": "unresolved", "affected_dimensions": ["soundness"], "evidence": "Current proof drops a necessary premise in step 2.", "score_effect": {"historical": 0, "current": -1}}
        regression["issues"] = [issue]
        if validate(regression):
            fail(errors, "review validator rejects a traceable current-version regression")
        issue["origin"] = "previously_undetected"
        if not validate(regression):
            fail(errors, "review validator penalizes only the current version for a latent shared issue")

        criteria = review_tools["_canonical_criteria"]()
        independent_readiness = copy.deepcopy(sample)
        independent_readiness["absolute_readiness_scorecard"].update(
            rubric="generic-7", current_dimension_scores={key: 4 for key, _, _ in criteria})
        independent_readiness["absolute_readiness_scorecard"]["current_dimension_scores"]["ethics_limitations"] = "N/A"
        if validate(independent_readiness):
            fail(errors, "review validator forces a new readiness rubric into the frozen historical dimensions")
        invalid_readiness = copy.deepcopy(independent_readiness)
        invalid_readiness["absolute_readiness_scorecard"]["current_dimension_scores"]["ethics_limitations"] = 0
        if not validate(invalid_readiness):
            fail(errors, "review validator accepts zero as unassessed generic readiness")

        check_report = review_tools["validate_report"]
        finding = """### C001: A located concern
Type: clarification
Severity: major
Location: Section 3, paragraph 2
Evidence: The claim has two possible readings.
Countercheck: The supplied appendix resolves one reading but not the other.
Judgment: Clarification could change the assessment.
Criterion: Soundness
Resolution: Identify which reading the claim asserts.
Status: unresolved
"""

        def report(mode="scientific", detail="detailed", no_scores=False, chinese=False):
            parts = ["# Review fixture"]
            headings = review_tools["_profile_headings"](mode, detail)
            for number, labels in headings:
                english = next(label for label in labels if label.isascii())
                label = next(label for label in labels if not label.isascii() and " / " not in label) if chinese else english
                parts.append(f"## {number}. {label}")
                concern_section = 3 if detail == "brief" else 5 if mode == "writing" else 6
                ratings_section = 4 if detail == "brief" else 7 if mode == "writing" else 12
                if number == concern_section:
                    parts.append(finding)
                elif number == ratings_section:
                    table = ["| Dimension | Judgment | Confidence | Evidence basis | Deduction / score-change condition |" if no_scores else
                             "| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |",
                             "| --- | --- | --- | --- | --- |"]
                    for key, english_label, chinese_label in criteria:
                        dimension = chinese_label if chinese else english_label
                        score = "Supported" if no_scores else "4"
                        confidence = "Well checked" if no_scores else "4"
                        if key == "ethics_limitations":
                            score = confidence = "N/A"
                        table.append(f"| {dimension} | {score} | {confidence} | Section 3; [C001] | Reassess after clarification. |")
                    table.append("**Overall:** evidence-limited stance | **Scholarly Confidence:** moderate" if no_scores else
                                 "**Overall:** 6 | **Scholarly Confidence:** 4")
                    if mode == "writing":
                        parts.append("Writing criteria are not scientifically scored in this fixture.")
                    elif mode == "version-comparison":
                        parts.extend(["### Relative Progress / 相对进步", "Historical dimensions remain frozen.",
                                      "### Absolute Readiness / 绝对成熟度", "\n".join(table),
                                      "### Confidence And Comparability / 置信度与可比性", "Separate evidence coverage."])
                    elif detail == "brief":
                        parts.append(table[-1])
                    else:
                        parts.append("\n".join(table))
                else:
                    parts.append("Scope-specific structural fixture; see [C001].")
            return "\n\n".join(parts) + "\n"

        good = report()
        bold_fields = finding
        bilingual_fields = finding
        chinese_fields = finding
        for key, chinese in review_tools["FINDING_FIELDS"].items():
            label = key.title()
            bold_fields = bold_fields.replace(f"{label}:", f"- **{label}:**")
            bilingual_fields = bilingual_fields.replace(f"{label}:", f"- **{chinese} / {label}:**")
            chinese_fields = chinese_fields.replace(f"{label}:", f"**{chinese}：**")
        comparison_confidence = report(mode="version-comparison").replace(" | **Scholarly Confidence:** 4", "").replace(
            "Separate evidence coverage.", "**Scholarly Confidence:** 4\nSeparate evidence coverage.")
        valid_profiles = [
            (good, {}), (report(mode="full"), {"mode": "full"}),
            (report(chinese=True), {}),
            (good.replace(finding, bold_fields), {}),
            (good.replace(finding, bilingual_fields).replace("**Overall:**", "**Overall / 总分:**").replace("**Scholarly Confidence:**", "**总体置信度 / Scholarly Confidence:**"), {}),
            (good.replace(finding, chinese_fields), {}),
            (report(no_scores=True), {"no_scores": True}),
            (report(mode="writing"), {"mode": "writing"}),
            (report(detail="brief"), {"detail": "brief"}),
            (report(mode="writing", detail="brief"), {"mode": "writing", "detail": "brief"}),
            (report(mode="version-comparison"), {"mode": "version-comparison"}),
            (comparison_confidence, {"mode": "version-comparison"}),
            (report(mode="version-comparison", detail="brief"), {"mode": "version-comparison", "detail": "brief"}),
            (good.replace("C001", "R1"), {}),
            (good.replace("# Review fixture", "# Review fixture\n\n```text\n## 99. Quoted heading\n[C999]\n```\n> [C998]"), {}),
            (good.replace("| Novelty | 4 |", "| Originality | 3.5 |"), {"rubric": "external"}),
        ]
        for text, options in valid_profiles:
            findings = check_report(text, **options)
            if findings:
                fail(errors, f"review report validator rejects a valid profile {options}: {findings}")
        invalid_reports = {
            "renamed heading": good.replace("## 2. Expected Review Outcome", "## 2. Different heading"),
            "reordered heading": good.replace("## 2. Expected Review Outcome", "## 5. Strengths"),
            "missing section": good.replace("## 3. Desk Rejection Assessment", "### Desk Rejection Assessment"),
            "empty section": good.replace("## 3. Desk Rejection Assessment\n\nScope-specific structural fixture; see [C001].", "## 3. Desk Rejection Assessment"),
            "undefined ID": good + "\nSee [C999].\n",
            "duplicate ID": good.replace(finding, finding + "\n" + finding),
            "missing evidence field": good.replace("Evidence: The claim has two possible readings.\n", ""),
            "unsupported finding type": good.replace("Type: clarification", "Type: definitely_wrong"),
            "invalid severity": good.replace("Severity: major", "Severity: severe"),
            "zero criterion": good.replace("| Novelty | 4 |", "| Novelty | 0 |"),
            "fractional criterion": good.replace("| Novelty | 4 |", "| Novelty | 3.5 |"),
            "missing dimension": "\n".join(line for line in good.splitlines() if not line.startswith("| Novelty |")),
            "alias dimension": good.replace("| Novelty |", "| Originality |"),
            "invented dimension": good.replace("| Novelty |", "| Quality |"),
            "wrong table width": good.replace("| Novelty | 4 | 4 |", "| Novelty | 4 |"),
            "broken separator": good.replace("| --- | --- | --- | --- | --- |", "| - | - | - | - | - |"),
            "N/A as zero": good.replace("| N/A | N/A |", "| 0 | N/A |"),
            "N/A decorated with zero": good.replace("| N/A | N/A |", "| N/A (0) | N/A |"),
            "zero overall": good.replace("**Overall:** 6", "**Overall:** 0"),
            "missing overall": good.replace("**Overall:** 6 | ", ""),
            "missing overall confidence": good.replace(" | **Scholarly Confidence:** 4", ""),
            "empty overall confidence": good.replace("**Scholarly Confidence:** 4", "**Scholarly Confidence:**"),
            "fractional overall": good.replace("**Overall:** 6", "**Overall:** 6.5"),
            "out-of-range confidence": good.replace("**Scholarly Confidence:** 4", "**Scholarly Confidence:** 6"),
        }
        for label, text in invalid_reports.items():
            if not check_report(text):
                fail(errors, f"review report validator accepts {label}")
        if not check_report(good, no_scores=True):
            fail(errors, "review report validator accepts numeric scores in a qualitative report")
        if not check_report(report(mode="version-comparison").replace("### Absolute Readiness / 绝对成熟度", "### Combined score"), mode="version-comparison"):
            fail(errors, "review report validator accepts fused comparison scorecard headings")
    except Exception as exc:
        fail(errors, f"review validator could not run regression cases: {type(exc).__name__}: {exc}")


def check_artifact_regressions(errors: list[str]) -> None:
    """Exercise current-file updates in one managed temporary directory."""
    try:
        plots = runpy.run_path(str(ROOT / "ccf-visual-composer/resources/python/ccfa_plot_recipes.py"), run_name="ccfa_plot_check")
        convert = runpy.run_path(str(ROOT / "ccf-paper-to-exemplar/scripts/convert.py"), run_name="ccfa_convert_check")
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><text>Current figure 中文𠮷🔬與繁體</text></svg>'
        with tempfile.TemporaryDirectory(prefix="ccfa-validation-") as temporary:
            work = Path(temporary).resolve()
            if not work.is_relative_to(Path(tempfile.gettempdir()).resolve()):
                raise ValueError("validation directory escaped the managed temporary root")
            target = work / "figures" / "中文图𠮷.svg"
            save = plots["save_svg"]
            save(svg, target)
            if target.read_text(encoding="utf-8") != svg:
                raise AssertionError("SVG export changed the authoring content")
            with patch.dict(save.__globals__, {"replace": lambda *args: (_ for _ in ()).throw(AssertionError("unchanged SVG was rewritten"))}):
                save(svg, target)
            try:
                save("<svg>", target)
            except Exception as exc:
                if type(exc).__name__ != "ParseError":
                    raise
            else:
                raise AssertionError("invalid SVG replaced the usable figure")
            with patch.dict(save.__globals__, {"replace": lambda *args: (_ for _ in ()).throw(OSError("simulated export failure"))}):
                try:
                    save(svg.replace("Current", "Changed"), target)
                except OSError:
                    pass
                else:
                    raise AssertionError("failed SVG publication was reported successful")
            if target.read_text(encoding="utf-8") != svg or list(target.parent.glob("*.tmp")):
                raise AssertionError("failed SVG publication damaged the current file or left temporary output")
            save(svg.replace("Current", "Changed"), target)
            if len(list(target.parent.iterdir())) != 1 or "Changed" not in target.read_text(encoding="utf-8"):
                raise AssertionError("SVG iteration did not replace the single canonical artifact")

            source = work / "论文𠮷.pdf"
            source.write_bytes(b"fixture; extraction is supplied by the test")
            cards = work / "cards"
            cards.mkdir()
            card = cards / "论文𠮷.md"
            card.write_text("# Completed analysis\nRetain the supplied writing insight.\n", encoding="utf-8")
            cache = work / "cache"
            main = convert["main"]
            output = io.StringIO()
            argv = ["convert.py", str(source), "--output-dir", str(cards), "--full-text", "--full-text-dir", str(cache)]
            with patch.object(sys, "argv", argv), patch.dict(main.__globals__, {"_check_pymupdf": lambda: None, "extract_text": lambda path: "## Page 1\n\nAbstract\nCurrent source. 中文𠮷🔬與繁體。"}), contextlib.redirect_stdout(output):
                if main() != 0:
                    raise AssertionError("exemplar refresh failed")
            if not card.read_text(encoding="utf-8").startswith("# Completed analysis"):
                raise AssertionError("extraction overwrote a completed exemplar card")
            extracted = cache / "论文𠮷.full.md"
            if not extracted.is_file() or (cards / "论文𠮷.full.md").exists():
                raise AssertionError("explicit extraction cache location was ignored")
            previous = extracted.read_text(encoding="utf-8")
            if "中文𠮷🔬與繁體" not in previous:
                raise AssertionError("exemplar extraction changed Chinese text")
            write = convert["write_current"]
            with patch.dict(write.__globals__, {"replace": lambda *args: (_ for _ in ()).throw(OSError("simulated text export failure"))}):
                try:
                    write(extracted, "new extraction")
                except OSError:
                    pass
                else:
                    raise AssertionError("failed text publication was reported successful")
            if extracted.read_text(encoding="utf-8") != previous or list(cache.glob("*.tmp")):
                raise AssertionError("failed text publication damaged the cache or left temporary output")
    except Exception as exc:
        fail(errors, f"artifact regression failed: {type(exc).__name__}: {exc}")


def main() -> int:
    # Standalone reports and redirected diagnostics use UTF-8 on every platform.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    errors: list[str] = []
    names = check_skills(errors)
    check_registry(names, errors)
    check_venue_guides(errors)
    check_required_files(errors)
    check_resources_and_scripts(errors)
    check_text_encodings(errors)
    check_encoding_regressions(errors)
    check_project_and_plugins(errors)
    check_prose_regressions(errors)
    check_review_regressions(errors)
    check_artifact_regressions(errors)
    if errors:
        print("CCFA validation failed:")
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print(f"CCFA validation passed. Skills: {len(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
