---
name: asplos
description: Writing and formatting guidance for ASPLOS (International Conference on Architectural Support for Programming Languages and Operating Systems) papers. Use when drafting, formatting, or submitting to ASPLOS 2026. ASPLOS is a unique cross-disciplinary venue at the intersection of architecture, systems, and PL. Covers ACM acmart sigplan format with anonymous review mode, ASPLOS-specific writing conventions (contribution clarity, architectural methodology, real-system evaluation), 14-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ASPLOS Writing Guide

ASPLOS (International Conference on Architectural Support for Programming Languages and Operating Systems) is a **CCF-A architecture conference** (https://www.asplos-conference.org/asplos2026). **ASPLOS IS double-blind — papers must be anonymized.** ASPLOS uniquely bridges architecture, systems, and programming languages research.

## Document Setup

### Template Files
- Template folder: `ASPLOS/`
- Document class: ACM `acmart` with sigplan format
- Style files from ACM distribution

### Required LaTeX Structure

**For Submission (ANONYMOUS):**
```latex
\documentclass[sigplan,review,anonymous]{acmart}
\acmartConference[ASPLOS'26]{ASPLOS 2026}{March 2026}{Singapore}

% Optional packages
\usepackage{draftwatermark}  % For review copies
\usepackage[]{graphicx}

\begin{document}

% Anonymized title
\title{Your Paper Title}

% Anonymized abstract
\begin{abstract}
Your abstract here.
\end{abstract}

% Anonymized author command
% Omit or use anonymous affiliations
\setcopyright{} % Remove copyright for review

% Main content
\section{Introduction}
...

% Bibliography: ACM style
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
```

**For Camera-Ready (NOT anonymous):**
```latex
\documentclass[sigplan]{acmart}
\acmartConference[ASPLOS'26]{ASPLOS 2026}{March 2026}{Singapore}

% Include author information
\title{Your Paper Title}
\author{Author Name}
\affiliation{...}
\email{...}

% Include copyright
\setcopyright{...}

\begin{document}
...
\end{document}
```

### Key Formatting Requirements
- **Document class**: `acmart` with `[sigplan]` option
- **Review mode**: `[sigplan,review,anonymous]` for submission
- **Layout**: Two-column (ACM SIGPLAN format)
- **Review mode**: Remove all identifying information

## Page Limits

- **14 pages** maximum for ASPLOS 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**ASPLOS IS double-blind.** Authors must anonymize their submissions:

### Required Anonymization
1. Remove author names from title page
2. Use third-person references to prior work (e.g., "Smith et al. [5]" not "we")
3. Remove acknowledgments
4. Exclude funding information
5. Anonymize URLs that identify authors
6. Avoid self-citations that reveal identity
7. Do not upload preprints to venues with author names

### Permitted
- GitHub links with anonymized repos
- Technical reports on arXiv (after submission)
- Preprints that don't identify authors

## Cross-Disciplinary Scope

ASPLOS accepts papers at the intersection of:
- **Architecture**: Hardware design, ISA, microarchitecture
- **Systems**: Operating systems, runtime systems, compilers
- **Programming Languages**: Languages, type systems, verification
- **Applications**: Domain-specific computing, emerging workloads

### Contribution Types
1. **Hardware-software co-design**: Novel hardware with software stack
2. **Systems infrastructure**: New OS/runtime/compiler features
3. **Programming models**: Languages and abstractions for emerging platforms
4. **Methodology**: New evaluation methods, benchmarks, tools

## Section Ordering (Recommended)

1. **Abstract** — 150 words, contribution-focused
2. **Introduction** — Problem, motivation, 4-5 concrete contributions
3. **Background/Preliminaries** — Hardware/software context
4. **Design/Approach** — Technical contribution with rationale
5. **Implementation** — System prototype details
6. **Evaluation** — Methodology, experiments, comparison
7. **Related Work** — Positioning within literature
8. **Discussion/Limitations** — Scope, deployment, future work
9. **Conclusion** — Summary
10. **References**
11. **Appendix** — Additional analysis, proofs

## Architecture-Specific Guidelines

### Methodology Transparency
- Describe simulation/hardware setup in detail
- Report all configuration parameters
- Include sensitivity analysis
- Discuss validity threats

### Evaluation Standards
- **Simulation papers**: Describe simulator, configuration, workloads
- **Hardware papers**: Describe implementation, measurement setup
- **Hybrid**: Combine both approaches

### Metrics Reporting
- Architecture metrics: IPC, CPI, performance speedup
- Area/power/energy if applicable
- Software metrics: execution time, memory usage
- Always include baseline comparisons

## Figure and Table Guidelines

### Architecture Figures
- Pipeline diagrams
- Block diagrams of hardware/software
- Execution timelines
- Memory hierarchy visualizations
- Use consistent notation

### Evaluation Figures
- Performance comparison bar charts
- Speedup graphs
- Area/power trade-off plots
- Sensitivity analysis curves
- Workload characterization

### Table Best Practices
- Clear column headers with units
- Baselines highlighted
- Statistical significance noted
- Use booktabs formatting

## Reference Format

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}
```

- ACM citation style
- Full author names
- Proper proceedings abbreviations

## Camera-Ready Preparation

1. Switch to non-anonymous mode
2. Add all author information
3. Include acknowledgments
4. Add copyright notice
5. Verify formatting
6. Submit through HotCRP or ACM SORS

## Common Mistakes to Avoid

1. **De-anonymizing** submission (revealing author identity)
2. Including acknowledgments in submission
3. Self-citations that identify authors
4. Exceeding 14 pages
5. Weak architectural methodology
6. Insufficient evaluation

## Useful Resources

- [ASPLOS 2026 Author Guide](https://www.asplos-conference.org/asplos2026)
- [ACM LaTeX Template Guide](https://www.acm.org/publications/proceedings-template)
- Publisher: ACM
