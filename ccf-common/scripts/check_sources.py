#!/usr/bin/env python3
"""Check the CCFA source registry without rewriting it."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

REQUIRED_FIELDS = {
    "id",
    "title",
    "url",
    "source_type",
    "used_by",
    "recorded_at",
    "verified_at",
    "stale_after_days",
    "notes",
}

WIN_HOME_DIR = "Us" + "ers"

PRIVATE_PATH_PATTERNS = (
    re.compile(rf"[A-Za-z]:[\\/]+{WIN_HOME_DIR}[\\/]+", re.IGNORECASE),
    re.compile(r"/" + WIN_HOME_DIR + r"/[^/\s]+/"),
    re.compile(r"\\.codex[\\/]+skills[\\/]+\\.system", re.IGNORECASE),
    re.compile(r"\$HOME[\\/]+\\.codex[\\/]+skills[\\/]+\\.system", re.IGNORECASE),
)


def parse_date(value):
    if value in (None, ""):
        return None
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def check_url(url, timeout):
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        return "skip-local"
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "ccfa-source-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return f"ok:{response.status}"
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405}:
            return f"reachable-with-caveat:{exc.code}"
        return f"http-error:{exc.code}"
    except Exception as exc:  # noqa: BLE001 - report-only diagnostic script
        return f"error:{type(exc).__name__}"


def main():
    # Standalone reports and redirected diagnostics use UTF-8 on every platform.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description="Validate ccf-common/references/source-registry.yaml")
    parser.add_argument(
        "registry",
        nargs="?",
        default=Path(__file__).resolve().parents[1] / "references" / "source-registry.yaml",
        help="Path to source-registry.yaml",
    )
    parser.add_argument("--check-urls", action="store_true", help="Also perform report-only URL checks")
    parser.add_argument("--timeout", type=float, default=8.0, help="Per-URL timeout for --check-urls")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    try:
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        parser.error(f"Cannot read UTF-8 registry: {exc}")
    sources = data.get("sources", []) if isinstance(data, dict) else []

    errors = []
    warnings = []
    seen_ids = set()
    today = dt.date.today()

    for index, source in enumerate(sources, start=1):
        if not isinstance(source, dict):
            errors.append(f"source #{index}: expected mapping")
            continue
        missing = REQUIRED_FIELDS - set(source)
        if missing:
            errors.append(f"{source.get('id', f'source #{index}')}: missing {', '.join(sorted(missing))}")
        source_id = source.get("id")
        if source_id in seen_ids:
            errors.append(f"{source_id}: duplicate id")
        seen_ids.add(source_id)
        if not isinstance(source.get("used_by"), list) or not source.get("used_by"):
            errors.append(f"{source_id}: used_by must be a non-empty list")
        url = source.get("url")
        if isinstance(url, str) and any(pattern.search(url) for pattern in PRIVATE_PATH_PATTERNS):
            errors.append(f"{source_id}: url must not contain a personal absolute path or local skill-root leak")

        verified_at = parse_date(source.get("verified_at"))
        stale_after = source.get("stale_after_days")
        if verified_at is None:
            warnings.append(f"{source_id}: unverified")
        elif isinstance(stale_after, int) and (today - verified_at).days > stale_after:
            warnings.append(f"{source_id}: stale, verified_at={verified_at}, stale_after_days={stale_after}")

        if args.check_urls:
            warnings.append(f"{source_id}: url_status={check_url(source.get('url'), args.timeout)}")

    print(f"Registry: {registry_path}")
    print(f"Sources: {len(sources)}")
    for warning in warnings:
        print(f"[WARN] {warning}")
    for error in errors:
        print(f"[ERROR] {error}")

    if errors:
        return 1
    print("Source registry check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
