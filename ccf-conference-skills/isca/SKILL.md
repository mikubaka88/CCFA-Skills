---
name: isca
description: Writing and formatting guidance for ISCA (International Symposium on Computer Architecture) papers. Use when drafting, formatting, or submitting to ISCA 2026. Covers ACM acmart sigplan format with anonymous review mode, architecture-specific writing conventions (simulation vs hardware evaluation, metric reporting, methodology transparency, sensitivity analysis), 12-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ISCA Writing Guide

ISCA (International Symposium on Computer Architecture) is a **CCF-A architecture conference** (https://www.iscaconf.org/isca2026). **ISCA IS double-blind — papers must be anonymized.** ISCA is one of the top venues for computer architecture research, emphasizing novel microarchitectural contributions, rigorous evaluation, and insights that advance the field.

## Document Setup

### Template Files
- Template folder: `ISCA/`
- Document class: ACM `acmart` with sigplan format
- Style files from ACM distribution

### Required LaTeX Structure

**For Submission (ANONYMOUS):**
```latex
\documentclass[sigplan,review,anonymous]{acmart}
\acmartConference[ISCA'26]{ISCA 2026}{June 2026}{Seoul, South Korea}

% Optional packages
\usepackage{draftwatermark}
\usepackage[]{graphicx}

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

**For Camera-Ready (NOT anonymous):**
```latex
\documentclass[sigplan]{acmart}
\acmartConference[ISCA'26]{ISCA 2026}{June 2026}{Seoul, South Korea}

% Include author information
\title{Your Paper Title}
\author{Author Name}
\affiliation{...}
\email{...}
\setcopyright{...}

\begin{document}
...
\end{document}
```

### Key Formatting Requirements
- **Document class**: `acmart` with `[sigplan]` option
- **Review mode**: `[sigplan,review,anonymous]` for submission
- **Layout**: Two-column (ACM SIGPLAN format)
- **Double-blind**: All identifying information must be removed

## Page Limits

- **12 pages** maximum for ISCA 2026
- References do NOT count toward page limit
- Supplementary materials may be submitted separately

## Double-Blind Requirements

**ISCA IS double-blind.** Anonymization is mandatory:

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
- Preprints on arXiv (without author names)
- Anonymized code repositories

## Architecture-Specific Writing Conventions

### Simulation Methodology
ISCA papers must have rigorous, reproducible evaluation:

**Simulator Description**:
- Name and version of simulator
- Configuration parameters (ISA, cache sizes, etc.)
- Simulation mode (functional vs timing)
- Simulation time and sampling strategy

**Workload Description**:
- Benchmark suite name and version
- Input data sets used
- Why these workloads represent the target domain
- Pre-processing or preparation steps

**Metrics Reported**:
- Performance: IPC, CPI, execution time, speedup
- Area/power/energy (if applicable)
- Cache miss rates, branch misprediction rates
- Any architecture-specific metrics

### Hardware Evaluation
If implemented in hardware:
- Implementation technology (process node, etc.)
- Synthesis results (area, frequency, power)
- Physical constraints
- Measurement methodology

### Sensitivity Analysis
Required for credible evaluation:
- Vary key parameters (cache size, issue width, etc.)
- Show performance across workload classes
- Discuss cliff points and trade-offs
- Report statistical significance

### Comparison with Baselines
- Use well-known, publicly available baselines
- Describe baseline configurations precisely
- Be fair to comparison targets
- Include confidence intervals where applicable

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution and results
2. **Introduction** — Problem, motivation, 4-5 contributions
3. **Background/Motivation** — Architecture context, prior work limitations
4. **Design/Approach** — Technical contribution with rationale
5. **Implementation/Methodology** — Experimental setup, simulation details
6. **Evaluation** — Results, comparison, sensitivity analysis
7. **Related Work** — Positioning within architecture literature
8. **Discussion/Limitations** — Scope, applicability, future directions
9. **Conclusion** — Summary of contributions
10. **References**
11. **Appendix** — Additional evaluation, proofs, simulator details

## Figure and Table Guidelines

### Architecture Figures
- Microarchitecture block diagrams
- Pipeline diagrams
- State machines
- Memory hierarchy visualizations
- Consistent notation across figures

### Evaluation Figures
- Performance bar charts (speedup over baseline)
- Trend lines (sensitivity analysis)
- CDFs (performance distribution)
- Trade-off plots (area vs performance)
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Include standard deviations or confidence intervals
- Use booktabs style
- Report absolute values, not just percentages

## Reference Format

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}
```

- ACM citation format
- Full author names (except self-citations in anonymous mode)
- Complete conference/proceedings names

## Camera-Ready Preparation

1. Switch to non-anonymous mode
2. Add author names and affiliations
3. Include acknowledgments
4. Add copyright notice
5. Verify 12-page limit
6. Ensure PDF/A compliance
7. Submit through the ISCA submission system

## Common Mistakes to Avoid

1. **Breaching anonymity** (author identity revealed)
2. Missing sensitivity analysis
3. Unclear simulation methodology
4. Cherry-picking workloads
5. Insufficient baseline comparison
6. Exceeding 12-page limit
7. Weak statistical rigor

## Useful Resources

- [ISCA 2026 Author Information](https://www.iscaconf.org/isca2026)
- [ACM LaTeX Guidelines](https://www.acm.org/publications/proceedings-template)
- Publisher: IEEE Computer Society / ACM
