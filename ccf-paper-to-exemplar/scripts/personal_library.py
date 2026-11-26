"""Register reusable writing cards outside installed skills and query metadata.

Registration references existing cards and original sources; it copies neither.
Queries read the small registry and file stats, never paper or card contents.
A changed size or modification time invalidates a registered analysis until it
is checked and registered again. This is a reuse cache, not a content audit.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import tempfile


class LibraryError(ValueError):
    """An exemplar cannot be registered or the library cannot be read."""


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise LibraryError(label + " must be nonempty text")
    value.encode("utf-8", errors="strict")
    return value.strip()


def _labels(values, label):
    if not isinstance(values, (list, tuple)) or not values:
        raise LibraryError(label + " must contain at least one value")
    return list(dict.fromkeys(_text(v, label) for v in values))


def library_path(*, project=None, scope="project"):
    if scope == "project":
        if project is None:
            raise LibraryError("Project registration requires --project; use --scope user for an explicit personal library")
        base = Path(project).expanduser().resolve()
        path = base / ".ccfa/exemplars/library.json"
    elif scope == "user":
        home = os.environ.get("CODEX_HOME")
        base = (Path(home).expanduser() if home else Path.home() / ".codex").resolve()
        path = base / "ccfa/exemplars/library.json"
    else:
        raise LibraryError("scope must be project or user")
    if not path.resolve().is_relative_to(base):
        raise LibraryError("The exemplar registry escapes its selected root")
    return path


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise LibraryError("Duplicate registry key: " + key)
        result[key] = value
    return result


def _read(path):
    if not path.exists():
        return {"version": 1, "entries": {}}
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=_unique)
    except (OSError, UnicodeError, ValueError) as exc:
        raise LibraryError("Cannot read exemplar registry: " + str(path)) from exc
    if (not isinstance(value, dict) or not {"version", "entries"}.issubset(value)
            or set(value) - {"version", "entries", "defaults"} or value["version"] != 1
            or not isinstance(value["entries"], dict)):
        raise LibraryError("Unsupported exemplar registry: " + str(path))
    if "defaults" in value and (not isinstance(value["defaults"], list)
                                or any(not isinstance(key, str) or not key.strip() for key in value["defaults"])
                                or len(value["defaults"]) != len(set(value["defaults"]))):
        raise LibraryError("Invalid default exemplar selection: " + str(path))
    for key, entry in value["entries"].items():
        try:
            if not isinstance(entry, dict) or entry["id"] != key:
                raise ValueError("entry identity mismatch")
            _text(entry["title"], "title")
            _labels(entry["functions"], "functions")
            if entry["coverage"] not in {"passage", "section", "paper"}:
                raise ValueError("invalid coverage")
            _text(entry["source"]["id"], "source ID")
            _text(entry["source"]["version"], "source version")
            _labels(entry["source"]["locations"], "source locations")
            for item in (entry["card"], entry["source"]):
                _text(item["path"], "local path")
                stamp = item["stamp"]
                if set(stamp) != {"bytes", "mtime_ns"} or any(type(n) is not int or n < 0 for n in stamp.values()):
                    raise ValueError("invalid source stamp")
        except (KeyError, TypeError, ValueError) as exc:
            raise LibraryError("Invalid exemplar entry: " + str(key)) from exc
    return value


def _stamp(path):
    try:
        if not path.is_file():
            raise OSError("not a file")
        stat = path.stat()
        return {"bytes": stat.st_size, "mtime_ns": stat.st_mtime_ns}
    except OSError as exc:
        raise LibraryError("Cannot inspect local exemplar file: " + str(path)) from exc


def _publish(path, value):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent,
                                         prefix=".library-", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


@contextmanager
def _locked(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(".library.lock")
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise LibraryError("Another exemplar update holds the library lock; retry after it finishes") from exc
    os.close(descriptor)
    try:
        yield
    finally:
        lock.unlink(missing_ok=True)


def register(*, key, card, source, source_id, source_version, locations, functions,
             project=None, scope="project", coverage="passage", title=None, replace_source=False):
    """Register a completed, source-anchored card; repeated input is a no-op."""
    path = library_path(project=project, scope=scope)
    key = _text(key, "entry ID").casefold()
    if not re.fullmatch(r"[\w][\w.-]{0,127}", key, flags=re.UNICODE):
        raise LibraryError("Entry ID must contain letters, numbers, dots, underscores or hyphens")
    if coverage not in {"passage", "section", "paper"}:
        raise LibraryError("coverage must be passage, section or paper")
    card_path, source_path = Path(card).expanduser().resolve(), Path(source).expanduser().resolve()
    if card_path == source_path:
        raise LibraryError("The original source must be distinct from the derived card")
    before = _stamp(card_path)
    try:
        body = card_path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise LibraryError("Card must be a readable UTF-8 Markdown file") from exc
    if re.search(r"\[(?:ANALYZE|MANUAL|TODO|TBD)\]", body, flags=re.IGNORECASE):
        raise LibraryError("Complete the card analysis before registration")
    required = ["Reusable Techniques", "Do-Not-Copy Boundary"]
    if coverage == "paper":
        required += ["Story Pattern", "Abstract Moves", "Introduction Moves", "Method Moves", "Evidence Moves", "Citation Patterns"]
    for heading in required:
        section = re.search(r"^##[ \t]+" + re.escape(heading) + r"[ \t]*\r?$\n(.*?)(?=^##[ \t]+|\Z)", body,
                            flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)
        if section is None or not section.group(1).strip():
            raise LibraryError("A completed card needs the " + heading + " section")
    observation = re.search(r"^##[ \t]+(?:Story Pattern|Source Observations|\w+ Moves|Citation Patterns)[ \t]*\r?$\n(.*?)(?=^##[ \t]+|\Z)", body,
                            flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)
    if observation is None or not observation.group(1).strip():
        raise LibraryError("Include a source observation for the analyzed writing function")
    card_stamp = _stamp(card_path)
    if card_stamp != before:
        raise LibraryError("Card changed during registration; read the current analysis again")
    heading = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    entry = {"id": key, "title": _text(title or (heading.group(1) if heading else key), "title"),
             "functions": _labels(functions, "functions"), "coverage": coverage,
             "card": {"path": str(card_path), "stamp": card_stamp},
             "source": {"id": _text(source_id, "source ID"), "version": _text(source_version, "source version"),
                        "path": str(source_path), "locations": _labels(locations, "source locations"),
                        "stamp": _stamp(source_path)}}
    with _locked(path):
        library = _read(path)
        previous = library["entries"].get(key)
        if previous and previous["source"]["id"] != entry["source"]["id"] and not replace_source:
            raise LibraryError("This ID belongs to another paper; use a new ID or explicitly --replace-source")
        if previous == entry:
            action = "unchanged"
        else:
            library["entries"][key] = entry
            _publish(path, library)
            action = "updated" if previous else "registered"
    return {"action": action, "scope": scope, "library": str(path), "entry": entry}


def _libraries(project=None):
    entries, defaults, defaults_scope = {}, [], "none"
    for scope in (["user", "project"] if project is not None else ["user"]):
        path = library_path(project=project, scope=scope)
        library = _read(path)
        for key, entry in library["entries"].items():
            entries[key] = {**entry, "scope": scope, "library": str(path)}
        if "defaults" in library:
            defaults, defaults_scope = library["defaults"], scope
    return entries, defaults, defaults_scope


def _unavailable(entry):
    reasons = []
    for kind in ("card", "source"):
        item = entry[kind]
        try:
            if _stamp(Path(item["path"])) != item["stamp"]:
                reasons.append(kind + " changed")
        except LibraryError:
            reasons.append(kind + " missing")
    return reasons


def set_defaults(*, keys=None, project=None, scope="project", inherit=False):
    """Save only an explicitly selected default list, or restore inheritance."""
    path = library_path(project=project, scope=scope)
    if inherit:
        if scope != "project" or keys is not None:
            raise LibraryError("Default inheritance applies to a project without an explicit ID selection")
        if not path.exists():
            return {"action": "unchanged", "scope": scope, "library": str(path), "defaults": None}
        selected = None
    else:
        if not isinstance(keys, (list, tuple)):
            raise LibraryError("Supply explicit exemplar IDs, or an empty list to clear defaults")
        selected = list(dict.fromkeys(_text(key, "default ID").casefold() for key in keys))
        # User defaults cannot depend on one project's private entries.
        entries, _, _ = _libraries(project if scope == "project" else None)
        for key in selected:
            if key not in entries:
                raise LibraryError("Register the exemplar before selecting it as a default: " + key)
            reasons = _unavailable(entries[key])
            if reasons:
                raise LibraryError("Recheck and register the changed default exemplar first: " + key)
    with _locked(path):
        library = _read(path)
        if inherit:
            changed = "defaults" in library
            library.pop("defaults", None)
        else:
            changed = library.get("defaults") != selected
            library["defaults"] = selected
        if changed:
            _publish(path, library)
    return {"action": "updated" if changed else "unchanged", "scope": scope,
            "library": str(path), "defaults": selected}


def query(*, project=None, text="", functions=(), limit=6):
    """Return matching, current metadata; project IDs shadow personal IDs."""
    if type(limit) is not int or limit < 1:
        raise LibraryError("limit must be a positive integer")
    requested = {_text(v, "function").casefold() for v in functions}
    terms = re.findall(r"[^\W_]+", text.casefold(), flags=re.UNICODE)
    entries, defaults, defaults_scope = _libraries(project)
    candidates = []
    for entry in entries.values():
        tags = {v.casefold() for v in entry["functions"]}
        if requested and not requested.intersection(tags):
            continue
        haystack = " ".join([entry["id"], entry["title"], entry["source"]["id"], *entry["functions"]]).casefold()
        score = sum(term in haystack for term in terms)
        if terms and not score:
            continue
        candidates.append((score, {**entry, "is_default": entry["id"] in defaults}))
    candidates.sort(key=lambda pair: (not pair[1]["is_default"], -pair[0], pair[1]["id"]))
    matches, unavailable = [], []
    for _, entry in candidates:
        reasons = _unavailable(entry)
        if reasons:
            # Keep registered locations for recovery, without treating the old
            # analysis or its recorded source version as current coverage.
            unavailable.append({"id": entry["id"], "scope": entry["scope"], "library": entry["library"],
                                "reason": ", ".join(reasons), "analysis_current": False,
                                "card": {"path": entry["card"]["path"]},
                                "source": {key: entry["source"][key] for key in ("path", "id", "version", "locations")}})
        else:
            matches.append(entry)
    return {"matches": matches[:limit], "total_matches": len(matches),
            "unavailable": unavailable[:limit], "total_unavailable": len(unavailable),
            "limit": limit, "defaults_scope": defaults_scope}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("register", help="Register a completed card without copying its original source")
    add.add_argument("--project", type=Path)
    add.add_argument("--scope", choices=("project", "user"), default="project")
    add.add_argument("--id", dest="key", required=True)
    add.add_argument("--card", type=Path, required=True)
    add.add_argument("--source", type=Path, required=True)
    add.add_argument("--source-id", required=True)
    add.add_argument("--source-version", required=True)
    add.add_argument("--location", dest="locations", action="append", required=True)
    add.add_argument("--function", dest="functions", action="append", required=True)
    add.add_argument("--coverage", choices=("passage", "section", "paper"), default="passage")
    add.add_argument("--title")
    add.add_argument("--replace-source", action="store_true")
    find = commands.add_parser("query", help="Find current card/source metadata without reading their contents")
    find.add_argument("--project", type=Path)
    find.add_argument("--query", dest="text", default="")
    find.add_argument("--function", dest="functions", action="append", default=[])
    find.add_argument("--limit", type=int, default=6)
    prefer = commands.add_parser("set-default", help="Explicitly choose registered defaults without editing installed skills")
    prefer.add_argument("--project", type=Path)
    prefer.add_argument("--scope", choices=("project", "user"), default="project")
    selection = prefer.add_mutually_exclusive_group(required=True)
    selection.add_argument("--id", dest="keys", action="append")
    selection.add_argument("--clear", action="store_true", help="Select no defaults in this scope")
    selection.add_argument("--inherit", action="store_true", help="Restore inheritance of personal defaults for this project")
    args = vars(parser.parse_args())
    command = args.pop("command")
    try:
        if command == "set-default":
            if args.pop("clear"):
                args["keys"] = []
            result = set_defaults(**args)
        else:
            result = register(**args) if command == "register" else query(**args)
    except (LibraryError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    for stream in (__import__("sys").stdout, __import__("sys").stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    raise SystemExit(main())
