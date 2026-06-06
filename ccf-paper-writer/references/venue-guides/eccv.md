# ECCV Venue Guide

> Migrated from the legacy `ccf-conference-skills/eccv/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `eccv` |
| Venue family | AI |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ECCV/main.tex` |
| Official URL | https://eccv.ecva.net/Conferences/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ECCV 2026 Conference Writing Skill

**CCF-B | AI | Publisher: Springer**
**Conference:** https://eccv.ecva.net/Conferences/2026
**Template:** `ccf-latex-templates/ECCV/main.tex`
**Base:** Springer LNCS (llncs.cls)

## Document Setup

### Preamble Structure

```latex
\documentclass[runningheads]{llncs}

% === MODE SELECTION ===
% Review version:
\usepackage[review,year=2026,ID=*****]{eccv}
% OR for camera-ready:
% \usepackage{eccv}

% Abbreviations:
\usepackage{eccvabbrv}

% Packages:
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{subcaption}

% Hyperref:
\usepackage[pagebackref,breaklinks,colorlinks,citecolor=eccvblue]{hyperref}
```

### Mode Options

| Mode | Declaration | Features |
|------|-------------|----------|
| Review | `\usepackage[review,year=2026,ID=*****]{eccv}` | Line numbers, anonymized, paper ID on each page |
| Camera-Ready | `\usepackage{eccv}` | No line numbers, author info |

Replace `*****` with your assigned paper ID.

## Page Limits

- **Main content:** 14 pages maximum
- **Excluded:** References, acknowledgments
- Papers exceeding 14 pages **will be rejected without review**
- This is a generous limit compared to CVPR/ICCV

## Anonymity Requirements (Double-Blind)

1. No author identification in submission
2. Use `\author{}` with real names only for camera-ready
3. Third-person self-citations ("Smith et al. showed..." not "we showed...")
4. Remove acknowledgments from submission
5. Anonymize identifying URLs
6. If citing concurrent submission: cite anonymously, include anonymized copy as supplementary

## Title and Author Formatting

```latex
\title{Full Paper Title}

% Short title for running head:
\titlerunning{Abbreviated paper title}

% Full author list (for camera-ready):
\author{First Author\inst{1}\orcidlink{0000-1111-2222-3333} \and
Second Author\inst{2,3}\orcidlink{1111-2222-3333-4444} \and
Third Author\inst{3}\orcidlink{2222-3333-4444-5555}}

% Abbreviated for running head:
\authorrunning{F. Author et al.}

% Full affiliations:
\institute{
  Princeton University, Princeton NJ 08544, USA \and
  ABC Institute, Rupert-Karls-University Heidelberg, Germany\\
  \email{\{abc\}@uni-heidelberg.de}
}
```

## Abstract and Keywords

```latex
\begin{abstract}
The abstract should concisely summarize the contents of the paper.
While there is no fixed length restriction, approximately 150 words is recommended.
Please include keywords as shown below.
\keywords{First keyword \and Second keyword \and Third keyword}
\end.Abstract}
```

## Recommended CV Paper Structure for ECCV

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
% What is the task? Why is it important?

% Paragraph 3: Gap in prior work
% What have others done? What are their limitations?

% Paragraph 4: Our approach
% What is our key insight?

% Paragraph 5: Contributions (numbered)
The main contributions of this work are:
\begin{itemize}
    \item We propose a novel approach to X that achieves Y...
    \item We introduce a new benchmark dataset for...
    \item We demonstrate through extensive experiments that...
\end{itemize}

\section{Related Work}
% Categorize prior work by approach type
% Position your work against each category

\section{Preliminaries}
% Notation, definitions, background concepts

\section{Method}
% Core technical contribution
% Include figures showing architecture

\section{Experiments}
\subsection{Setup}
% Datasets, metrics, baselines, implementation

\subsection{Results}
% Main findings in tables
% Comparison with state-of-the-art

\subsection{Ablation and Analysis}
% Study each component
% Qualitative results

\section{Conclusion}
% Summary, limitations, future work
```

## Figures and Tables

### Figure Guidelines

```latex
\begin{figure}[tb]
  \centering
  \includegraphics[height=6.5cm]{figure}
  \caption{
    One kernel at $x_s$ (\emph{dotted kernel}) or two kernels at $x_i$ and $x_j$.
    Elements described in caption should be set in italics, in parentheses.
  }
  \label{fig:example}
\end{figure}

% Full-width figure:
\begin{figure*}[tb]
  \centering
  \includegraphics[width=0.9\textwidth]{figure}
  \caption{Full-width figure caption.}
  \label{fig:wide}
\end{figure*}
```

- Caption **below** figures
- Use vector formats (PDF, EPS)
- 800 DPI minimum for line drawings
- 6pt minimum font size in figures

### Table Guidelines

```latex
\begin{table}[tb]
  \caption{
    Font sizes of headings.
    Table captions should always be positioned \emph{above} the tables.
  }
  \label{tab:headings}
  \centering
  \begin{tabular}{@{}lll@{}}
    \toprule
    Heading level & Example & Font size\\
    \midrule
    Title & 14pt, bold & centered \\
    1st-level & 12pt, bold & left \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Caption **above** tables
- Use `booktabs`
- No vertical rules

## Vision-Specific Writing Conventions

### Dataset Description

```latex
\section{Experiments}
\subsection{Datasets}
We evaluate on standard vision benchmarks:

\begin{itemize}
    \item \textbf{COCO}: 118K training, 5K validation images.
    \item \textbf{ADE20K}: 20K training, 2K validation images.
    \item \textbf{Cityscapes}: 2,975 training, 500 validation images.
\end{itemize}
```

### Evaluation Metrics

```latex
\subsection{Metrics}
We report standard vision metrics:
\begin{itemize}
    \item \textbf{Object detection:} mAP@0.5:0.95 (COCO standard)
    \item \textbf{Semantic segmentation:} mIoU
    \item \textbf{Instance segmentation:} AP$^{bbox}$, AP$^{mask}$
    \item \textbf{Panoptic segmentation:} PQ
\end{itemize}
```

## References (Springer LNCS Style)

```latex
\bibliographystyle{splncs04}
\bibliography{main}
```

Citation format:
```latex
\cite{Author22}           % [1]
\citep{Author22}          % [1]
\citet{Author22}          % Author (2022)
```

## Heading Styles (LNCS)

| Level | Format | Numbering |
|-------|--------|-----------|
| Title | 14pt, bold, centered | No |
| 1st-level | 12pt, bold, left | Yes |
| 2nd-level | 10pt, bold, left | Yes |
| 3rd-level | 10pt, bold, left | No |

Capitalize headings (first word + content words).

## Camera-Ready Compilation

1. Comment out review mode:
```latex
% \usepackage[review,year=2026,ID=*****]{eccv}
\usepackage{eccv}
```

2. Add complete author information with ORCID
3. Include acknowledgments (unnumbered section)
4. Remove line numbers
5. Update hyperref settings
6. Verify 14-page limit

## Checklist Before Submission

- [ ] 14 pages or fewer (excluding references)
- [ ] Paper ID on each page (review mode)
- [ ] No author identification
- [ ] Third-person self-citations
- [ ] References in splncs04 format
- [ ] Figure captions below, table captions above
- [ ] Heading capitalization correct
- [ ] No \vspace or \hspace modifications
- [ ] DOIs included in references
- [ ] Acknowledgments removed from submission
