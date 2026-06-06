# CVPR Venue Guide

> Migrated from the legacy `ccf-conference-skills/cvpr/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `cvpr` |
| Venue family | AI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/CVPR/main.tex`, `ccf-latex-templates/CVPR/preamble.tex`, `ccf-latex-templates/CVPR/rebuttal.tex` |
| Official URL | https://cvpr2026.thecvf.com |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CVPR 2026 Conference Writing Skill

**CCF-A | AI | Publisher: CVF (IEEE)**
**Conference:** https://cvpr2026.thecvf.com
**Template:** `ccf-latex-templates/CVPR/main.tex`, `CVPR/preamble.tex`, `CVPR/rebuttal.tex`
**Shared with ICCV** — same `cvpr.sty` class

## Document Setup

### Preamble Structure

```latex
\documentclass[10pt,twocolumn,letterpaper]{article}

% === MODE SELECTION ===
\usepackage{cvpr}              % Camera-ready
\usepackage[review]{cvpr}      % Review version
% \usepackage[pagenumbers]{cvpr} % ArXiv version

% Additional packages in preamble:
\input{preamble}

% Hyperref (strongly recommended):
\definecolor{cvprblue}{rgb}{0.21,0.49,0.74}
\usepackage[pagebackref,breaklinks,colorlinks,allcolors=cvprblue]{hyperref}

% Paper ID and conference info:
\def\paperID{*****}   % Enter Paper ID
\def\confName{CVPR}
\def\confYear{2026}
```

### Template Files

The CVPR template uses multiple files:
- `main.tex` — main document
- `preamble.tex` — additional packages
- `main.bib` — bibliography
- `rebuttal.tex` — rebuttal template
- `sec/` folder — section files (optional)

### Mode Options

| Mode | Declaration | Features |
|------|-------------|----------|
| Camera-Ready | `\usepackage{cvpr}` | Final formatting |
| Review | `\usepackage[review]{cvpr}` | Line numbers, anonymized |
| ArXiv | `\usepackage[pagenumbers]{cvpr}` | Page numbers shown |

## Page Limits

- **Main content:** 8 pages maximum
- **Excluded:** References, appendix, supplementary
- Papers exceeding limit may be rejected without review

## Anonymity Requirements (Double-Blind)

1. No author names or affiliations in submission
2. Use placeholder author block:
```latex
\author{First Author\\
Institution1\\
Institution1 address\\
{\tt\small firstauthor@i1.org}
\and
Second Author\\
Institution2\\
{\tt\small secondauthor@i2.org}
}
```
3. Third-person self-citations
4. Anonymize URLs that identify authors
5. Paper ID on each page (for review)

## Title and Author Formatting

```latex
\title{\LaTeX\ Author Guidelines for \confName~\confYear~Proceedings}

\author{First Author\\
Institution1\\
Institution1 address\\
{\tt\small firstauthor@i1.org}
% Additional authors with \and:
\and
Second Author\\
Institution2\\
First line of institution2 address\\
{\tt\small secondauthor@i2.org}
}
```

## Abstract

```latex
\begin{document}
\maketitle
\input{sec/0_abstract}
% ... rest of sections
```

## Recommended CVPR Paper Structure

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
% What is the task? Why is it important?
% What are the challenges?

% Paragraph 3: Gap in prior work
% What have others done? What are their limitations?
% Why is this problem hard?

% Paragraph 4: Our approach
% What is our key insight?
% What makes our approach different?

% Paragraph 5: Contributions (numbered list)
The main contributions of this work are:
\begin{itemize}
    \item We propose a novel approach to X that achieves Y...
    \item We introduce a new benchmark dataset for...
    \item We demonstrate through extensive experiments that...
\end{itemize}

% Paragraph 6 (optional): Roadmap
The remainder of this paper is organized as follows...

\section{Related Work}
% Categorize prior work by approach or method type
% Position your work against each category
% Clearly identify the gap your work fills

\section{Preliminaries}
% Define notation, task formulation
% Background concepts necessary to understand the method

\section{Method}
% Core technical contribution
% Include figures showing architecture/pipeline
% Mathematical formulation with clear equations
% Detailed description of each component

\section{Experiments}
\subsection{Setup}
% Datasets, metrics, implementation details
% Baselines (cite properly)

\subsection{Results}
% Quantitative results in tables
% Comparison with state-of-the-art
% Statistical significance

\subsection{Ablation and Analysis}
% Study each component
% Qualitative results, visualizations
% Error analysis

\section{Conclusion}
% Summary of contributions
% Limitations
% Future directions
```

## References (IEEE Style)

```latex
\bibliographystyle{ieeenat_fullname}
\bibliography{main}

% Use small font for references:
{\small
  \bibliographystyle{ieeenat_fullname}
  \bibliography{main}
}
```

## Figures and Tables

### Figure Guidelines

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{figure}
  \caption{Figure caption below the figure.}
  \label{fig:example}
\end{figure}

% Full-width figure:
\begin{figure*}
  \centering
  \includegraphics[width=0.9\textwidth]{figure}
  \caption{Full-width figure.}
  \label{fig:wide}
\end{figure*}
```

- Place near the top of the page when possible
- Caption **below** the figure
- Use vector formats (.pdf, .eps) when possible
- 300 DPI minimum for raster images
- Ensure legible when printed in B&W

### Table Guidelines

