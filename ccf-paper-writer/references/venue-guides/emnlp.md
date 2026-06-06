# EMNLP Venue Guide

> Migrated from the legacy `ccf-conference-skills/emnlp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `emnlp` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/EMNLP` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# EMNLP 2026 Conference Writing Skill

## Overview

This skill covers LaTeX formatting, submission rules, and writing conventions for **EMNLP (Conference on Empirical Methods in Natural Language Processing)** — a **CCF-B** conference in the AI category, held annually at [https://2026.emnlp.org](https://2026.emnlp.org). The publisher is **ACL**.

> **Prerequisite:** EMNLP shares the same `acl.sty` template as ACL, NAACL, COLING, and CoNLL. **Read the ACL skill first** for shared formatting rules (documentclass, packages, citations, bibliography, figures, tables, equations, appendix). This skill covers EMNLP-specific rules and differences only.

**Template path:** `ccf-latex-templates/EMNLP/`
- `acl_latex.tex` — main template (identical to ACL/NAACL)
- `acl.sty` — shared style file

---

## EMNLP-Specific Rules

### Document Class and Modes

EMNLP uses the same three-mode system as ACL:

```latex
% Submission (anonymized review)
\documentclass[11pt]{article}
\usepackage[review]{acl}

% Camera-ready (final)
\documentclass[11pt]{article}
\usepackage{acl}

% Non-anonymous preprint
\documentclass[11pt]{article}
\usepackage[preprint]{acl}
```

### Standard Packages

Identical to ACL:

```latex
\usepackage{times}
\usepackage{latexsym}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{microtype}
\usepackage{inconsolata}
\usepackage{graphicx}
```

If the title/author block overflows:

```latex
\setlength\titlebox{6cm}  % minimum is 5cm
```

---

## Title and Author

```latex
\title{Your EMNLP Paper Title}

\author{First Author \\
  Institution, City, Country \\
  \texttt{email@domain} \\\And
  Second Author \\
  Institution, City, Country \\
  \texttt{email@domain} \\}
```

In **review mode**, `acl.sty` automatically replaces the author block with "Anonymous ACL submission".

---

## Page Limit

**EMNLP 2026: 8 pages** for the main paper, **excluding** references and appendix.

> Confirm the exact limit in the official EMNLP 2026 Call for Papers, as policies can change year-to-year.

---

## Submission Policies

### Double-Blind Review

- Submission must be anonymized: no author names, affiliations, or acknowledgments that reveal identity.
- In review mode, `acl.sty` automatically shows "Anonymous ACL submission" as the author block.
- **Self-citations:** Remove or anonymize citations to prior work by the authors. Replace with "[REMOVED FOR REVIEW]" or similar placeholder, then restore for the camera-ready.
- Do not post anonymized drafts to arXiv or public repositories before the review period ends.
- Do not anonymize citations to non-author prior work.

### Originality and Reproducibility

- Submissions must be original, unpublished work not currently under review elsewhere.
- EMNLP increasingly emphasizes **reproducibility**. Include:
  - Hyperparameters and training details in appendices.
  - Links to code repositories (anonymized if submitted as supplementary).
  - Results averaged over multiple random seeds where applicable.

### Conflicts of Interest

- Declare all conflicts of interest in the submission system.
- Do not include conflict declarations in the PDF.

### Multiple Submission Policy

- Do not submit the same work to EMNLP and another venue simultaneously.
- Withdrawal and desk-rejection policies follow EMNLP guidelines.

---

## Camera-Ready Preparation

After acceptance, prepare the camera-ready version:

- [ ] Switch `\usepackage[review]{acl}` to `\usepackage{acl}`
- [ ] Restore author names and affiliations
- [ ] Restore self-citations
- [ ] Add/update the Acknowledgments section
- [ ] Include the full ACL Anthology bibliography for cited works
- [ ] Verify the paper compiles without errors
- [ ] Check that the page count is within limits (main text ≤ 8 pages, excluding refs/appendix)
- [ ] Add any required supplementary materials before the deadline
- [ ] Upload to the official submission system before the deadline

---

## NLP Writing Conventions for EMNLP

EMNLP papers typically follow this structure:

1. **Abstract** — 150–200 words, state problem/method/results
2. **Introduction** — motivation, task, challenge, contribution list (4–5 bullet points)
3. **Related Work** — prior work categorized by approach or task
4. **Background / Preliminaries** — formal notation, task definition
5. **Method / Model** — core contribution with enough detail to reproduce
6. **Experimental Setup** — datasets, metrics, baselines, implementation details
7. **Results and Analysis** — quantitative results, ablation studies, error analysis, qualitative examples
8. **Conclusion** — summary, limitations, broader impact
9. **Acknowledgments**
10. **References**
11. **Appendix**

### Recommended EMNLP Introduction Structure

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation
Natural language processing has seen significant advances with...
However, the task of X remains challenging due to Y...

% Paragraph 2: Gap in prior work
Prior work has addressed this problem through approaches A, B, and C.
While effective, these approaches suffer from limitations:
(1) They require large amounts of labeled data...
(2) They fail to capture semantic nuances...
(3) They are not generalizable to new domains...

% Paragraph 3: Our approach
In this paper, we propose a novel approach that...
Our key insight is that...

% Paragraph 4: Contributions (numbered list)
Our main contributions are:
\begin{itemize}
    \item We propose a new model architecture for X that achieves Y...
    \item We introduce a benchmark dataset consisting of Z...
    \item We demonstrate through extensive experiments that our method
    outperforms prior approaches by X\% on standard benchmarks.
\end{itemize}
```

### EMNLP Writing Conventions

#### Dataset Description (Required)

```latex
\section{Experimental Setup}
\subsection{Datasets}
We evaluate on four standard benchmarks:

\begin{table}[h]
  \caption{Dataset statistics. All datasets are English unless noted.}
  \label{tab:datasets}
  \centering
  \begin{tabular}{lrrrr}
    \toprule
    Dataset & Train & Dev & Test & Source \\
    \midrule
    CoNLL-2003 & 14,987 & 3,466 & 3,684 & Reuters \\
    Ontonotes & 75,722 & 8,321 & 8,263 & Various \\
    \bottomrule
  \end{tabular}
\end{table}

\textbf{Preprocessing:} Tokenized using spaCy, lowercased.
Rare entities (<5 occurrences) replaced with <UNK>.
```

#### Baseline Selection

```latex
We compare our approach against the following baselines:

\textbf{Standard baselines:}
\begin{itemize}
    \item \textbf{Baseline A}: The method of \citet{smith2023}.
    \item \textbf{Baseline B}: Vanilla BERT fine-tuning \citep{devlin2019}.
\end{itemize}

\textbf{State-of-the-art:}
\begin{itemize}
    \item \textbf{Method C}: Recent state-of-the-art from \citet{jones2024}.
    \item \textbf{Method D}: The approach of \citet{brown2022}.
\end{itemize}
```

#### Metric Reporting

```latex
\subsection{Metrics}
We report standard NLP metrics for each task:

\textbf{Sequence labeling:} Token-level F1 score (CoNLL-style).
\textbf{Text classification:} Accuracy, macro F1 score.
\textbf{Generation:} BLEU \citep{papineni2002bleu}, ROUGE-L \citep{lin2004rouge},
METEOR \citep{banerjee2005meteor}.

All scores are computed using the official evaluation scripts.
```

#### Statistical Significance

```latex
\subsection{Statistical Significance}
We assess statistical significance using paired t-tests
(5 seeds, $\alpha = 0.05$) following \citet{berg2012empirical}.
Results marked with $\dagger$ indicate $p < 0.05$ vs. the best baseline.
```

#### Error Analysis

```latex
\subsection{Error Analysis}
We manually analyze 200 randomly sampled errors.

\textbf{Main error categories:}
\begin{itemize}
    \item \textbf{Long-range dependencies} (34\%): The model struggles
    with dependencies spanning more than 512 tokens.
    \item \textbf{Rare tokens} (28\%): OOV words that appear fewer
    than 5 times in training.
    \item \textbf{Ambiguous cases} (22\%): Examples where even human
    annotators disagree.
    \item \textbf{Annotation noise} (16\%): Likely annotation errors in
    the dataset.
\end{itemize}
```

### Key EMNLP Expectations

- **Datasets:** Describe source, size, language, domain, preprocessing, licensing. Include data splits (train/dev/test).
- **Baselines:** Compare against strong, well-established baselines (not strawmen).
- **Metrics:** Report standard NLP metrics (accuracy, F1, BLEU, ROUGE-L, BERTScore, etc.). Include confidence intervals or statistical significance tests.
- **Ablation:** Include ablation studies to isolate the effect of each component.
- **Error Analysis:** Provide qualitative examples of successes and failures. Show representative errors.
- **Limitations:** Discuss limitations honestly (model assumptions, computational cost, generalizability, bias).

---

## References

Same as ACL — use `acl_natbib`:

```latex
\bibliographystyle{acl_natbib}
\bibliography{anthology,your_file}  % include Anthology bibliography
```

Download the ACL Anthology BibTeX: [https://aclweb.org/anthology/anthology.bib.gz](https://aclweb.org/anthology/anthology.bib.gz).

---

## Figures and Tables

Same as ACL:

```latex
\begin{figure}[t]
  \includegraphics[width=\linewidth]{figure}
  \caption{Caption here.}
  \label{fig:label}
\end{figure}
```

Use PDF, PNG, or EPS. Match fonts to document. Do not override caption sizes.

For tables, use `booktabs`-style rules (no vertical lines). See ACL skill for examples.

---

## Supplementary Materials

Check the EMNLP 2026 CFP for supplementary material policy. Typical rules:

- Supplementary files (code, data, proofs, additional experiments) are **not** reviewed.
- Label supplementary files clearly and reference them from the main text.
- Do not exceed file size limits.
- Anonymize any supplementary code or data before uploading.

### Supplementary Checklist

```latex
% In main paper:
Detailed proofs are provided in Appendix A.
Extended experimental results are in Appendix B.
Our code is available at [anonymous URL].

% In supplementary:
\section*{Appendix A: Proofs}
\section*{Appendix B: Extended Experiments}
\section*{Appendix C: Hyperparameters}
```

---

## Checklist Summary

- [ ] `\usepackage[review]{acl}` for submission
- [ ] All authors anonymized (auto via review mode)
- [ ] Self-citations anonymized or removed
- [ ] No author-identifying metadata in PDF
- [ ] ≤ 8 pages main text (excluding refs/appendix)
- [ ] natbib citations: `\citet{}`, `\citep{}`
- [ ] `acl_natbib` bibliography style
- [ ] Figures: PDF/PNG/EPS, `\includegraphics`, captions
- [ ] Tables: `booktabs`, no vertical rules
- [ ] `\appendix` for supplementary content
- [ ] Limitations section if required
- [ ] Dataset descriptions complete
- [ ] Baseline methods properly cited
- [ ] Statistical significance tested
- [ ] Error analysis included
- [ ] Camera-ready: switch to `\usepackage{acl}`, restore authors and self-citations
