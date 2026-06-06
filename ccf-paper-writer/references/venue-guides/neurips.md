# NeurIPS Venue Guide

> Migrated from the legacy `ccf-conference-skills/neurips/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `neurips` |
| Venue family | AI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/NeurIPS/neurips_2026.tex` |
| Official URL | https://nips.cc/Conferences/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# NeurIPS 2026 Conference Writing Skill

**CCF-A | AI | Publisher: MIT Press**
**Conference:** https://nips.cc/Conferences/2026
**Template:** `ccf-latex-templates/NeurIPS/neurips_2026.tex`

## Document Setup

### Preamble Structure

```latex
\documentclass{article}

% === TRACK SELECTION (for submission) ===
\usepackage{neurips_2026}           % Default: main track (double-blind)
% Or specify track:
% \usepackage[main]{neurips_2026}           % Main Track
% \usepackage[position]{neurips_2026}        % Position Paper Track
% \usepackage[eandd]{neurips_2026}           % E&D Track
% \usepackage[creativeai]{neurips_2026}      % Creative AI Track
% \usepackage[sglblindworkshop]{neurips_2026}% Workshop (single-blind)
% \usepackage[dblblindworkshop]{neurips_2026}% Workshop (double-blind)

% === AFTER ACCEPTANCE: Add final option ===
% \usepackage[main, final]{neurips_2026}    % Camera-ready

% === FOR ARXIV/PREPRINT ===
% \usepackage[preprint]{neurips_2026}       % Non-anonymous, "Preprint" footer

% === OPTIONAL: Pass options to natbib ===
% \PassOptionsToPackage{numbers, compress}{natbib}
% Before loading neurips_2026

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{hyperref}
\usepackage{url}
\usepackage{booktabs}
\usepackage{amsfonts}
\usepackage{nicefrac}
\usepackage{microtype}
\usepackage{xcolor}
```

### Track Options

| Track | Option | Review Type | Page Limit |
|-------|--------|-------------|------------|
| Main Track | `main` | Double-blind | 9 pages content |
| Position Paper | `position` | Double-blind | Check CFP |
| E&D Track | `eandd` | Double-blind | Check CFP |
| Creative AI | `creativeai` | Double-blind | Check CFP |
| Workshop (single-blind) | `sglblindworkshop` | Single-blind | Check CFP |
| Workshop (double-blind) | `dblblindworkshop` | Double-blind | Check CFP |

## Page Limits

- **Main content:** 9 pages maximum (strictly enforced)
- **Excluded from count:** Acknowledgments, references, checklist, technical appendices
- Papers exceeding page limit **will not be reviewed**
- For arXiv: Use `preprint` option

## Anonymity Requirements

Double-blind reviewing is default:
1. Do not refer to your own work in first person
2. Use third person: "Smith et al. showed..." not "we showed..."
3. For papers under review: cite as "Anonymous" or omit
4. Include anonymized copies of closely related work in supplementary

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

\author{%
  First Author\thanks{Use footnote for funding, web pages, etc.} \\
  Department\\
  University\\
  \texttt{email@example.com}
  % Use \And for LaTeX to decide break point
  % Use \AND to force a line break
  \And
  Second Author\\
  Affiliation\\
  \texttt{email2@example.com}
}
```

Multi-author formatting:
- `\And` — lets LaTeX decide where to break lines
- `\AND` — forces a line break at that point

## Abstract

```latex
\begin{document}
\maketitle

\begin{abstract}
  Abstract paragraph: indented 0.5 inch on both margins.
  Use 10 point type with 11 point leading.
  Word "Abstract" is centered, bold, 12 point.
  One paragraph only.
