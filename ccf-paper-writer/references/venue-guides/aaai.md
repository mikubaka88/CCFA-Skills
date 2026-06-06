# AAAI Venue Guide

> Migrated from the legacy `ccf-conference-skills/aaai/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `aaai` |
| Venue family | AI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/AAAI/aaai2026_template.tex` |
| Official URL | https://aaai.org/conference/aaai/aaai-26 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# AAAI 2026 Conference Writing Skill

**CCF-A | AI | Publisher: AAAI**
**Conference:** https://aaai.org/conference/aaai/aaai-26
**Template:** `ccf-latex-templates/AAAI/aaai2026_template.tex`

## Document Setup

### Preamble Structure

```latex
\documentclass[letterpaper]{article}

% Switch between modes:
% Uncomment for anonymous submission:
% \def\aaaianonymous{true}

% Conditional package loading:
\ifdefined\aaaianonymous
    \usepackage[submission]{aaai2026}
\else
    \usepackage{aaai2026}
\fi

% REQUIRED fonts (DO NOT CHANGE):
\usepackage{times}
\usepackage{helvet}
\usepackage{courier}
\usepackage[hyphens]{url}
\usepackage{graphicx}
\urlstyle{rm}
\def\UrlFont{\rm}

% REQUIRED (no options):
\usepackage{natbib}
\usepackage{caption}
\frenchspacing
\setlength{\pdfpagewidth}{8.5in}
\setlength{\pdfpageheight}{11in}

% Required pdfinfo:
\pdfinfo{
/TemplateVersion (2026.1)
}
```

### Required Packages

Always include these packages in the exact order shown. The template enforces Times font via `times`, `helvet`, and `courier` packages — this is **mandatory** and cannot be changed.

### Submission vs Camera-Ready

| Mode | Declaration | Effect |
|------|-------------|--------|
| Anonymous Submission | `\def\aaaianonymous{true}` | Hides author info, no copyright notice |
| Camera-Ready | Comment out `\def\aaaianonymous` | Shows authors, includes copyright |

## Page Limits

- **Main content:** 7 pages
- **References:** 1 page (separate)
- **Total submission:** 8 pages maximum
- Camera-ready: Follow conference-specific guidelines

## Anonymity Requirements

For anonymous submission mode:
1. Author names and affiliations must not appear
2. Use "Anonymous Submission" as sole author
3. Anonymize self-citations (cite as third person)
4. Clear PDF metadata with a metadata-cleaning tool
5. Do not include links that reveal identity
6. References to authors' previous work must be anonymized

## Title and Author Formatting

```latex
% Single institution:
\author{
    Author Name
}
\affiliations{
    Affiliation Name\\
    Address Line 1\\
    email@example.com
}

% Multiple institutions with superscripts:
\author{
    Author One\textsuperscript{\rm 1},
    Author Two\textsuperscript{\rm 2}
}
\affiliations{
    \textsuperscript{\rm 1}Affiliation 1\\
    \textsuperscript{\rm 2}Affiliation 2\\
    first@affil1.com, second@affil2.com
}
```

Use `\equalcontrib` for equal contribution footnotes.

## Abstract and Links

```latex
\begin{abstract}
Your abstract here (no references in abstract).
\end{abstract}

% For camera-ready (only):
\begin{links}
    \link{Code}{https://example.com/code}
    \link{Datasets}{https://example.com/datasets}
\end{links}
```

## Section Organization

Arrange sections in this order:
1. Main content sections (numbered)
2. Appendices (optional, use `\appendix` then lettered sections)
3. Ethical Statement (optional, unnumbered)
4. Acknowledgments (optional, unnumbered)
5. References (unnumbered, last section)

### Recommended Section Structure for AI Papers

1. **Introduction** — Problem statement, motivation, contributions (enumerate 3-5 key contributions)
2. **Related Work** — Background and positioning against prior work
3. **Preliminaries** — Mathematical notation, definitions, background concepts
4. **Methodology** — Core algorithm/model with sufficient technical depth
5. **Experiments** — Datasets, baselines, metrics, results, statistical analysis
6. **Conclusion** — Summary, limitations, future work

