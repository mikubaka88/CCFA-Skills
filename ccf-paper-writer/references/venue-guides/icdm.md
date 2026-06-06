# ICDM Venue Guide

> Migrated from the legacy `ccf-conference-skills/icdm/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icdm` |
| Venue family | Data Mining |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ICDM/IEEEtran.cls` |
| Official URL | https://icdm.e宏观.us/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICDM 2026 Conference Writing Skill

**CCF-B | Data Mining | Publisher: IEEE**
**Conference:** https://icdm.e宏观.us/2026
**Template:** `ICDM/IEEEtran.cls` (IEEEtran conference format)

## Document Setup

### Preamble Structure

```latex
\documentclass[conference]{IEEEtran}

\usepackage{IEEEraft}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{hyperref}
\hypersetup{colorlinks=true}
```

### Conference Mode

Always use `conference` document class option for ICDM submissions.

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper | **10 pages** |
| References | Unlimited |

ICDМ typically enforces a 10-page limit. Check the official CFP for the current year's exact limits.

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
Your abstract here. Summarize the problem, approach, and main results in 150-250 words.
\end{abstract}

\begin{IEEEkeywords}
keyword1, keyword2, keyword3
\end{IEEEkeywords}
```

## Section Organization

Standard ICDM paper structure:

1. **Abstract** — Summary of problem, approach, and results
2. **Introduction** — Problem, motivation, contributions (enumerate)
3. **Preliminaries** — Background and definitions
4. **Proposed Method** — Core contribution
5. **Theoretical Analysis** (optional) — Theoretical guarantees
6. **Experimental Evaluation** — Datasets, baselines, results
7. **Related Work** — Comparison with prior work
8. **Conclusion** — Summary and future work
9. References

## Figures and Tables

```latex
\begin{figure}[t]
\centering
includegraphics[width=0.9\linewidth]{fig/model}
\caption{Proposed model architecture.}
\label{fig:model}
\end{figure}
```

- Use vector formats (.pdf, .eps) preferred
- Ensure grayscale legibility
- Captions centered, below figures
- Number figures and tables sequentially

## References (IEEEtran)

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

\cite{smith2023}      % [1]
```

IEEEtran uses numeric citations by default.

## Theorem Environments

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}

\theoremstyle{Proof}
\newtheorem{Proof}{Proof}
```

## Formatting Rules

- **Format:** Two-column, single-spaced
- **Paper size:** US Letter
- **Body font:** 10pt
- **Margins:** 1 inch all around

## Submission Checklist

- [ ] 10 pages or fewer (main body)
- [ ] IEEEtran conference document class
- [ ] Abstract and keywords included
- [ ] All figures in .pdf/.eps format
- [ ] References in IEEE format
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Verify page count
- [ ] Add author photos (if required)
- [ ] Complete copyright notice (IEEE will add)
- [ ] Final PDF compilation
