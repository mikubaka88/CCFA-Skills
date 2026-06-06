#!/usr/bin/env python3
"""Check local Markdown links without rewriting files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


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


def main() -> int:
    errors: list[str] = []
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = strip_fenced_code(path.read_text(encoding="utf-8", errors="replace"))
        for match in LINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if target is None:
                continue
            checked += 1
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repo: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link target: {target}")
    print(f"Checked local Markdown links: {checked}")
    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
