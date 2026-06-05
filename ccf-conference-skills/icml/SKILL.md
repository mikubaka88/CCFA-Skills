---
name: icml
description: Writing and formatting guidance for ICML (International Conference on Machine Learning) papers. Use when drafting, revising, and formatting papers for ICML 2026. Covers icml2026 LaTeX class options (submission/accepted/preprint), theorem environment setup, title formatting with running title, cleveref usage, double-blind anonymization, and camera-ready compilation with the accepted option.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ICML 2026 Conference Writing Skill

**CCF-A | AI | Publisher: ACM**
**Conference:** https://icml.cc/2026
**Template:** `ccf-latex-templates/ICML/example_paper.tex`

## Document Setup

### Preamble Structure

```latex
\documentclass{article}

% Recommended packages:
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{subcaption}
\usepackage{booktabs}

% Hyperref (required/recommended):
\usepackage{hyperref}
% If build issues: use \usepackage[nohyperref]{icml2026}

% === MODE SELECTION ===
\usepackage{icml2026}              % Review/submission (double-blind)
% OR:
% \usepackage[preprint]{icml2026}  % Preprint/arxiv
% OR:
\usepackage[accepted]{icml2026}   % Camera-ready

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{mathtools}
\usepackage{amsthm}

% Optional cleveref:
\usepackage[capitalize,noabbrev]{cleveref}
```

### Package Loading Order

1. Standard packages (microtype, graphicx, etc.)
2. `hyperref` (before `icml2026` if issues)
3. `icml2026` with appropriate mode option
4. Math packages (amsmath, amssymb, mathtools, amsthm)
5. Optional: cleveref

## Mode Options

| Mode | Option | Purpose |
|------|--------|---------|
| Submission | (default) or `icml2026` | Double-blind review |
| Preprint | `[preprint]` | arXiv submissions |
| Camera-ready | `[accepted]` | Final version with author info |

The style file automatically handles author visibility — author info is removed for submission unless `accepted` option is used.

## Page Limits

- **Main content:** 8 pages (submission)
- **Final version:** 9 pages (one extra page allowed)
- **References/Appendices:** Not counted toward limit
- **File size:** Maximum 10MB total

## Title and Author Formatting

```latex
% Full title (for abstract page):
\icmltitle{Submission and Formatting Instructions for \\
  International Conference on Machine Learning (ICML 2026)}

% Short title (for running head on each page):
\icmltitlerunning{Submission and Formatting Instructions for ICML 2026}

% Author list with affiliations:
\begin{icmlauthorlist}
  \icmlauthor{Firstname1 Lastname1}{equal,yyy}
  \icmlauthor{Firstname2 Lastname2}{equal,yyy,comp}
  \icmlauthor{Firstname3 Lastname3}{comp}
  \icmlauthor{Firstname4 Lastname4}{sch}
\end{icmlauthorlist}

\icmlaffiliation{yyy}{Department of XXX, University of YYY, Country}
\icmlaffiliation{comp}{Company Name, Country}
\icmlaffiliation{sch}{School of ZZZ, Institute of WWW, Country}

\icmlcorrespondingauthor{Firstname1 Lastname1}{first1@xxx.edu}
\icmlcorrespondingauthor{Firstname2 Lastname2}{first2@www.uk}

% Equal contribution symbol:
\icmlsetsymbol{equal}{*}

% Print affiliations (required):
\printAffiliationsAndNotice{}  % No special notice
% OR for equal contribution:
% \printAffiliationsAndNotice{\icmlEqualContribution}
```

## Abstract

```latex
\begin{abstract}
  Abstract must be a single paragraph, ideally 4-6 sentences.
  Gross violations will trigger corrections at camera-ready phase.
\end{abstract}

% Keywords (optional, for PDF metadata):
\icmlkeywords{Machine Learning, ICML}
```

## Theorem Environments

Set up before `\begin{document}`:

```latex
% Theorem style setup:
\theoremstyle{plain}
\newtheorem{observation}[theorem]{Observation}
\newtheorem{example}[theorem]{Example}
```

### Complete Theorem Setup for ML Papers

