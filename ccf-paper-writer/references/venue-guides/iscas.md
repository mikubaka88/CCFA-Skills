# ISCAS Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/iscas/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `iscas` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/ISCAS` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ISCAS Writing Guide

ISCAS (International Symposium on Circuits and Systems) is a **CCF-B circuits and systems conference** (https://iscas2026.org). **ISCAS uses single-blind review — author information is typically included.** ISCAS is a premier venue for circuit and system design research.

## Document Setup

### Template Files
- Template folder: `ISCAS/`
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

% Author blocks — ISCAS uses IEEE author format
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
circuits, systems, VLSI, keywords
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

- **5-6 pages** typical for ISCAS 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**ISCAS is typically single-blind.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow IEEE Xplore compatibility guidelines

## Circuits and Systems Writing Conventions

### Circuit Design Focus
ISCAS papers focus on:
- VLSI circuit design
- Analog and mixed-signal circuits
- RF circuits
- System-on-chip design

### Methodology Requirements
- Describe circuit design clearly
- Report circuit measurements
- Include simulation results
- Discuss design trade-offs

### Evaluation Best Practices
- Report circuit performance metrics
- Compare with state-of-the-art
- Include chip micrographs if available
- Discuss limitations

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Circuit design context
4. **Design/Approach** — Circuit architecture
5. **Implementation/Results** — Measurements and analysis
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**

## Figure and Table Guidelines

### Circuit Figures
- Circuit schematics
- Chip layouts
- Measurement results
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

- [ISCAS 2026 Author Information](https://iscas2026.org)
- [IEEE LaTeX Guidelines](https://www.ieee.org/publications/standards/publications/authors/author-templates.html)
- Publisher: IEEE Circuits and Systems Society
