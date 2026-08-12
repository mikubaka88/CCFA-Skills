#!/usr/bin/env python3
"""Check manuscript prose for repeated, mechanical writing patterns.

The checker is deliberately non-mutating. It reads one file or stdin and emits
text or JSON, allowing callers to keep the result ephemeral.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


OPENING_FILLER = [
    r"\bin the realm of\b",
    r"\bit is important to note that\b",
    r"\bit should be (?:noted|emphasized) that\b",
    r"\bit is worth (?:noting|mentioning) that\b",
    r"\bwe would like to (?:note|emphasize|highlight) that\b",
    r"\bin today'?s rapidly evolving\b",
    r"\bthis serves as a testament to\b",
    r"\bit goes without saying that\b",
    r"\bin order to\b",
    r"\bas a matter of fact\b",
    r"\bwhen it comes to\b",
    r"\bat the end of the day\b",
    r"\bwith that being said\b",
    r"\bthis section will discuss\b",
    r"\bthe following paragraph examines\b",
    r"\bwe now turn our attention to\b",
]
PRECISION_TERMS = (
    "delve",
    "tapestry",
    "landscape",
    "pivotal",
    "crucial",
    "foster",
    "showcase",
    "testament",
    "navigate",
    "leverage",
    "realm",
    "embark",
    "underscore",
    "multifaceted",
    "nuanced",
    "comprehensive",
    "robust",
    "intricate",
    "cornerstone",
    "paradigm",
    "synergy",
    "holistic",
    "streamline",
    "cutting-edge",
    "groundbreaking",
)
FORMULAIC_PATTERNS = {
    "not_only_but_also": r"\bnot only\b.{0,140}\bbut also\b",
    "first_second_third": r"\bfirst(?:ly)?\b.{0,300}\bsecond(?:ly)?\b.{0,300}\bthird(?:ly)?\b",
    "three_labels": r"(?:^|\n)\s*(?:1[.)]|first[:,]).*(?:\n|.){0,500}(?:2[.)]|second[:,]).*(?:\n|.){0,500}(?:3[.)]|third[:,])",
}


def _read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def _prose_only(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\\begin\{(?:verbatim|lstlisting|minted|equation\*?|align\*?)\}.*?\\end\{[^}]+\}", " ", text, flags=re.S)
    # Markdown tables and HTML figure tags are document structure, not authored
    # prose. Ignoring their delimiter runs prevents `| --- |` from being
    # misclassified as em dashes and keeps numeric table cells out of sentence
    # rhythm checks.
    text = re.sub(r"^\s*\|.*\|\s*$", " ", text, flags=re.M)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^\s*(?:---+|___+|\*\*\*+)\s*$", " ", text, flags=re.M)
    text = re.sub(r"\\begin\{quote\}.*?\\end\{quote\}", " ", text, flags=re.S)
    text = re.sub(r'“[^”]*”|"[^"\n]*"|‘[^’]*’', " ", text)
    return text


def _words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*|[\u4e00-\u9fff]", text)


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?。！？])\s+", text) if len(_words(s)) >= 3]


def _line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def inspect(text: str, scope: str) -> dict:
    prose = _prose_only(text)
    issues: list[dict] = []
    word_count = len(_words(prose))
    em_dash_count = prose.count("—") + len(re.findall(r"(?<!-)---(?!-)", prose))
    limit = 3 if scope == "paper" else 0
    if em_dash_count > limit:
        issues.append({
            "code": "em_dash_limit",
            "severity": "error",
            "count": em_dash_count,
            "limit": limit,
            "message": f"Authored prose contains {em_dash_count} em dashes; {scope} limit is {limit}.",
        })

    for pattern in OPENING_FILLER:
        for match in re.finditer(pattern, prose, flags=re.I):
            issues.append({
                "code": "opening_filler",
                "severity": "warning",
                "line": _line_number(prose, match.start()),
                "text": match.group(0),
                "message": "Delete the throat-clearing opener if the following clause stands directly.",
            })

    lower = prose.lower()
    flagged_terms = {term: len(re.findall(rf"\b{re.escape(term)}\b", lower)) for term in PRECISION_TERMS}
    flagged_terms = {term: count for term, count in flagged_terms.items() if count}
    if flagged_terms:
        issues.append({
            "code": "precision_terms",
            "severity": "advisory",
            "terms": flagged_terms,
            "message": "Verify that each promotional or vague term is earned by evidence and scope.",
        })

    for name, pattern in FORMULAIC_PATTERNS.items():
        matches = list(re.finditer(pattern, prose, flags=re.I | re.S | re.M))
        if matches:
            issues.append({
                "code": "formulaic_structure",
                "severity": "warning",
                "pattern": name,
                "count": len(matches),
                "message": "Check whether the enumeration or contrast follows the argument rather than a fixed template.",
            })

    sentences = _sentences(prose)
    lengths = [len(_words(sentence)) for sentence in sentences]
    narrow_runs = []
    for start in range(max(0, len(lengths) - 4)):
        window = lengths[start : start + 5]
        if len(window) == 5 and max(window) - min(window) <= 5:
            narrow_runs.append({"sentences": [start + 1, start + 5], "word_counts": window})
    if narrow_runs:
        issues.append({
            "code": "uniform_sentence_run",
            "severity": "warning",
            "runs": narrow_runs,
            "message": "Review five-sentence runs with nearly identical length for repeated syntax.",
        })

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", prose) if len(_words(p)) >= 20]
    paragraph_lengths = [len(_words(p)) for p in paragraphs]
    if len(paragraph_lengths) >= 3:
        mean = sum(paragraph_lengths) / len(paragraph_lengths)
        if mean and max(abs(length - mean) / mean for length in paragraph_lengths) <= 0.15:
            issues.append({
                "code": "uniform_paragraphs",
                "severity": "advisory",
                "word_counts": paragraph_lengths,
                "message": "Review unusually uniform paragraph lengths; retain them when the genre requires regularity.",
            })

    semicolons = prose.count(";")
    semicolon_rate = (semicolons * 1000 / word_count) if word_count else 0.0
    if semicolon_rate > 2:
        issues.append({
            "code": "semicolon_density",
            "severity": "advisory",
            "count": semicolons,
            "per_1000_words": round(semicolon_rate, 2),
            "message": "Review semicolon density above two per 1,000 prose words.",
        })

    return {
        "scope": scope,
        "word_count": word_count,
        "em_dash_count": em_dash_count,
        "em_dash_limit": limit,
        "issue_count": len(issues),
        "issues": issues,
    }


def _render_text(result: dict) -> str:
    status = "PASS" if not result["issues"] else "REVIEW"
    lines = [
        f"{status}: {result['word_count']} words; em dashes {result['em_dash_count']}/{result['em_dash_limit']}; {result['issue_count']} issue(s)."
    ]
    for issue in result["issues"]:
        lines.append(f"- {issue['severity'].upper()} {issue['code']}: {issue['message']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="UTF-8 manuscript path; omit to read stdin")
    parser.add_argument("--scope", choices=("paper", "section", "paragraph"), default="paper")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="Return exit code 1 when an error or warning is found")
    args = parser.parse_args()

    result = inspect(_read_text(args.path), args.scope)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(_render_text(result))
    blocking = any(issue["severity"] in {"error", "warning"} for issue in result["issues"])
    return 1 if args.strict and blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