```latex
% === Put in preamble before \begin{document} ===

% Plain style (for theorems, lemmas, propositions, corollaries)
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{prop}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{cor}[theorem]{Corollary}

% Definition style (for definitions, conditions, assumptions)
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{condition}[theorem]{Condition}
\newtheorem{assumption}[theorem]{Assumption}

% Remark style (for remarks, notes, examples)
\theoremstyle remark}
\newtheorem{note}[theorem]{Note}
\newtheorem{remark}[theorem]{Remark}
```

### Theorem Examples

```latex
\begin{assumption}
\label{assum:lip}
The loss function $\ell$ is $L$-Lipschitz continuous with respect
to the model parameters $\theta$:
$|\ell(\theta_1) - \ell(\theta_2)| \leq L \|\theta_1 - \theta_2\|$
for all $\theta_1, \theta_2$.
\end{assumption}

\begin{convergence}
Let $\hat{f}_t$ be the model at iteration $t$.
Under Assumption \ref{assum:lip}, we have:
\[
\mathbb{E}[\|\hat{f}_t - f^*\|] \leq O\left(\frac{1}{\sqrt{t}}\right)
\]
\end{convergence}
```

## Section Organization

```latex
\section{First Level Heading}
\subsection{Second Level Heading}
\subsubsection{Third Level Heading}
```

- Use maximum three heading levels
- Section headings: 11pt bold, capitalized
- Subsection headings: 10pt bold, capitalized
- Subsubsection headings: 10pt small caps, capitalized

### Recommended ICML Paper Structure

1. **Abstract** — Problem, method, results in 4-6 sentences
2. **Introduction** — Motivation, contributions (enumerate), roadmap
3. **Background** — Notation, definitions, related concepts
4. **Method** — Core contribution with clear description
5. **Theoretical Analysis** — Guarantees, convergence, bounds
6. **Experiments** — Setup, results, analysis
7. **Related Work** — Positioning against prior work
8. **Conclusion** — Summary, limitations, future work
9. **Impact Statement** (required) — Broader societal impact
10. **Acknowledgments** — Funding, collaborators

## Figures and Tables

```latex
% Figure: caption UNDER
\begin{figure}[ht]
  \vskip 0.2in
  \begin{center}
    \centerline{\includegraphics[width=\columnwmain]{figure}}
    \caption{
      Historical locations and number of accepted papers.
      Explain what the figure shows.
    }
    \label{fig:example}
  \end{center}
\end{figure}

% Table: caption ABOVE
\begin{table}[t]
  \caption{Classification accuracies for methods.}
  \label{sample-table}
  \begin{center}
    \begin{small}
      \begin{sc}
        \begin{tabular}{lcccr}
          \toprule
          Data & Method A & Method B & Better? \\
          \midrule
          Set1 & 95.9 & 96.7 & $\surd$ \\
          \bottomrule
        \end{tabular}
      \end{sc}
    \end{small}
  \end{center}
  \vskip -0.1in
\end{table}
```

- Figure captions: 9pt type, centered
- Table captions: 9pt type, above table
- Use `booktabs` (no vertical rules)
- Labels after caption, before punctuation

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

## References (APA Format)

Use `natbib` with `icml2026.bst`:

```latex
\bibliography{example_paper}
\bibliographystyle{icml2026}
```

Citation format (APA):
```latex
\citet{Samuel59}       % Samuel (1959)
\citep{Sabato25}       % (Author, Year)
\citeyear{Sabato25}    % (Year)
```

- Cite in third person for blind review
- List references alphabetically by first author
- Include all authors (no "et al." in references)

## Required Sections (Camera-Ready)

### Impact Statement (Required)

```latex
\section*{Impact Statement}
Authors are required to include a statement of potential broader impact...
This section does not count toward page limit.
```

### Acknowledgements (Camera-Ready Only)

```latex
\section*{Acknowledgements}
% Do NOT include in initial submission
% Add after acceptance
```

## Anonymization Rules

1. No author information on title page
2. Use `\icmlauthor{}` commands — style file removes automatically
3. Third-person self-citations only
4. Do not anonymize reference entries
5. Exception: unpublished manuscripts — cite as Anonymous, submit as supplementary