### Writing the Introduction (Critical for AAAI)

AAAI reviewers often decide within the first page. Structure your introduction as:

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation (2-3 sentences)
The problem of X has become increasingly important due to Y...

% Paragraph 2: Gap in existing work (2-3 sentences)
Prior work has addressed X through approaches A, B, and C.
However, these approaches suffer from limitations including...

% Paragraph 3-4: Our approach (3-4 sentences)
In this paper, we propose a novel approach that...
Key contributions of our work include:
\begin{itemize}
    \item A new formulation of X as a Y problem...
    \item An efficient algorithm with O(n) complexity...
    \item Extensive experiments on 5 benchmark datasets...
\end{itemize}

% Paragraph 5: Paper roadmap (optional)
The remainder of this paper is organized as follows...
```

## Figures and Tables

- Use `.jpg`, `.png`, or `.pdf` only (no `.eps`, `.ps`, `.gif`)
- Place at top of page when possible
- Caption **under** the figure, **above** the table
- 9-point minimum for caption text, 10-point roman
- Use `booktabs` for professional tables (no vertical rules)
- Number figures/tables sequentially

```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.9\linewidth]{figure}
\caption{Figure caption here.}
\label{fig:example}
\end{figure}

% Professional table with booktabs:
\begin{table}[t]
\caption{Main results on benchmark datasets. Best results in \textbf{bold}.}
\label{tab:results}
\centering
\begin{tabular}{lccc}
    \toprule
    Dataset & Method A & Method B & Ours \\
    \midrule
    Dataset1 & 85.2 & 87.4 & \textbf{91.3} \\
    Dataset2 & 72.1 & 75.8 & \textbf{79.2} \\
    \bottomrule
\end{tabular}
\end{table}
```

## References (natbib)

The `aaai2026.sty` automatically sets the bibliography style. Use natbib commands:

```latex
% In preamble:
\usepackage{natbib}  % NO options

% In document:
\bibliography{your_bibfile}

% Citation commands:
\citet{key}         % (Author Year)
\shortcite{key}     % (Year)
\citeauthor{key}    % Author
\citeyear{key}      % Year
```

For self-citations in anonymous mode: cite in third person ("Smith et al. showed..." not "we showed").

### Bibliography Best Practices

```latex
% Good bibliography entry:
@inproceedings{smith2024example,
  author    = {Smith, John and Doe, Jane},
  title     = {A Novel Approach to X},
  booktitle = {Proceedings of AAAI},
  year      = {2024},
  pages     = {1234--1245},
  publisher = {AAAI}
}

% For anonymous submission, cite as:
Smith et al. showed that...  % Instead of We showed...
```

## Disallowed Commands and Packages

**Forbidden packages:**
- `authblk`, `balance`, `color`, `CJK`, `float`, `flushend`, `fontenc`
- `fullpage`, `geometry`, `grffile`, `hyperref`, `navigator`
- `multicol`, `nameref`, `savetrees`, `setspace`, `stfloats`
- `tabu`, `titlesec`, `tocbibind`, `ulem`, `wrapfig`

**Forbidden commands:**
- `\nocopyright`, `\addtolength`, `\balance`, `\baselinestretch`
- `\clearpage`, `\columnsep`, `\newpage`, `\pagebreak`
- `\pagestyle`, `\tiny`, `\vspace{-...}`, `\vskip{-...}`

## Typography Rules

- **Font:** Times Roman or Nimbus (required)
- **Size:** 10-point text with 12-point leading
- **Margins:** 0.75" sides, 0.75" top (non-first pages), 1.25" bottom
- **Columns:** Two-column format (required)
- **No color text** — color only in figures (CMYK, not RGB)
- **No Type 3 fonts** in any portion including graphics

## AI-Specific Writing Conventions

### Mathematical Notation

Define all notation clearly before use:

```latex
\section{Preliminaries}
Let $\mathcal{X} = \{x_1, \dots, x_n\}$ denote the set of input instances...
We use bold lowercase letters $\mathbf{x}$ for vectors and uppercase
$\mathbf{X}$ for matrices. $\|\mathbf{x}\|_2$ denotes the Euclidean norm.
```

### Algorithm Description

```latex
\begin{algorithm}[tb]
\caption{The Proposed Algorithm}
\label{alg:proposed}
\begin{algorithmic}[1]
\REQUIRE Dataset $\mathcal{D}$, learning rate $\eta$, epochs $T$
\ENSURE Trained model parameters $\theta$
\STATE Initialize $\theta_0$ randomly
\FOR{$t = 1$ to $T$}
    \STATE Sample mini-batch $\mathcal{B} \sim \mathcal{D}$
    \STATE Compute gradient $\nabla \mathcal{L}(\theta_{t-1}; \mathcal{B})$
    \STATE Update $\theta_t \leftarrow \theta_{t-1} - \eta \nabla \mathcal{L}$
