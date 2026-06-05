---
name: rtas
description: Writing and formatting guidance for RTAS (Real-Time and Embedded Technology and Applications Symposium) papers. Use when drafting, formatting, or submitting to RTAS 2026. Covers IEEEtran conference class, real-time systems-specific conventions, 10-page limit, and camera-ready preparation with IEEE Xplore metadata.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# RTAS Writing Guide

RTAS (Real-Time and Embedded Technology and Applications Symposium) is a **CCF-B embedded systems conference** (https://rtas2026.sigbed.org). **RTAS uses single-blind review — author information is typically included.** RTAS is a top venue for real-time and embedded systems research.

## Document Setup

### Template Files
- Template folder: `RTAS/`
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

% Author blocks — RTAS uses IEEE author format
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
real-time systems, embedded systems, keywords
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

- **10 pages** maximum for RTAS 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**RTAS is typically single-blind.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow IEEE Xplore compatibility guidelines

## Real-Time Systems Writing Conventions

### Real-Time Focus
RTAS papers focus on:
- Real-time scheduling
- Embedded systems design
- Cyber-physical systems
- Timing analysis

### Methodology Requirements
- Describe real-time system design clearly
- Report timing guarantees
- Include schedulability analysis
- Discuss worst-case performance

### Evaluation Best Practices
- Report WCET (Worst-Case Execution Time)
- Include timing measurements
- Compare scheduling algorithms
- Discuss constraints and trade-offs

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Real-time systems context
4. **Design/Approach** — System design with timing analysis
5. **Implementation** — Technical details
6. **Evaluation** — Methodology, results, comparison
7. **Related Work** — Positioning within literature
8. **Conclusion** — Summary
9. **References**

## Figure and Table Guidelines

### Real-Time System Figures
- Timing diagrams
- Architecture diagrams
- Scheduling visualizations
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use IEEE style formatting
- Include timing metrics

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
5. Missing timing analysis

## Useful Resources

- [RTAS 2026 Author Information](https://rtas2026.sigbed.org)
- [IEEE LaTeX Guidelines](https://www.ieee.org/publications/standards/publications/authors/author-templates.html)
- Publisher: IEEE Computer Society / ACM SIGBED