## Camera-Ready Compilation

```latex
% Change from:
\usepackage{icml2026}
% To:
\usepackage[accepted]{icml2026}
```

The footnote changes from:
```
Preliminary work. Under review by ICML 2026. Do not distribute.
```
To:
```
Proceedings of the 43rd International Conference on Machine Learning,
Seoul, South Korea, PMLR 306, 2026.
Copyright 2026 by the author(s).
```

### Camera-Ready Checklist

- [ ] Changed to `\usepackage[accepted]{icml2026}`
- [ ] All author information restored
- [ ] Impact statement included
- [ ] Acknowledgments section added
- [ ] Self-citations restored
- [ ] Page count ≤ 9 pages (one extra page for final)
- [ ] All figures and tables properly formatted

## ICML-Specific Writing Conventions

### Theoretical Writing

ICML values rigorous theoretical analysis:

```latex
\section{Theoretical Analysis}

\begin{assumption}
\label{assum:bounded}
All input vectors $\mathbf{x}$ satisfy $\|\mathbf{x}\|_2 \leq R$ for
some constant $R > 0$.
\end{assumption}

\begin{assumption}
\label{assum:convex}
The population risk $R(\theta) = \mathbb{E}[\ell(\theta; X)]$ is
$\mu$-strongly convex in $\theta$.
\end{assumption}

\begin{convergence}
\label{them:convergence}
Under Assumptions \ref{assum:bounded} and \ref{assum:convex},
the iterates $\{\theta_t\}$ generated by Algorithm \ref{alg:main}
satisfy:
\[
\mathbb{E}[R(\theta_t) - R(\theta^*)] \leq
\left(1 - \frac{\mu}{L}\right)^t [R(\theta_0) - R(\theta^*)].
\]
\end{convergence}
```

### Experimental Rigor

ICML expects comprehensive experiments:

```latex
\section{Experiments}

\subsection{Setup}
\textbf{Datasets:} We evaluate on 8 standard benchmarks including:
\begin{itemize}
    \item \textbf{Image classification:} CIFAR-10, CIFAR-100, ImageNet
    \item \textbf{Natural language:} GLUE, SQuAD
    \item \textbf{Graph:} Cora, CiteSeer, PubMed
\end{itemize}

\textbf{Baselines:} We compare against:
\begin{itemize}
    \item Standard methods (vanilla baselines)
    \item State-of-the-art methods from recent ML conferences
    \item Ablation variants of our method
\end{itemize}

\textbf{Implementation:} PyTorch implementation. All experiments run
on NVIDIA V100 GPUs with 32GB memory. Learning rates tuned via
grid search on validation sets.

\textbf{Statistics:} All results reported as mean $\pm$ std over 5
independent runs with different random seeds. Statistical significance
assessed via paired t-tests with Bonferroni correction.

\subsection{Main Results}
\autoref{tab:main} shows our method achieves state-of-the-art
performance across all benchmarks, improving over previous best by
1.3\% on average.

\subsection{Ablation Study}
\autoref{tab:ablation} analyzes each component of our approach.
The key finding is that component X contributes Y\% of the
overall improvement.
```

### Reproducibility Checklist

Address these in your paper or appendix:

```latex
\section*{Reproducibility (Optional Section)}

\subsection{Hyperparameters}
All hyperparameters are listed in \autoref{tab:hyperparams}.
We use grid search with ranges specified in the text.

\subsection{Computational Requirements}
Training time: ~24 GPU hours for largest model.
Memory: ~16GB GPU memory required.
Code available at: [URL]

\subsection{Random Seeds}
All experiments use seeds 0-4 for reproducibility.
```

## Checklist Before Submission

- [ ] 8 pages or fewer (9 for final version)
- [ ] No author identification visible
- [ ] Third-person self-citations
- [ ] Theorem environments properly defined
- [ ] Figure captions below, table captions above
- [ ] References in APA format
- [ ] Type-1 fonts only
- [ ] Running title set with `\icmltitlerunning{}`
- [ ] Impact statement included
- [ ] All notation defined before use
- [ ] Baselines properly documented
- [ ] Statistical significance tested
