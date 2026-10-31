"""Shared, standard-library release paths and resource selection."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat

REQUIRED = {"ccf-humanization", "ccf-common"}
MANIFEST = "release-manifest.json"
RECEIPT = ".ccfa-release-receipt.json"
PAPERS = "ccf-paper-writer/references/exemplars/papers/"
RESOURCE_RULES = {
    "ccf-paper-reviewer": ["ccf-paper-writer/references", "ccf-paper-writer/scripts"],
    "ccf-experiment-designer": ["ccf-paper-writer/references"],
    "ccf-project-scaffolder": ["ccf-paper-writer/references", "ccf-latex-templates"],
    "ccf-submission-checker": ["ccf-paper-writer/references", "ccf-latex-templates"],
    "ccf-rebuttal-writer": ["ccf-paper-writer/references"],
    "ccf-paper-writer": ["ccf-latex-templates", "ccf-paper-to-exemplar/scripts"],
    "ccf-paper-to-exemplar": ["ccf-paper-writer/references"],
    "ccf-paper-writer/scripts": ["ccf-paper-writer/references", "ccf-paper-to-exemplar/scripts"],
    "ccf-visual-composer": ["assets/visual-showcase"],
}


def is_paper_pdf(name):
    return name.startswith((PAPERS, "ccf-paper-writer/paper_ref/")) and name.lower().endswith(".pdf")


def relative_path(value):
    if not isinstance(value, str) or not value or "\\" in value or re.search(r'[<>:"|?*\x00-\x1f]', value):
        raise ValueError("Release paths must be portable relative POSIX paths")
    parts = value.split("/")
    if any(part in ("", ".", "..") or part.endswith((" ", ".")) for part in parts):
        raise ValueError("Unsafe release path: " + value)
    if any(re.fullmatch(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?", part) for part in parts):
        raise ValueError("Reserved device path: " + value)
    if PurePosixPath(value).is_absolute():
        raise ValueError("Absolute release paths are forbidden")
    return value


def public_path(value):
    relative_path(value)
    parts = value.split("/")
    return not any(p in {".git", ".secrets", "ccfa-workfiles", "output", "__pycache__"} for p in parts) and not (
        value.endswith(".pyc") or parts[-1] == ".env" or parts[-1].startswith(".env.")
        or value.endswith("/.ccfa/preferences.json") or value == ".ccfa/preferences.json")


def no_links(path):
    path = Path(path).absolute()
    for candidate in (path, *path.parents):
        if candidate.exists() or candidate.is_symlink():
            info = candidate.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                raise ValueError("Symlinks and reparse points are not release inputs or targets: " + str(candidate))
    return path


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def read_json(path):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError("Duplicate JSON key: " + key)
            value[key] = item
        return value
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique)


def load_release(source):
    source = no_links(Path(source).expanduser()).resolve()
    if not source.is_dir():
        raise ValueError("--source must be an extracted release directory")
    for path in source.rglob("*"):
        no_links(path)
    manifest = read_json(source / MANIFEST)
    if not isinstance(manifest, dict) or type(manifest.get("schema_version")) is not int or manifest["schema_version"] != 1:
        raise ValueError("Unsupported release manifest")
    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Release version must use major.minor.patch")
    if manifest.get("release_id") != "ccfa-skills-" + version or manifest.get("profile") not in {"lean", "papers"}:
        raise ValueError("Invalid release identity or profile")
    skills = manifest.get("skills")
    if not isinstance(skills, list) or any(not isinstance(s, str) or not re.fullmatch(r"ccf-[a-z0-9-]+", s) for s in skills):
        raise ValueError("Invalid release skill name")
    if len(set(skills)) != len(skills) or not REQUIRED.issubset(skills):
        raise ValueError("Release skill inventory lacks required preflights")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("Release manifest has no files")
    found = {}
    for entry in files:
        if not isinstance(entry, dict) or set(entry) != {"path", "sha256", "bytes"}:
            raise ValueError("Invalid release file entry")
        rel = relative_path(entry["path"])
        if not public_path(rel) or rel == MANIFEST or rel.casefold() in found:
            raise ValueError("Private or duplicate release path: " + rel)
        if not isinstance(entry["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            raise ValueError("Invalid file hash: " + rel)
        if type(entry["bytes"]) is not int or entry["bytes"] < 0:
            raise ValueError("Invalid file size: " + rel)
        path = no_links(source / rel)
        if not path.is_file() or path.stat().st_size != entry["bytes"] or digest(path) != entry["sha256"]:
            raise ValueError("Release content does not match its manifest: " + rel)
        if manifest["profile"] == "lean" and is_paper_pdf(rel):
            raise ValueError("A lean profile cannot contain complete writing PDFs")
        found[rel.casefold()] = entry
    if manifest["profile"] == "lean":
        if any((skill + "/SKILL.md").casefold() not in found for skill in skills):
            raise ValueError("Release is missing a listed SKILL.md")
    return source, manifest


def select_files(manifest, requested=None):
    skills = set(manifest["skills"] if not requested else requested) | REQUIRED
    if not skills.issubset(manifest["skills"]):
        raise ValueError("Unknown selected skill: " + ", ".join(sorted(skills-set(manifest["skills"]))))
    prefixes = set(skills)
    while True:
        expanded = prefixes | {item for key in prefixes for item in RESOURCE_RULES.get(key, [])}
        if expanded == prefixes:
            break
        prefixes = expanded
    selected = [e for e in manifest["files"] if any(e["path"] == p or e["path"].startswith(p + "/") for p in prefixes)]
    for prefix in prefixes:
        if not any(e["path"] == prefix or e["path"].startswith(prefix+"/") for e in selected):
            raise ValueError("Release lacks a required sibling resource: " + prefix)
    return sorted(skills), selected
