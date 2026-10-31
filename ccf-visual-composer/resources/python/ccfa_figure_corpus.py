#!/usr/bin/env python3
"""Search a compact paper inventory without loading it into an agent prompt.

The inventory records discoverable papers, not figures already reproduced.
Only selected visually inspected designs appear in the separate figure library.
Uses the Python standard library; importing this module reads no inventory.
"""
from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
import re
import sys
import unicodedata


DEFAULT_DIRECTORY = Path(__file__).resolve().parents[1] / "figure-library"
FIELDS = ("title", "url", "venue", "year", "track", "pdf")
VENUE_ALIASES = {"nips": "neurips", "nature machine intelligence": "nmi",
                 "naturemachineintelligence": "nmi"}


class CorpusError(ValueError):
    """An unavailable or invalid inventory cannot establish corpus coverage."""


def _normal(value):
    return unicodedata.normalize("NFKC", str(value)).casefold().strip()


def _venue(value):
    value = _normal(value)
    return VENUE_ALIASES.get(value, value)


def iter_papers(directory=None):
    """Yield inventory rows lazily; never import NumPy or open the network."""
    path = Path(directory or DEFAULT_DIRECTORY) / "papers.jsonl.gz"
    try:
        with gzip.open(path, "rt", encoding="utf-8", errors="strict") as stream:
            for number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise CorpusError(f"Invalid paper JSON at inventory line {number}") from exc
                if not isinstance(row, dict) or not isinstance(row.get("title"), str):
                    raise CorpusError(f"Invalid paper record at inventory line {number}")
                if not row["title"].strip():
                    raise CorpusError(f"Empty title at inventory line {number}")
                yield {key: row.get(key) for key in FIELDS}
    except (OSError, EOFError, UnicodeError) as exc:
        raise CorpusError("Cannot read the packaged UTF-8 paper inventory") from exc


def coverage(directory=None, *, venue=None, year=None):
    """Read the small coverage manifest, with optional venue/year filtering."""
    path = Path(directory or DEFAULT_DIRECTORY) / "corpus.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CorpusError("Cannot read the packaged corpus coverage manifest") from exc
    if (not isinstance(manifest, dict) or not isinstance(manifest.get("coverage"), list)
            or any(not isinstance(row, dict) for row in manifest["coverage"])):
        raise CorpusError("Corpus manifest must contain a coverage list")
    visible = ("venue", "year", "entry_url", "status", "record_count", "packaged_records",
               "exhaustive_listing", "scope", "listing_scope", "exhaustiveness_scope",
               "visually_inspected_design_studies", "reused_visual_design_studies")
    rows = [{key: row[key] for key in visible if key in row} for row in manifest["coverage"]
            if (venue is None or _venue(row.get("venue", "")) == _venue(venue))
            and (year is None or row.get("year") == year)]
    # Top-level totals always describe the packaged inventory, not a filtered hit count.
    summary = ("version", "checked_at", "publication_years", "record_count", "all_figures_reproduced",
               "visually_inspected_design_studies", "reused_visual_design_studies", "new_visual_design_studies",
               "inventory_scope", "figure_scope")
    return {**{key: manifest[key] for key in summary if key in manifest}, "coverage": rows,
            "filtered": venue is not None or year is not None}


def search(query=None, *, venue=None, year=None, limit=8, directory=None):
    """Return bounded metadata hits. Search is lexical, not a figure recommendation.

    All normalized query terms must occur in the title, venue, or track. The
    additional matching row is used only to set ``has_more``; no total hit count
    is invented when the stream stops early.
    """
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 50:
        raise ValueError("limit must be an integer between 1 and 50")
    if year is not None and (isinstance(year, bool) or not isinstance(year, int)):
        raise ValueError("year must be an integer")
    terms = re.findall(r"\w+", _normal(query or ""), flags=re.UNICODE)
    if query is not None and not terms:
        raise ValueError("query must contain a searchable word")
    matches = []
    scanned = 0
    has_more = False
    for row in iter_papers(directory):
        scanned += 1
        if venue is not None and _venue(row.get("venue") or "") != _venue(venue):
            continue
        if year is not None and row.get("year") != year:
            continue
        haystack = _normal(" ".join(str(row.get(k) or "") for k in ("title", "venue", "track")))
        if not all(term in haystack for term in terms):
            continue
        if len(matches) == limit:
            has_more = True
            break
        matches.append(row)
    return {"matches": matches, "returned": len(matches), "limit": limit,
            "has_more": has_more, "records_scanned": scanned,
            "all_figures_reproduced": False,
            "scope": "Paper metadata search; use the figure-library router for inspected designs."}


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", help="Words in paper titles, venue, or track (all terms must match)")
    parser.add_argument("--venue", help="Venue name, e.g. CVPR, ACL, ICLR, ICML, NeurIPS or NMI")
    parser.add_argument("--year", type=int, help="Publication year")
    parser.add_argument("--limit", type=int, default=8, help="Return 1–50 records (default 8)")
    parser.add_argument("--coverage", action="store_true", help="Print the small coverage manifest")
    parser.add_argument("--corpus-dir", type=Path, help="Alternative directory containing the two inventory files")
    args = parser.parse_args(argv)
    try:
        if args.coverage:
            if args.query:
                parser.error("--query and --coverage are separate inventory operations")
            result = coverage(args.corpus_dir, venue=args.venue, year=args.year)
        else:
            result = search(args.query, venue=args.venue, year=args.year,
                            limit=args.limit, directory=args.corpus_dir)
    except (CorpusError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
