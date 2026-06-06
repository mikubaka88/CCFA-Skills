# ICPP Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/icpp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icpp` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/ICPP` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICPP Writing Guide

ICPP (International Conference on Parallel Processing) is a **CCF-B parallel computing conference** (https://cs.uwaterloo.ca/~icpp2026). **ICPP uses double-blind review — papers should be anonymized.** ICPP is one of the premier venues for parallel processing research, covering architectures, algorithms, and systems.

## Document Setup

### Template Files
- Template folder: `ICPP/`
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
\acmConference[ICPP 2026]{International Conference on Parallel Processing}{August 2026}{Calgary, Canada}
\acmISBN{978-X-XXXX-XXXX-X/26/08}
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

- **10 pages** maximum for ICPP 2026 (typical)
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**ICPP uses double-blind review.** Anonymization is mandatory:

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

## Parallel Computing Writing Conventions

### Performance Focus
ICPP papers emphasize performance evaluation:
- Speedup metrics
- Scalability analysis
- Parallel efficiency
- Resource utilization

### Methodology Requirements
- Describe parallel algorithm or approach clearly
- Report baseline comparisons
- Include strong/weak scaling analysis
- Discuss overhead sources

### Platform Details
- CPU/GPU/FPGA specifications
- Memory hierarchy details
- Network topology (for distributed systems)
- Programming model used

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Parallel computing context
4. **Design/Approach** — Parallel algorithm or system
5. **Implementation** — Technical details
6. **Evaluation** — Methodology, results, comparison
7. **Related Work** — Positioning within literature
8. **Conclusion** — Summary
9. **References**
10. **Appendix** — Additional details

## Figure and Table Guidelines

### Performance Figures
- Speedup curves
- Scaling plots (strong/weak)
- Resource utilization charts
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use booktabs style
- Include speedup percentages

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
2. Missing scalability analysis
3. Weak baseline comparisons
4. Insufficient methodology description
5. Exceeding page limit

## Useful Resources

- [ICPP 2026 Author Information](https://cs.uwaterloo.ca/~icpp2026)
- [ACM LaTeX Guidelines](https://www.acm.org/publications/proceedings-template)
- Publisher: ACM
