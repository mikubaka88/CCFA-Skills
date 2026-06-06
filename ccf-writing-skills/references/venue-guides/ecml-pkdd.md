# ECML PKDD Venue Guide

> Migrated from the legacy `ccf-conference-skills/ecml-pkdd/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ecml-pkdd` |
| Venue family | ML/DB |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ECML-PKDD/llncs.cls` |
| Official URL | https://ecmlpkdd.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ECML PKDD 2026 Conference Writing Skill

**CCF-B | ML/DB | Publisher: Springer**
**Conference:** https://ecmlpkdd.org/2026
**Template:** `ECML-PKDD/llncs.cls` (Springer LNCS)

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
\usepackage{natbib}
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
| Main paper | **14 pages** |
| References | No specific limit |

ECML PKDD typically allows 14 pages for the main content. Check the official CFP for the current year's exact limits, as limits may differ between research papers and applied data science papers.

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

Standard ECML PKDD paper structure:

1. **Abstract** — Summary of problem, approach, and results
2. **Introduction** — Problem, motivation, contributions (enumerate)
3. **Background and Notation** — ML background and definitions
4. **Proposed Method** — Core contribution with formal treatment
5. **Theoretical Analysis** (optional) — Theoretical guarantees
6. **Experimental Evaluation** — Datasets, baselines, results, analysis
7. **Related Work** — Comparison with prior ML/KDD work
8. **Conclusion** — Summary and future directions
9. References

## Figures and Tables

```latex
\begin{figure}[t]
\centering
includegraphics[width=0.8\linewidth]{fig/model}
\caption{Proposed model architecture.}
\label{fig:model}
\end{figure}
```

- Use PDF, PNG, or EPS
- Ensure grayscale legibility
- Self-contained captions
- Number figures and tables sequentially
- Use `booktabs` for tables (no vertical rules)

## References (natbib)

```latex
\bibliographystyle{spbasic}  % Springer basic style
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

## ML-Specific Writing Conventions

- Clearly state research questions and hypotheses
- Report standard ML metrics (accuracy, F1, AUC, RMSE, etc.)
- Include confidence intervals or statistical significance tests
- Describe datasets: source, size, preprocessing, train/test split
- Include ablation studies when applicable
- Address reproducibility (code, hyperparameters, random seeds)

## Formatting Rules

- **Format:** Two-column, single-spaced
- **Paper size:** A4
- **Body font:** 10pt
- **Margins:** 2.5cm all around

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] Springer LNCS llncs document class
- [ ] Abstract and keywords included
- [ ] All figures in .pdf/.png/.eps format
- [ ] References in correct format
- [ ] Compiles with `pdflatex`
- [ ] ML metrics reported with statistical significance
