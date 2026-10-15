#!/usr/bin/env python3
"""Scan repository text files for local path and identity leaks."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", ".venv", "venv"}
SKIP_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".exe",
    ".dll",
    ".bin",
}

WIN_HOME_DIR = "Us" + "ers"
LINUX_HOME_DIR = "ho" + "me"
SKILL_CREATOR = "skill-" + "creator"


def default_patterns():
    return [
        ("windows-user-home", re.compile(rf"[A-Za-z]:[\\/]+{WIN_HOME_DIR}[\\/]+[^\\/\s\"'<>]+", re.IGNORECASE)),
        ("macos-user-home", re.compile(r"/" + WIN_HOME_DIR + r"/[^/\s\"'<>]+/")),
        ("linux-user-home", re.compile(r"/" + LINUX_HOME_DIR + r"/[^/\s\"'<>]+/")),
        (
            "expanded-codex-system-scripts",
            re.compile(
                r"(?:\$HOME|~)?[\\/]*\.codex[\\/]+skills[\\/]+\.system[\\/]+"
                + re.escape(SKILL_CREATOR)
                + r"[\\/]+scripts",
                re.IGNORECASE,
            ),
        ),
    ]


def private_token_patterns():
    raw = os.environ.get("CCFA_PRIVATE_TOKENS", "")
    patterns = []
    for token in [item.strip() for item in raw.split(";") if item.strip()]:
        patterns.append(("private-token", re.compile(re.escape(token))))
    return patterns


def git_candidates(root: Path):
    """Return tracked and nonignored untracked paths, or None outside Git."""
    try:
        inside = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
            capture_output=True, timeout=15, check=False,
        )
        if inside.returncode or inside.stdout.strip() != b"true":
            return None
        inventory = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "."],
            capture_output=True, timeout=30, check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if inventory.returncode:
        # Fall back to a full walk rather than silently accepting an empty
        # release inventory after a Git failure.
        return None
    return [root / os.fsdecode(name) for name in sorted(set(inventory.stdout.split(b"\x00"))) if name]


def iter_files(root: Path, include_ignored: bool = False):
    candidates = git_candidates(root)
    seen = set()
    if candidates is not None:
        for path in candidates:
            # Git-tracked files remain publication candidates even under a
            # directory normally excluded from fallback filesystem walks.
            if path.is_file() and path.suffix.lower() not in SKIP_SUFFIXES:
                seen.add(path)
                yield path
        if not include_ignored:
            return
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        if path not in seen:
            yield path


def read_text(path: Path):
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data:
        return None
    for encoding in ("utf-8", "utf-8-sig"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    try:
        return data.decode("latin-1")
    except UnicodeDecodeError:
        return None


def main():
    # Standalone reports and redirected diagnostics use UTF-8 on every platform.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description="Scan text files for personal local paths or private tokens.")
    parser.add_argument("root", nargs="?", default=".", help="Repository or directory to scan")
    parser.add_argument("--include-ignored", action="store_true", help="Also scan ignored working files, retaining binary/cache exclusions")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print("[ERROR] Scan root must be an existing directory.", file=sys.stderr)
        return 2
    patterns = default_patterns() + private_token_patterns()
    findings = []
    scanned = 0

    for path in iter_files(root, include_ignored=args.include_ignored):
        text = read_text(path)
        if text is None:
            continue
        scanned += 1
        rel = path.relative_to(root)
        for line_no, line in enumerate(text.splitlines(), start=1):
            for name, pattern in patterns:
                if pattern.search(line):
                    findings.append((str(rel).replace("\\", "/"), line_no, name))

    print(f"Scanned text files: {scanned}")
    if findings:
        for rel, line_no, name in findings:
            print(f"[ERROR] {rel}:{line_no}: {name}")
        return 1

    print("Path privacy check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
