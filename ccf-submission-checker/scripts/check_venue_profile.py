#!/usr/bin/env python3
"""Check an edition-specific CCFA submission profile against local TeX/PDF."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess

from check_cvpr2027 import expand_inputs

PROFILE_ROOT = Path(__file__).resolve().parents[1] / "references" / "venue-profiles"
DECLARATION = re.compile(r"\\(documentclass|usepackage)\s*(?:\[([^]]*)\])?\s*\{([^}]+)\}")
APPENDIX = re.compile(r"\\appendi(?:x|ces)\b")
SECTION = re.compile(r"\\section\*?\s*(?:\[[^]]*\])?\s*\{\s*([^{}]+?)\s*\}")
BIBLIOGRAPHY = re.compile(r"\\(?:bibliography\s*\{|printbibliography\b|begin\s*\{thebibliography\})")


def declarations(text):
    return {(match[1], name.strip()): {opt.strip() for opt in (match[2] or "").split(",") if opt.strip()}
            for match in DECLARATION.finditer(text) for name in match[3].split(",")}


def audit_source(tex, profile, stage, add):
    try:
        text = expand_inputs(tex.resolve(), tex.resolve().parent)
    except (OSError, ValueError) as error:
        add("source", "not_verified", str(error))
        return
    if re.search(r"\\if[A-Za-z@]*\b", text):
        add("source", "not_verified", "Conditional TeX needs actual build inspection.")
        return
    add("source", "pass", "Read local TeX inputs.")
    preamble, _, body = text.partition(r"\begin{document}")
    packages = declarations(preamble)
    for requirement in profile["stage_checks"].get(stage, []):
        key, name = requirement["kind"], requirement["name"]
        options = packages.get((key, name))
        valid = options is not None and set(requirement.get("options", ())) <= options
        if valid and set(requirement.get("forbid", ())) & options:
            valid = False
        if valid and requirement.get("paper_id"):
            valid = any(re.fullmatch(r"ID=[0-9]+", option) for option in options)
        add(name + "_mode", "pass" if valid else "fail", requirement["detail"])
    if not body:
        add("source_sections", "not_verified", "Document body unavailable. Inspect the actual PDF.")
        return
    appendix = APPENDIX.search(body)
    bibliography = BIBLIOGRAPHY.search(body)
    headings = list(SECTION.finditer(body))
    for name in profile.get("required_appendix_sections", ()):
        section = next((row for row in headings if row[1].casefold() == name.casefold()), None)
        if section is None:
            add(name, "not_verified", "Required heading not detected. Inspect the actual appendix.")
        elif appendix is None or section.start() < appendix.start():
            add(name, "fail", "Required section belongs in the appendix.")
        else:
            later = [row.start() for row in headings if row.start() > section.start()]
            if bibliography and bibliography.start() > section.start():
                later.append(bibliography.start())
            tail = body[section.end():min(later, default=len(body))].split(r"\end{document}", 1)[0].strip()
            ready = bool(tail) and not re.match(r"^(?:\[ *)?(?:todo|tbd|placeholder)\b", tail, re.I)
            add(name, "pass" if ready else "fail", "Check content against actual scientific work and truthful author disclosures.")
    if stage == "review" and profile.get("separate_supplement") and appendix:
        add("appendix", "not_verified", "Check the main PDF and separate supplementary package. Main-only page exemptions are not assumed.")


def audit_pdf(pdf, profile, stage, track, main_pages, add):
    if pdf is None or shutil.which("pdfinfo") is None:
        add("pdf", "not_verified", "Compiled PDF and Poppler pdfinfo are needed for local PDF checks.")
        return
    try:
        info = subprocess.run(
            ["pdfinfo", "-enc", "UTF-8", "-isodates", "-f", "1", "-l", "1000000", str(pdf)],
            check=True, capture_output=True, timeout=20, encoding="utf-8",
        ).stdout
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
    except (OSError, TypeError, ValueError, subprocess.SubprocessError) as error:
        add("pdf", "not_verified", f"PDF properties unavailable: {type(error).__name__}.")
        return
    add("pdf", "pass", f"Readable PDF, {pages} total pages.")
    total = profile.get("total_pages", {}).get(stage)
    if total is not None:
        add("total_pages", "pass" if pages <= total else "fail", f"Total {pages}; cap {total}.")
    maximum = profile["page_limits"].get(stage, {}).get(track)
    if maximum is None:
        add("main_pages", "not_applicable" if profile.get("review_unlimited") and stage == "review" else "not_verified",
            "Use the exact stage and publisher instructions.")
    elif main_pages is not None:
        add("main_pages", "pass" if 0 < main_pages <= min(pages, maximum) else "fail",
            f"Inspected page count {main_pages}; cap {maximum}; total {pages}.")
    elif pages <= maximum:
        add("main_pages", "pass", f"The entire PDF fits the {maximum}-page cap.")
    else:
        add("main_pages", "not_verified", "Inspect page boundaries and provide --main-pages.")
    if profile.get("letter"):
        dimensions = re.findall(r"^Page\s+\d+\s+size:\s+([\d.]+) x ([\d.]+) pts", info, re.M)
        wrong = any(abs(float(w)-612)>=1 or abs(float(h)-792)>=1 for w,h in dimensions)
        add("page_size", "fail" if wrong else "pass" if len(dimensions) == pages else "not_verified",
            "Expected US Letter across the PDF.")
    if stage == "review":
        field = re.search(r"^Author:[ \t]*([^\r\n]*)", info, re.M)
        author = field[1].strip().casefold() if field else ""
        valid = author in {"", "anonymous", "anonymous author(s)", "anonymous authors", "anonymous submission"}
        add("author_metadata", "pass" if valid else "fail", "Inspect author names, links and metadata.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=sorted(p.stem for p in PROFILE_ROOT.glob("*.json")))
    parser.add_argument("--stage", choices=("review", "camera-ready"), default="review")
    parser.add_argument("--track")
    parser.add_argument("--tex", type=Path, required=True)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--main-pages", type=int)
    args = parser.parse_args()
    profile = json.loads((PROFILE_ROOT / f"{args.profile}.json").read_text(encoding="utf-8"))
    tracks = profile["tracks"]
    track = args.track or (tracks[0] if len(tracks) == 1 else None)
    if track not in tracks:
        parser.error(f"--track must be one of {', '.join(tracks)}")
    if args.main_pages is not None and (args.main_pages < 1 or args.pdf is None):
        parser.error("--main-pages must be positive and requires --pdf")

    checks = []

    def add(name, status, detail):
        checks.append({"id": name, "status": status, "detail": detail})

    audit_source(args.tex, profile, args.stage, add)
    audit_pdf(args.pdf, profile, args.stage, track, args.main_pages, add)
    for detail in profile["manual_checks"]:
        add("manual", "not_verified", detail)
    print(json.dumps({"profile": args.profile, "stage": args.stage, "track": track, "checks": checks}, indent=2))
    return int(any(check["status"] == "fail" for check in checks))


if __name__ == "__main__":
    raise SystemExit(main())
