# PLDI Venue Guide

> Migrated from the legacy `ccf-conference-skills/pldi/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `pldi` |
| Venue family | SE/PL |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/PLDI/acmart.cls` |
| Official URL | https://dl.acm.org/conference/pldi |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# PLDI Conference Writing Skill

**CCF-A | SE/PL | Publisher: ACM**
**Conference:** https://dl.acm.org/conference/pldi
**Template:** `PLDI/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{acmlicensed}
\acmConference[PLDI 2026]{Proceedings of the 47th ACM SIGPLAN Symposium on
  Programming Language Design and Implementation}{June 14--18, 2026}{Seattle, WA, USA}
\acmISBN{978-X-XXXX-XXXX-X/26/06}
\acmDOI{10.1145/XXXXXXX}
\acmPrice{}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

PLDI enforces a strict 12-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix. No appendix may appear in the submission.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. Do not include author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize URLs (e.g., GitHub repositories)
4. Remove PDF metadata that reveals authorship
5. Do not include acknowledgments

## Camera-Ready Differences

When preparing camera-ready after acceptance:

1. Remove `review` and `anonymous` options from `\documentclass`
2. Add `\setcopyright{acmlicensed}` or appropriate rights mode
3. Fill in `\acmConference` with full conference title and dates
4. Add `\acmISBN`, `\acmDOI`, and `\acmPrice` fields
5. Restore all author names and affiliations
6. Add acknowledgments if desired

## Section Organization

Standard PLDI paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background & Motivation** — Context and why the problem matters
3. **Design/Approach** — Core technical contribution
4. **Implementation** — System details, complexity, design decisions
5. **Evaluation** — Experimental methodology, results, comparisons
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future work
8. References

## Theorem Environments

PLDI papers commonly use formal reasoning environments:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}      % unnumbered for main theorems
\newtheorem*{lemma}{Lemma}

\theoremstyle{plain}
\newtheorem*{corollary}{Corollary}

\theoremstyle{plain}
\newtheorem*{invariant}{Invariant}
```

Use `\qed` (from amsthm) to close proofs.

## Code Listings

Use `lstinline{}` for inline code and `lstlisting` for blocks:

```latex
% Inline code:
The compiler uses \lstinline!spin_lock_irqsave()! to protect the shared queue.

% Code blocks:
\begin{lstlisting}[caption={Ring buffer implementation}, label={lst:ringbuf}]
struct ring_buffer {
    void **entries;
    size_t head, tail;
    size_t capacity;
};
\end{lstlisting}
```

Configure with `\lstset{basicstyle=\small\ttfamily}` in preamble.

## Figures and Tables

- Use vector formats (.pdf, .eps) where possible
- Ensure figures are legible in grayscale (reviewers often print in B&W)
- Number figures and tables sequentially
- Captions should be descriptive and self-contained
- Place tables near their first reference

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/design-overview}
  \caption{System architecture overview showing the interaction
    between the scheduler and worker threads.}
  \label{fig:overview}
\end{figure}
```

## References (natbib)

ACM-Reference-Format bibstyle with author-year citations:

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

% Citations:
\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

Each reference must list **all authors** — do not use "et al." in the bibliography.

## Formatting Rules

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, no page limit
- **Line spacing:** Single-spaced (template default)

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[sigplan,review,anonymous]`
- [ ] All author/anonymization info removed
- [ ] No self-identifying URLs or citations
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add `\setcopyright{acmlicensed}` (or appropriate)
- [ ] Fill `\acmConference`, `\acmISBN`, `\acmDOI`, `\acmPrice`
- [ ] Restore author names and affiliations
- [ ] Include page numbers (`\settopmatter{printfolios=true}`)