\end{abstract}
```

## Section Organization

Standard order:
1. Main content (numbered sections)
2. Acknowledgments (`\section*{Acknowledgments}`) — **not in submission**
3. References (`\section*{References}`) — unnumbered, small font allowed

For camera-ready, include:
- Funding disclosure
- Competing interests declaration
- Optional technical appendices (no page limit)

### Recommended ML Paper Structure

```latex
\section{Introduction}
% 1. Problem motivation (1-2 paragraphs)
% 2. Gap in existing work (1 paragraph)
% 3. Our approach and contributions (bullet points)
% 4. Paper roadmap

\section{Preliminaries}
% Notation, definitions, background concepts
% Define: dataset notation, model architecture, loss functions

\section{Method}
% Core contribution - describe clearly and completely
% Use figures to illustrate architecture when possible
% Include mathematical formulation with clear equations

\section{Experiments}
\subsection{Setup}
% Datasets, metrics, baselines, implementation details

\subsection{Main Results}
% Present main findings in tables/figures
% Compare against strong baselines
% Include statistical significance when appropriate

\subsection{Ablation and Analysis}
% Study contribution of each component
% Error analysis, qualitative examples

\section{Related Work}
% Position your work against existing literature
% Categorize by approach, not just list

\section{Conclusion}
% Summary, limitations, future directions
```

## Figures and Tables

```latex
\begin{figure}
  \centering
  % Use \fbox with rules as placeholder
  \fbox{\rule[-.5cm]{0cm}{4cm} \rule[-.5cm]{4cm}{0cm}}
  \caption{Sample figure caption.}
  \label{fig:sample}
\end{figure}
```

- Caption **after** figure, lowercase except first word/proper nouns
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- Color allowed for figures (ensure legible in B&W too)

```latex
\begin{table}
  \caption{Sample table caption.}
  \label{tab:sample}
  \centering
  \begin{tabular}{lll}
    \toprule
    Column 1 & Column 2 & Column 3 \\
    \midrule
    Data & Data & Data \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References (natbib)

`natbib` is loaded automatically. Use consistently (author/year or numeric):

```latex
% Author-year citations:
\citet{hasselmo}  % Hasselmo, et al. (1995) investigated...
\citep{sabato}    % (Smith et al. 2025)

% Numeric citations:
% Load with \PassOptionsToPackage{numbers}{natbib} before neurips_2026

% References section:
\section*{References}
{\small
  % Any citation style is acceptable if consistent
  [1] Author, A. (2025). Title. Journal.
}
```

## Formatting Rules

- **Paper size:** US Letter
- **Margins:** 1.5" left, 1" top, 5.5" text width, 9" text height
- **Font:** Times New Roman preferred (automatic)
- **Text:** 10 point, 11 point leading
- **Paragraphs:** No indentation, half-line spacing between paragraphs
- **Sections:** Lowercase except first word/proper nouns, flush left, bold
- **Headings:** 12pt first-level, 10pt second-level, 10pt third-level

## Math and Display Equations

Use LaTeX commands (not bare TeX) for display math:

```latex
% Use these (not $$...$$):
\begin{equation}
  E = mc^2
\end{equation}

\begin{align}
  x &= y + z \\
  a &= b + c
\end{align}
```

## Algorithm Formatting

```latex
\usepackage{algorithm}
\usepackage{algorithmic}

\begin{algorithm}[tb]
  \caption{Bubble Sort}
  \label{alg:example}
  \begin{algorithmic}
    \STATE {\bfseries Input:} data $x_i$, size $m$
    \REPEAT
    \STATE Initialize $noChange = true$.
    \FOR{$i=1$ {\bfseries to} $m-1$}
      \IF{$x_i > x_{i+1}$}
        \STATE Swap $x_i$ and $x_{i+1}$
      \ENDIF
    \ENDFOR
    \UNTIL{$noChange$ is $true$}
  \end{algorithmic}
\end{algorithm}
```

## NeurIPS-Specific Writing Conventions

### Theoretical Contributions

For papers with theoretical analysis:

```latex
\section{Theoretical Analysis}
\begin{assumption}
\label{assum:linear}
The data points $\{x_i\}$ are drawn i.i.d. from a distribution $P$
with bounded second moment...
\end{assumption}

\begin{theorem}
\label{th:convergence}
Under Assumption \ref{assum:linear}, the proposed algorithm converges
to the optimal solution at a rate of $O(1/t)$.
\end{theorem}

\begin{Proof}
% Proof here
\end{Proof}
```

### Experimental Rigor

NeurIPS expects thorough experimental evaluation:

```latex
\section{Experiments}
\subsection{Setup}
\textbf{Datasets:} We evaluate on 6 benchmark datasets spanning
computer vision (CIFAR-10, ImageNet) and NLP (GLUE, SQuAD) domains.

\textbf{Baselines:} We compare against: (1) standard methods,
(2) state-of-the-art approaches from recent conferences.

\textbf{Implementation:} All models trained on NVIDIA A100 GPUs.
Learning rate selected via grid search on validation set.
Code available at [anonymized URL].

\textbf{Metrics:} Accuracy for classification, F1 for sequence labeling,
BLEU/ROUGE for generation tasks.

\subsection{Main Results}
Results in \autoref{tab:main} show our method consistently outperforms
baselines. Improvements are statistically significant (paired t-test,
$p < 0.01$) across all datasets.

\subsection{Ablation Study}
\autoref{tab:ablation} ablates each component of our approach.
Removing the attention mechanism (row 2) degrades performance by 3.2\%,
confirming its importance to the overall method.
```

### Reproducibility

NeurIPS has a reproducibility checklist. Address these in your paper:

```latex
% In supplementary or appendix:
\section*{Reproducibility}
\subsection{Hyperparameters}
All hyperparameters and their search ranges are listed in
\autoref{tab:hyper}.

\subsection{Computational Resources}
Training required approximately 48 GPU hours on NVIDIA V100 GPUs.
Inference runs in real-time on a single GPU.

\subsection{Statistical Tests}
All comparisons use paired t-tests with Bonferroni correction for
multiple comparisons. Confidence intervals are 95\%.
```

## Rebuttal Preparation

NeurIPS uses author responses during review:

```latex
\section*{Response to Reviewers}

We thank the reviewers for their thoughtful comments and constructive feedback.

\textbf{Regarding Reviewer X's concern about Y:}
We agree that Y is an important consideration. Our experiments in
Figure Z address this concern by showing that...

\textbf{Regarding the comparison with Z:}
We have added comparisons with Z in the revised submission.
Results demonstrate that our method maintains advantages even under
the suggested evaluation protocol.

\textbf{Regarding theoretical assumptions:}
The reviewer raises a valid point. We acknowledge this limitation
and discuss it in the revised Related Work section.
```

## Final/Camera-Ready Compilation

After acceptance:
1. Add `final` option: `\usepackage[main, final]{neurips_2026}`
2. Add author acknowledgments and funding
3. Complete `\author{}` block with all authors
4. Remove any anonymization

**Do NOT use `final` option for arXiv/preprint versions.**

### Camera-Ready Checklist

- [ ] `final` option added to `\usepackage`
- [ ] All author names and affiliations complete
- [ ] Acknowledgments section added
- [ ] Funding disclosures included
- [ ] Competing interests declared (if applicable)
- [ ] Anonymization removed
- [ ] References and appendix complete

## Checklist Before Submission

- [ ] 9 pages or fewer (content only)
- [ ] No author identification in submission
- [ ] Third-person self-citations only
- [ ] Type-1 or Embedded TrueType fonts only
- [ ] US Letter paper size
- [ ] PDF generated with `pdflatex`
- [ ] Consistent citation style
- [ ] No forbidden modifications to style files
- [ ] All notation defined before use
- [ ] Experimental results include baselines
- [ ] Statistical significance testing performed
- [ ] Ablation studies included
- [ ] Code/anonymized supplementary available