```latex
\begin{table}
  \caption{Table caption above the table.}
  \label{tab:example}
  \centering
  \begin{tabular}{ccc}
    \toprule
    Header1 & Header2 & Header3 \\
    \midrule
    data & data & data \\
    data & data & data \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Caption **above** the table
- Use `booktabs` (no vertical rules)
- Professional-quality formatting
- Best results in **bold**, significance markers ($\dagger$, $\ddagger$)

### Subfigures with subcaption

```latex
\begin{figure}
  \centering
  \begin{subfigure}[b]{0.23\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig1}
    \caption{Input image}
    \label{fig:sub1}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.23\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig2}
    \caption{Ground truth}
    \label{fig:sub2}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.23\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig3}
    \caption{Method A}
    \label{fig:sub3}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.23\textwidth}
    \centering
    \includegraphics[width=\textwidth]{fig4}
    \caption{Ours}
    \label{fig:sub4}
  \end{subfigure}
  \caption{Comparison of different methods on the task.}
  \label{fig:main}
\end{figure}
```

## Section Organization

Standard order:
1. Abstract (in `sec/0_abstract.tex`)
2. Introduction (`sec/1_intro.tex`)
3. Related Work (optional)
4. Method
5. Experiments
6. Conclusion
7. References (in `main.bib`)
8. Appendix (optional, after references)

## CVPR-Specific Writing Conventions

### Vision-Specific Content

```latex
\section{Experiments}
\subsection{Datasets}
We evaluate on standard benchmarks:
\begin{itemize}
    \item \textbf{COCO}: 118K training, 5K validation images.
    Annotations include bounding boxes and segmentation masks.
    \item \textbf{ADE20K}: 20K training, 2K validation images.
    Scene parsing with 150 thing/stuff classes.
    \item \textbf{Cityscapes}: 2,975 training, 500 validation images.
    Urban scene understanding with 19 classes.
\end{itemize}

\subsection{Metrics}
We report standard metrics:
\begin{itemize}
    \item \textbf{Object detection:} mAP@0.5:0.95 (COCO standard)
    \item \textbf{Semantic segmentation:} mIoU
    \item \textbf{Instance segmentation:} AP$^{bbox}$, AP$^{mask}$
\end{itemize}
```

### Qualitative Results

```latex
\subsection{Qualitative Results}
\autoref{fig:qual} shows qualitative comparisons.
Our method handles challenging cases including...
(Show failure cases in supplementary)
```

## Rebuttal Preparation

CVPR uses an author response period. Use the rebuttal template:

```latex
% rebuttal.tex structure:
\section*{Response to Reviewers}

We thank the reviewer for the constructive feedback.

\textbf{R1: Regarding the concern about X...}
We address this concern in two ways: (1) We provide additional
experiments in the revised supplementary material. (2) We clarify
the design choice in the method description...

\textbf{R2: Comparison with method Y...}
We added method Y to our comparison in \autoref{tab:updated}.
Our method remains superior...

\textbf{R3: Mathematical formulation...}
The reviewer raises a valid point. We have added a more detailed
derivation in the appendix.
```

### Rebuttal Best Practices

**DO:**
- Address every point raised by each reviewer
- Provide new evidence when questioned
- Be specific and concrete
- Acknowledge valid criticisms
- Thank reviewers for their time

**DON'T:**
- Be defensive or argumentative
- Make vague promises
- Introduce new experiments without context
- Dismiss concerns without explanation

### Rebuttal Template Structure

```latex
\section*{Response to Reviewers}

\textbf{Overall:} We thank all reviewers for their time and constructive
comments. We address each concern below.

\textbf{Reviewer 1:}
\textbf{Q1: [Summarize question]}
\textbf{A:} [Your response]...

\textbf{Reviewer 2:}
\textbf{Q1: [Summarize question]}
\textbf{A:} [Your response]...

% Appendix: Any additional experiments/changes
```

## Camera-Ready Submission

1. Change to: `\usepackage{cvpr}`
2. Add complete author information
3. Set correct `\paperID`
4. Remove any anonymization
5. Verify page limits
6. Generate PDF and validate

### Camera-Ready Checklist

- [ ] `\usepackage{cvpr}` (no review option)
- [ ] All author names and affiliations complete
- [ ] Paper ID correctly set
- [ ] Page count verified (≤ 8 pages)
- [ ] All figures in final format
- [ ] References complete and properly formatted

## Supplementary Material

CVPR allows supplementary material:

```latex
% Reference supplementary in main text:
Results on additional datasets are provided in Appendix A (supplementary material).

% Supplementary structure:
\appendix
\section{Additional Qualitative Results}
% More figures, videos, etc.

\section{Implementation Details}
% Extended technical description

\section{Proofs}
% Mathematical proofs
```

### Supplementary Guidelines
- Clearly label as "Supplementary Material"
- Maximum file size as specified in CFP
- Anonymized as with main paper
- Referenced in main text
- Not required for acceptance

## Shared Template: CVPR and ICCV

CVPR and ICCV share the **same `cvpr.sty`** class and formatting rules. Use the same approach for both conferences. Key differences:
- Conference name in `\confName`
- Paper ID system may differ
- Submission systems differ (CVF for both)

## Formatting Rules

- **Paper size:** US Letter
- **Font:** Times New Roman (10pt)
- **Columns:** Two-column
- **Margins:** Standard CVPR margins
- **Line numbers:** Shown in review mode
- **Page numbers:** Hidden in review, shown in camera-ready

## Checklist Before Submission

- [ ] 8 pages or fewer (excluding refs/appendix)
- [ ] No author identification
- [ ] Paper ID on each page
- [ ] Third-person self-citations
- [ ] References use ieeenat_fullname style
- [ ] Figure captions below, table captions above
- [ ] Vector figures preferred
- [ ] B&W legible figures
- [ ] All figures referenced in text
- [ ] Supplementary material noted (if any)
- [ ] Proper notation defined before use
- [ ] State-of-the-art baselines compared
- [ ] Ablation experiments included
- [ ] Statistical significance reported
