# SIGKDD Venue Guide

> Migrated from the legacy `ccf-conference-skills/sigkdd/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `sigkdd` |
| Venue family | DB/Mining |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/SIGKDD/acmart.cls` |
| Official URL | https://kdd.org/kdd2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# SIGKDD 2026 Conference Writing Skill

**CCF-A | DB/Mining | Publisher: ACM**
**Conference:** https://kdd.org/kdd2026
**Template:** `ccf-latex-templates/SIGKDD/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[SIGKDD 2026]{KDD '26: 2026 ACM SIGKDD Conference...}
               {August 10--14, 2026}{Philadelphia, PA, USA}
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
\usepackage{balance}
\usepackage{cleveref}          % For consistent cross-references
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{xcolor}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **10 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

SIGKDD enforces a strict 10-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, data repository links
4. Clear PDF metadata
5. Remove acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore all author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

SIGKDD papers typically follow a data science paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate explicitly)
2. **Background & Preliminaries** — Problem formalization, related definitions
3. **Related Work** — Can also appear after Introduction for brevity
4. **Problem Statement** — Formal problem definition with notation
5. **Proposed Approach** — Core technical contribution (algorithm, model, framework)
6. **Theoretical Analysis** — Optional: correctness, complexity, convergence proofs
7. **Experimental Evaluation** — Datasets, baselines, metrics, results
8. **Discussion** — Limitations, extensions, implications
9. **Conclusion**
10. References
11. Appendix (optional)

## Problem Formalization

SIGKDD values clear mathematical formalization:

```latex
\section{Problem Definition}

\begin{problem}[Top-K Diverse Clustering]
Given a set of $n$ data points $\mathcal{X} = \{x_1, \dots, x_n\}$ in
metric space $(\mathcal{X}, d)$, a distance threshold $\epsilon > 0$,
and an integer $k$, find a subset $\mathcal{C} \subseteq \mathcal{X}$
such that $|\mathcal{C}| = k$ and the clustering diversity
$\text{Div}(\mathcal{C}) = \sum_{c \in \mathcal{C}} \min_{c' \in \mathcal{C} \setminus \{c\}} d(c, c')$ is maximized, subject to $\forall c \in \mathcal{C}, \forall x \in \mathcal{X} \setminus \mathcal{C}: d(c, x) \leq \epsilon$.
\end{problem}
```

## KDD-Specific Writing Conventions

### Introduction Structure for KDD Papers

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
With the exponential growth of data, extracting actionable insights from
large-scale datasets has become increasingly important. In this paper,
we address the problem of [X], which is crucial for [application Y].

% Paragraph 3: Gap in prior work
Prior approaches to X fall into two categories: (1) methods based on
[approach A] \citep{a2023}, which suffer from [limitation], and
(2) methods based on [approach B] \citep{b2023}, which fail to
handle [challenge]. These limitations motivate the need for a new approach.

% Paragraph 4: Our approach
We propose a novel approach called [Name] that addresses these challenges
by [key insight]. Our approach leverages [technical contribution].

% Paragraph 5: Contributions (numbered)
Our main contributions are:
\begin{itemize}
    \item We formalize the problem of X as [formal definition],
    identifying key challenges.
    \item We propose [method name], a novel algorithm that achieves
    [benefit] while maintaining [property].
    \item We provide theoretical analysis showing [guarantee].
    \item Through extensive experiments on [datasets], we demonstrate
    that our approach outperforms state-of-the-art methods by [X\%].
\end{itemize}
```

### Dataset Description (Critical for KDD)

```latex
\section{Experimental Evaluation}
\subsection{Datasets}
We evaluate on six real-world datasets spanning three application domains:

\begin{table}[h]
  \caption{Dataset statistics. All datasets are publicly available.}
  \label{tab:datasets}
  \centering
  \begin{tabular}{lrrr}
    \toprule
    Dataset & Instances & Features & Source \\
    \midrule
    MovieLens-1M & 1,000,209 & 3 & MovieLens \\
    Adult & 48,842 & 14 & UCI \\
    Cora & 2,708 & 1,433 & CiteSeer \\
    \bottomrule
  \end{tabular}
\end{table}

For each dataset, we use the standard train/test splits provided by
the data repository. Preprocessing details are in the appendix.
```

