---
name: iccad
description: Writing and formatting guidance for ICCAD (International Conference on Computer-Aided Design) papers. Use when drafting, formatting, or submitting to ICCAD 2026. Covers IEEEtran conference class, EDA-specific conventions, page limits, and camera-ready preparation with IEEE Xplore metadata.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ICCAD Writing Guide

ICCAD (International Conference on Computer-Aided Design) is a **CCF-B computer-aided design conference** (https://iccad.com). **ICCAD uses single-blind review — author information is typically included.** ICCAD is a premier venue for electronic design automation and electronic system-level design research.

## Document Setup

### Template Files
- Template folder: `ICCAD/`
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

% Author blocks — ICCAD uses IEEE author format
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
EDA, VLSI, CAD, keywords
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

- **8-10 pages** typical for ICCAD 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**ICCAD is typically single-blind.** Author information should be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF
- Follow IEEE Xplore compatibility guidelines

## EDA Writing Conventions

### CAD Focus
ICCAD papers focus on:
- Electronic design automation
- Logic synthesis and optimization
- Physical design
- Verification and testing

### Methodology Requirements
- Describe EDA algorithms clearly
- Report experimental results
- Include comparison with existing tools
- Discuss scalability

### Evaluation Best Practices
- Report runtime, quality of results
- Include benchmark comparisons
- Discuss limitations
- Report any novel techniques

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, contributions
3. **Background** — EDA context
4. **Design/Approach** — Algorithm or tool design
5. **Implementation/Evaluation** — Results and analysis
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**

## Figure and Table Guidelines

### EDA Figures
- Algorithm flowcharts
- Circuit/layout examples
- Experimental results
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Use IEEE style formatting
- Include runtime/QoR metrics

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

- [ICCAD 2026 Author Information](https://iccad.com)
- [IEEE LaTeX Guidelines](https://www.ieee.org/publications/standards/publications/authors/author-templates.html)
- Publisher: IEEE / ACM
