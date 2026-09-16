#!/usr/bin/env python3
"""Validate current CCFA structure without rewriting files."""

from __future__ import annotations

import ast
import contextlib
import copy
import io
import json
import math
import re
import runpy
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree

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
        validate = runpy.run_path(str(ROOT / "ccf-paper-reviewer/scripts/validate_version_comparison.py"), run_name="ccfa_review_check")["validate"]
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
    except Exception as exc:
        fail(errors, f"review validator could not run regression cases: {type(exc).__name__}: {exc}")


def check_plot_regressions(errors: list[str]) -> None:
    """Check grouped bars against zero, signed values, and plot bounds."""
    try:
        plots = runpy.run_path(str(ROOT / "ccf-visual-composer/resources/python/ccfa_plot_recipes.py"), run_name="ccfa_plot_check")
        cases = (
            ("all zero", [0, 0], 468.0),
            ("positive", [1, 2], 468.0),
            ("positive and zero", [0, 2], 468.0),
            ("mixed signs", [-1, 0, 1], 300.0),
            ("asymmetric signs", [-1, 0, 2], 356.0),
            ("negative", [-2, -1], 132.0),
            ("negative and zero", [-2, 0], 132.0),
            ("empty", [], 468.0),
        )
        for name, values, baseline in cases:
            rows = [{"group": str(index), "value": value} for index, value in enumerate(values)]
            svg = plots["grouped_bar_chart"](rows, "group", ["value"], "Regression fixture")
            root = ElementTree.fromstring(svg)
            bars = [node for node in root.findall("{http://www.w3.org/2000/svg}rect") if node.get("opacity") == "0.920"]
            if len(bars) != len(values):
                fail(errors, f"grouped bars ({name}): incorrect bar count")
                continue
            heights_per_unit = []
            for value, bar in zip(values, bars):
                y, height = float(bar.attrib["y"]), float(bar.attrib["height"])
                if not all(math.isfinite(number) for number in (y, height)) or height < 0 or y < 131.99 or y + height > 468.01:
                    fail(errors, f"grouped bars ({name}): invalid geometry or bar outside plot bounds")
                if value == 0:
                    if height != 0 or not math.isclose(y, baseline, abs_tol=0.01):
                        fail(errors, f"grouped bars ({name}): zero must have no height at the baseline")
                else:
                    anchor = y + height if value > 0 else y
                    if height <= 0 or not math.isclose(anchor, baseline, abs_tol=0.01):
                        fail(errors, f"grouped bars ({name}): bar must extend from zero in the value's direction")
                    heights_per_unit.append(height / abs(value))
            if heights_per_unit and max(heights_per_unit) - min(heights_per_unit) > 0.01:
                fail(errors, f"grouped bars ({name}): bar heights must be proportional to magnitude")
    except Exception as exc:
        fail(errors, f"plot regression failed: {type(exc).__name__}: {exc}")


def check_artifact_regressions(errors: list[str]) -> None:
    """Exercise current-file updates in one managed temporary directory."""
    try:
        plots = runpy.run_path(str(ROOT / "ccf-visual-composer/resources/python/ccfa_plot_recipes.py"), run_name="ccfa_plot_check")
        convert = runpy.run_path(str(ROOT / "ccf-paper-to-exemplar/scripts/convert.py"), run_name="ccfa_convert_check")
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><text>Current figure</text></svg>'
        with tempfile.TemporaryDirectory(prefix="ccfa-validation-") as temporary:
            work = Path(temporary).resolve()
            if not work.is_relative_to(Path(tempfile.gettempdir()).resolve()):
                raise ValueError("validation directory escaped the managed temporary root")
            target = work / "figures" / "main.svg"
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

            source = work / "paper.pdf"
            source.write_bytes(b"fixture; extraction is supplied by the test")
            cards = work / "cards"
            cards.mkdir()
            card = cards / "paper.md"
            card.write_text("# Completed analysis\nRetain the supplied writing insight.\n", encoding="utf-8")
            cache = work / "cache"
            main = convert["main"]
            output = io.StringIO()
            argv = ["convert.py", str(source), "--output-dir", str(cards), "--full-text", "--full-text-dir", str(cache)]
            with patch.object(sys, "argv", argv), patch.dict(main.__globals__, {"_check_pymupdf": lambda: None, "extract_text": lambda path: "## Page 1\n\nAbstract\nCurrent source."}), contextlib.redirect_stdout(output):
                if main() != 0:
                    raise AssertionError("exemplar refresh failed")
            if not card.read_text(encoding="utf-8").startswith("# Completed analysis"):
                raise AssertionError("extraction overwrote a completed exemplar card")
            extracted = cache / "paper.full.md"
            if not extracted.is_file() or (cards / "paper.full.md").exists():
                raise AssertionError("explicit extraction cache location was ignored")
            previous = extracted.read_text(encoding="utf-8")
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
    errors: list[str] = []
    names = check_skills(errors)
    check_registry(names, errors)
    check_venue_guides(errors)
    check_required_files(errors)
    check_resources_and_scripts(errors)
    check_project_and_plugins(errors)
    check_prose_regressions(errors)
    check_review_regressions(errors)
    check_plot_regressions(errors)
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