\ENDFOR
\RETURN $\theta_T$
\end{algorithmic}
\end{algorithm}
```

### Experiment Reporting Standards

AAAI expects rigorous experimental evaluation:

```latex
\section{Experiments}
\subsection{Setup}
We evaluate on four benchmark datasets:
\begin{itemize}
    \item \textbf{Dataset A}: X instances, Y features, source: URL
    \item \textbf{Dataset B}: ...
\end{itemize}
Metrics: Accuracy, F1-score (macro-averaged), and AUC-ROC.
We compare against: (1) baseline method, (2) state-of-the-art method A,
(3) state-of-the-art method B. All experiments run 5 times with different
random seeds; we report mean $\pm$ standard deviation.

\subsection{Main Results}
Results are summarized in \autoref{tab:results}.
Our method outperforms all baselines with statistically significant
improvements (paired t-test, $p < 0.01$).

\subsection{Ablation Study}
We ablate each component of our approach in \autoref{tab:ablation}.
Removing component X degrades performance by Y\%, confirming its importance.
```

## Rebuttal Preparation

AAAI uses author responses during review:

```latex
\section*{Response to Reviewers}

% Address each concern systematically
\textbf{Regarding Reviewer 1's concern about X:}
We thank the reviewer for this comment. To clarify...
[Provide additional evidence, analysis, or explanation]

\textbf{Regarding the comparison with Y:}
We added new experiments comparing with Y in the supplementary material.
Results show our method remains superior even under the suggested settings.
```

### Rebuttal Do's and Don'ts

**DO:**
- Thank reviewers for constructive feedback
- Address every concern systematically
- Provide new evidence when asked
- Be polite and professional
- Acknowledge valid criticisms

**DON'T:**
- Be defensive or argumentative
- Dismiss concerns without explanation
- Make unsubstantiated claims
- Argue about scores

## Camera-Ready Specifics

After acceptance:
1. Comment out `\def\aaaianonymous{true}`
2. Add complete author/affiliation information
3. Include links environment with code/dataset URLs
4. Sign and submit AAAI copyright form
5. Submit as single `.tex` file (no `\input` for sections)
6. Include `.bib` file(s) separately

### Camera-Ready Checklist

- [ ] Anonymous flag commented out
- [ ] All author names and affiliations complete
- [ ] `\begin{links}` with code/dataset URLs added
- [ ] Copyright form signed and submitted
- [ ] Single `.tex` file (no `\input` commands)
- [ ] `.bib` file included separately
- [ ] All figures in correct format
- [ ] Compiles without errors

## Checklist Before Submission

- [ ] Compiles with `pdflatex` without errors
- [ ] Author info removed (submission) or complete (camera-ready)
- [ ] PDF uses only Type-1 or Embedded TrueType fonts
- [ ] All figures in .jpg/.png/.pdf format
- [ ] No forbidden packages or commands used
- [ ] Page count within limits (7+1 pages)
- [ ] References in correct format using natbib
- [ ] Abstract contains no citations
- [ ] Self-citations anonymized (submission mode)
- [ ] All notation defined before use
- [ ] Experimental results include statistical significance
- [ ] Introduction clearly states contributions
