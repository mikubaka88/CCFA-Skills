#!/usr/bin/env python3
"""Check local Markdown links without rewriting files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from check_path_privacy import git_candidates


ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")
FALLBACK_SKIP_DIRS = {".git", "ccfa-workfiles"}


def strip_fenced_code(text: str) -> str:
    lines = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    return "\n".join(lines)


def normalize_target(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split()[0]
    if target.startswith(SKIP_PREFIXES):
        return None
    target = target.split("#", 1)[0]
    if not target:
        return None
    return unquote(target)


def markdown_candidates(root: Path):
    """Check published candidates, not ignored task backups or build reports."""
    candidates = git_candidates(root)
    if candidates is not None:
        # A tracked file is still a release candidate even when its directory
        # is ignored or normally excluded from a filesystem fallback.
        yield from (path for path in candidates if path.is_file() and path.suffix.lower() == ".md")
        return
    for path in sorted(root.rglob("*")):
        if any(part in FALLBACK_SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.is_file() and path.suffix.lower() == ".md":
            yield path


def check_links(root: Path) -> tuple[int, list[str]]:
    root = root.resolve()
    errors: list[str] = []
    checked = 0
    for path in markdown_candidates(root):
        try:
            text = strip_fenced_code(path.read_text(encoding="utf-8-sig"))
        except UnicodeDecodeError as exc:
            errors.append(f"{path.relative_to(root)}: invalid UTF-8 at byte {exc.start}; verify the source encoding")
            continue
        except OSError as exc:
            errors.append(f"{path.relative_to(root)}: cannot read Markdown: {exc}")
            continue
        for match in LINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if target is None:
                continue
            checked += 1
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: link escapes repo: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(root)}: missing link target: {target}")
    return checked, errors


def main() -> int:
    # Standalone reports and redirected diagnostics use UTF-8 on every platform.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    checked, errors = check_links(ROOT)
    print(f"Checked local Markdown links: {checked}")
    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
