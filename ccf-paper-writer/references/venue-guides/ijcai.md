# IJCAI Venue Guide

> Migrated from the legacy `ccf-conference-skills/ijcai/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ijcai` |
| Venue family | AI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/IJCAI/ijcai26.tex` |
| Official URL | https://2026.ijcai.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# IJCAI 2026 Conference Writing Skill

**CCF-A | AI | Publisher: Morgan Kaufmann (IJCAI-ECAI Joint)**
**Conference:** https://2026.ijcai.org
**Template:** `ccf-latex-templates/IJCAI/ijcai26.tex`

## Document Setup

### Preamble Structure

```latex
\documentclass{article}
\pdfpagewidth=8.5in
\pdfpageheight=11in

\usepackage{ijcai26}

% Required packages:
\usepackage{times}
\usepackage{soul}
\usepackage{url}
\usepackage[hidelinks]{hyperref}
\usepackage[utf8]{inputenc}
\usepackage[small]{caption}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage[switch]{lineno}

% Line numbering - comment out for camera-ready:
\linenumbers

\urlstyle{same}

% REQUIRED pdfinfo (MUST include):
\pdfinfo{
/TemplateVersion (IJCAI.2026.0)
}
```

### Line Numbering Toggle

```latex
% For submission (include line numbers):
\linenumbers

% For camera-ready (remove/comment):
% \linenumbers
```

Line numbers are **required for submission** but **forbidden for camera-ready**.

## Page Limits

- **Main content:** 7 pages
- **References/Acknowledgments/Ethics/Contribution:** Up to 2 pages
- **Total:** 9 pages maximum
- Some tracks allow purchasing extra pages (check CFP)

## Required pdfinfo Block

This is **mandatory** — include exactly as shown:

```latex
\pdfinfo{
/TemplateVersion (IJCAI.2026.0)
}
```

Omitting this block will result in rejection.

## Anonymity Requirements (Double-Blind)

For anonymous submission tracks:
1. Remove author names, affiliations, emails
2. Use third-person self-citations
3. Anonymize identifying URLs
4. Remove acknowledgments and contribution statements
5. Clear PDF metadata

```latex
% Anonymized author block:
\author{
    Anonymous Author
}
```

## Title and Author Formatting

```latex
% Single author:
\author{
    Author Name
    \affiliations
    Affiliation Name
    \emails
    email@example.com
}

% Multiple authors:
\author{
First Author$^1$
\and
Second Author$^2$\and
Third Author$^{2,3}$\And
Fourth Author$^4$}
\affiliations
$^1$First Affiliation\\
$^2$Second Affiliation\\
$^3$Third Affiliation\\
$^4$Fourth Affiliation
\emails
\{first, second\}@example.com,
third@other.example.com,
fourth@example.com
```

## IJCAI-Specific Writing Conventions

### Introduction Structure for AI Papers

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
The problem of X has become increasingly important due to Y.
Current approaches suffer from limitations including...

% Paragraph 3: Gap in prior work
Prior work has addressed X through approaches A, B, and C.
However, these approaches fail to handle...

% Paragraph 4: Our approach
In this paper, we propose a novel approach that...
Key contributions of our work include:
\begin{itemize}
    \item A new formulation of X as a Y problem...
    \item An efficient algorithm with O(n) complexity...
    \item Extensive experiments on 5 benchmark datasets...
\end{itemize}
```

### Mathematical Notation

```latex
\section{Preliminaries}
Let $\mathcal{X} = \{x_1, \dots, x_n\}$ denote the set of input instances...
We use bold lowercase letters $\mathbf{x}$ for vectors and uppercase
$\mathbf{X}$ for matrices. $\|\mathbf{x}\|_2$ denotes the Euclidean norm.
```

### Theorem Environments

```latex
% Define before \begin{document}:
\theoremstyle{plain}
\newtheorem{observation}{Observation}
\newtheorem{example}{Example}
```

## Abstract

```latex
\begin.Abstract}
The abstract should be a concise, one-paragraph summary describing
the general thesis and conclusion of your paper. The abstract should
be no more than 200 words long.
\end.Abstract}
```

