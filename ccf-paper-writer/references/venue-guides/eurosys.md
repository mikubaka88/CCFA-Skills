# EuroSys Venue Guide

> Migrated from the legacy `ccf-conference-skills/eurosys/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `eurosys` |
| Venue family | Systems |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/EuroSys/acmart.cls` |
| Official URL | https://2026.eurosys.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# EuroSys 2026 Conference Writing Skill

**CCF-A | Systems | Publisher: ACM**
**Conference:** https://2026.eurosys.org
**Template:** `EuroSys/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[EuroSys 2026]{EuroSys '26: Twenty-First European...}
               {April 14--17, 2026}{Stavanger, Norway}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}
\usepackage{graphicx}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **16 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

EuroSys enforces a 16-page limit for the main body. References and appendix do not count.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names anywhere in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub, institutional pages)
4. Clear PDF metadata
5. Do not include acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

EuroSys papers follow the systems paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, existing approaches and limits
3. **Design/Approach** — Core contribution with sufficient technical depth
4. **Implementation** — Practical system details, complexity, challenges solved
5. **Evaluation** — Rigorous experimental methodology, baseline comparisons, sensitivity analysis
6. **Related Work** — Thorough positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

EuroSys values papers that show **systems depth**: thorough motivation, honest trade-off discussion, and reproducible evaluation.

## Systems Paper Conventions

EuroSys has particular expectations for systems papers:

- **Real systems**: Must be implemented and evaluated, not just designed
- **Design rationale**: Explain why design decisions were made
- **Implementation challenges**: Describe real challenges encountered
- **Evaluation rigor**: Compare against the best existing systems, include sensitivity analysis

```latex
\section{Design}

\subsection{Design Goals}
Our system aims to achieve:
\begin{itemize}
  \item \textbf{Low latency}: Sub-millisecond tail latency under
    production workloads
  \item \textbf{High throughput}: 10M ops/sec on a single server
  \item \textbf{Strong consistency}: Linearizability guarantees
\end{itemize}

\subsection{Design Decisions}
We chose a log-structured design rather than update-in-place
because it provides better write amplification characteristics
for our target workload. We evaluated three alternatives:
...
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Self-contained captions
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/architecture}
  \caption{System architecture showing the coordination layer
    and data plane components. The coordination layer uses
    Raft consensus for leader election while the data plane
    handles request routing and replication.}
  \label{fig:architecture}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{doe2025}      % Doe et al. (2025)
\citep{doe2025}     % (Doe et al. 2025)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 16 pages or fewer (main body)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author identification removed
- [ ] No self-referential citations in first person
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
