# PODS Venue Guide

> Migrated from the legacy `ccf-conference-skills/pods/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `pods` |
| Venue family | DB |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/PODS/acmart.cls` |
| Official URL | https://sigmod.org/pods2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# PODS 2026 Conference Writing Skill

**CCF-B | DB | Publisher: ACM**
**Conference:** https://sigmod.org/pods2026
**Template:** `PODS/acmart.cls` (ACM acmart, sigplan format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{acmcopyright}
\acmConference[PODS 2026]{PODS '26: 2026 ACM SIGMOD Conference...}
               {June 2026}{Chicago, IL, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}
\usepackage{graphicx}
```

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

PODS typically enforces a 12-page limit for the main body. References and appendix do not count toward this limit. Check the official CFP for the current year's exact limits.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, personal pages
4. Clear PDF metadata
5. Remove acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Add appropriate `\setcopyright` mode
3. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
4. Restore all author names and affiliations
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

PODS papers typically follow database theory structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Preliminaries** — Formal definitions and notation
3. **Problem Definition** — Formal statement of the problem
4. **Upper Bounds** — Algorithms and positive results
5. **Lower Bounds** — Hardness results and separations
6. **Related Work** — Comparison with prior theoretical results
7. **Conclusion** — Summary and open problems
8. References
9. Appendix (optional) — Omitted proofs

## Theorem Environments

PODS papers emphasize formal theory with theorem environments:

```latex
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}
\newtheorem*{theorem*}{Theorem}      % unnumbered
\newtheorem{lemmma}{Lemma}
\newtheorem{property}{Property}
\newtheorem{claim}{Claim}

\theoremstyle{definition}
\newtheorem{definition}{Definition}
\newtheorem{example}{Example}

\theoremstyle{Proof}
\newtheorem{Proof}{Proof}
```

Use `\qed` or `\qedhere` from amsthm to close proofs.

## Sub-subsections

PODS uses `\paragraph{}` for sub-subsections:

```latex
\section{Upper Bounds}
\subsection{Algorithmic Framework}
paragraph{Data Structures}  % This is a sub-subsection
The main data structure used is a...
```

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/example}
  \caption{Example illustrating the query semantics.}
  \label{fig:example}
\end{figure}
```

- Vector formats (.pdf) preferred
- Ensure grayscale legibility
- Self-contained captions
- Use `booktabs` for tables (no vertical rules)

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[sigplan, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] References list all authors
- [ ] Grayscale-legible figures
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add `\setcopyright{acmcopyright}` (or appropriate)
- [ ] Fill `\acmConference`, `\acmISBN`, `\acmDOI`
- [ ] Restore author names and affiliations
- [ ] Enable page numbers
