# ASPLOS Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/asplos/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `asplos` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/ASPLOS` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

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
