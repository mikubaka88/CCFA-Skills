#!/usr/bin/env python3
"""Check factual anchors before optional blind semantic assessment; no LLM API.

String anchors are narrow regression signals, not a measure of natural prose,
scientific novelty or humanization. Grade those from the actual outputs.
"""
import argparse
import json
from pathlib import Path
import sys


def check_outputs(suite, outputs):
    tasks = suite["tasks"]
    if not isinstance(outputs, dict) or set(outputs) != {task["id"] for task in tasks}:
        raise ValueError("Outputs must map every declared task ID to its actual text")
    result = []
    for task in tasks:
        text = outputs[task["id"]]
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Empty output: " + task["id"])
        missing = [term for term in task["invariants"]["contains"] if term not in text]
        result.append({"task": task["id"], "nonempty": True, "missing_factual_anchors": missing,
                       "characters": len(text), "semantic_assessment_required": True})
    return {"schema_version": 1, "checks": result,
            "factual_anchor_checks_pass": not any(item["missing_factual_anchors"] for item in result),
            "quality_score": None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs", required=True, help="JSON object: task ID to generated text")
    parser.add_argument("--suite", default=str(Path(__file__).with_name("tasks.json")))
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    try:
        suite = json.loads(Path(args.suite).read_text(encoding="utf-8-sig"))
        outputs = json.loads(Path(args.outputs).read_text(encoding="utf-8-sig"))
        result = check_outputs(suite, outputs)
    except (ValueError, OSError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["factual_anchor_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
