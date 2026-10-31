#!/usr/bin/env python3
"""Check factual anchors before optional blind semantic assessment; no LLM API.

String anchors are narrow regression signals, not a measure of natural prose,
scientific novelty or humanization. Grade those from the actual outputs.
"""
import argparse
import json
from pathlib import Path
import sys


def suite_tasks(suite):
    tasks = suite.get("tasks") if isinstance(suite, dict) else None
    if not isinstance(tasks, list) or not tasks:
        raise ValueError("Suite must declare a nonempty task list")
    ids = []
    for task in tasks:
        if not isinstance(task, dict) or not isinstance(task.get("id"), str) or not task["id"]:
            raise ValueError("Each task needs a nonempty ID")
        ids.append(task["id"])
        invariants = task.get("invariants", {})
        if not isinstance(invariants, dict):
            raise ValueError("Task invariants must be an object")
        anchors = invariants.get("contains", [])
        alternatives = invariants.get("contains_any", [])
        if not isinstance(anchors, list) or not all(isinstance(value, str) and value for value in anchors):
            raise ValueError("contains must list nonempty literal anchors")
        if not isinstance(alternatives, list) or not all(
                isinstance(group, list) and group and all(isinstance(value, str) and value for value in group)
                for group in alternatives):
            raise ValueError("contains_any must list nonempty groups of alternative literal anchors")
        outcomes = task.get("outcome_checks", [])
        if not isinstance(outcomes, list) or not all(isinstance(value, str) and value for value in outcomes):
            raise ValueError("outcome_checks must list semantic questions")
    if len(ids) != len(set(ids)):
        raise ValueError("Task IDs must be unique")
    return tasks


def model_requests(suite):
    """Separate task inputs from answer anchors and the assessor's questions."""
    return {task["id"]: {**({"execution": suite["execution"]} if "execution" in suite else {}),
                         **{key: task[key] for key in ("owner", "request", "materials", "conversation") if key in task}}
            for task in suite_tasks(suite)}


def check_outputs(suite, outputs):
    tasks = suite_tasks(suite)
    if not isinstance(outputs, dict) or set(outputs) != {task["id"] for task in tasks}:
        raise ValueError("Outputs must map every declared task ID to its actual text")
    result = []
    for task in tasks:
        text = outputs[task["id"]]
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Empty output: " + task["id"])
        invariants = task.get("invariants", {})
        missing = [term for term in invariants.get("contains", []) if term not in text]
        missing_alternatives = [group for group in invariants.get("contains_any", []) if not any(term in text for term in group)]
        semantic_outcomes = list(task.get("outcome_checks", []))
        if invariants.get("forbids_fabricated_results"):
            semantic_outcomes.append("Are result claims limited to the supplied or actually observed findings?")
        result.append({"task": task["id"], "nonempty": True, "missing_factual_anchors": missing,
                       "missing_anchor_alternatives": missing_alternatives,
                       "characters": len(text), "semantic_assessment_required": True,
                       "semantic_outcomes_to_check": semantic_outcomes})
    anchors_pass = not any(item["missing_factual_anchors"] or item["missing_anchor_alternatives"] for item in result)
    return {"schema_version": 1, "checks": result,
            "factual_anchor_checks_pass": anchors_pass,
            "automatic_check_scope": "Literal source anchors only; semantic outcomes and quality remain ungraded",
            "quality_score": None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--outputs", help="JSON object: task ID to generated text")
    mode.add_argument("--prepare", action="store_true", help="Emit only model-facing task inputs, without grading anchors")
    parser.add_argument("--suite", default=str(Path(__file__).with_name("tasks.json")))
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    try:
        suite = json.loads(Path(args.suite).read_text(encoding="utf-8-sig"))
        if args.prepare:
            result = model_requests(suite)
        else:
            outputs = json.loads(Path(args.outputs).read_text(encoding="utf-8-sig"))
            result = check_outputs(suite, outputs)
    except (ValueError, OSError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if args.prepare or result["factual_anchor_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
