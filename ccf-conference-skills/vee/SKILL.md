---
name: vee
description: Writing and formatting guidance for VEE (ACM SIGPLAN/SIGOPS International Conference on Virtual Execution Environments) papers. Use when drafting, formatting, or submitting to VEE 2026. Covers ACM acmart sigplan format with anonymous review mode, virtualization-specific conventions, 12-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# VEE Writing Guide

VEE (International Conference on Virtual Execution Environments) is a **CCF-B virtualization and systems conference** (https://conf.researchr.org/track/vee-2026/vee-2026-papers). **VEE uses double-blind review — papers should be anonymized.** VEE is a premier venue for virtualization, system software, and execution environment research.

## Document Setup

### Template Files
- Template folder: `VEE/`
- Document class: ACM `acmart` with sigplan format
- Style files from ACM distribution

### Required LaTeX Structure

**For Submission (ANONYMOUS):**
```latex
\documentclass[sigplan,review,anonymous]{acmart}
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
\documentclass[sigplan]{acmart}
\settopmatter{printfolios=true}
\setcopyright{acmcopyright}
\acmConference[VEE 2026]{International Conference on Virtual Execution Environments}{April 2026}{Toronto, Canada}
\acmISBN{978-X-XXXX-XXXX-X/26/04}
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
- **Document class**: `acmart` with `[sigplan]` option
- **Review mode**: `[sigplan,review,anonymous]` for submission
- **Layout**: Two-column (ACM SIGPLAN format)
- **Double-blind**: All identifying information must be removed

## Page Limits

- **12 pages** maximum for VEE 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**VEE uses double-blind review.** Anonymization is mandatory:

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

## Virtualization Writing Conventions

### System Software Focus
VEE papers focus on virtualization and execution environments:
- Virtual machine monitors
- Operating system design
- Runtime environments
- System-level optimizations

### Implementation Requirements
- Describe system architecture clearly
- Include implementation details (lines of code, platforms used)
- Report real performance metrics
- Compare against existing systems

### Evaluation Best Practices
- Use real workloads or representative benchmarks
- Report both performance and overhead metrics
- Include sensitivity analysis
- Discuss limitations and trade-offs

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Virtualization context
4. **Design/Approach** — System architecture and design decisions
5. **Implementation** — Technical details, challenges
6. **Evaluation** — Methodology, results, comparison
7. **Related Work** — Positioning within literature
8. **Discussion/Limitations** — Scope, applicability
9. **Conclusion** — Summary
10. **References**
11. **Appendix** — Additional details

## Figure and Table Guidelines

### System Figures
- Architecture diagrams
- Data flow diagrams
- Performance comparison charts
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use booktabs style
- Include standard deviations where applicable

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
2. Missing system design rationale
3. Weak evaluation methodology
4. Cherry-picking workloads
5. Insufficient baseline comparison
6. Exceeding 12-page limit

## Useful Resources

- [VEE 2026 Author Information](https://conf.researchr.org/track/vee-2026/vee-2026-papers)
- [ACM LaTeX Guidelines](https://www.acm.org/publications/proceedings-template)
- Publisher: ACM
