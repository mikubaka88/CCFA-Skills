# HotStorage Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/hotstorage/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `hotstorage` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/HotStorage` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# HotStorage Writing Guide

HotStorage (Workshop on Hot Topics in Storage Systems) is a **CCF-B storage workshop** (https://www.usenix.org/conferences/hotstorage). **HotStorage is NOT double-blind — author information is included.** HotStorage is a venue for innovative storage systems research, focusing on hot topics in storage and file systems.

## Document Setup

### Template Files
- Template folder: `HotStorage/`
- Document class: article with USENIX styling
- Style files: `usenix-2020-09.sty`, `usenix2019_v3.sty`

### Required LaTeX Structure

**For Submission:**
```latex
\documentclass[letterpaper,twocolumn,10pt]{article}
\usepackage{usenix-2020-09}

% Optional packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}

\begin{document}

% Title
\title{Your Paper Title}

% Author block
\author{
  {\rm Author Name}\\
  Institution
  \and
  {\rm Second Author}\\
  Second Institution
}

% Don't print date
\date{}

\maketitle

\begin{abstract}
Your abstract here — summarize contribution and key results.
\end.Abstract}

% Main content
\section{Introduction}
...

% References
\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### Key Formatting Requirements
- **Document class**: `article` with USENIX styling
- **Layout**: Two-column (USENIX format)
- **Margins**: 0.75" sides, 1" top/bottom
- **Text width**: 7" with 0.33" column gap
- **Not anonymous**: Author information is included

## Page Limits

- **12 pages** maximum for HotStorage 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**HotStorage is NOT anonymous.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow USENIX guidelines

## Storage Systems Writing Conventions

### Storage Focus
HotStorage papers focus on:
- File systems
- Storage architectures
- Data management
- Emerging storage technologies

### Workshop Style
- Shorter, more focused papers
- Novel ideas and preliminary results welcome
- Emphasis on hot topics in storage

### Methodology Requirements
- Describe storage system design clearly
- Report performance metrics
- Include workload characterization
- Discuss limitations

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Storage context
4. **Design/Approach** — System design
5. **Evaluation** — Results and analysis
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**

## Figure and Table Guidelines

### Storage System Figures
- Architecture diagrams
- Performance charts
- Trace visualizations
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Include performance metrics

## Reference Format

```latex
\bibliographystyle{plain}
\bibliography{references}
```

- Plain bibliography style
- Numbered citations

## Camera-Ready Preparation

1. Verify PDF compliance with USENIX requirements
2. Include all author information
3. Ensure page numbers are correct
4. Submit through USENIX submission system

## Common Mistakes to Avoid

1. Using wrong document class
2. Exceeding 12-page limit
3. Non-embedded fonts in PDF
4. Missing abstract

## Useful Resources

- [HotStorage 2026 Author Information](https://www.usenix.org/conferences/hotstorage)
- [USENIX LaTeX Guidelines](https://www.usenix.org/conferences/author-resources)
- Publisher: USENIX
