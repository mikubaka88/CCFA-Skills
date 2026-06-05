---
name: socc
description: Writing and formatting guidance for SoCC (ACM Symposium on Cloud Computing) papers. Use when drafting, formatting, or submitting to SoCC 2026. Covers ACM acmart sigconf format with anonymous review mode, cloud computing-specific conventions, 14-page limit, and camera-ready preparation with DOI/ISBN metadata.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# SoCC Writing Guide

SoCC (ACM Symposium on Cloud Computing) is a **CCF-B cloud systems conference** (https://acmsocc.org/socc26). **SoCC is double-blind — papers must be anonymized.** SoCC brings together researchers working on cloud computing, distributed systems, and datacenter-scale computing.

## Document Setup

### Template Files
- Template folder: `SoCC/`
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
\acmConference[SoCC'26]{ACM Symposium on Cloud Computing}{September 2026}{Seattle, WA, USA}
\acmISBN{978-X-XXXX-XXXX-X/26/09}
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

- **14 pages** maximum for SoCC 2026 main paper
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**SoCC IS double-blind.** Anonymization is mandatory:

### Required Anonymization
1. Remove author names from submission
2. Use third-person voice ("Smith et al. showed" not "we showed")
3. Remove acknowledgments section
4. Exclude funding acknowledgments
5. Anonymize URLs and links to author-specific content
6. Avoid self-citations that reveal identity
7. Do not post submissions with author names

### Permitted
- Citation of own prior work (without breaking anonymity)
- Anonymized code repositories
- Technical appendices

## Cloud Computing Writing Conventions

### System Focus
SoCC papers typically describe real systems and cloud infrastructure:
- Production deployment experience
- Scalability and performance evaluation
- Operational insights and lessons learned
- Real-world workload analysis

### Methodology Requirements
- Describe system architecture clearly
- Include implementation details (lines of code, platforms used)
- Report real deployment metrics where applicable
- Compare against state-of-the-art systems

### Evaluation Best Practices
- Use real-world workloads or traces
- Report both performance and cost metrics
- Include sensitivity analysis
- Discuss limitations and trade-offs

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background/Motivation** — Cloud computing context
4. **Design/Approach** — System architecture and design decisions
5. **Implementation** — Technical details, challenges
6. **Evaluation** — Methodology, results, comparison
7. **Related Work** — Positioning within literature
8. **Discussion/Limitations** — Scope, applicability
9. **Conclusion** — Summary
10. **References**
11. **Appendix** — Additional details

## Figure and Table Guidelines

### Cloud System Figures
- System architecture diagrams
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
7. Submit through HotCRP or conference system

## Common Mistakes to Avoid

1. **Breaching anonymity** (author identity revealed)
2. Missing system design rationale
3. Weak evaluation methodology
4. Cherry-picking workloads
5. Insufficient baseline comparison
6. Exceeding 14-page limit

## Useful Resources

- [SoCC 2026 Author Information](https://acmsocc.org/socc26)
- [ACM LaTeX Guidelines](https://www.acm.org/publications/proceedings-template)
- Publisher: ACM