## Section Organization

Required order:
1. Main content sections (numbered)
2. Appendices (optional, lettered: A, B, C...)
3. Ethical Statement (optional, unnumbered)
4. Acknowledgments (optional, unnumbered, camera-ready only)
5. Contribution Statement (optional, unnumbered, camera-ready only)
6. References (unnumbered)

```latex
% Formatting:
\section*{Ethical Statement}
\section*{Acknowledgments}
\section*{Contribution Statement}
\section*{References}
```

## Figures and Tables

```latex
% Figure: caption BELOW
\begin{figure}
  \centering
  \includegraphics[width=0.9\linewidth]{figure}
  \caption{Figure caption here (9pt).}
  \label{fig:example}
\end{figure}

% Professional tables with booktabs:
\begin{table}
  \centering
  \begin{tabular}{lrr}
    \toprule
    Scenario & $\delta$ (s) & Runtime (ms) \\
    \midrule
    Paris & 0.1 & 13.65 \\
    \bottomrule
  \end{tabular}
  \caption{Booktabs style table.}
  \label{tab:booktabs}
\end{table}
```

## Algorithms

```latex
\begin{algorithm}[tb]
  \caption{Example Algorithm}
  \label{alg:example}
  \textbf{Input:} Your input\\
  \textbf{Output:} Your output
  \begin{algorithmic}[1]
    \STATE Let $t=0$.
    \WHILE{condition}
      \STATE Do some action.
      \IF{conditional}
        \STATE Perform task A.
      \ENDIF
    \ENDWHILE
    \STATE \textbf{return} solution
  \end{algorithmic}
\end{algorithm}
```

Algorithm caption: in header, left-justified, between horizontal lines.

## Experimental Reporting

```latex
\section{Experimental Evaluation}
\subsection{Setup}
We evaluate on four benchmark datasets:
\begin{itemize}
    \item \textbf{Dataset A}: X instances, Y features, source: URL
    \item \textbf{Dataset B}: ...
\end{itemize}
Metrics: Accuracy, F1-score (macro-averaged), and AUC-ROC.
We compare against: (1) baseline method, (2) state-of-the-art method A.

\subsection{Results}
Results are summarized in \autoref{tab:results}.
Our method outperforms all baselines with statistically significant
improvements (paired t-test, $p < 0.01$).
```

## Formula Formatting

IJCAI's two-column format requires careful formula handling:

**DO NOT use small/tiny font for formulas** — this breaks line spacing and is forbidden.

```latex
% Split long formulas:
\begin{align}
  x = & \prod_{i=1}^n \sum_{j=1}^n j_i + \prod_{i=1}^n \sum_{j=1}^n i_j \label\\
  +   & \prod_{i=1}^n \sum_{j=1}^n j_i.
\end{align}
```

Rules:
- Equation numbers in same font as text (10pt)
- Formula symbols minimum 9pt
- No color in equations

## Camera-Ready Compilation

1. Comment out `\linenumbers`:
```latex
% \linenumbers
```

2. Add complete author information
3. Include acknowledgments and contribution statements
4. Update \pdfinfo block if needed
5. Verify page limits

## Formatting Rules

- **Paper size:** US Letter (8.5" × 11")
- **Font:** Times Roman
- **Text:** 10pt, 1pt leading
- **Margins:** 0.75" sides, 1.375" top (first page), 0.75" top (other pages), 1.25" bottom
- **Columns:** Two-column, 3.375" width, 0.25" gap
- **Column height:** 6.625" (first page), 9" (other pages)

## Checklist Before Submission

- [ ] `\pdfinfo{/TemplateVersion (IJCAI.2026.0)}` included
- [ ] 7 pages content + 2 pages refs/ack/ethics maximum
- [ ] `\linenumbers` included for submission
- [ ] `\linenumbers` commented for camera-ready
- [ ] No author identification (submission)
- [ ] Third-person self-citations
- [ ] Figure captions below, table captions below
- [ ] No small/tiny fonts in formulas
- [ ] Professional table formatting (booktabs)
- [ ] References in named style
- [ ] All notation defined before use
- [ ] Experimental results include statistical significance
