# ICS Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/ics/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ics` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/ICS` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICS Writing Guide

ICS (International Conference on Supercomputing) is a **CCF-B supercomputing conference** (https://ics2026.github.io). **ICS uses double-blind review — papers should be anonymized.** ICS is a top venue for high-performance computing and supercomputing research.

## Document Setup

### Template Files
- Template folder: `ICS/`
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
\acmConference[ICS 2026]{International Conference on Supercomputing}{June 2026}{Chicago, IL, USA}
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

- **12 pages** maximum for ICS 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**ICS uses double-blind review.** Anonymization is mandatory:

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

## Supercomputing Writing Conventions

### HPC Focus
ICS papers focus on high-performance computing:
- Supercomputer-scale performance
- Novel algorithms or optimizations
- Hardware-software co-design
- Real-world HPC applications

### Performance Evaluation
- Strong/weak scaling studies
- Performance comparison with state-of-the-art
- Resource utilization analysis
- Roofline analysis where applicable

### Platform Details
- Machine specifications (cores, memory, network)
- Programming models (MPI, OpenMP, CUDA, etc.)
- Benchmark suites used
- Measurement methodology

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — HPC context, related approaches
4. **Design/Approach** — Technical contribution
5. **Implementation** — System/algorithm details
6. **Evaluation** — Methodology, results, comparison
7. **Related Work** — Positioning within literature
8. **Conclusion** — Summary
9. **References**
10. **Appendix** — Additional details

## Figure and Table Guidelines

### HPC Performance Figures
- Performance scaling plots
- Comparison bar charts
- Heat maps for data movement
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use booktabs style
- Include performance metrics

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
2. Missing scaling analysis
3. Weak baseline comparisons
4. Insufficient methodology description
5. Exceeding 12-page limit

## Useful Resources

- [ICS 2026 Author Information](https://ics2026.github.io)
- [ACM LaTeX Guidelines](https://www.acm.org/publications/proceedings-template)
- Publisher: ACM
