# CLUSTER Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/cluster/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `cluster` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/CLUSTER` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CLUSTER Writing Guide

CLUSTER (IEEE International Conference on Cluster Computing) is a **CCF-B HPC conference** (https://cluster2026.hpcaworkshop.com). **CLUSTER uses single-blind review — author information is typically included.** CLUSTER is a top venue for cluster computing and high-performance distributed systems research.

## Document Setup

### Template Files
- Template folder: `CLUSTER/`
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

% Author blocks — CLUSTER uses IEEE author format
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
cluster computing, HPC, distributed systems, keywords
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

- **8-10 pages** typical for CLUSTER 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**CLUSTER is typically single-blind.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow IEEE Xplore compatibility guidelines

## Cluster Computing Writing Conventions

### HPC Focus
CLUSTER papers focus on:
- Cluster architecture
- High-performance computing
- Distributed resource management
- Performance optimization

### Methodology Requirements
- Describe cluster system design clearly
- Report performance metrics
- Include scalability analysis
- Discuss overhead sources

### Evaluation Best Practices
- Report speedup, efficiency
- Include comparison with baselines
- Discuss limitations
- Report real-world experiments where possible

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — HPC context
4. **Design/Approach** — System design
5. **Implementation/Evaluation** — Results and analysis
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**

## Figure and Table Guidelines

### HPC Figures
- Cluster architecture diagrams
- Performance charts
- Scaling plots
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

- [CLUSTER 2026 Author Information](https://cluster2026.hpcaworkshop.com)
- [IEEE LaTeX Guidelines](https://www.ieee.org/publications/standards/publications/authors/author-templates.html)
- Publisher: IEEE Computer Society
