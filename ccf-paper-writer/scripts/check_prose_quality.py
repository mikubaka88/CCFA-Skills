#!/usr/bin/env python3
"""Locate defensive and mechanical prose for context-aware humanization.

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
DEFENSIVE_PATTERNS = {
    "imagined_reviewer": r"\b(?:to\s+)?(?:address|avoid|preempt|pre-empt|anticipate)\s+(?:any\s+|potential\s+|possible\s+)?reviewer(?:s['’]?)?\s+(?:concerns?|criticism|objections?|questions?)\b|(?:为(?:了)?避免|为回应|为打消|考虑到)审稿人[^。！？\n]{0,24}(?:质疑|担忧|顾虑)",
    "apologetic_framing": r"\bwe\s+(?:merely|only)\s+(?:offer|propose|provide)\b|\b(?:merely|just)\s+(?:a\s+)?(?:simple|incremental|minor)\s+(?:extension|improvement|modification)\b|(?:尽管|虽然)[^。！？\n]{0,30}(?:只是|仅仅是)(?:一个)?(?:简单|微小|增量)",
    "denial_led_scope": r"\bwe\s+(?:do not|don't)\s+(?:claim|intend|aim|seek)\s+to\b|\b(?:our|the)\s+(?:goal|aim|intention)\s+is\s+not\s+to\b|我们(?:并不|并非|不)(?:试图|旨在|声称)",
    "generic_disclaimer": r"\b(?:not\s+without\s+(?:its\s+)?limitations|as\s+with\s+any\s+(?:method|model|approach)|cannot\s+guarantee\s+(?:universal|general|all)|do\s+not\s+guarantee\s+universal)\b|(?:并非没有局限|任何方法都有局限|不能保证[^。！？\n]{0,25}(?:所有|任何|普遍)|不保证[^。！？\n]{0,25}(?:所有|普遍))",
    "empty_assurance": r"\b(?:to\s+ensure|we\s+(?:carefully\s+)?ensure)\s+(?:the\s+|a\s+)?(?:fair(?:ness)?\s+and\s+rigor(?:ous)?|rigor(?:ous)?\s+and\s+fair(?:ness)?)\b|\bto\s+avoid\s+(?:any\s+|possible\s+)?misunderstanding\b|(?:为确保|为了保证)(?:论文|研究|实验|评估)的?(?:严谨性|科学性)|为避免(?:可能的)?误解",
    "stacked_hedging": r"\b(?:may|might|could)\s+(?:potentially|possibly|perhaps)\b|\b(?:seems?|appears?)\s+to\s+(?:potentially|possibly)\b|(?:或许可能|可能潜在地|似乎可能表明)",
    "engineering_status": r"\b(?:confirmed\s+(?:full\s+)?(?:version|method|configuration|baseline)|approved\s+configuration|publication-ready\s+(?:method|version|configuration))\b|(?:经过确认的完整版本|已批准的配置|通过内部(?:门禁|检查)的(?:方法|版本))",
}


def _read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8-sig")
    return sys.stdin.read()


def _prose_only(text: str) -> str:
    # Preserve offsets and newlines so every diagnostic points into the source.
    # Code, equations, comments, table structure and direct quotations are not
    # authored narrative. This is a heuristic filter, not a complete TeX parser.
    patterns = (
        r"```.*?```|~~~.*?~~~",
        r"`[^`\n]+`",
        r"\\begin\{(?P<env>verbatim|lstlisting|minted|equation\*?|align\*?|quote|quotation)\}.*?\\end\{(?P=env)\}",
        r"(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$[^$\n]*(?<!\\)\$",
        r"\\\[.*?\\\]|\\\(.*?\\\)",
        r"(?m)(?<![\\\d])%[^\n]*",
        r"(?m)^[ \t]*\|[^\n]*\|[ \t]*$",
        r"<[^>]+>",
        r"(?m)^[ \t]*(?:---+|___+|\*\*\*+)[ \t]*$",
        r"(?m)^[ \t]*>[^\n]*$",
        r'“[^”]*”|"[^"\n]*"|‘[^’]*’',
    )
    for pattern in patterns:
        text = re.sub(pattern, lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)
    return text


def _words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*|[\u4e00-\u9fff]", text)


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|(?<=[。！？])\s*", text) if len(_words(s)) >= 3]


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

    for pattern in [*OPENING_FILLER, r"需要(?:强调|指出|说明)的是|值得(?:注意|强调|一提)的是"]:
        for match in re.finditer(pattern, prose, flags=re.I):
            issues.append({
                "code": "opening_filler",
                "severity": "warning",
                "line": _line_number(prose, match.start()),
                "text": match.group(0),
                "message": "Delete the throat-clearing opener if the following clause stands directly.",
            })

    for category, pattern in DEFENSIVE_PATTERNS.items():
        for match in re.finditer(pattern, prose, flags=re.I):
            issues.append({
                "code": "defensive_framing",
                "severity": "warning",
                "pattern": category,
                "line": _line_number(prose, match.start()),
                "text": match.group(0),
                "message": "State the supported scientific payload directly or delete empty self-defense; preserve material facts, meaningful uncertainty, and required disclosures.",
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
        location = f" line {issue['line']}" if "line" in issue else ""
        excerpt = f" [{issue['text']}]" if "text" in issue else ""
        pattern = f"/{issue['pattern']}" if "pattern" in issue else ""
        lines.append(f"- {issue['severity'].upper()} {issue['code']}{pattern}{location}{excerpt}: {issue['message']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="UTF-8 manuscript path; omit to read stdin")
    parser.add_argument("--scope", choices=("paper", "section", "paragraph"), default="paper")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="Return 1 for error/warning candidates; matches still require contextual judgment")
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
