# ICRA Venue Guide

> Migrated from the legacy `ccf-conference-skills/icra/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icra` |
| Venue family | Robotics |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ICRA/IEEEtran.cls` |
| Official URL | https://www.ieee-icra.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICRA 2026 Conference Writing Skill

**CCF-B | Robotics | Publisher: IEEE**
**Conference:** https://www.ieee-icra.org
**Template:** `ICRA/IEEEtran.cls`

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind peer review) ===
\documentclass[10pt,conference,peerreviewca]{IEEEtran}

% === CAMERA-READY MODE ===
\documentclass[10pt,conference]{IEEEtran}

% Required packages
\usepackage{cite}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{url}
\usepackage{amssymb}     % For special symbols
\usepackage{algorithm}   % For algorithmic descriptions
\usepackage[noend]{algorithmic}
```

### Required Packages

```latex
\usepackage{cite}              % IEEE citation style
\usepackage{amsmath}           % Math
\usepackage{graphicx}         % Figures
\usepackage{booktabs}         % Professional tables
\usepackage{url}               % URLs in references
\usepackage{microtype}         % Improved typography
\usepackage{amssymb}           % Special symbols
\usepackage{algorithm}         % Algorithm listings
\usepackage[noend]{algorithmic} % Pseudocode
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **6 pages** (typical, check CFP) |
| References | No limit |
| Appendix | Not typically permitted |

ICRA typically allows 6 pages for the main content. Always check the official CFP.

## Anonymity Requirements

ICRA uses **double-blind peer review**. Use the `peerreviewca` class option:

1. No author names or affiliations in the submission
2. Use third-person self-citations
3. Anonymize all URLs
4. Clear PDF metadata
5. Remove acknowledgments from the submission

## Title and Author Formatting

```latex
% Camera-ready (all authors visible):
\title{Your Paper Title}

\author{
  \IEEEauthorblockN{First Author}
  \IEEEauthorblockA{Department\\
    University\\
    email@example.com}
  \and
  \IEEEauthorblockN{Second Author}
  \IEEEauthorblockA{Department\\
    University\\
    email2@example.com}
}
```

## Camera-Ready Differences

After acceptance:

1. Remove the `peerreviewca` option
2. Add author names and affiliations
3. Add `\IEEEmembership{}` if needed
4. Include the standard IEEE copyright notice

## Section Organization

ICRA papers typically follow a robotics research structure:

1. **Introduction** — Robotics problem, motivation, contributions
2. **Related Work / Background** — Prior robotics research
3. **System Design / Methods** — Proposed robot system, algorithm, or control approach
4. **Implementation** — Technical details of the robot or system
5. **Experimental Results** — Physical experiments, simulation results, or analysis
6. **Discussion** — Limitations, future work
7. **Conclusion**
8. References

ICRA values papers with **physical experiments** or **substantial simulation results** demonstrating the approach.

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system}
  \caption{Robot system overview showing (a) hardware components
    and (b) software architecture.}
  \label{fig:system}
\end{figure}

\begin{table}[t]
  \caption{Comparison of motion planning algorithms.}
  \label{tab:comparison}
  \centering
  \begin{tabular}{lcc}
    \toprule
    Method & Success Rate & Time (s) \\
    \midrule
    RRT & 85\% & 2.3 \\
    Ours & 97\% & 0.8 \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Use vector formats (.pdf, .eps) where possible
- Ensure grayscale legibility
- Caption **below** figures, **above** tables

## References

IEEEtran uses numbered citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations:
\citep{key}    % [1]
\citep{key1,key2}  % [1,2]
```

## ICRA-Specific Writing Conventions

- **System substantiation**: The robotic system must be real and evaluated
- **Experimental validation**: Physical experiments are highly valued; simulations alone may not be sufficient
- **Quantitative results**: Report success rates, errors, timing, and other performance metrics
- **Algorithmic clarity**: Describe algorithms in sufficient detail
- **Reproducibility**: Include key parameters and setup details
- **Video**: Consider submitting an accompanying video demonstrating the system

## Formatting Rules

- **Paper size:** US Letter
- **Font:** 10pt default, Times New Roman recommended
- **Margins:** Top 0.75in, bottom 1in, left/right 0.75in or 1in (check CFP)
- **Columns:** Two-column format

## Submission Checklist

- [ ] `\documentclass[10pt,conference,peerreviewca]{IEEEtran}`
- [ ] No author identification in submission
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Compiles with `pdflatex`
- [ ] References in IEEEtran format
- [ ] Physical experiments or substantial simulation results included
