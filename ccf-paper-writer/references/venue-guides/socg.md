# SoCG Venue Guide

> Migrated from the legacy `ccf-conference-skills/socg/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `socg` |
| Venue family | Theory/Geometry |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/SoCG/socg-lipics-v2021.cls` |
| Official URL | https://socg.compute.dgeo.de |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SoCG 2026 Conference Writing Skill

**CCF-B | Theory/Geometry | Publisher: LIPIcs**
**Conference:** https://socg.compute.dgeo.de
**Template:** `SoCG/socg-lipics-v2021.cls` (LIPIcs-based)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous) ===
\documentclass[anonymous]{socg-lipics-v2021}

% === CAMERA-READY MODE ===
\documentclass{socg-lipics-v2021}
```

### Class Options

| Option | Description |
|--------|-------------|
| `anonymous` | Hide author info for submission |
| `nolineno` | Disable line numbering |
| `noalgorithm2e` | Don't patch algorithm2e |
| `noalgorithms` | Don't patch algorithm/algorithmic |
| `nosubfigcap` | Don't patch subcaptions |
| `notab` | Don't patch tabular |

### Required Packages

```latex
\usepackage{mathtools}
\usepackage{amsmath, amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{algorithm2e}  % For pseudocode
```

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper | **12 pages** |
| References | Separate |

SoCG enforces a strict 12-page limit for the main paper. References are separate and unlimited.

## Anonymity Requirements

Use `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs
4. Use "Anonymous Submission" as author block

## Camera-Ready Differences

After acceptance:

1. Remove `anonymous` option
2. Fill in full author and affiliation information
3. The LIPIcs DOI will be assigned by the publisher

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

\author{First Author}{Institution}{\email{author1@example.com}}
\author{Second Author}{Institution}{\email{author2@example.com}}

\authorsaddresses{...}

\titlecomment{Subtitle or talk context (optional)}
```

## Section Organization

Standard SoCG paper structure:

1. **Abstract** — Concise summary
2. **Introduction** — Problem, motivation, contributions
3. **Preliminaries** — Geometric definitions and notation
4. **Main Results** — Core technical contribution
5. **Upper/Lower Bounds** — Algorithmic results or hardness
6. **Proofs** — Formal proofs of theorems
7. **Related Work** — Comparison with prior geometry work
8. References

## Theorem Environments

SoCG papers emphasize formal proofs:

```latex
\theoremstyle{plain}
\newtheorem{observation}{Observation}
\newtheorem{invariant}{Invariant}
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
\begin{figure}
\centering
\begin{picture}(300,150)
% Draw geometric figure using LaTeX picture commands
\end{picture}
\caption{Example illustrating the algorithm.}
\label{fig:example}
\end{figure}
```

- Use LaTeX picture/tikz for geometric figures when possible
- Vector formats preferred
- Self-contained captions with line numbers
- Ensure clarity at publication scale

## References

SoCG uses standard author-year citations. Check the style file for the bibliography style.

```latex
\bibliographystyle{...}
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

## Formatting Rules

- **Format:** Single-column (LIPIcs style)
- **Paper size:** A4
- **Body font:** 10pt
- **Margins:** Standard LIPIcs margins
- **Line numbering:** Enabled by default (can disable with `nolineno`)

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[anonymous]{socg-lipics-v2021}`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Geometric figures clear and readable
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Remove `anonymous` option
- [ ] Add complete author information
- [ ] Verify page count
- [ ] Check figure quality
