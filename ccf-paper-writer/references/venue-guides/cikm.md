# CIKM Venue Guide

> Migrated from the legacy `ccf-conference-skills/cikm/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `cikm` |
| Venue family | DB/Mining |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/CIKM/acmart.cls` |
| Official URL | https://www.cikm2026.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CIKM 2026 Conference Writing Skill

**CCF-B | DB/Mining | Publisher: ACM**
**Conference:** https://www.cikm2026.org
**Template:** `CIKM/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\setcopyright{acmcopyright}
\acmConference[CIKM 2026]{CIKM '26: 2026 ACM SIGIR Conference...}
               {October 2026}{Atlanta, GA, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{hyperref}
\hypersetup{colorlinks=true}
```

## Page Limits

|| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

CIKM typically enforces a 10-page limit for the main body. References and appendix do not count toward this limit. Check the official CFP for the current year's exact limits.

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

Standard CIKM paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Related Work** — Positioning against prior work
3. **Background / Preliminaries** — Background and definitions
4. **Method / Approach** — Core technical contribution
5. **Theoretical Analysis** (optional) — Theoretical guarantees
6. **Experiments** — Datasets, metrics, comparison with baselines
7. **Conclusion** — Summary and future work
8. References
9. Appendix (optional)

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/overview}
  \caption{System architecture overview.}
  \label{fig:overview}
\end{figure}
```

- Vector formats (.pdf) preferred
- Ensure grayscale legibility
- Self-contained captions
- Number figures and tables sequentially
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

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 10 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
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
