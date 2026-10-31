"""Read-only, source-anchored context for a scoped manuscript revision.

No model, network, or project-state writes are performed. Relative library paths
resolve against the current directory; a CLI reading a source-list file should
resolve that list's relative paths before calling this module. The budget is
the length of ``json.dumps(packet['context'], ensure_ascii=False)``. Targets and
the supplied scientific brief are never shortened to satisfy it.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re


NEIGHBOR_CHARS = 1200
SOURCE_CHARS = 2400


class WritingContextError(ValueError):
    """The requested context cannot be prepared without losing its contract."""


def _inspect_manuscript(path):
    # A lazy import keeps impact checks of missing files usable independently.
    from manuscript_patch import inspect_manuscript
    return inspect_manuscript(path)


def _text(value, name, *, empty=False):
    if not isinstance(value, str) or (not empty and not value.strip()):
        raise WritingContextError(f"{name} must be {'text' if empty else 'nonempty text'}")
    return value


def _ids(values, name, *, allow_empty=False):
    if not isinstance(values, (list, tuple)) or isinstance(values, str):
        raise WritingContextError(f"{name} must list explicit IDs")
    result = [_text(value, name) for value in values]
    if len(result) != len(set(result)) or (not result and not allow_empty):
        raise WritingContextError(f"{name} must contain distinct IDs")
    return result


def _path(value):
    if not isinstance(value, (str, Path)) or not str(value).strip():
        raise WritingContextError("A source path must be a local file path")
    if isinstance(value, str) and re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", value):
        raise WritingContextError("Source paths must be local; no network retrieval is performed")
    return Path(value).expanduser().resolve()


def _snapshot(path):
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig", errors="strict")
    except (OSError, UnicodeError) as exc:
        raise WritingContextError(f"Cannot read UTF-8 file {path}: {type(exc).__name__}") from exc
    return text, hashlib.sha256(raw).hexdigest()


def _brief(value):
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise WritingContextError("brief must be a scientific task object")
    allowed = {"message", "throughline", "terminology", "protected_literals"}
    unknown = set(value) - allowed
    if unknown:
        raise WritingContextError(f"Unknown scientific brief fields: {', '.join(sorted(unknown))}")
    result = copy.deepcopy(value)
    for key in ("message", "throughline"):
        if key in result:
            _text(result[key], f"brief.{key}")
    if "terminology" in result:
        if not isinstance(result["terminology"], dict):
            raise WritingContextError("brief.terminology must map terms to their intended meanings")
        for key, meaning in result["terminology"].items():
            _text(key, "terminology key")
            _text(meaning, f"terminology[{key}]")
    if "protected_literals" in result:
        result["protected_literals"] = _ids(result["protected_literals"], "protected_literals", allow_empty=True)
    return result


def _line_number(text, offset):
    return text.count("\n", 0, offset) + 1


def _location(text, start, end):
    return {"start": start, "end": end,
            "start_line": _line_number(text, start),
            "end_line": _line_number(text, max(start, end - 1))}


def _section(item, text):
    if not isinstance(item, dict):
        raise WritingContextError("Manuscript sections must be objects")
    key = _text(item.get("id"), "section ID")
    heading = _text(item.get("heading", ""), "section heading", empty=True)
    start, end = item.get("start"), item.get("end")
    if (isinstance(start, bool) or isinstance(end, bool) or not isinstance(start, int)
            or not isinstance(end, int) or not 0 <= start <= end <= len(text)):
        raise WritingContextError(f"Invalid manuscript character span for {key}")
    actual = text[start:end]
    if item.get("text") != actual:
        raise WritingContextError(f"Section {key} text does not match its inspected source span")
    return {"id": key, "heading": heading, **_location(text, start, end),
            "sha256": hashlib.sha256(actual.encode("utf-8")).hexdigest(), "text": actual}


def _inspected(path):
    try:
        inspected = _inspect_manuscript(path)
    except (OSError, UnicodeError, ValueError) as exc:
        raise WritingContextError(f"Cannot inspect manuscript {path}: {exc}") from exc
    if not isinstance(inspected, dict) or not isinstance(inspected.get("sections"), list):
        raise WritingContextError("Manuscript inspection did not return a section inventory")
    text, digest = _snapshot(path)
    if inspected.get("sha256") != digest:
        raise WritingContextError("Manuscript changed during inspection; read the current source again")
    sections = [_section(item, text) for item in inspected["sections"]]
    if len({s["id"] for s in sections}) != len(sections):
        raise WritingContextError("Manuscript inspection returned duplicate section IDs")
    if any(b["start"] < a["end"] for a, b in zip(sections, sections[1:])):
        raise WritingContextError("Manuscript inspection returned overlapping or unordered sections")
    return text, digest, sections


def _fragment(identity, text, start, end, *, limit, tail=False, **extra):
    item = {**identity, **extra, "requested": _location(text, start, end)}
    state = {"item": item, "source_text": text, "start": start, "end": end, "tail": tail}
    _resize(state, min(limit, end - start), "excerpt_limit")
    return state


def _resize(state, length, reason):
    start, end = state["start"], state["end"]
    length = max(0, min(length, end - start))
    used_start, used_end = ((end - length, end) if state["tail"] else (start, start + length))
    text, item = state["source_text"], state["item"]
    item.update(_location(text, used_start, used_end), text=text[used_start:used_end], complete=(length == end-start))
    omitted = []
    for left, right in ((start, used_start), (used_end, end)):
        if left < right:
            omitted.append({**_location(text, left, right), "reason": reason})
    item["omitted"] = omitted


def _source(entry, snapshots):
    if not isinstance(entry, dict):
        raise WritingContextError("Each source must be an object")
    required = {"id", "path", "kind", "used_by"}
    if not required.issubset(entry) or set(entry) - required - {"start_line", "end_line"}:
        raise WritingContextError("Sources require id, path, kind and used_by; only line bounds are optional")
    identity = {"id": _text(entry["id"], "source ID"), "kind": _text(entry["kind"], "source kind"),
                "used_by": _ids(entry["used_by"], "source.used_by")}
    path = _path(entry["path"])
    if path not in snapshots:
        snapshots[path] = _snapshot(path)
    text, digest = snapshots[path]
    lines = text.splitlines(keepends=True)
    if not lines:
        raise WritingContextError(f"Source {identity['id']} contains no text lines")
    start_line, end_line = entry.get("start_line", 1), entry.get("end_line", len(lines))
    if (isinstance(start_line, bool) or isinstance(end_line, bool) or not isinstance(start_line, int)
            or not isinstance(end_line, int) or not 1 <= start_line <= end_line <= len(lines)):
        raise WritingContextError(f"Source {identity['id']} line bounds must lie inside its actual file")
    start = sum(len(line) for line in lines[:start_line-1])
    end = start + sum(len(line) for line in lines[start_line-1:end_line])
    identity.update(path=str(path), sha256=digest)
    return identity, text, start, end


def _json_size(value):
    return len(json.dumps(value, ensure_ascii=False, allow_nan=False))


def prepare_context(manuscript, targets, brief=None, sources=None, max_chars=None):
    """Return actual target text, adjacent excerpts and explicitly mapped sources.

    Default excerpts retain up to 1,200 characters per neighbor (the preceding
    section's end or following section's start) and 2,400 per source. Every
    omission has exact character and line locations. A supplied budget may trim
    these optional excerpts further, never targets or the scientific brief.
    """
    path = _path(manuscript)
    text, digest, sections = _inspected(path)
    target_ids = _ids(targets, "targets")
    indexed = {item["id"]: item for item in sections}
    missing = set(target_ids) - set(indexed)
    if missing:
        raise WritingContextError(f"Unknown manuscript target IDs: {', '.join(sorted(missing))}")
    if max_chars is not None and (isinstance(max_chars, bool) or not isinstance(max_chars, int) or max_chars < 1):
        raise WritingContextError("max_chars must be a positive integer")
    context = _brief(brief)
    context.update(targets=[copy.deepcopy(indexed[key]) for key in target_ids], neighbors=[], sources=[])
    optional = []
    neighbors = {}
    for i, section in enumerate(sections):
        if section["id"] not in target_ids:
            continue
        for j, side in ((i-1, "previous"), (i+1, "next")):
            if 0 <= j < len(sections) and sections[j]["id"] not in target_ids:
                key = sections[j]["id"]
                neighbors.setdefault(key, []).append({"target": section["id"], "side": side})
    for key, adjacency in neighbors.items():
        other = indexed[key]
        length = other["end"] - other["start"]
        sides = {item["side"] for item in adjacency}
        if len(sides) == 2 and length > NEIGHBOR_CHARS:
            # A shared middle section can supply two different transitions.
            # Keep both adjacent edges without repeating overlapping text.
            head_length = min(NEIGHBOR_CHARS, (length + 1)//2)
            edges = [("head", head_length, False),
                     ("tail", min(NEIGHBOR_CHARS, length-head_length), True)]
        else:
            edges = [("full" if length <= NEIGHBOR_CHARS else
                      ("tail" if "previous" in sides else "head"), NEIGHBOR_CHARS,
                      "previous" in sides)]
        for edge, limit, tail in edges:
            relevant = [item for item in adjacency if len(edges) == 1 or
                        item["side"] == ("previous" if tail else "next")]
            state = _fragment({"id": key, "heading": other["heading"], "path": str(path), "sha256": digest},
                              text, other["start"], other["end"], limit=limit, tail=tail,
                              edge=edge, adjacent_to=relevant)
            optional.append(state)
            context["neighbors"].append(state["item"])
    if sources is None:
        sources = []
    if not isinstance(sources, (list, tuple)):
        raise WritingContextError("sources must be a list of explicitly mapped source objects")
    dependencies, source_ids, source_snapshots = [], set(), {}
    source_states = []
    for entry in sources:
        identity, source_text, start, end = _source(entry, source_snapshots)
        if Path(identity["path"]) == path:
            raise WritingContextError("Use manuscript targets and neighbors, not the manuscript as its own source dependency")
        if identity["id"] in source_ids:
            raise WritingContextError(f"Duplicate source ID: {identity['id']}")
        source_ids.add(identity["id"])
        dependencies.append({**identity, "requested": _location(source_text, start, end)})
        users = [key for key in identity["used_by"] if key in target_ids]
        if users:
            state = _fragment({**identity, "used_by": users}, source_text, start, end, limit=SOURCE_CHARS)
            source_states.append(state)
            context["sources"].append(state["item"])
    # Optional source text is reduced before immediate manuscript neighbors.
    shrink_order = sorted(source_states, key=lambda state: len(state["item"]["text"]), reverse=True)
    shrink_order += sorted(optional, key=lambda state: len(state["item"]["text"]), reverse=True)
    if max_chars is not None:
        for state in shrink_order:
            if _json_size(context) <= max_chars:
                break
            original_length = len(state["item"]["text"])
            _resize(state, 0, "context_budget")
            if _json_size(context) > max_chars:
                continue
            low, high = 0, original_length
            while low < high:
                candidate = (low + high + 1)//2
                _resize(state, candidate, "context_budget")
                if _json_size(context) <= max_chars:
                    low = candidate
                else:
                    high = candidate - 1
            _resize(state, low, "context_budget")
        if _json_size(context) > max_chars:
            raise WritingContextError("max_chars cannot hold complete targets, the scientific brief and explicit read-back locations; increase it or narrow the targets")
    return {"schema_version": 1, "manuscript": {"path": str(path), "sha256": digest},
            "targets": target_ids, "sections": [{key: value for key, value in item.items() if key != "text"} for item in sections],
            "context": context, "dependencies": dependencies,
            "budget": {"measure": "json_context_characters", "max_chars": max_chars, "used_chars": _json_size(context)}}


def _current(identity, snapshots):
    path_value = identity.get("path")
    expected = identity.get("sha256")
    if not isinstance(path_value, str) or not path_value or not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
        return {"status": "unknown", "current_sha256": None, "reason": "Missing or invalid stored source identity"}
    try:
        path = _path(path_value)
    except (WritingContextError, OSError, RuntimeError) as exc:
        return {"status": "unknown", "current_sha256": None, "reason": str(exc)}
    if path not in snapshots:
        try:
            raw = path.read_bytes()
            raw.decode("utf-8-sig", errors="strict")
            snapshots[path] = {"current_sha256": hashlib.sha256(raw).hexdigest()}
        except FileNotFoundError:
            snapshots[path] = {"status": "missing", "current_sha256": None}
        except (OSError, UnicodeError) as exc:
            snapshots[path] = {"status": "unreadable", "current_sha256": None, "reason": type(exc).__name__}
    current = snapshots[path]
    if "status" in current:
        return dict(current)
    digest = current["current_sha256"]
    return {"status": "unchanged" if digest == expected else "changed", "current_sha256": digest}


def assess_impact(packet):
    """Report changed identities and their explicit dependents; never edit files."""
    if not isinstance(packet, dict) or packet.get("schema_version") != 1 or isinstance(packet.get("schema_version"), bool):
        raise WritingContextError("Impact assessment requires a schema_version=1 context packet")
    manuscript = packet.get("manuscript")
    sections, dependencies = packet.get("sections"), packet.get("dependencies")
    if not isinstance(manuscript, dict) or not isinstance(sections, list) or not isinstance(dependencies, list):
        raise WritingContextError("Context packet lacks manuscript, sections or dependencies")
    if any(not isinstance(item, dict) or not isinstance(item.get("id"), str) for item in sections):
        raise WritingContextError("Context packet has an invalid section inventory")
    known_sections = {item["id"] for item in sections}
    snapshots = {}
    current_manuscript = _current(manuscript, snapshots)
    changed_sections, removed_sections, added_sections = [], [], []
    manuscript_parse_error = None
    if current_manuscript["status"] == "changed":
        try:
            _, _, latest = _inspected(_path(manuscript["path"]))
            old = {item["id"]: item.get("sha256") for item in sections}
            new = {item["id"]: item["sha256"] for item in latest}
            changed_sections = [key for key in old.keys() & new.keys() if old[key] != new[key]]
            removed_sections = sorted(old.keys()-new.keys())
            added_sections = sorted(new.keys()-old.keys())
        except (WritingContextError, ImportError) as exc:
            manuscript_parse_error = str(exc)
    changed_sources, affected, unknown_dependencies, unknown_scope = [], set(), [], []
    for dependency in dependencies:
        if not isinstance(dependency, dict) or not isinstance(dependency.get("id"), str):
            raise WritingContextError("Context packet has an invalid dependency record")
        users = _ids(dependency.get("used_by"), "dependency.used_by", allow_empty=True)
        current = _current(dependency, snapshots)
        if current["status"] != "unchanged":
            changed_sources.append({"id": dependency["id"], "path": dependency.get("path"), "kind": dependency.get("kind"),
                                    "expected_sha256": dependency.get("sha256"), "used_by": users, **current})
            affected.update(users)
            if not users:
                unknown_scope.append(dependency["id"])
            if current["status"] in ("unknown", "missing", "unreadable") or not users:
                unknown_dependencies.append(dependency["id"])
    affected.update(changed_sections)
    affected.update(removed_sections)
    figure = re.compile(r"^(?:fig(?:ure)?(?:[:_\s./-]|\d)|f\d)", re.IGNORECASE)
    table = re.compile(r"^(?:tab(?:le)?(?:[:_\s./-]|\d)|t\d)", re.IGNORECASE)
    affected_sections = sorted(affected & known_sections)
    affected_figures = sorted(key for key in affected-known_sections if figure.match(key))
    affected_tables = sorted(key for key in affected-known_sections if table.match(key))
    unmapped = sorted(affected-known_sections-set(affected_figures)-set(affected_tables))
    status = current_manuscript["status"]
    result = {"schema_version": 1, "manuscript_changed": (status=="changed") if status in ("changed", "unchanged") else None,
              "manuscript": {**manuscript, **current_manuscript}, "changed_sources": changed_sources,
              "changed_sections": sorted(changed_sections), "removed_sections": removed_sections, "added_sections": added_sections,
              "affected_sections": affected_sections, "affected_figures": affected_figures,
              "affected_tables": affected_tables, "unmapped_dependents": unmapped,
              "affected_targets": sorted(set(packet.get("targets",[])) & affected), "unknown_dependencies": unknown_dependencies,
              "scope_unknown": bool(unknown_scope or unmapped or manuscript_parse_error or status not in ("changed", "unchanged")),
              "scope_unknown_dependencies": unknown_scope}
    if manuscript_parse_error:
        result["manuscript_parse_error"] = manuscript_parse_error
    return result
