---
name: msst
description: Writing and formatting guidance for MSST (International Conference on Massive Storage Systems and Technology) papers. Use when drafting, formatting, or submitting to MSST 2026. Covers IEEEtran conference class, storage systems-specific conventions, 10-page limit, and camera-ready preparation with IEEE Xplore metadata.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# MSST Writing Guide

MSST (International Conference on Massive Storage Systems and Technology) is a **CCF-B storage conference** (https://storageconference.us/MSST/MSST2026). **MSST uses single-blind review — author information is typically included.** MSST is a premier venue for storage systems and technology research.

## Document Setup

### Template Files
- Template folder: `MSST/`
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

% Author blocks — MSST uses IEEE author format
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
storage systems, file systems, keywords
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

- **10 pages** maximum for MSST 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**MSST is typically single-blind.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow IEEE Xplore compatibility guidelines

## Storage Systems Writing Conventions

### Storage Focus
MSST papers focus on:
- File systems
- Storage architectures
- Data management
- Performance optimization

### Methodology Requirements
- Describe storage system design clearly
- Report performance metrics
- Include workload characterization
- Discuss scalability

### Evaluation Best Practices
- Use real workloads or traces
- Report I/O performance metrics
- Include comparison with existing systems
- Discuss limitations

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Storage systems context
4. **Design/Approach** — System design
5. **Implementation** — Technical details
6. **Evaluation** — Methodology, results, comparison
7. **Related Work** — Positioning within literature
8. **Conclusion** — Summary
9. **References**

## Figure and Table Guidelines

### Storage System Figures
- Architecture diagrams
- Performance charts
- Trace visualizations
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
3. Exceeding 10-page limit
4. Non-embedded fonts in PDF
5. Missing abstract or keywords

## Useful Resources

- [MSST 2026 Author Information](https://storageconference.us/MSST/MSST2026)
- [IEEE LaTeX Guidelines](https://www.ieee.org/publications/standards/publications/authors/author-templates.html)
- Publisher: IEEE Computer Society
