---
name: nsdi
description: Writing and formatting guidance for NSDI (Symposium on Network System Design and Implementation) papers. Use when drafting, formatting, or submitting to NSDI 2026. NSDI is NOT double-blind — author identities are visible. Covers usenix-2020-09.sty format with \\maketitles, systems paper conventions (motivation, design rationale, implementation challenges, evaluation with real-world deployment), 16-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# NSDI Writing Guide

NSDI (Symposium on Network System Design and Implementation) is a **CCF-A networks conference** (https://www.usenix.org/conference/nsdi26). **IMPORTANT: NSDI is NOT double-blind — author identities are visible to reviewers.** NSDI is a systems paper venue emphasizing practical design and real-world evaluation.

## Document Setup

### Template Files
- Style file: `NSDI/usenix-2020-09.sty` (same as USENIX Security, OSDI, ATC, etc.)
- Note: NSDI shares the same USENIX template family with OSDI, USENIX ATC, FAST, HotStorage

### Required LaTeX Structure

```latex
\documentclass[11pt]{article}
\usepackage{usenix-2020-09}

% Optional packages
\usepackage{graphicx}
\usepackage{hyperref}

\begin{document}

% IMPORTANT: Use \maketitles (NOT \maketitle)
\maketitles

\begin{abstract}
Your abstract here — motivation, problem, design decisions, key results.
\end{abstract}

% Main content
\section{Introduction}
...

% Bibliography: plain style
\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### Key Formatting Requirements
- **Document class**: `article` (11pt)
- **Layout**: Single-column
- **Font size**: 10pt (enforced by style file)
- **Title command**: `\maketitles` — NSDI uses this USENIX-style command

## Page Limits

- **16 pages** maximum for NSDI 2026
- References and appendices do NOT count toward the page limit
- Balance depth with accessibility

## Submission Requirements

### Double-Blind Status
**NSDI is NOT anonymous.** Author names and affiliations are visible to reviewers.

### Submission Format
- Single PDF submission
- Embed all fonts
- Include all figures in PDF

## Systems Paper Conventions

NSDI publishes **systems papers** — papers about the design, implementation, and evaluation of practical systems. Key characteristics:

### What Makes a Good NSDI Paper
1. **Real systems**: Must be implemented and evaluated, not just designed
2. **Design rationale**: Explain why design decisions were made
3. **Practical evaluation**: Show real-world deployment or realistic experiments
4. **Lessons learned**: Insights that benefit the community
5. **Working code**: Preferably open-sourced

### Paper Structure Emphasis

**Introduction** (critical for NSDI):
- Problem statement and motivation
- Key challenges
- Contributions (3-5 concrete, verifiable claims)
- Roadmap of the paper

**Design Section**:
- Design goals and constraints
- Architecture overview
- Component design with rationale
- Design decisions trade-offs

**Implementation Section**:
- Prototype details
- System complexity metrics
- Key implementation challenges
- Deployment considerations

**Evaluation Section**:
- Real-world deployment preferred
- Testbed/simulation acceptable with justification
- Baseline comparison (existing systems)
- Sensitivity analysis
- Performance under stress

## Section Ordering (Recommended)

1. **Abstract** — 150-250 words
2. **Introduction** — Problem, challenges, contributions (4-6 paragraphs)
3. **Background/Motivation** — Context and problem space
4. **Design** — System architecture and components
5. **Implementation** — Prototype details and challenges
6. **Evaluation** — Experiments, results, comparison with baselines
7. **Related Work** — Existing approaches and how this differs
8. **Discussion/Limitations** — Scope, future directions
9. **Conclusion** — Summary
10. **References**
11. **Appendix** — Additional evaluation, proofs, source links

## Figure and Table Guidelines

### Systems Diagrams
- Architecture diagrams showing components
- Data flow diagrams
- State machines (if applicable)
- Sequence diagrams for protocols
- Use consistent styling and color schemes

### Evaluation Figures
- Performance graphs with error bars
- Latency/throughput CDFs
- Scalability plots
- Resource utilization over time
- Comparison bar charts

### Table Best Practices
- Use booktabs formatting
- Include baseline comparisons
- Report statistical significance where applicable
- Label units clearly

## Reference Format

```latex
\bibliographystyle{plain}
\bibliography{references}
```

- Author names in standard format
- Full conference proceedings names
- Prioritize recent work and foundational papers

## Camera-Ready Preparation

1. Final review of all content
2. Include author acknowledgments
3. Verify page formatting
4. Ensure figures are high quality
5. Submit through USENIX submission system

## Common Mistakes to Avoid

1. Submitting theory papers (NSDI is for systems)
2. Using `\maketitle` instead of `\maketitles`
3. Lightweight evaluation (NSDI expects rigorous evaluation)
4. Missing design rationale (just showing, not explaining)
5. Claiming contributions without sufficient evidence

## Useful Resources

- [NSDI 2026 Call for Papers](https://www.usenix.org/conference/nsdi26/call-for-papers)
- [NSDI Paper Review Guidelines](https://www.usenix.org/conference/nsdi26/reviewing-guidelines)
- Publisher: USENIX Association
