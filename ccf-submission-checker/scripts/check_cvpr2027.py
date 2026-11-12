#!/usr/bin/env python3
"""Local CVPR 2027 source/PDF preflight; never uploads or approves a submission."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
KIT = ROOT / "ccf-latex-templates/CVPR/2027"
POLICY = "https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines"


def source_text(value):
    """Exclude comments and literal examples from executable-source candidates."""
    value = re.sub(r"\\begin\{(verbatim\*?|lstlisting|minted)\}.*?\\end\{\1\}", "", value, flags=re.S)
    value = re.sub(r"\\verb\*?([^\w\s])(.*?)\1", "", value)
    lines = []
    for line in value.splitlines():
        for i, char in enumerate(line):
            if char == "%":
                prefix = line[:i]
                if (len(prefix) - len(prefix.rstrip("\\"))) % 2 == 0:
                    line = line[:i]
                    break
        lines.append(line)
    return "\n".join(lines)


def expand_inputs(path, project, stack=(), visited=None):
    path = path.resolve()
    if not path.is_relative_to(project):
        raise ValueError("TeX input escapes --project-root")
    if path in stack:
        raise ValueError("Cyclic TeX input: " + path.name)
    if not path.is_file():
        raise ValueError("Missing TeX input: " + path.name)
    if visited is not None:
        visited.add(path)
    text = source_text(path.read_text(encoding="utf-8-sig"))

    def load(match):
        target = match.group(1) or match.group(2)
        if any(c in target for c in "\\#$"):
            raise ValueError("Dynamic TeX input needs rendered inspection")
        local = path.parent / target
        if not local.suffix:
            local = local.with_suffix(".tex")
        return expand_inputs(local, project, (*stack, path), visited)

    return re.sub(r"\\(?:input|include)\s*(?:\{([^}]+)\}|([^\s\\{}%]+))", load, text)


def audit(tex, stage="review", pdf=None, main_pages=None, project_root=None):
    tex = Path(tex).resolve()
    project = Path(project_root).resolve() if project_root else tex.parent
    checks = []

    def add(key, status, detail):
        checks.append({"id": key, "status": status, "detail": detail})

    visited = set()
    try:
        text = expand_inputs(tex, project, visited=visited)
    except (OSError, UnicodeError, ValueError) as error:
        add("source_inputs", "fail", str(error))
        text = None
    if text is not None:
        add("source_inputs", "pass", f"Read {len(visited)} local TeX files; literal examples/comments excluded")
        conditional = bool(re.search(r"\\if[A-Za-z]*\b|\\(?:input|include)\b", text))
        if conditional:
            add("conditional_source", "not_verified", "Conditional TeX needs actual compilation/inspection; lexical mode/year/statement checks are provisional")
        years = re.findall(r"\\def\s*\\confYear\s*\{(\d{4})\}", text)
        add("year", "not_verified" if conditional else "pass" if years and set(years) == {"2027"} else "fail",
            "Expected active confYear 2027; found " + repr(years))
        declarations = []
        for match in re.finditer(r"\\usepackage\s*(?:\[([^]]*)\])?\s*\{([^}]+)\}", text):
            if "cvpr" in [v.strip() for v in match.group(2).split(",")]:
                declarations.append({v.strip() for v in (match.group(1) or "").split(",") if v.strip()})
        expected = {"review"} if stage == "review" else {"rebuttal"} if stage == "rebuttal" else set()
        options = declarations[0] if len(declarations) == 1 else set()
        modes = options & {"review", "rebuttal"}
        unknown_options = options - {"review", "rebuttal", "pagenumbers"}
        mode_ok = len(declarations) == 1 and modes == expected and not unknown_options
        detail = f"Stage {stage}: select one matching mode; pagenumbers is an independent supported option"
        if unknown_options:
            detail += "; unknown options: " + ", ".join(sorted(unknown_options))
        add("mode", "not_verified" if conditional else "pass" if mode_ok else "fail", detail)
        if stage == "camera-ready" and "pagenumbers" in options:
            add("final_page_numbering", "not_verified", "Supported forced page numbers: check the actual final/archival destination's instructions")
        style = tex.parent / "cvpr.sty"
        if not style.is_file():
            style = project / "cvpr.sty"
        if not style.is_file():
            add("style", "fail", "Missing local cvpr.sty; copy the complete matching bundle")
        else:
            digest = hashlib.sha256(style.read_bytes()).hexdigest()
            try:
                source = json.loads((KIT / "template-source.json").read_text(encoding="utf-8"))
                expected_hash = next(row["sha256"] for row in source["files"] if row["path"] == "cvpr.sty")
                accepted_hashes = {expected_hash} | {row["sha256"] for row in source.get("equivalent_styles", [])}
            except (OSError, ValueError, KeyError, StopIteration):
                expected_hash = None
                accepted_hashes = set()
            legacy = ROOT / "ccf-latex-templates/CVPR/cvpr.sty"
            old_hash = hashlib.sha256(legacy.read_bytes()).hexdigest() if legacy.is_file() else None
            status = "pass" if digest in accepted_hashes else "fail" if digest == old_hash else "not_verified"
            add("style", status, "Official 2027 style hash matched" if status == "pass" else
                "Historical 2026 style used for 2027" if status == "fail" else "Custom/other style: inspect differences and rendered format")
        if stage == "review":
            section = re.search(r"\\section\*?\s*(?:\[[^]]*\])?\s*\{\s*LLM Usage Statement\s*\}", text, re.I)
            bibliography = re.search(r"\\(?:bibliography\s*\{|printbibliography\b|begin\s*\{thebibliography\})", text)
            valid = section is not None and bibliography is not None and section.start() < bibliography.start()
            if valid:
                content = text[section.end():bibliography.start()]
                later_section = bool(re.search(r"\\section\*?\b", content))
                visible = re.sub(r"\\(?:label|ref|cite\w*|[vh]space\*?)\s*(?:\[[^]]*\])?\s*\{[^}]*\}", "", content)
                visible = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", "", visible)
                valid = not later_section and bool(re.search(r"[A-Za-z]{2,}", visible)) and not re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", content, re.I)
            add("llm_statement", "not_verified" if conditional else "pass" if valid else "fail", "Required non-placeholder section before references; verify it follows all main text")
            add("disclosure_truth", "not_verified", "Presence does not establish actual tools, scope, extent or anonymity; author confirmation required")
        else:
            add("llm_statement", "not_applicable" if stage == "rebuttal" else "not_verified",
                "Review placement check does not apply to rebuttal" if stage == "rebuttal" else "Check current final-version acknowledgment/disclosure rules")
        urls = re.findall(r"https?://[^\s}]+", text)
        if urls:
            add("external_links", "not_verified", f"{len(urls)} source URL candidates: inspect content expansion and identity, not a blanket URL ban")
    _pdf_checks(pdf, stage, main_pages, checks)
    add("anonymity", "not_applicable" if stage == "camera-ready" else "not_verified",
        "Final copies may identify authors; verify final-stage instructions" if stage == "camera-ready" else
        "Inspect visible text, citations, acknowledgments, supplement, links and identifying visuals")
    add("administration", "not_verified", "Confirm OpenReview profiles, enrollment, conflicts and submission/reciprocal-reviewer quotas outside the PDF")
    failures = sum(c["status"] == "fail" for c in checks)
    unknown = sum(c["status"] == "not_verified" for c in checks)
    return {"venue": "CVPR", "year": 2027, "track": "main research", "stage": stage,
            "policy": POLICY, "policy_checked": "2026-11-12", "checks": checks,
            "status": "fail" if failures else "not_verified" if unknown else "pass",
            "failures": failures, "not_verified": unknown,
            "scope": "Local source/PDF preflight; conditional TeX, disclosure facts and full submission readiness need actual inspection"}


def _pdf_checks(pdf, stage, main_pages, checks):
    def add(key, status, detail):
        checks.append({"id": key, "status": status, "detail": detail})
    if pdf is None:
        add("pdf", "not_verified", "No compiled PDF supplied; source inspection is not a successful build")
        return
    path = Path(pdf).resolve()
    if not path.is_file():
        add("pdf", "fail", "Compiled PDF not found")
        return
    executable = shutil.which("pdfinfo")
    if not executable:
        add("pdf", "not_verified", "pdfinfo unavailable; inspect the compiled PDF with an available PDF tool")
        return
    try:
        # On Windows, ordinary date strings can contain an ANSI-encoded timezone
        # even with -enc UTF-8. ISO dates keep stdout uniformly decodable without
        # guessing an encoding or losing non-ASCII PDF metadata.
        result = subprocess.run([executable, "-enc", "UTF-8", "-isodates", str(path)],
                                capture_output=True, timeout=20, check=True)
        info = result.stdout.decode("utf-8")
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    except (subprocess.SubprocessError, UnicodeError, AttributeError, ValueError) as error:
        add("pdf", "not_verified", "Could not inspect PDF: " + type(error).__name__)
        return
    add("pdf", "pass", f"Readable PDF, {pages} total pages; this does not prove current-source build success")
    size = re.search(r"^Page size:\s+([\d.]+) x ([\d.]+) pts", info, re.M)
    letter = size is not None and abs(float(size[1]) - 612) < 1 and abs(float(size[2]) - 792) < 1
    add("paper_size", "pass" if letter else "fail", "Expected US Letter (612 x 792 pt)")
    if stage == "rebuttal":
        add("page_budget", "pass" if pages <= 1 else "fail", "Rebuttal allows at most one total page")
    elif stage == "review":
        if main_pages is not None:
            valid = 0 < main_pages <= pages
            add("page_budget", "pass" if valid and main_pages <= 8 else "fail",
                f"User-inspected main-text boundary: {main_pages}; eight-page limit excludes only allowed matter")
        elif pages <= 8:
            add("page_budget", "pass", "Entire PDF fits eight pages")
        else:
            add("page_budget", "not_verified", "More than eight total pages can be valid; inspect main-text boundary and allowed reference/statement pages")
    else:
        add("page_budget", "not_verified", "Verify final/Findings stage rules; no review-stage budget inferred")
    if stage != "camera-ready":
        author = re.search(r"^Author:[ \t]*([^\r\n]*)", info, re.M)
        value = author[1].strip() if author else ""
        add("pdf_author_metadata", "pass" if not value or value.lower() in {"anonymous", "anonymous authors"} else "fail",
            "Author metadata empty/anonymous" if not value or value.lower() in {"anonymous", "anonymous authors"} else "Author metadata may identify authors")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", type=Path, required=True)
    parser.add_argument("--stage", choices=["review", "rebuttal", "camera-ready"], default="review")
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--main-pages", type=int, help="Actual main-text page count after rendered inspection, not total pages")
    args = parser.parse_args()
    if args.main_pages is not None and (args.pdf is None or args.stage != "review"):
        parser.error("--main-pages requires a review-stage --pdf")
    report = audit(args.tex, args.stage, args.pdf, args.main_pages, args.project_root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
