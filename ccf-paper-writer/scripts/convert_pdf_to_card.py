#!/usr/bin/env python3
"""Compatibility entry for PDF exemplar extraction; preserve legacy arguments."""

from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_path", nargs="?", help="Single PDF file")
    parser.add_argument("--batch", help="Directory of PDFs")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--full-text", action="store_true", help="Also save full text")
    args = parser.parse_args()
    if bool(args.pdf_path) == bool(args.batch):
        parser.error("Provide one PDF path or --batch, not both.")
    pdfs = sorted(Path(args.batch).glob("*.pdf")) if args.batch else [Path(args.pdf_path)]
    if not pdfs:
        parser.error("No PDF files found in the batch directory.")
    converter = Path(__file__).resolve().parents[2] / "ccf-paper-to-exemplar" / "scripts" / "convert.py"
    if not converter.is_file():
        parser.error("Install ccf-paper-to-exemplar alongside ccf-paper-writer to use PDF conversion.")
    saved_argv = sys.argv
    sys.argv = [str(converter), *map(str, pdfs), "--output-dir", args.output_dir]
    if args.full_text:
        sys.argv.append("--full-text")
    try:
        module = runpy.run_path(str(converter), run_name="ccfa_exemplar_converter")
        return module["main"]()
    finally:
        sys.argv = saved_argv


if __name__ == "__main__":
    raise SystemExit(main())
