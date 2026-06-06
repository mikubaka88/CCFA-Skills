# CONCUR Venue Guide

> Migrated from the legacy `ccf-conference-skills/concur/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `concur` |
| Venue family | Concurrency |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/CONCUR/llncs.cls` |
| Official URL | https://concur2026.compute.dela |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CONCUR 2026 Conference Writing Skill

**CCF-B | Concurrency | Publisher: Springer**
**Conference:** https://concur2026.compute.dela
**Template:** `CONCUR/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass[envcountsame]{llncs}

\usepackage{makeidx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{url}
\usepackage{hyperref}
\hypersetup{colorlinks=true}
```

### Springer LNCS Options

| Option | Description |
|--------|-------------|
| `envcountsame` | Number theorem-like environments per section |
| `envcountreset` | Reset theorem counters per section |
| `runningheads` | Short titles in page headers |

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper | **15 pages** |
| References | No specific limit |

CONCUR typically allows 15 pages for the main content. Check the official CFP for the current year's exact limits.

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

\author{First Author\inst{1} \and
        Second Author\inst{2}}

\institute{
  Institution 1\\
  \email{author1@example.com}
  \and
  Institution 2\\
  \email{author2@example.com}
}
```

## Abstract

```latex
\begin{document}
\maketitle

\begin{abstract}
Your abstract here. Summarize the problem, approach, and main results.
\keywords{keyword1, keyword2, keyword3}
\end{abstract}
```

## Section Organization

Standard CONCUR paper structure:

1. **Abstract** — Summary of problem, approach, and results
2. **Introduction** — Problem, motivation, contributions
3. **Preliminaries** — Formal definitions and notation
4. **Background** — Related models and approaches
5. **Main Contribution** — Core technical contribution
6. **Technical Results** — Theorems and proofs
7. **Related Work** — Comparison with prior work
8. **Conclusion** — Summary and future work
9. References

## Theorem Environments

CONCUR papers emphasize formal proofs:

```latex
\theoremstyle{plain}
\newtheorem{observation}{Observation}
\newtheorem{property}{Property}
\newtheorem{invariant}{Invariant}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem*{proposition}{Proposition}
\newtheorem*{claim}{Claim}

\theoremstyle{Proof}
\newtheorem{Proof}{Proof}
```

## Process Algebra Notation

CONCUR papers often use process algebra notation:

```latex
% Examples of process expressions:
% P := a.0 | Q := b.(P || R)
% Bisimulation: P \sim Q
```

Use standard process algebra operators:
- Prefix: $a.P$
- Choice: $P + Q$
- Parallel: $P \mid Q$ or $P \parallel Q$
- Restriction: $P \backslash L$
- Recursion: $A \stackrel{\text{def}}{=} P$

## Figures and Tables

```latex
\begin{figure}[t]
\centering
includegraphics[width=0.8\linewidth]{fig/lts}
\caption{Labeled transition system.}
\label{fig:lts}
\end{figure}
```

- Use PDF, PNG, or EPS
- Ensure grayscale legibility
- Self-contained captions
- Use `booktabs` for tables (no vertical rules)

## References (natbib)

```latex
\bibliographystyle{spbasic}  % Springer basic style
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

## Formatting Rules

- **Format:** Two-column, single-spaced
- **Paper size:** A4
- **Body font:** 10pt
- **Margins:** 2.5cm all around

## Submission Checklist

- [ ] 15 pages or fewer (main body)
- [ ] Springer LNCS llncs document class
- [ ] Abstract and keywords included
- [ ] All figures in .pdf/.png/.eps format
- [ ] References in correct format
- [ ] Compiles with `pdflatex`
