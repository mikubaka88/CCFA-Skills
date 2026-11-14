#!/usr/bin/env python3
"""Install a CCFA release, retiring unchanged managed files within its selection."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

from release_support import RECEIPT, digest, is_paper_pdf, load_release, no_links, read_json, relative_path, resource_prefixes, select_files


def _hash(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _receipt(target):
    path = no_links(target / RECEIPT)
    if not path.exists():
        return {"schema_version": 1, "owner": "ccfa-release-installer", "files": {}, "skills": {}}
    value = read_json(path)
    if not isinstance(value, dict) or value.get("owner") != "ccfa-release-installer" or value.get("schema_version") != 1:
        raise ValueError("Existing receipt is not owned by this installer")
    if not isinstance(value.get("files"), dict) or not isinstance(value.get("skills"), dict):
        raise ValueError("Invalid installation receipt")
    for name, entry in value["files"].items():
        relative_path(name)
        if not isinstance(entry, dict) or not _hash(entry.get("sha256")):
            raise ValueError("Invalid managed-file receipt")
    pending = value.get("pending")
    if pending is not None:
        if not isinstance(pending, dict) or not _hash(pending.get("operation")) or not isinstance(pending.get("before"), dict):
            raise ValueError("Invalid pending installation receipt")
        for name, previous in pending["before"].items():
            relative_path(name)
            if previous is not None and not _hash(previous):
                raise ValueError("Invalid pending destination hash")
    return value


def _write_receipt(target, value):
    fd, name = tempfile.mkstemp(prefix=".ccfa-receipt-", suffix=".json", dir=target)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as out:
            json.dump(value, out, ensure_ascii=False, indent=2); out.write("\n")
            out.flush(); os.fsync(out.fileno())
        os.replace(temporary, no_links(target / RECEIPT))
    finally:
        temporary.unlink(missing_ok=True)


def _operation(manifest, skills, entries, retired=()):
    # Identify content and selection, independent of the extracted source location.
    value = {"release_id": manifest["release_id"], "profile": manifest["profile"], "skills": skills,
             "files": sorted((entry["path"], entry["sha256"]) for _, entry in entries)}
    if retired:
        value["retired"] = sorted(retired)
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def install(source, target, requested=None, papers=None, dry_run=False):
    source, manifest = load_release(source)
    target = no_links(Path(target).expanduser()).resolve()
    if source == target or source in target.parents or target in source.parents:
        raise ValueError("Source and skills target must be separate directory trees")
    if target.exists() and not target.is_dir():
        raise ValueError("--target must name a skills directory")
    old = _receipt(target)
    if manifest["profile"] == "papers":
        if papers or requested:
            raise ValueError("A papers-only source adds PDFs to the existing installation; do not select new skills")
        if old.get("version") != manifest["version"]:
            raise ValueError("Install the matching lean release before adding its papers")
        skills = []
        entries = [(source, e) for e in manifest["files"] if is_paper_pdf(e["path"])]
    else:
        skills, selected = select_files(manifest, requested)
        entries = [(source, e) for e in selected]
        if papers:
            paper_source, paper_manifest = load_release(papers)
            if paper_manifest["profile"] != "papers" or paper_manifest["release_id"] != manifest["release_id"] or paper_manifest["skills"] != manifest["skills"]:
                raise ValueError("The optional papers must match the lean release")
            if paper_source == target or paper_source in target.parents or target in paper_source.parents:
                raise ValueError("Papers and target must be separate directory trees")
            entries += [(paper_source, e) for e in paper_manifest["files"] if is_paper_pdf(e["path"])]
    # A lean manifest is the complete inventory for the selected resource paths.
    # PDFs installed from the optional papers pack are deliberately absent from it.
    prefixes = resource_prefixes(skills) if manifest["profile"] == "lean" else set()
    current_inventory = {entry["path"] for entry in manifest["files"]}
    retired = sorted(name for name in old["files"]
                     if name not in current_inventory and not is_paper_pdf(name)
                     and any(name == p or name.startswith(p + "/") for p in prefixes))
    operation = _operation(manifest, skills, entries, retired)
    pending = old.get("pending")
    affected = {e["path"] for _, e in entries} | set(retired)
    if pending is not None and (pending["operation"] != operation or set(pending["before"]) != affected):
        raise ValueError("An interrupted update is pending; retry its same release, skill selection, and papers first")
    changes = []
    observed = {}
    unchanged = 0
    for origin, entry in entries:
        path = no_links(target / entry["path"])
        if path.exists() and not path.is_file():
            raise ValueError("An installation file conflicts with a directory: "+entry["path"])
        current = digest(path) if path.exists() else None
        observed[entry["path"]] = current
        if pending is not None and current not in (pending["before"][entry["path"]], entry["sha256"]):
            raise ValueError("Preserving a change made after an interrupted update; reconcile before retrying: "+entry["path"])
        if current == entry["sha256"]:
            unchanged += 1
        elif pending is None and current is not None and old["files"].get(entry["path"], {}).get("sha256") != current:
            raise ValueError("Preserving a personal or unmanaged edit; reconcile before updating: "+entry["path"])
        else:
            changes.append((origin, entry, path, current))
    retiring = []
    for name in retired:
        path = no_links(target / name)
        if not path.resolve().is_relative_to(target):
            raise ValueError("Retired path escapes the skills target: " + name)
        if path.exists() and not path.is_file():
            raise ValueError("A retired managed file conflicts with a directory: " + name)
        current = digest(path) if path.exists() else None
        observed[name] = current
        expected = pending["before"][name] if pending is not None else old["files"][name]["sha256"]
        if current is not None and current != expected:
            raise ValueError("Preserving a personal edit to a retired file; reconcile before updating: " + name)
        retiring.append((name, path, current))
    result = {"version": manifest["version"], "profile": manifest["profile"], "skills": skills,
              "dry_run": dry_run, "new_files": sum(c[3] is None for c in changes),
              "updated_files": sum(c[3] is not None for c in changes), "unchanged_files": unchanged,
              "retired_files": sum(current is not None for _, _, current in retiring), "retired_paths": retired,
              "extra_user_files": "preserved", "preferences": "unchanged", "resuming": pending is not None}
    if dry_run:
        return result
    target.mkdir(parents=True, exist_ok=True)
    lock = no_links(target / ".ccfa-release-install.lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError("An installation is pending; confirm it stopped before removing its lock") from exc
    os.close(fd)
    staged = []
    try:
        if _receipt(target) != old:
            raise ValueError("Installation receipt changed; inspect and retry")
        for origin, entry, path, previous in changes:
            no_links(path)
            if (digest(path) if path.exists() else None) != previous:
                raise ValueError("Target changed during preparation: "+entry["path"])
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, name = tempfile.mkstemp(prefix=".ccfa-install-", suffix=".tmp", dir=path.parent)
            temporary = Path(name)
            staged.append((temporary, path))
            measured = hashlib.sha256()
            size = 0
            with os.fdopen(fd, "wb") as out, no_links(origin / entry["path"]).open("rb") as inp:
                for block in iter(lambda: inp.read(1024 * 1024), b""):
                    out.write(block); measured.update(block); size += len(block)
            if measured.hexdigest() != entry["sha256"] or size != entry["bytes"]:
                raise ValueError("Source changed during copy: "+entry["path"])
        # Recheck every destination before committing any replacement.
        for name, previous in observed.items():
            path = no_links(target / name)
            if (digest(path) if path.exists() else None) != previous:
                raise ValueError("Target changed during staging: "+name)
        journal = {**old, "pending": pending or {"operation": operation, "before": observed}}
        _write_receipt(target, journal)
        # A durable journal makes a partial replacement resumable. A retry accepts
        # only the original or expected new bytes, never intervening user edits.
        for temporary, path in staged:
            rel = path.relative_to(target).as_posix()
            if (digest(no_links(path)) if path.exists() else None) != observed[rel]:
                raise ValueError("Target changed during commit: "+rel)
            os.replace(temporary, path)
        for name, path, previous in retiring:
            if (digest(no_links(path)) if path.exists() else None) != previous:
                raise ValueError("Retired file changed during commit: " + name)
            if previous is not None:
                path.unlink()
        if _receipt(target) != journal:
            raise ValueError("Installation receipt changed during commit; inspect before retrying")
        receipt = {**old, "version": manifest["version"], "files": dict(old["files"]), "skills": dict(old["skills"])}
        receipt.pop("pending", None)
        for name in retired:
            receipt["files"].pop(name, None)
        for _, entry in entries:
            receipt["files"][entry["path"]] = {"sha256": entry["sha256"], "version": manifest["version"]}
        for skill in skills:
            receipt["skills"][skill] = manifest["version"]
        _write_receipt(target, receipt)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)
        lock.unlink()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Extracted lean or papers directory")
    parser.add_argument("--target", type=Path, required=True, help="Actual client skills root; no automatic discovery")
    parser.add_argument("--skill", action="append", help="Repeat exact skill names; omit for all skills")
    parser.add_argument("--papers", type=Path, help="Optional matching extracted offline-PDF pack")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.source, args.target, args.skill, args.papers, args.dry_run), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"): stream.reconfigure(encoding="utf-8", errors="strict")
    main()
