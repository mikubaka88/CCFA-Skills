# SIGMETRICS Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/sigmetrics/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `sigmetrics` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/SIGMETRICS` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SIGMETRICS Writing Guide

SIGMETRICS (Conference on Measurement and Modeling of Computer Systems) is a **CCF-B performance evaluation conference** (https://sigmetrics.org/sigmetrics2026). **SIGMETRICS uses double-blind review — papers should be anonymized.** SIGMETRICS is the premier venue for analytical and experimental performance evaluation research.

## Document Setup

### Template Files
- Template folder: `SIGMETRICS/`
- Document class: ACM `acmart` with sigconf format
- Style files from ACM distribution

### Required LaTeX Structure

**For Submission (ANONYMOUS):**
```latex
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% Optional packages
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{natbib}

\begin{document}

% Anonymized title
\title{Your Paper Title}

% Anonymized abstract
\begin{abstract}
Your abstract here — summarize contribution and key results.
\end{abstract}

% Remove identifying information
\setcopyright{}

% Main content
\section{Introduction}
...

% Bibliography: ACM style
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
```

**For Camera-Ready:**
```latex
\documentclass[sigconf]{acmart}
\settopmatter{printfolios=true}
\setcopyright{acmcopyright}
\acmConference[SIGMETRICS 2026]{ACM SIGMETRICS}{June 2026}{Philadelphia, PA, USA}
\acmISBN{978-X-XXXX-XXXX-X/26/06}
\acmDOI{10.1145/XXXXXXX.XXXXXXX}

% Include author information
\title{Your Paper Title}
\author{Author Name}
\affiliation{...}
\email{...}

\begin{document}
...
\end{document}
```

### Key Formatting Requirements
- **Document class**: `acmart` with `[sigconf]` option
- **Review mode**: `[sigconf,review,anonymous]` for submission
- **Layout**: Two-column (ACM SIGCONF format)
- **Double-blind**: All identifying information must be removed

## Page Limits

- **12 pages** maximum for SIGMETRICS 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**SIGMETRICS uses double-blind review.** Anonymization is mandatory:

### Required Anonymization
1. Remove author names from submission
2. Use third-person voice ("Smith et al. showed" not "we showed")
3. Remove acknowledgments section
4. Exclude funding acknowledgments
5. Anonymize URLs and links to author-specific content
6. Avoid self-citations that reveal identity

### Permitted
- Citation of own prior work (without breaking anonymity)
- Anonymized code repositories
- Technical appendices

## Performance Evaluation Writing Conventions

### Measurement and Modeling Focus
SIGMETRICS papers focus on:
- Performance measurement methodologies
- Analytical modeling
- Queueing theory
- Workload characterization

### Methodology Requirements
- Describe evaluation methodology clearly
- Report both analytical and experimental results
- Include sensitivity analysis
- Discuss limitations and assumptions

### Evaluation Best Practices
- Use real workloads or traces
- Report confidence intervals
- Include comparison with baselines
- Discuss statistical significance

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Performance evaluation context
4. **Model/Method** — Theoretical framework or methodology
5. **Validation/Evaluation** — Experimental results
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**
9. **Appendix** — Additional details

## Figure and Table Guidelines

### Performance Evaluation Figures
- Throughput/latency curves
- Queueing model diagrams
- CDF/ECDF plots
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use booktabs style
- Include confidence intervals

## Reference Format

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}
```

- ACM citation format
- Full author names (except self-citations)
- Complete conference/proceedings names

## Camera-Ready Preparation

1. Switch to non-anonymous mode
2. Add author names and affiliations
3. Include acknowledgments
4. Add copyright notice with DOI
5. Add ISBN metadata
6. Verify page limit compliance
7. Submit through conference system

## Common Mistakes to Avoid

1. **Breaching anonymity** (author identity revealed)
2. Missing confidence intervals
3. Weak methodology description
4. Cherry-picking workloads
5. Insufficient baseline comparison
6. Exceeding 12-page limit

## Useful Resources

- [SIGMETRICS 2026 Author Information](https://sigmetrics.org/sigmetrics2026)
- [ACM LaTeX Guidelines](https://www.acm.org/publications/proceedings-template)
- Publisher: ACM