### Baseline Selection

```latex
We compare against four categories of baselines:

\textbf{Classical methods:}
\begin{itemize}
    \item \textbf{K-means++}: The standard k-means initialization method \citep{arthur2007}.
    \item \textbf{DBSCAN}: Density-based clustering \citep{ester1996}.
\end{itemize}

\textbf{State-of-the-art methods:}
\begin{itemize}
    \item \textbf{Method A}: The approach of \citet{smith2023}.
    \item \textbf{Method B}: Recent work from \citet{jones2024}.
\end{itemize}

\textbf{Our baselines:}
\begin{itemize}
    \item \textbf{Ours-b}: Our method without component X.
    \item \textbf{Ours-c}: Our method with component Y only.
\end{itemize}
```

## Experimental Evaluation

SIGKDD evaluation standards are high — include:

- **Dataset description**: size, features, source, preprocessing
- **Baselines**: well-known methods from literature
- **Metrics**: standard measures for the task (AUC, F1, NDCG, RMSE, etc.)
- **Statistical significance**: confidence intervals, p-values
- **Scalability**: runtime vs. dataset size
- **Ablation studies**: component-wise contribution

```latex
\section{Experimental Evaluation}
\subsection{Setup}
We evaluate on six real-world datasets spanning three domains:
\begin{itemize}
    \item \textbf{Recommendation}: MovieLens-1M (1M ratings, 6K users, 4K movies),
    \item \textbf{Classification}: UCI Adult (48,842 instances, 14 attributes),
    \item \textbf{Graph}: Cora citation network (2,708 nodes, 5,278 edges).
\end{itemize}
Baseline methods include k-means++, DBSCAN, and the method of~\citet{jin2019}.
All experiments are run 10 times with different random seeds and
we report mean $\pm$ standard deviation.

\subsection{Results}
Results are summarized in \autoref{tab:results}.
Our method achieves the best performance across all datasets,
outperforming the best baseline by 3.7\% on average in F1 score.
Improvements are statistically significant (paired t-test, $p < 0.01$).

\subsection{Ablation Study}
\autoref{tab:ablation} shows the contribution of each component.
Removing component X degrades performance by Y\%, confirming its importance.
```

## Algorithm Formatting

Use `algorithm` and `algorithmic` environments:

```latex
\begin{algorithm}[t]
\caption{The MIDA Algorithm}
\label{alg:mida}
\begin{algorithmic}[1]
\REQUIRE Dataset $\mathcal{D}$, privacy budget $\epsilon$, parameter $k$
\ENSURE $(\epsilon, \delta)$-private clustering $\mathcal{C}$
\STATE $\mathcal{D}' \gets \text{LaplaceMechanism}(\mathcal{D}, \epsilon)$
\STATE $\mathcal{C} \gets \text{K-Means}(\mathcal{D}', k)$
\RETURN $\mathcal{C}$
\end{algorithmic}
\end{algorithm}
```

## Figures and Tables

- Vector formats (.pdf) preferred
- Grayscale legibility required
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- Self-contained captions

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/algorithm-flow}
  \caption{The proposed framework consists of three stages:
    (1) feature extraction, (2) similarity computation,
    (3) clustering. Arrows indicate data flow.}
  \label{fig:algorithm-flow}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{aggarwal}         % Aggarwal et al. (2021)
\citep{aggarwal}         % (Aggarwal et al. 2021)
```

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Reproducibility Checklist

SIGKDD values reproducibility. Address these in your paper:

```latex
\section*{Reproducibility}
\subsection{Hyperparameters}
All hyperparameters are listed in \autoref{tab:hyperparams}.
We tune them via grid search on validation sets.

\subsection{Computational Resources}
Training time: ~24 GPU hours for largest model.
Memory: ~16GB RAM required.
Code available at: [URL]

\subsection{Random Seeds}
All experiments use seeds 0-9 for reproducibility.
```

## Submission Checklist

- [ ] 10 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs and dataset links
- [ ] Formal problem definition included
- [ ] Strong experimental evaluation with baselines
- [ ] References list all authors
- [ ] Grayscale-legible figures
- [ ] Statistical significance tested
- [ ] Ablation studies included

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
- [ ] Add acknowledgments if desired
