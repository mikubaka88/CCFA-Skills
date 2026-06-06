# ICDCS Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/icdcs/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icdcs` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/ICDCS` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICDCS Writing Guide

ICDCS (International Conference on Distributed Computing Systems) is a **CCF-B distributed computing conference** (https://icdcs2026.srieru.com). **ICDCS uses single-blind review — author information is typically included.** ICDCS is a premier venue for distributed computing systems and networking research.

## Document Setup

### Template Files
- Template folder: `ICDCS/`
- Document class: IEEEtran with conference mode
- Main class file: `IEEEtran.cls`

### Required LaTeX Structure

**For Submission:**
```latex
\documentclass[conference,compsoc]{IEEEtran}

% Optional packages
\usepackage{graphicx}
\usepackage{cite}
\usepackage{amsmath}
\usepackage{hyperref}

\begin{document}

% Title
\title{Your Paper Title}

% Author blocks — ICDCS uses IEEE author format
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

\maketitle

\begin{abstract}
Your abstract here — summarize contribution and key results.
\end{abstract}

% Keywords
\begin{IEEEkeywords}
distributed systems, networking, keywords
\end{IEEEkeywords}

% Main content
\section{Introduction}
...

% References: IEEE style
\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

### Key Formatting Requirements
- **Document class**: `IEEEtran` with `[conference]` option
- **Layout**: Two-column (IEEE conference format)
- **Author format**: `\IEEEauthorblockN{}` and `\IEEEauthorblockA{}`

## Page Limits

- **10 pages** typical for ICDCS 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**ICDCS is typically single-blind.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow IEEE Xplore compatibility guidelines

## Distributed Systems Writing Conventions

### Distributed Computing Focus
ICDCS papers focus on:
- Distributed algorithms
- Network protocols
- Cloud computing
- Edge computing

### Methodology Requirements
- Describe distributed system design clearly
- Report performance metrics
- Include scalability analysis
- Discuss fault tolerance

### Evaluation Best Practices
- Report latency, throughput
- Include comparison with baselines
- Discuss limitations
- Report real-world experiments where possible

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Distributed systems context
4. **Design/Approach** — System design
5. **Implementation/Evaluation** — Results and analysis
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**

## Figure and Table Guidelines

### Distributed System Figures
- System architecture diagrams
- Performance charts
- Network topology diagrams
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use IEEE style formatting
- Include performance metrics

## Reference Format

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

- IEEE citation format
- Numbered citations `[1]`, `[2]`
- Full author names

## Camera-Ready Preparation

1. Verify PDF compliance with IEEE Xplore requirements
2. Include all author information and acknowledgments
3. Ensure page numbers are correct
4. Add IEEE copyright notice
5. Submit through IEEE PDF eXpress or conference system

## Common Mistakes to Avoid

1. Using wrong document class (use IEEEtran conference mode)
2. Missing `\IEEEauthorblockN{}` for author names
3. Exceeding page limit
4. Non-embedded fonts in PDF
5. Missing abstract or keywords

## Useful Resources

- [ICDCS 2026 Author Information](https://icdcs2026.srieru.com)
- [IEEE LaTeX Guidelines](https://www.ieee.org/publications/standards/publications/authors/author-templates.html)
- Publisher: IEEE Computer Society
