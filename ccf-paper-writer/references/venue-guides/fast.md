# FAST Venue Guide

> Migrated from the legacy `ccf-conference-skills/fast/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `fast` |
| Venue family | Systems |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/FAST/usenix-2020-09.sty` |
| Official URL | https://www.usenix.org/conference/fast26 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# FAST 2026 Conference Writing Skill

**CCF-A | Systems | Publisher: USENIX**
**Conference:** https://www.usenix.org/conference/fast26
**Template:** `FAST/usenix-2020-09.sty` (or `usenix2019_v3.sty`)

## Document Setup

### Preamble Structure

```latex
\documentclass[letterpaper,twocolumn,10pt]{article}
\usepackage{usenix-2020-09}
% OR: \usepackage{usenix2019_v3}

% Optional packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}
\usepackage{hyperref}
```

### Required Packages

```latex
\usepackage{usenix-2020-09}  % or usenix2019_v3
\usepackage{cite}             % order multiple entries in \cite{...}
\usepackage{url}             % allow \url in bibtex for clickable links
\usepackage{xcolor}           % color definitions
\usepackage[]{hyperref}      % clickable refs within pdf
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **16 pages** |
| References | No limit |
| Appendix | Permitted |

FAST enforces a 16-page limit for the main body. References and appendix do not count.

## Anonymity Requirements

FAST uses double-blind review:

1. No author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub repos, institutional pages)
4. Clear PDF metadata
5. Do not include acknowledgments in submission

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations
2. Verify figure quality and resolution
3. Add acknowledgments if desired
4. USENIX provides page numbers for camera-ready

## Section Organization

FAST papers follow the systems paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, prior approaches and their limits
3. **Design/Approach** — Core technical contribution with rationale
4. **Implementation** — System details, complexity, challenges solved
5. **Evaluation** — Rigorous experimental methodology, baselines, sensitivity analysis
6. **Related Work** — Thorough positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Storage Systems Conventions

FAST papers typically cover:
- File systems and storage architectures
- Storage performance and reliability
- Distributed storage systems
- Storage security and privacy
- New storage technologies (NVMe, persistent memory, etc.)

### Performance Evaluation

```latex
\section{Evaluation}
We evaluate our file system using:
\begin{itemize}
  \item \textbf{Benchmarks}: fio, IOzone, Filebench
  \item \textbf{Workloads}: synthetic and real-world traces
  \item \textbf{Metrics}: throughput (ops/sec), latency (usec), bandwidth (MB/s)
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all diagrams
- Ensure grayscale legibility — reviewers often print in B&W
- Self-contained captions: describe what to observe and why it matters
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/design-arch}
  \caption{Architecture overview: (a) metadata server layout,
    (b) data plane organization. Our design reduces metadata
    lookup latency by 3x compared to the baseline.}
  \label{fig:arch}
\end{figure}
```

## References

```latex
\bibliographystyle{plain}
\bibliography{references}

% Citations:
~\cite{smith2023}        % [1]
```

Use `plain` bibstyle with numerical citations.

## Formatting Rules

- **Format:** USENIX two-column, 10pt body
- **Paper size:** US Letter
- **Margins:** 0.75" sides, 1" top/bottom
- **Text width:** 7"
- **Column gap:** 0.33"
- **Font:** Times New Roman (mathptmx)

## Submission Checklist

- [ ] 16 pages or fewer (main body)
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References properly formatted
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Restore author names and affiliations
- [ ] Verify figure quality (high resolution)
- [ ] Add acknowledgments
- [ ] Ensure no forbidden packages
