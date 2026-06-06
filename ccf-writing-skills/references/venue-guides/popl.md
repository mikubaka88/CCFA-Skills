# POPL Venue Guide

> Migrated from the legacy `ccf-conference-skills/popl/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `popl` |
| Venue family | SE/PL |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/POPL/acmart.cls` |
| Official URL | https://dl.acm.org/conference/popl |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# POPL Conference Writing Skill

**CCF-A | SE/PL | Publisher: ACM**
**Conference:** https://dl.acm.org/conference/popl
**Template:** `POPL/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{acmlicensed}
\acmConference[POPL 2026]{Proceedings of the 43rd ACM SIGPLAN Symposium on
  Principles of Programming Languages}{January 20--22, 2026}{Denver, CO, USA}
\acmISBN{978-X-XXXX-XXXX-X/26/01}
\acmDOI{10.1145/XXXXXXX}
\acmPrice{}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{mathpartir}        % For inference rules and semantics
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

POPL enforces a strict 12-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

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

Standard POPL paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background** — Technical context, existing work
3. **Language/Formalism** — Core definitions, syntax, semantics
4. **Technical Development** — Proofs, metatheory, type systems, etc.
5. **Implementation/Applications** — Practical aspects if applicable
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future work
8. References

## Theorem Environments

POPL papers rely heavily on formal definitions and proofs:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{proposition}{Proposition}
\newtheorem*{corollary}{Corollary}

\theoremstyle{definition}
\newtheorem{example}{Example}

\theoremstyle{note}
\newtheorem*{remark}{Remark}
```

Use `\qed` (from amsthm) to close proofs. Use `\qedhere` when the proof ends with a displayed equation.

## Formal Semantics

POPL papers typically include formal semantics using mathpartir or similar:

```latex
\usepackage{mathpartir}

% Inference rules:
\infersection{Soundness}
\inferrule{
  \Gamma \vdash e : \tau \\
  \tau <: \tau'
}{
  \Gamma \vdash e : \tau'
}

% Typing rules:
\Judgment{$e$}{$e'$}{$v$}
  {Step}{$e \step e'$}
  {Value}{$v$ is a value}
```

## References (natbib)

ACM-Reference-Format bibstyle with author-year citations:

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

% Citations:
\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}     % (Smith et al. 2023)
```

Each reference must list **all authors** — do not use "et al." in the bibliography.

## Figures and Tables

- Use vector formats (.pdf, .eps) where possible
- Ensure figures are legible in grayscale
- Number figures and tables sequentially
- Captions should be descriptive and self-contained
- Keep figures simple when possible — clarity over decoration

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
