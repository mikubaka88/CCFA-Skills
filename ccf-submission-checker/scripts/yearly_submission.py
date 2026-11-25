#!/usr/bin/env python3
"""Shared local TeX and PDF preflight for year-specific conference checkers."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

from check_cvpr2027 import expand_inputs

TEMPLATES = Path(__file__).resolve().parents[2] / "ccf-latex-templates"
PACKAGE = re.compile(r"\\usepackage\s*(?:\[([^]]*)\])?\s*\{([^}]+)\}")
SECTION = re.compile(r"\\section\*?\s*(?:\[[^]]*\])?\s*\{\s*([^{}]+?)\s*\}")
REFERENCES = re.compile(r"\\(?:bibliography\s*\{|printbibliography\b|begin\s*\{thebibliography\})")
APPENDIX = re.compile(r"\\appendix\b")
@dataclass(frozen=True)
class VenuePolicy:
    name: str
    year: int
    package: str
    bibliography_style: str
    dimensions: tuple[float, float]
    size_name: str
    policy_records: tuple[str, ...]
    policy_checked: str
    review_budgets: dict[str, int]
    review_modes: tuple[frozenset[str], ...]
    final_modes: tuple[frozenset[str], ...]
    independent_options: frozenset[str]
    section_titles: dict[str, frozenset[str]]
    manual_review: tuple[str, str]
    manual_final: tuple[str, str]
    sections_may_follow_references: frozenset[str] = frozenset()
    other_style_pattern: str | None = None
    extra_anonymous_metadata: frozenset[str] = frozenset()


def check_source(tex, project, policy, stage, add):
    package = policy.package
    visited = set()
    try:
        text = expand_inputs(tex, project, visited=visited)
    except (OSError, ValueError) as error:
        add("source_inputs", "not_verified", f"Inspect the rendered build and inputs: {error}")
        return
    add("source_inputs", "pass", f"Read {len(visited)} local TeX files")
    if re.search(r"\\if[A-Za-z@]*\b", text):
        add("source_declarations", "not_verified", "Conditional TeX requires inspection of the active build")
        return

    body_parts = re.split(r"\\begin\s*\{document\}", text, maxsplit=1)
    preamble, body = body_parts if len(body_parts) == 2 else (text, "")
    declarations = [(set(map(str.strip, match[2].split(","))),
                     {option.strip() for option in (match[1] or "").split(",") if option.strip()})
                    for match in PACKAGE.finditer(preamble)]
    options = [parsed_options for names, parsed_options in declarations if package in names]
    other_style = policy.other_style_pattern and any(
        name != package and re.fullmatch(policy.other_style_pattern, name)
        for names, _ in declarations for name in names
    )
    expected_modes = policy.final_modes if stage == "camera-ready" else policy.review_modes
    if not options and not other_style:
        add("template_mode", "not_verified", f"No direct {package} declaration found. Check active class/package and options.")
    else:
        mode_ok = len(options) == 1 and (options[0] - policy.independent_options) in expected_modes and not other_style
        add("template_mode", "pass" if mode_ok else "fail", f"Expected one {package} declaration with options for {stage}")

    kit = TEMPLATES / policy.name / str(policy.year)
    try:
        manifest = json.loads((kit / "template-source.json").read_text(encoding="utf-8"))
        hashes = {item["path"]: item["sha256"] for item in manifest["files"]}
    except (OSError, ValueError, KeyError):
        hashes = {}
    for name in (f"{package}.sty", f"{policy.bibliography_style}.bst"):
        file = next((base / name for base in (tex.parent, project) if (base / name).is_file()), None)
        expected = hashes.get(name)
        if file and expected:
            data = file.read_bytes()
            valid = expected in {hashlib.sha256(data).hexdigest(),
                                 hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()}
            add(name, "pass" if valid else "not_verified", "Official snapshot matched" if valid else
                "Snapshot differs. Compare the style selected by the build with the current official file.")
        else:
            add(name, "not_verified", "Inspect the file source and TeX search path")

    if not body:
        add("required_sections", "not_verified", "Document body not found in standard form. Inspect the compiled paper.")
        return

    check_sections(body, policy, add)


def check_sections(body, policy, add):
    references = REFERENCES.search(body)
    appendix = APPENDIX.search(body)
    headings = list(SECTION.finditer(body))
    boundaries = [match.start() for match in [*headings, references, appendix] if match]

    titles = policy.section_titles
    end_matter = set().union(*titles.values(), {
        "acknowledgments", "acknowledgements", "ethical considerations", "ethics statement",
    })
    tail_offsets = [match.start() for match in (references, appendix) if match]
    text_end = min(tail_offsets, default=len(body))
    main_headings = [heading for heading in headings
                     if heading.start() < text_end and heading[1].casefold() not in end_matter]
    for key, names in titles.items():
        sections = [heading for heading in headings if heading[1].casefold() in names]
        if not sections:
            add(key, "not_verified", "Required heading not detected. Inspect the PDF, including macro-defined headings.")
            continue
        heading = sections[0]
        end = min((offset for offset in boundaries if offset > heading.start()), default=len(body))
        content = body[heading.end():end].split(r"\end{document}", 1)[0].strip()
        visible = re.sub(r"\\(?:label|index)\s*\{[^{}]*\}", "", content).strip()
        if len(sections) != 1 or not visible or re.match(r"^(?:\[\s*)?(?:todo|tbd|placeholder)\b", visible, re.I):
            add(key, "fail", "Expected one populated section")
        elif main_headings and heading.start() < main_headings[-1].start():
            add(key, "fail", "Required section appears before the last main-text section")
        elif key not in policy.sections_may_follow_references and references is None:
            add(key, "not_verified", "Heading found. Verify its placement before references in the PDF.")
        elif key not in policy.sections_may_follow_references and heading.start() > references.start():
            add(key, "fail", "Required section appears after references")
        elif appendix and heading.start() > appendix.start():
            add(key, "not_verified", "Section appears inside appendix source. Verify required placement in the PDF.")
        else:
            add(key, "pass", "Matching source section found. Verify rendered placement and content.")

    if appendix and references:
        proper_order = references.start() < appendix.start()
        add("appendix_order", "pass" if proper_order else "fail", "Appendices follow references")


def check_pdf(pdf, main_pages, limit, policy, stage, add):
    if pdf is None:
        add("pdf", "not_verified", "Supply the compiled PDF to inspect the package")
        return
    if not pdf.is_file():
        add("pdf", "fail", "PDF not found")
        return
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        add("pdf", "not_verified", "pdfinfo unavailable")
        return
    try:
        result = subprocess.run([pdfinfo, "-enc", "UTF-8", "-isodates", "-f", "1", "-l", "1000000",
                                 str(pdf.resolve())],
                                capture_output=True, check=True, timeout=20)
        info = result.stdout.decode("utf-8")
        pages_match = re.search(r"^Pages:[ \t]+(\d+)", info, re.M)
        if not pages_match:
            raise ValueError("Page count unavailable")
        pages = int(pages_match[1])
    except (OSError, subprocess.SubprocessError, ValueError) as error:
        add("pdf", "not_verified", f"Could not inspect PDF: {type(error).__name__}")
        return
    add("pdf", "pass", f"Readable PDF, {pages} total pages")

    dimensions, size_name = policy.dimensions, policy.size_name
    sizes = {int(number): (float(width), float(height)) for number, width, height in re.findall(
        r"^Page[ \t]+(\d+)[ \t]+size:[ \t]+([\d.]+) x ([\d.]+) pts", info, re.M
    )}
    if not sizes:
        first_size = re.search(r"^Page size:[ \t]+([\d.]+) x ([\d.]+) pts", info, re.M)
        if first_size:
            sizes[1] = (float(first_size[1]), float(first_size[2]))
    wrong = [page for page, size in sizes.items()
             if any(abs(value - target) >= 1 for value, target in zip(size, dimensions))]
    first_page_status = "fail" if 1 in wrong else "pass" if 1 in sizes else "not_verified"
    add("first_page_size", first_page_status, f"Expected {size_name} on the first page")
    if wrong:
        numbers = ", ".join(map(str, wrong[:10]))
        add("page_geometry", "fail", f"Expected {size_name}. Off-size pages: {numbers} ({len(wrong)} total)")
    elif len(sizes) == pages:
        add("page_geometry", "pass", f"All {pages} pages use {size_name}")
    else:
        add("page_geometry", "not_verified", f"Measured {len(sizes)} of {pages} pages")

    if main_pages is not None:
        valid = 0 < main_pages <= min(pages, limit)
        add("main_pages", "pass" if valid else "fail", f"Inspected main pages: {main_pages}, limit: {limit}, total: {pages}")
    elif pages <= limit:
        add("main_pages", "pass", f"The entire PDF fits the {limit}-page main-text cap")
    else:
        add("main_pages", "not_verified", f"Inspect the body boundary before comparing with the {limit}-page cap")

    if stage == "review":
        author = re.search(r"^Author:[ \t]*([^\r\n]*)", info, re.M)
        value = author[1].strip().casefold() if author else ""
        accepted = {"", "anonymous", "anonymous authors", "anonymous submission",
                    "anonymous author(s)"} | policy.extra_anonymous_metadata
        add("pdf_author_metadata", "pass" if value in accepted else "fail",
            "Author metadata is empty or anonymous" if value in accepted else
            "Non-anonymous Author metadata. Inspect it and remove identifying information.")


def audit(policy, track, stage, tex, pdf=None, main_pages=None, project_root=None):
    checks = []

    def add(key, status, detail):
        checks.append({"id": key, "status": status, "detail": detail})

    tex = tex.resolve()
    project = project_root.resolve() if project_root else tex.parent
    limit = policy.review_budgets[track] + (stage == "camera-ready")
    check_source(tex, project, policy, stage, add)
    check_pdf(pdf, main_pages, limit, policy, stage, add)
    add("manual", "not_verified", "Verify live rules, build logs, rendered submission, supplements and required section content")
    key, detail = policy.manual_final if stage == "camera-ready" else policy.manual_review
    add(key, "not_verified", detail)
    failures = sum(check["status"] == "fail" for check in checks)
    return {"venue": policy.name, "year": policy.year, "track": track, "stage": stage,
            "policy_records": policy.policy_records, "policy_checked": policy.policy_checked,
            "status": "fail" if failures else "not_verified", "failures": failures, "checks": checks}


def main(policy, description):
    parser = argparse.ArgumentParser(description=description)
    tracks = tuple(policy.review_budgets)
    if len(tracks) == 1:
        parser.add_argument("--track", choices=tracks, default=tracks[0])
    else:
        parser.add_argument("--track", choices=tracks, required=True)
    parser.add_argument("--stage", choices=("review", "camera-ready"), default="review")
    parser.add_argument("--tex", type=Path, required=True)
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--main-pages", type=int, help="Main-text pages after inspecting the compiled PDF")
    args = parser.parse_args()
    if args.main_pages is not None and (args.pdf is None or args.main_pages < 1):
        parser.error("--main-pages must be positive and requires --pdf")
    report = audit(policy, args.track, args.stage, args.tex, args.pdf,
                   args.main_pages, args.project_root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["failures"] else 0
