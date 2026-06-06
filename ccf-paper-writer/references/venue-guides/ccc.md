# CCC Venue Guide

> Migrated from the legacy `ccf-conference-skills/ccc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ccc` |
| Venue family | Complexity |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/CCC/IEEEtran.cls` |
| Official URL | https://computationalcomplexity.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CCC 2026 Conference Writing Skill

**CCF-B | Complexity | Publisher: IEEE**
**Conference:** https://computationalcomplexity.org
**Template:** `CCC/IEEEtran.cls` (IEEEtran conference format)

## Document Setup

### Preamble Structure

```latex
\documentclass[conference]{IEEEtran}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{hyperref}
\hypersetup{colorlinks=true}
```

### Conference Mode

Always use `conference` document class option for CCC submissions.

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper | **12 pages** |
| References | Unlimited |

CCC typically enforces a 12-page limit. Check the official CFP for the current year's exact limits.

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

\author{\IEEEauthorblockN{First Author}
\IEEEauthorblockA{Department\\
Institution\\
City, Country\\
email@example.com}
\and
\IEEEauthorblockN{Second Author}
\IEEEauthorblockA{Department\\
Institution\\
City, Country\\
email2@example.com}}
```

## Abstract

```latex
\begin{document}
\maketitle

\begin{abstract}
Your abstract here. Summarize the problem, approach, and main results.
\end{abstract}

\begin{IEEEkeywords}
keyword1, keyword2, keyword3
\end{IEEEkeywords}
```

## Section Organization

Standard CCC paper structure:

1. **Abstract** — Summary of problem and results
2. **Introduction** — Problem, motivation, contributions
3. **Preliminaries** — Complexity classes and definitions
4. **Main Results** — Core contributions
5. **Proofs** — Detailed proofs of theorems
6. **Related Work** — Comparison with prior complexity results
7. References

## Theorem Environments

CCC papers emphasize formal complexity proofs:

```latex
\theoremstyle{plain}
\newtheorem{conjecture}{Conjecture}
\newtheorem{question}{Question}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem*{claim}{Claim}

\theoremstyle{Proof}
\newtheorem{Proof}{Proof}
```

## Figures and Tables

```latex
\begin{figure}[t]
\centering
includegraphics[width=0.9\linewidth]{fig/reduction}
\caption{Reduction diagram.}
\label{fig:reduction}
\end{figure}
```

- Use vector formats (.pdf, .eps) preferred
- Ensure grayscale legibility
- Self-contained captions

## References (IEEEtran)

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

\cite{smith2023}      % [1]
```

IEEEtran uses numeric citations by default.

## Complexity-Specific Conventions

- Clearly state complexity classes involved (P, NP, BPP, PSPACE, etc.)
- Include formal reductions when proving hardness
- State assumptions explicitly (e.g., "assuming P ≠ NP")
- Use standard complexity notation and terminology
- Include comparisons with known separation results

## Formatting Rules

- **Format:** Two-column, single-spaced
- **Paper size:** US Letter
- **Body font:** 10pt
- **Margins:** 1 inch all around

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] IEEEtran conference document class
- [ ] Abstract and keywords included
- [ ] All figures in .pdf/.eps format
- [ ] References in IEEE format
- [ ] Complexity classes properly defined
- [ ] Compiles with `pdflatex`
