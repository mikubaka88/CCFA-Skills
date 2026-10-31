#!/usr/bin/env python3
"""Prepare focused writing inputs, apply scoped edits and reuse exact reviews.

No network, LLM API, preference write, or ccfa.yaml update is performed here.
Paths in a source list are relative to that list's directory; other paths are
relative to the caller. Inspect each manuscript to obtain its actual section IDs.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import secrets
import sys
import tempfile

from manuscript_patch import inspect_manuscript, apply_patch
from writing_context import prepare_context, assess_impact
from writing_review_cache import review_cache


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def _json_snapshot(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return json.loads(raw.decode("utf-8-sig")), {
        "path": str(path), "sha256": hashlib.sha256(raw).hexdigest()}


def _guidance(mode):
    path = Path(__file__).resolve().parents[1] / "references" / "writing-execution.md"
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    marker = re.escape(mode)
    matches = re.findall(r"<!-- prompt:" + marker + r" -->\s*(.*?)\s*<!-- /prompt:" + marker + r" -->",
                         text, re.DOTALL)
    if len(matches) != 1 or not matches[0].strip():
        raise ValueError("Missing or ambiguous writing prompt: " + mode)
    return {"mode": mode, "text": matches[0].strip(), "path": str(path),
            "sha256": hashlib.sha256(raw).hexdigest()}


def _pending_mode(args):
    """Reuse preflight's explicit value, or read sparse preferences without writes."""
    if args.results_pending is not None:
        return args.results_pending
    path = Path(__file__).resolve().parents[2] / "ccf-common" / "scripts" / "preferences.py"
    spec = importlib.util.spec_from_file_location("ccfa_writer_preferences", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        return module.PreferenceStore(project_root=args.project).resolve()["effective"]["preferences"]["results_pending_draft"]
    except module.PreferenceError as exc:
        raise ValueError("Cannot resolve writing preferences: " + str(exc)) from exc


def _sources(path):
    if path is None:
        return [], None
    source_path = Path(path).resolve()
    sources, identity = _json_snapshot(source_path)
    if not isinstance(sources, list):
        raise ValueError("Sources JSON must be an array of source declarations")
    for source in sources:
        if not isinstance(source, dict) or not isinstance(source.get("path"), str):
            raise ValueError("Each source needs an actual file path")
        source["path"] = str((source_path.parent / source["path"]).resolve())
    return sources, identity


def _write_packet(payload, output, forbidden):
    path = Path(output).absolute()
    if path.suffix.lower() != ".json":
        raise ValueError("Writing packets use a .json task file")
    if path.is_symlink() or path.resolve() != path:
        raise ValueError("Use a packet path without symlinks or unresolved path components")
    if any(path.resolve() == Path(other).resolve() for other in forbidden):
        raise ValueError("A packet must not overwrite its manuscript, brief, or sources")
    if path.exists():
        old = read_json(path)
        if not isinstance(old, dict) or old.get("record_type") != "ccfa-writing-packet":
            raise ValueError("Existing file is not a writing packet; refusing to replace it")
    if not path.parent.is_dir():
        raise ValueError("Select an existing task directory for --output")
    lock = path.with_name("." + path.name + ".lock")
    token = secrets.token_hex(16).encode("ascii")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError("Writing packet is being updated by another owner") from exc
    temporary = None
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(token)
        # Recheck after acquiring the cooperative lock.
        if path.exists():
            old = read_json(path)
            if not isinstance(old, dict) or old.get("record_type") != "ccfa-writing-packet":
                raise ValueError("Existing file changed and is not a writing packet")
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=path.parent, prefix="." + path.name + ".",
                                         suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(payload, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        try:
            if not lock.is_symlink() and lock.read_bytes() == token:
                lock.unlink()
        except FileNotFoundError:
            pass


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    commands = cli.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="List actual manuscript sections and version")
    inspect.add_argument("--manuscript", required=True)
    prepare = commands.add_parser("prepare", help="Read target sections, main line, neighbors and selected source passages")
    prepare.add_argument("--manuscript", required=True)
    prepare.add_argument("--target", action="append", required=True, help="Actual section ID; repeat for a coherent section group")
    prepare.add_argument("--brief", help="JSON: message, throughline, optional terminology/protected_literals")
    prepare.add_argument("--sources", help="JSON array: id, path, kind, used_by, optional start_line/end_line")
    prepare.add_argument("--mode", choices=["draft", "related-work", "results", "consistency"], default="draft")
    prepare.add_argument("--max-chars", type=int, help="Bound context JSON characters, not a measured token count")
    prepare.add_argument("--output", help="Optional existing-task .json path, updated in place")
    prepare.add_argument("--results-pending", choices=["off", "on"],
                         help="Reuse resolved preflight choice; on permits marked conditional drafting, never fabricated results")
    prepare.add_argument("--project", type=Path, help="Explicit project root for optional preference overrides")
    apply = commands.add_parser("apply", help="Apply literal edits only to the prepared version and sections")
    apply.add_argument("--packet", required=True)
    apply.add_argument("--patch", required=True, help="JSON: base_sha256, edits[{section_id,before,after}]")
    impact = commands.add_parser("impact", help="Report changed inputs and mapped dependent section/figure IDs")
    impact.add_argument("--packet", required=True)
    cache = commands.add_parser("review-cache", help="Optional receipt; never starts or retries a review")
    cache.add_argument("action", choices=["begin", "complete", "lookup", "abandon"])
    cache.add_argument("--packet", required=True)
    cache.add_argument("--cache", required=True, help="One current task-local JSON receipt")
    cache.add_argument("--model", required=True, help="Actual reviewer model/runtime identity")
    cache.add_argument("--options", help="JSON object with rubric/policy identity and all actual review parameters")
    cache.add_argument("--result", help="Existing nonempty UTF-8 review file for complete")
    cache.add_argument("--coverage", help="JSON: kind full|excerpt, sections[IDs], other actual coverage details")
    cache.add_argument("--call-stopped", action="store_true", help="For abandon: actual review call no longer running")
    return cli


def run(args):
    if args.command == "inspect":
        inventory = inspect_manuscript(args.manuscript)
        inventory["sections"] = [{k: v for k, v in section.items() if k != "text"}
                                 for section in inventory["sections"]]
        return inventory
    if args.command == "prepare":
        sources, source_map = _sources(args.sources)
        brief, brief_identity = _json_snapshot(args.brief) if args.brief else (None, None)
        reserved = {"ccfa-writing-guidance", "ccfa-writing-brief", "ccfa-writing-source-map"}
        if any(source.get("id") in reserved for source in sources):
            raise ValueError("Source ID is reserved for writing runtime inputs")
        packet = prepare_context(args.manuscript, args.target,
                                 brief=brief, sources=sources, max_chars=args.max_chars)
        guidance = _guidance(args.mode)
        pending_mode = _pending_mode(args)
        if pending_mode == "on" and args.mode in {"draft", "results", "consistency"}:
            guidance["text"] += "\n\n" + _guidance("pending-results")["text"]
        packet["draft_policy"] = {"results_pending": pending_mode,
                                  "alignment_required": pending_mode == "on",
                                  "fabricated_observations_allowed": False}
        packet["record_type"] = "ccfa-writing-packet"
        packet["operation"] = "review" if args.mode == "consistency" else "write"
        packet["guidance"] = guidance
        if packet["operation"] == "write":
            packet["patch_schema"] = {"base_sha256": packet["manuscript"]["sha256"],
                "edits": [{"section_id": "<prepared target ID>",
                           "before": "<unique exact original passage>", "after": "<replacement>"}]}
        packet["dependencies"].append({"id": "ccfa-writing-guidance", "path": guidance["path"],
                                        "sha256": guidance["sha256"], "used_by": packet["targets"]})
        for identity, name in [(brief_identity, "ccfa-writing-brief"), (source_map, "ccfa-writing-source-map")]:
            if identity:
                packet["dependencies"].append({"id": name, **identity, "used_by": packet["targets"]})
        for item in [packet["manuscript"], *packet["dependencies"]]:
            if hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest() != item["sha256"]:
                raise ValueError("Input changed while preparing context; read the current version: " + item["path"])
        if args.output:
            forbidden = [packet["manuscript"]["path"], *(s["path"] for s in packet["dependencies"])]
            _write_packet(packet, args.output, forbidden)
            return {"packet": str(Path(args.output).resolve()), "manuscript_sha256": packet["manuscript"]["sha256"],
                    "targets": packet["targets"], "mode": args.mode}
        return packet
    packet = read_json(args.packet)
    if args.command == "apply":
        return apply_patch(packet, read_json(args.patch))
    if args.command == "impact":
        return assess_impact(packet)
    return review_cache(args.action, packet, args.cache, args.model,
                        options=read_json(args.options) if args.options else None,
                        result_path=args.result,
                        coverage=read_json(args.coverage) if args.coverage else None,
                        call_stopped=args.call_stopped,
                        forbidden=[args.packet, *([args.options] if args.options else []),
                                   *([args.coverage] if args.coverage else [])])


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    args = parser().parse_args(argv)
    try:
        result = run(args)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
