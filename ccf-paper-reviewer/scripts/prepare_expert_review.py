#!/usr/bin/env python3
"""Prepare one independent GPT-6 expert request for the host to execute.

This standard-library helper never calls an API, starts an agent, saves a
preference, or expands a budget. Supply the real host model inventory and fresh
context capability. Manuscript/supplement/criteria inputs here are UTF-8 text;
native PDF and vision workflows remain available through the reviewing owner.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import sys


MODES = {"scientific", "full", "writing", "concept"}
LANGUAGES = {"zh-CN", "zh-TW", "en"}
TRIGGERS = {"unresolved-judgment", "pre-submission"}
PHASES = {"unspecified", "draft", "results-pending", "submission"}
FAMILY_ROOT = Path(__file__).resolve().parents[2]
PROMPT_PATH = Path(__file__).resolve().parents[1] / "references/plain-expert-review.md"


def _decision(status, reason, owner="ccf-paper-reviewer"):
    return {"schema_version": 1, "status": status, "reason": reason,
            "owner": owner, "executed": False, "primary_review_continues": True}


def _source(path, role):
    path = Path(path).expanduser().resolve()
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    if not text.strip():
        raise ValueError("Empty review input: " + str(path))
    return {"role": role, "path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "text": text, "coverage": "complete supplied text file"}


def _prompt(language):
    path = PROMPT_PATH
    raw = path.read_bytes()
    marker = re.escape(language)
    matches = re.findall(r"<!-- prompt:" + marker + r" -->\s*(.*?)\s*<!-- /prompt:" + marker + r" -->",
                         raw.decode("utf-8-sig"), re.DOTALL)
    if len(matches) != 1 or not matches[0].strip():
        raise ValueError("Missing or ambiguous plain expert prompt: " + language)
    text = matches[0].strip()
    return {"language": language, "text": text,
            "path": str(path), "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}


def _optional_text(value, name):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValueError(name + " must be text")
    return value.strip()


def _strings(values, name):
    if not isinstance(values, (list, tuple)):
        raise ValueError(name + " must be a list of explicit instructions")
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(name + " entries must be nonempty text")
    return [item.strip() for item in values]


def _focus_locations(values, documents):
    if not isinstance(values, (list, tuple)):
        raise ValueError("focus_locations must be a list of source locations")
    sources = {item["path"]: item for item in documents}
    result = []
    for item in values:
        if not isinstance(item, dict) or set(item) - {"path", "anchor", "start_line", "end_line"} or "path" not in item:
            raise ValueError("Focus locations accept path, anchor and optional inclusive start_line/end_line")
        path = str(Path(item["path"]).expanduser().resolve())
        if path not in sources:
            raise ValueError("A focus location must refer to a supplied review document")
        source = sources[path]
        location = {"path": path, "sha256": source["sha256"]}
        anchor = _optional_text(item.get("anchor"), "focus anchor")
        if anchor:
            location["anchor"] = anchor
        if "start_line" in item or "end_line" in item:
            start, end = item.get("start_line"), item.get("end_line")
            if type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(source["text"].splitlines()):
                raise ValueError("Focus line bounds must lie inside the actual supplied file")
            location.update(start_line=start, end_line=end)
        elif not anchor:
            raise ValueError("A focus location needs a named anchor or an actual line range")
        result.append(location)
    return result


def _family_policies(extra_files):
    if not isinstance(extra_files, (list, tuple)):
        raise ValueError("policy_files must be a list of applied instruction files")
    identities, seen = [], set()
    files = [(name, FAMILY_ROOT / name / "SKILL.md") for name in ("ccf-humanization", "ccf-common")]
    files += [("additional-policy-" + str(i+1), path) for i, path in enumerate(extra_files)]
    for identity, path in files:
        source = _source(path, "applied-policy")
        if source["path"] in seen:
            raise ValueError("Declare an applied policy file once")
        seen.add(source["path"])
        identities.append({"id": identity, "path": source["path"], "sha256": source["sha256"]})
    return identities


def _execution_spec(runtime, effort, options):
    runtime = _optional_text(runtime, "runtime") or None
    effort = _optional_text(effort, "effort") or None
    if options is not None and not isinstance(options, dict):
        raise ValueError("options must be an object of effective execution settings")
    options = copy.deepcopy(options)
    # Reject unserializable values and NaN rather than inventing a configuration.
    json.dumps(options, ensure_ascii=False, allow_nan=False)
    return {"runtime": runtime, "effort": effort, "options": options}


def _request_fingerprint(request):
    signature = copy.deepcopy(request)
    # These paths locate instructions; only their effective text/identity is guidance.
    signature["guidance"].pop("path", None)
    for policy in signature["policies"]:
        policy.pop("path", None)
    return hashlib.sha256(json.dumps(signature, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def prepare_expert_review(manuscript, *, mode="scientific", independent_review="off",
                          explicit_expert=False, trigger=None, reason="",
                          available_models=(), model=None, context_isolation=False,
                          language="zh-CN", phase="unspecified", venue="",
                          criteria=None, supplements=(), max_input_chars=None,
                          review_question="", scope="", constraints=(), exclusions=(),
                          focus_locations=(), runtime=None, effort=None, options=None,
                          policy_files=()):
    """Return a ready request or a precise skip decision, without dispatching it.

    The native host must use a fresh context and the selected model; it must
    retain applicable family preflights. A declared capability is not a verified
    completed call. No lead verdict, score or drafting history is accepted here.
    """
    if mode not in MODES or independent_review not in {"off", "auto", "on"}:
        raise ValueError("Invalid review mode or independent_review value")
    if language not in LANGUAGES or phase not in PHASES:
        raise ValueError("Invalid language or manuscript phase")
    if trigger is not None and trigger not in TRIGGERS:
        raise ValueError("Invalid independent-review trigger")
    if not isinstance(reason, str) or not isinstance(venue, str):
        raise ValueError("Reason and venue must be text")
    if mode == "concept":
        return _decision("not_applicable", "Route concept-only expertise through the idea reviewer; do not impose manuscript experiments.", "ccf-idea-reviewer")
    if mode == "writing" and not explicit_expert:
        return _decision("not_applicable", "Writing-only review does not automatically add a scientific expert.")
    if independent_review == "off" and not explicit_expert:
        return _decision("disabled", "No additional expert requested; preserve the saved Off preference.")
    if independent_review == "auto" and not explicit_expert and (trigger is None or not reason.strip()):
        return _decision("needs_trigger", "Auto needs a consequential unresolved judgment or pre-submission trigger and its concrete reason.")
    if not context_isolation:
        return _decision("unavailable", "The extra expert needs an actual fresh-context capability; continue the primary review.")
    if (not isinstance(available_models, (list, tuple))
            or any(not isinstance(item, str) or not item.strip() for item in available_models)):
        raise ValueError("Use the actual host's list of available model IDs")
    if model is not None and (not isinstance(model, str) or not model.strip()):
        raise ValueError("Model ID must be nonempty text")
    is_gpt6 = lambda value: bool(re.match(r"^gpt-6(?:[.-]|$)", value))
    if model is not None:
        selected = model if model in available_models and is_gpt6(model) else None
    else:
        # The caller orders this inventory by the host/user's model preference.
        selected = next((item for item in available_models if is_gpt6(item)), None)
    if selected is None:
        return _decision("unavailable", "The requested GPT-6 model is not in the declared host inventory; do not silently substitute another model.")
    review_question = _optional_text(review_question, "review_question")
    scope = _optional_text(scope, "scope")
    constraints = _strings(constraints, "constraints")
    exclusions = _strings(exclusions, "exclusions")
    execution = _execution_spec(runtime, effort, options)
    if max_input_chars is not None and (type(max_input_chars) is not int or max_input_chars < 1):
        raise ValueError("max_input_chars must be a positive integer")
    if not isinstance(supplements, (list, tuple)):
        raise ValueError("Supplements must be a list of paths")
    documents, paths = [], set()
    for path, role in [(manuscript, "manuscript"), *[(p, "supplement") for p in supplements],
                       *([(criteria, "venue-criteria")] if criteria else [])]:
        source = _source(path, role)
        if source["path"] in paths:
            raise ValueError("Declare a source once; duplicate input: " + source["path"])
        paths.add(source["path"])
        documents.append(source)
    guidance = _prompt(language)
    task = {"mode": mode, "phase": phase, "venue": venue,
            "scope": ("Writing and argument only; no scientific acceptance score or new-experiment requirement."
                       if mode == "writing" else (scope or
                           ("Inspect the supplied material needed to answer the stated review question."
                            if review_question else "Assess the supplied manuscript as a whole within the requested scientific scope."))),
            "phase_rule": "Do not treat planned studies as observations. A results-pending draft remains a draft; unsupported empirical assertions are still findings."}
    if review_question:
        task["review_question"] = review_question
    if scope:
        task["requested_scope"] = scope
    if constraints:
        task["constraints"] = constraints
    if exclusions:
        task["exclusions"] = exclusions
    locations = _focus_locations(focus_locations, documents)
    if locations:
        task["focus_locations"] = locations
    # The trigger's existence controls the extra pass, but its diagnosis and the
    # lead reviewer's reason are not passed to the independent first reader.
    request = {"model": selected, "guidance": guidance, "task": task,
               "documents": documents, "fresh_context": True,
               "execution_spec": execution, "policies": _family_policies(policy_files)}
    input_chars = len(json.dumps(request, ensure_ascii=False, allow_nan=False))
    if max_input_chars is not None and input_chars > max_input_chars:
        return _decision("unavailable", "The complete expert request exceeds its declared character allowance; choose an authorized scope or allowance rather than silently truncating it.")
    fingerprint = _request_fingerprint(request)
    return {**_decision("ready", "One independent expert request prepared; native host execution is still required."),
            "fingerprint": fingerprint, "request": request,
            "dispatch": {"fresh_history": True, "include_lead_findings": False,
                         "initial_expert_passes": 1, "apply_family_preflights": True,
                         "verify_actual_model_and_completion": True},
            "input_characters": input_chars,
             "reuse_identity_complete": all(execution[key] is not None for key in ("runtime", "effort", "options")),
            "cost_note": "One additional reading may add input/output tokens and elapsed time. This helper measures no model tokens or costs."}


def assess_review_reuse(prepared, completed):
    """Compare declared execution evidence; never fabricate or dispatch a review.

    The host supplies the retained response, actual execution identity and inspected
    coverage. Matching metadata cannot independently prove a model ran or read it.
    """
    def result(reusable, reason):
        return {"reusable": reusable, "reason": reason}

    if not isinstance(prepared, dict) or prepared.get("status") != "ready":
        return result(False, "No ready expert request to match")
    request = prepared.get("request")
    try:
        fingerprint = _request_fingerprint(request)
    except (AttributeError, KeyError, TypeError, ValueError):
        return result(False, "Prepared request identity is missing or invalid")
    if prepared.get("fingerprint") != fingerprint:
        return result(False, "Prepared request identity is missing or stale")
    spec = request.get("execution_spec")
    if not isinstance(spec, dict):
        return result(False, "Effective execution settings are missing")
    if any(spec.get(key) is None for key in ("runtime", "effort", "options")):
        return result(False, "Effective runtime, effort and options must be declared before reuse")
    if not isinstance(completed, dict) or completed.get("status") != "complete" or completed.get("executed") is not True:
        return result(False, "A pending, interrupted or unexecuted request is not a completed review")
    if not isinstance(completed.get("response"), str) or not completed["response"].strip():
        return result(False, "The retained expert response is unavailable")
    if completed.get("fingerprint") != prepared["fingerprint"]:
        return result(False, "Scientific input, question or effective guidance changed")
    actual = completed.get("execution")
    if not isinstance(actual, dict) or actual.get("model") != request["model"] or actual.get("fresh_context") is not True:
        return result(False, "Actual model or fresh-context provenance does not match")
    if any(actual.get(key) != spec[key] for key in ("runtime", "effort", "options")):
        return result(False, "Actual runtime, effort or options do not match")
    expected_policies = [{"id": item["id"], "sha256": item["sha256"]} for item in request["policies"]]
    if actual.get("policies") != expected_policies:
        return result(False, "The actually applied policy identities do not match")
    coverage = completed.get("coverage")
    if not isinstance(coverage, list):
        return result(False, "Actual inspected source coverage is missing")
    try:
        for document in request["documents"] + request["policies"]:
            if _source(document["path"], "current-identity")["sha256"] != document["sha256"]:
                return result(False, "A scientific source or applied policy changed since preparation")
        if _prompt(request["guidance"]["language"])["sha256"] != request["guidance"]["sha256"]:
            return result(False, "The selected prompt changed since preparation")
    except (OSError, UnicodeError, ValueError, KeyError, TypeError):
        return result(False, "A required current source or instruction cannot be checked")
    sources = {(item["path"], item["sha256"]): item for item in coverage
               if isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(item.get("sha256"), str)}
    locations = request["task"].get("focus_locations", [])
    for document in request["documents"]:
        inspected = sources.get((document["path"], document["sha256"]))
        if not inspected:
            return result(False, "A required source/version was not covered")
        if inspected.get("complete") is True:
            continue
        needed = [item for item in locations if item["path"] == document["path"]]
        actual_locations = inspected.get("locations", [])
        if not isinstance(actual_locations, list) or not needed or any(item not in actual_locations for item in needed):
            return result(False, "The required document or focused locations were not fully inspected")
    return result(True, "Retained response, actual execution identity and requested coverage match")


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--manuscript", required=True)
    cli.add_argument("--mode", choices=sorted(MODES), default="scientific")
    cli.add_argument("--independent-review", choices=["off", "auto", "on"], default="off")
    cli.add_argument("--explicit-expert", action="store_true", help="Current user explicitly requested this additional expert")
    cli.add_argument("--trigger", choices=sorted(TRIGGERS))
    cli.add_argument("--reason", default="", help="Owner's Auto trigger reason, withheld from the independent reader")
    cli.add_argument("--available-model", action="append", default=[], help="Actual host model ID; repeat in host/user preference order")
    cli.add_argument("--model", help="Explicit requested GPT-6 ID; must be actually available")
    cli.add_argument("--context-isolation", action="store_true", help="Host actually supports a fresh independent agent context")
    cli.add_argument("--language", choices=sorted(LANGUAGES), default="zh-CN")
    cli.add_argument("--phase", choices=sorted(PHASES), default="unspecified")
    cli.add_argument("--venue", default="")
    cli.add_argument("--criteria", help="Relevant verified venue-criteria UTF-8 file")
    cli.add_argument("--supplement", action="append", default=[], help="Actual supporting UTF-8 file; repeat when needed")
    cli.add_argument("--max-input-chars", type=int, help="Bound complete serialized request characters; never silently trim")
    cli.add_argument("--review-question", default="", help="Neutral question to assess, without the lead verdict")
    cli.add_argument("--scope", default="", help="Actual user-requested assessment boundary")
    cli.add_argument("--constraint", action="append", default=[], help="Explicit user condition, such as no scores")
    cli.add_argument("--exclude", action="append", default=[], help="Out-of-scope subject; repeat as needed")
    cli.add_argument("--focus-locations", help="UTF-8 JSON list of supplied-document paths and anchors/line ranges")
    cli.add_argument("--runtime", help="Effective host/runtime identity; not inferred")
    cli.add_argument("--effort", help="Effective reasoning setting; do not replace the user's selection")
    cli.add_argument("--options-json", help="JSON object of effective execution options; use {} explicitly when none apply")
    cli.add_argument("--policy", action="append", default=[], help="Additional actually applied instruction file")
    cli.add_argument("--reuse-record", help="Existing UTF-8 completion record to compare read-only; does not run a review")
    return cli


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    args = parser().parse_args(argv)
    try:
        result = prepare_expert_review(args.manuscript, mode=args.mode, independent_review=args.independent_review,
                    explicit_expert=args.explicit_expert, trigger=args.trigger, reason=args.reason,
                    available_models=args.available_model, model=args.model, context_isolation=args.context_isolation,
                    language=args.language, phase=args.phase, venue=args.venue, criteria=args.criteria,
                    supplements=args.supplement, max_input_chars=args.max_input_chars,
                    review_question=args.review_question, scope=args.scope, constraints=args.constraint,
                    exclusions=args.exclude, focus_locations=(json.loads(Path(args.focus_locations).read_text(encoding="utf-8-sig"))
                                                             if args.focus_locations else ()),
                    runtime=args.runtime, effort=args.effort,
                    options=(json.loads(args.options_json) if args.options_json is not None else None),
                    policy_files=args.policy)
        if args.reuse_record:
            completed = json.loads(Path(args.reuse_record).read_text(encoding="utf-8-sig"))
            result["reuse_check"] = assess_review_reuse(result, completed)
    except (ValueError, OSError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
