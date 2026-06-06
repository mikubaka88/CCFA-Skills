# SOSP Venue Guide

> Migrated from the legacy `ccf-conference-skills/sosp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `sosp` |
| Venue family | SE/Systems |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/SOSP/acmart.cls` |
| Official URL | https://sosp2026.mpi-sws.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SOSP 2026 Conference Writing Skill

**CCF-A | SE/Systems | Publisher: ACM**
**Conference:** https://sosp2026.mpi-sws.org
**Template:** `ccf-latex-templates/SOSP/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\acmConference[SOSP 2026]{ACM SIGOPS 27th ACM Symposium on...}
               {November 9--13, 2026}{Edinburgh, United Kingdom}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
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
| Main paper (submission) | **14 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

SOSP enforces a strict 14-page limit for the main body. References and appendix pages do not count, but reviewers are not obligated to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. Author names must not appear anywhere in the submission
2. Cite your own prior work in third person: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (e.g., GitHub, institutional pages)
4. Clear PDF metadata (Author, Creator fields)
5. Remove acknowledgments from submission version

## Section Organization

SOSP papers follow a well-established structure emphasizing systems depth:

1. **Introduction** — Problem statement, contributions (enumerate 3-5 key contributions)
2. **Background & Motivation** — Why this problem matters, existing approaches and their limits
3. **Design/Approach** — Core contribution with sufficient technical depth
4. **Implementation** — Practical system details, complexity, challenges solved
5. **Evaluation** — Rigorous experimental methodology, baseline comparisons, sensitivity analysis
6. **Related Work** — Thorough positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

SOSP values papers that show **maturity of thought**: thorough motivation, honest discussion of tradeoffs, and reproducibility through evaluation.

## SOSP-Specific Writing Conventions

### Introduction Structure for SOSP Papers

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation
Modern [systems/applications] increasingly demand [requirements].
Current [systems/solutions] fail to meet these demands because [limitation].
As [trend] continues, this gap becomes more critical.

% Paragraph 2: Why existing approaches fail
Prior systems have addressed [related problems] through [approaches].
However, these systems assume [assumption] that no longer holds due to [changes].
Alternatively, [approaches] achieve [benefit] but sacrifice [property].

% Paragraph 3: Our approach
In this paper, we present [Name], a new [system/approach] that achieves [benefit]
while maintaining [properties]. The key insight is that [insight].
[Name] leverages [technical mechanism] to address [challenge].

% Paragraph 4: Contributions (numbered)
This paper makes the following contributions:
\begin{itemize}
    \item We design and implement [Name], a [system] that achieves [benefit].
    \item We identify key design principles: [principles].
    \item We evaluate [Name] on [workloads] showing [results].
    \item We make [artifacts] available.
\end{itemize}
```

### Design Section Structure

```latex
\section{Design}

\subsection{Overview}
\autoref{fig:overview} shows the high-level architecture of [Name].
The system consists of [components] that interact via [interfaces].

\subsection{Component A}
Component A handles [responsibility] by [mechanism].
Key design decisions:
\begin{itemize}
    \item \textbf{Decision 1:} [Rationale]
    \item \textbf{Decision 2:} [Trade-off analysis]
\end{itemize}

\subsection{Component B}
...

\subsection{Handling Edge Cases}
[Name] handles [challenging cases] by [mechanism].
```

### Implementation Section

```latex
\section{Implementation}
We implemented [Name] in [lines of code] of [language/framework].
Key implementation challenges:

\textbf{Challenge 1:} [Description]
We addressed this by [approach].

\textbf{Challenge 2:} [Description]
We addressed this by [approach].

The implementation required [N] months of effort and consists of:
\begin{itemize}
    \item Core system: [N] lines
    \item Supporting libraries: [N] lines
    \item Benchmark harnesses: [N] lines
\end{itemize}
```

## Theorem Environments

Use formal environments for papers with theoretical components:

```latex
\theoremstyle{plain}
\newtheorem{property}{Property}
\newtheorem{invariant}{Invariant}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
```

## Code Listings

```latex
% Inline code:
The replica uses \lstinline!two-phase commit! to ensure consistency.

% Code blocks:
\begin{lstlisting}[language=C++, caption={Configuration entry schema}, label={lst:config}]
struct ConfigEntry {
    uint64_t term;
    uint64_t index;
    ClusterConfig config;
    std::vector<uint8_t> data;
};
\end{lstlisting}
```

## Systems Evaluation Standards

```latex
\section{Evaluation}
We evaluate [Name] to answer:

\textbf{RQ1:} How does [Name] perform compared to [baselines]?

\textbf{RQ2:} What is the overhead of [Name]'s mechanisms?

\textbf{RQ3:} How does [Name] scale to [larger workloads]?

\subsection{Experimental Setup}
\textbf{Platform:} [Hardware configuration]
\textbf{Workloads:} [Description of workloads]
\textbf{Baselines:} [List of comparison systems]

\subsection{Microbenchmarks}
\autoref{fig:micro} shows component-level performance...
```

### Performance Results Table

```latex
\begin{table}[h]
  \caption{End-to-end performance comparison (throughput in ops/sec,
    latency in ms). Best results in \textbf{bold}.}
  \label{tab:perf}
  \centering
  \begin{tabular}{lrrrr}
    \toprule
    \multirow{2}{*}{System} & \multicolumn{2}{c}{Throughput} &
      \multicolumn{2}{c}{Latency (P99)} \\
    \cmidrule(lr){2-3}\cmidrule(lr){4-5}
          & Mean & SD & Mean & SD \\
    \midrule
    Baseline & 10.2K & 0.3K & 2.3 & 0.1 \\
    Related Work & 8.7K & 0.2K & 3.1 & 0.2 \\
    \textbf{Ours} & \textbf{18.7K} & \textbf{0.4K} & \textbf{1.1} & \textbf{0.05} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Figures and Tables

- Use vector formats (.pdf, .eps) for all figures
- Ensure grayscale legibility — reviewers print in B&W
- Self-contained captions: describe what to observe, not just the topic
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/architecture}
  \caption{System architecture: (a) shows the overall structure,
    (b) details the data flow between components, (c) shows the
    control plane protocol.}
  \label{fig:architecture}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{doe2025}      % Doe et al. (2025)
\citep{doe2025}      % (Doe et al. 2025)
```

All references must list **every author by full name** — no "et al." substitutions in the bibliography.

## Formatting Rules

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## SOSP Writing Conventions

SOSP has particular expectations for systems papers:

- **Motivation must be compelling** — explain why the problem is important and why existing solutions are insufficient before presenting your design
- **Design depth** — describe the actual mechanisms, not just high-level architecture; include design rationale and alternatives considered
- **Implementation maturity** — describe the real challenges encountered when building the system
- **Evaluation rigor** — compare against the best existing systems, include sensitivity analysis, and discuss limitations honestly
- **Reproducibility** — include enough detail for others to reproduce; artifacts are valued

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] `\documentclass[sigplan,review,anonymous]`
- [ ] All author identification removed
- [ ] No self-referential citations in first person
- [ ] Anonymized all URLs and external links
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`
- [ ] Design rationale explained
- [ ] Implementation challenges discussed
- [ ] Limitations acknowledged

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Add acknowledgments if desired
- [ ] Enable page numbers
- [ ] Verify all figures in final format
