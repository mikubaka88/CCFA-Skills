# ACL Venue Guide

> Migrated from the legacy `ccf-conference-skills/acl/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `acl` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/ACL` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ACL Conference Writing Skill

## Overview

This skill covers LaTeX formatting, submission rules, and writing conventions for **ACL (Association for Computational Linguistics)** — a **CCF-A** conference in the AI category, held annually at [https://2026.aclweb.org](https://2026.aclweb.org). The publisher is **ACL**.

> **Note:** EMNLP, NAACL, COLING, and CoNLL all share the same `acl.sty` template. Consult this skill for shared formatting rules, then check the EMNLP or NAACL skill for venue-specific policies.

**Template path:** `ccf-latex-templates/ACL/`
- `acl_latex.tex` — main template
- `acl.sty` — style file (sourced from [acl-style-files](https://github.com/acl-org/acl-style-files/))

---

## Document Class and Packages

### Modes

The `acl.sty` supports three modes, controlled via the `acl` package option (not a class option):

| Mode | Option | Effect |
|---|---|---|
| Submission (anonymized) | `\usepackage[review]{acl}` | Anonymous author block, line numbers, page numbers |
| Camera-ready | `\usepackage{acl}` (no option) | Final copy, no line/page numbers |
| Non-anonymous preprint | `\usepackage[preprint]{acl}` | Page numbers shown, authors visible |

```latex
% Submission
\documentclass[11pt]{article}
\usepackage[review]{acl}

% Camera-ready (final)
\documentclass[11pt]{article}
\usepackage{acl}

% Preprint
\documentclass[11pt]{article}
\usepackage[preprint]{acl}
```

### Standard Packages

Include these packages in every submission (review and final):

```latex
\usepackage{times}          % Times Roman font
\usepackage{latexsym}       % LaTeX symbols
\usepackage[T1]{fontenc}     % T1 font encoding (required for proper hyphenation)
\usepackage[utf8]{inputenc}  % UTF-8 source encoding
\usepackage{microtype}       % Improved typography, saves space
\usepackage{inconsolata}     % Monospace font for code
\usepackage{graphicx}        % Figures and images
```

### Title Box

If the title and author block overflows, increase `\titlebox`:

```latex
\setlength\titlebox{6cm}  % or larger; must be >= 5cm
```

---

## Title and Author

```latex
\title{Your Paper Title Here}

\author{First Author \\
  Affiliation / Address line 1 \\
  Affiliation / Address line 2 \\
  \texttt{email@domain} \\\And
  Second Author \\
  Affiliation / Address line 1 \\
  Affiliation / Address line 2 \\
  \texttt{email@domain} \\}
```

For authors from different institutions, use `\And` between groups:

```latex
\author{Author 1 \\ Institution 1 \\\texttt{email1}
  \And
  Author 2 \\ Institution 2 \\\texttt{email2}}
```

To start a separate row of authors, use `\AND`:

```latex
\author{Row 1 Author 1 \AND Row 1 Author 2 \\
       Row 2 Author 3 \And Row 2 Author 4}
```

> In **review mode**, `acl.sty` automatically replaces the author block with "Anonymous ACL submission". Do not manually anonymize.

---

## Document Structure

### Standard NLP Paper Structure

```latex
\begin{document}
\maketitle
\begin{abstract}
  Write your abstract here. Keep it concise (typically 150–250 words).
  State the problem, approach, and main results.
\end{abstract}

\section{Introduction}
% Problem, motivation, contributions (explicit bullet list)

\section{Related Work}
% Categorize by approach or task, not just list

\section{Background / Preliminaries}
% Formal notation, task definition, background concepts

\section{Method / Model}
% Core contribution with sufficient detail

\section{Experimental Setup}
% Datasets, metrics, baselines, implementation

\section{Results and Analysis}
% Quantitative results, ablation, error analysis

\section{Conclusion}
% Summary, limitations, future work

\section*{Acknowledgments}
% Funding, collaborators

% then references, then appendix
```

### Standard Section Order (ACL)

1. **Abstract** — mandatory, state problem/method/results
2. **Introduction** — motivation, problem, contributions (enumerate explicitly)
3. **Related Work** — positioning vs. prior work, categorized
4. **Background / Preliminaries** — formalism, definitions, notation
5. **Method / Model** — core contribution
6. **Experimental Setup** — datasets, metrics, baselines, implementation
7. **Results** — experiments, results, analysis
8. **Conclusion** — summary, limitations, future work
9. **Acknowledgments** — funding, collaborators
10. **References**
11. **Appendix / Supplementary**

---

## Citations

`acl.sty` loads `natbib`. Use these citation commands:

```latex
\citet{Gusfield:97}       % "Gusfield (1997)" — author in text
\citep{Gusfield:97}       % "(Gusfield, 1997)" — parenthetical
\citealp{Gusfield:97}     % "Gusfield, 1997" — alternative (no parens)
\citeyearpar{Gusfield:97} % "(1997)" — year only
\citeposs{Gusfield:97}    % "Gusfield's (1997)" — possessive (ACL-specific)
```

### ACL Anthology Bibliography

Obtain the full ACL Anthology BibTeX: [https://aclweb.org/anthology/anthology.bib.gz](https://aclweb.org/anthology/anthology.bib.gz).

Include in your bibliography:

```latex
\bibliographystyle{acl_natbib}
\bibliography{anthology,your_file}  % Include ACL Anthology + your file
```

---

## References

```latex
\bibliographystyle{acl_natbib}
\bibliography{your_file}        % single .bib file
\bibliography{anthology,your_file}  % include ACL Anthology + your file
```

Obtain the full ACL Anthology BibTeX: [https://aclweb.org/anthology/anthology.bib.gz](https://aclweb.org/anthology/anthology.bib.gz).

Include `doi` or `url` fields in every bibliography entry for hyperlinks.

### BibTeX Guidelines

- Use the accented-character commands from `acl.sty` in `.bib` files (e.g., `{\"a}` for ä).
- Do not use Unicode characters directly in BibTeX entries.
- Alphabetize references in the output.
- List all authors (no "et al." in bibliography).

---

## Figures

```latex
\usepackage{graphicx}  % already in preamble

\begin{figure}[t]
  \includegraphics[width=\linewidth]{your-figure}
  \caption{Descriptive caption. Keep it informative and concise.}
  \label{fig:your-label}
\end{figure}

% Wide figure spanning both columns
\begin{figure*}[t]
  \includegraphics[width=0.48\linewidth]{fig-a}\hfill
  \includegraphics[width=0.48\linewidth]{fig-b}
  \caption{Side-by-side caption.}
  \label{fig:side-by-side}
\end{figure*}
```

- Use PDF, PNG, or EPS for graphics.
- Match figure fonts to document fonts.
- **Do not override default caption sizes.**
- For subfigures, use the `subcaption` package (compatible with `acl.sty`).

### Figure Best Practices for NLP

```latex
\begin{figure}
  \centering
  \begin{tabular}{cc}
    \includegraphics[width=0.4\linewidth]{example1} &
    \includegraphics[width=0.4\linewidth]{example2} \\
    (a) Case 1 & (b) Case 2
  \end{tabular}
  \caption{Examples of qualitative analysis showing...}
  \label{fig:qual}
\end{figure}
```

---

## Tables

Use `booktabs`-style rules. Avoid vertical rules.

```latex
\begin{table}[t]
  \centering
  \begin{tabular}{lcc}
    \hline
    \textbf{Model} & \textbf{Precision} & \textbf{Recall} \\
    \hline
    BERT & 85.2 & 83.1 \\
    RoBERTa & 87.4 & 85.6 \\
    \hline
  \end{tabular}
  \caption{Results on the dev set.}
  \label{tab:results}
\end{table}
```

### Professional Table Formatting

```latex
\begin{table}[t]
  \caption{Comparison of models on standard benchmarks.
    Best results in \textbf{bold}. $\dagger$ indicates $p < 0.01$ vs. BERT.}
  \label{tab:comparison}
  \centering
  \begin{tabular}{lcccc}
    \toprule
    \multirow{2}{*}{Model} & \multicolumn{2}{c}{Task 1} &
      \multicolumn{2}{c}{Task 2} \\
    \cmidrule(lr){2-3}\cmidrule(lr){4-5}
          & Acc & F1 & Acc & F1 \\
    \midrule
    BERT & 85.2 & 84.1 & 78.3 & 77.5 \\
    RoBERTa & 87.4 & 86.2 & 80.1 & 79.2 \\
    \textbf{Ours} & \textbf{89.1} & \textbf{88.3} & \textbf{82.4} & \textbf{81.8} \\
    \bottomrule
  \end{tabular}
\end{table}
```

---

## Equations

```latex
\begin{equation}
  \label{eq:loss}
  \mathcal{L} = -\sum_{i=1}^{N} \log p(y_i \mid x_i; \theta)
\end{equation}
```

Label all equations; reference with `\eqref{eq:label}`.

### Mathematical Notation for NLP

```latex
\section{Preliminaries}

Let $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$ denote a dataset of
input-output pairs, where $\mathbf{x}_i \in \mathcal{X}$ is a sequence of
tokens and $y_i \in \mathcal{Y}$ is the corresponding label.

We denote the model's parameters by $\theta$. The conditional probability
of output $y$ given input $\mathbf{x}$ is:
\begin{equation}
  p_\theta(y \mid \mathbf{x}) = \text{softmax}(\mathbf{W} \mathbf{h}_\theta(\mathbf{x}))_y
\end{equation}
where $\mathbf{h}_\theta(\mathbf{x})$ is the encoding of $\mathbf{x}$.
```

---

## Appendix

Place appendix content after `\appendix`:

```latex
\appendix

\section{Additional Experimental Results}
\label{sec:app-results}

\section{Proofs}
\label{sec:proofs}
```

The `\appendix` command switches section numbering from numbers to letters (A, B, C...).

---

## Page Limit

**ACL 2026: 8 pages** for the main paper, **excluding** references and appendix.

Check the official CFP for the exact page limit and whether it includes tables and figures. Excess pages may be desk-rejected.

---

## Anonymity and Double-Blind Review

- In **review mode**, author names are automatically replaced with "Anonymous ACL submission". Do not add acknowledgments or self-citations that reveal identity.
- Remove or anonymize references to prior work by the authors (or use generic placeholders that you restore for the camera-ready).
- Do not upload anonymized drafts to public repositories.
- Check the CFP for specific anonymity policy updates.

### Self-Citation Anonymization

```latex
% In submission (anonymized):
...as shown in prior work~\citep{anonymous:2024:ourprior}...

% In camera-ready:
...as shown in our prior work~\citep{smith2024prior}...
```

---

## Camera-Ready Checklist

- [ ] Switch from `\usepackage[review]{acl}` to `\usepackage{acl}`
- [ ] Restore all author names and affiliations
- [ ] Restore self-citations removed for review
- [ ] Add or update acknowledgments
- [ ] Verify page count (main text ≤ 8 pages, excluding refs/appendix)
- [ ] Include DOI/URL in all bibliography entries
- [ ] Check that figures and tables are high-resolution
- [ ] Run a final PDF compilation and verify formatting

---

## Writing Conventions (NLP)

### Problem Definition

```latex
\section{Task Definition}
We focus on the task of $X$, formally defined as follows.

\textbf{Input:} A sequence of tokens $\mathbf{x} = (x_1, \dots, x_n)$.

\textbf{Output:} A structured object $y$ (e.g., a parse tree, label sequence).

\textbf{Evaluation:} We measure performance using standard metrics
including F1 score for token-level tasks and accuracy for sentence-level tasks.
```

### Dataset Description

```latex
\subsection{Datasets}
We evaluate on four standard benchmarks:
\begin{itemize}
    \item \textbf{Dataset A}: 10K training, 1K dev, 1K test examples.
    Source: URL. Domain: newswire. Language: English.
    \item \textbf{Dataset B}: 50K training, 5K dev, 5K test examples.
    Source: URL. Domain: social media. Language: multilingual (10 languages).
\end{itemize}
Preprocessing: tokenized using spaCy, lowercased, rare words replaced with <UNK>.
```

### Error Analysis

```latex
\subsection{Error Analysis}
We manually analyze 100 randomly sampled errors.

\textbf{Error categories:}
\begin{itemize}
    \item \textbf{Long sentences} (34\%): Performance degrades for inputs > 50 tokens.
    \item \textbf{Rare entities} (28\%): Named entities not seen during training.
    \item \textbf{Ambiguity} (22\%): Genuinely ambiguous inputs where even humans disagree.
    \item \textbf{Other} (16\%): Annotation errors, preprocessing issues.
\end{itemize}
```

### Qualitative Examples

```latex
\subsection{Qualitative Examples}
\autoref{tab:examples} shows representative examples from our model.

\begin{table}[h]
  \caption{Qualitative examples comparing model outputs.
    ``GT'' denotes ground truth, ``Err'' denotes error type.}
  \label{tab:examples}
  \centering
  \begin{tabular}{p{3cm}p{3cm}p{2cm}}
    \toprule
    Input & Output & Type \\
    \midrule
    The dog chased the cat. & nsubj(dog, chased) & Correct \\
    John gave Mary a book. & ROOT(gave) & Correct \\
    \bottomrule
  \end{tabular}
\end{table}
```

---

## Supplementary Materials

Check the ACL 2026 CFP for the supplementary materials policy. Common rules:

- Supplementary files are **not** part of the review process.
- Keep supplementary material minimal and clearly labeled.
- Do not exceed file size limits specified by the submission system.

### Typical Supplementary Contents

```latex
% In main paper:
Results on additional datasets are provided in Appendix A.

% In supplementary:
\section{Additional Datasets}
\section{Extended Error Analysis}
\section{Hyperparameter Sensitivity}
\section{Model Architecture Details}
```

---

## Checklist Before Submission

- [ ] `\usepackage[review]{acl}` for submission
- [ ] All author/anonymization complete
- [ ] Self-citations removed or anonymized
- [ ] Page count ≤ 8 pages (excluding refs/appendix)
- [ ] ACL Anthology bibliography included
- [ ] Figures: PDF/PNG/EPS, properly formatted
- [ ] Tables: booktabs style, no vertical rules
- [ ] All notation defined before use
- [ ] Dataset descriptions complete
- [ ] Baseline methods properly cited
- [ ] Error analysis included
- [ ] Limitations discussed
