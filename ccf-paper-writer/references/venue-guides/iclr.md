# ICLR Venue Guide

> Migrated from the legacy `ccf-conference-skills/iclr/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `iclr` |
| Venue family | AI |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/ICLR` |
| Official URL | https://iclr.cc |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ICLR 2026 Conference Writing Skill

**CCF-A | AI | Publisher: OpenReview**
**Conference:** https://iclr.cc
**Template:** `ccf-latex-templates/ICLR/main.tex`

## IMPORTANT: OpenReview Is NOT Double-Blind

ICLR uses OpenReview, an **open peer review** platform where:
- Authors are **NOT anonymous** — identities are visible
- Reviewers may be anonymous (not always)
- Papers, reviews, and author responses are all public
- This differs from all other major ML conferences

This means:
1. Include your name and affiliation in the submission
2. You CAN reference your own prior work normally
3. Reviews and your responses are publicly visible
4. The review process is transparent and interactive

## Document Setup

### Preamble Structure

```latex
% === MODE SELECTION ===
\usepackage[submission]{iclr2026_conference}  % For submission/review
% OR:
\usepackage[final]{iclr2026_conference}        % Camera-ready

% Additional packages:
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage{url}
```

### Mode Options

| Mode | Option | Effect |
|------|--------|--------|
| Submission | `[submission]` | Line numbers, review mode |
| Camera-Ready | `[final]` | Removes line numbers, copyright |

### Conditional Content

Use `\ificlrfinal` for content that differs between versions:

```latex
\ificlrfinal
  % Camera-ready specific content
  \section*{Acknowledgments}
\else
  % Submission specific content
\fi
```

## Page Limits

- **Check official CFP** for current page limits
- Limits vary by year — verify at https://iclr.cc
- Appendices typically allowed (check CFP)
- Supplementary material policies vary

## Title and Author Formatting

```latex
\title{Your Paper Title Here}

% Multi-author with \And and \AND:
\author{
  First Author \\
  Institution \\
  \texttt{email@example.com}
  \And
  Second Author \\
  Institution \\
  \texttt{email2@example.com}
  \AND
  Third Author \\
  Institution \\
  \texttt{email3@example.com}
}
```

### Affiliation Formatting

```latex
\affiliation{%
  \normalfont \centering
  \textbf{Institution Name} \\
  Address Line \\
  City, Country
}
```

## Abstract and Keywords

```latex
\begin{abstract}
Your abstract here. ICLR abstracts are typically 150-300 words.
Explain the problem, approach, and main contributions.
ICLR reviewers read abstracts carefully — make it compelling.
\end{abstract}

\keywords{keyword1 \and keyword2 \and keyword3}
```

## Two-Column Layout (Optional)

For two-column title format:
```latex
\twocoltitle[
  \centering
  \begin{tabular}{c}
    Your Title Here \\
    \hline
    \author{Name1 \And Name2 \AND Name3}
  \end{tabular}
]
```

## Recommended ICLR Paper Structure

ICLR values clear, well-motivated papers with strong empirical and/or theoretical contributions.

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
% Why is this problem important? What are the limitations of current approaches?

% Paragraph 3: Our approach
% What is the key insight? How does our approach work?
% What are the key contributions?

% Paragraph 4: Contributions (numbered)
The main contributions of this paper are:
\begin{itemize}
    \item We propose a novel approach to X that addresses Y...
    \item We provide theoretical analysis showing Z...
    \item We demonstrate through extensive experiments that...
\end{itemize}

% Paragraph 5 (optional): Roadmap
The remainder of this paper is organized as follows...

\section{Background and Motivation}
% Necessary context and notation
% Review of prior work and its limitations
% Clearly articulate the gap our work fills

\section{Method}
% Core technical contribution
% Include figures showing architecture/pipeline
% Mathematical formulation with clear equations
% Ablation-ready component design

\section{Theoretical Analysis (if applicable)}
% Formal guarantees, convergence proofs, complexity analysis
% Clear assumptions stated upfront

\section{Experiments}
\subsection{Setup}
% Datasets, metrics, baselines, implementation details
% All details necessary for reproducibility

\subsection{Main Results}
% Present main findings
% Compare against strong baselines
% Include statistical significance

\subsection{Ablation and Analysis}
% Study each component's contribution
% Error analysis, qualitative examples
% Sensitivity analysis

\section{Related Work}
% Position against existing literature
% Categorize by approach, not just list

\section{Conclusion}
% Summary, limitations, future directions
```

## References (natbib with authoryear)

`iclr2026_conference` uses `natbib` with `authoryear` style by default:

```latex
% In document:
\bibliographystyle{iclr2026_conference}
\bibliography{references}

% Citations:
\citet{Author20}    % Author (2020)
\citep{Author20}    % (Author, 2020)
```

## Figures and Tables

```latex
% Figure: include in single column or full width
\begin{figure}[t]
  \centering
  \includegraphics[width=0.8\linewidth]{figure}
  \caption{Figure caption here.}
  \label{fig:example}
\end{figure}

% For full-width figure:
\begin{figure*}[t]
  \centering
  \includegraphics[width=0.9\textwidth]{figure}
  \caption{Full-width figure caption.}
  \label{fig:wide}
\end{figure*}

% Table with booktabs:
\begin{table}
  \caption{Table caption above.}
  \label{tab:example}
  \centering
  \begin{tabular}{ccc}
    \toprule
    Col1 & Col2 & Col3 \\
    \midrule
    data & data & data \\
    \bottomrule
  \end{tabular}
\end{table}
```

## ICLR-Specific Writing Conventions

### What ICLR Reviewers Value

1. **Clear motivation**: Why should we care about this problem?
2. **Novelty**: What is the new insight or approach?
3. **Theoretical depth**: Formal analysis and guarantees
4. **Empirical rigor**: Thorough experiments with strong baselines
5. **Reproducibility**: Sufficient detail to reproduce results
6. **Clarity**: Well-written, well-organized paper

### Theoretical Writing for ICLR

```latex
\section{Theoretical Analysis}

\begin{assumption}
\label{assum:1}
[State your assumptions clearly]
\end{assumption}

\begin{convergence}
\label{them:main}
Under Assumption \ref{assum:1}, the algorithm converges at rate...
\end{convergence}

\begin{Proof}
[Proof here]
\end{Proof}
```

### Experimental Rigor

```latex
\section{Experiments}

\subsection{Setup}
\textbf{Datasets:} We evaluate on standard benchmarks:
\begin{itemize}
    \item \textbf{CIFAR-10}: 50K training, 10K test images.
    \item \textbf{ImageNet}: 1.2M training, 50K validation images.
    \item \textbf{GLUE}: 9 NLU tasks.
\end{itemize}

\textbf{Baselines:} We compare against:
\begin{itemize}
    \item Standard methods from literature
    \item State-of-the-art approaches on each benchmark
    \item Ablation variants of our method
\end{itemize}

\textbf{Implementation:} PyTorch. All experiments on NVIDIA A100 GPUs.
Learning rate: 1e-3, batch size: 256, trained for 100 epochs.
Hyperparameters selected via validation set tuning.

\textbf{Statistics:} Results are mean $\pm$ std over 5 seeds.
Statistical significance via paired t-test.

\subsection{Main Results}
\autoref{tab:main} shows our method achieves state-of-the-art
across all benchmarks, improving over previous best by X\%.

\subsection{Ablation Study}
\autoref{tab:ablation} shows the contribution of each component.
```

## OpenReview-Specific Requirements

Since papers are **not anonymous**:

1. **Include author information** — required for submission
2. **PDF metadata** — should contain author names
3. **Self-citations** — no special anonymization needed
4. **Dual submissions** — must be declared on OpenReview
5. **Camera-ready** — update with final author information

### Dual Submission Policy

ICLR has strict dual submission rules:
- Cannot submit the same paper to ICLR and another venue simultaneously
- Must withdraw from other venues if accepted at ICLR
- Can submit to arXiv before ICLR deadline (encouraged)
- Check current CFP for exact rules

### Preprint/ArXiv Policy

ICLR allows (and often encourages) posting preprints on arXiv:
- No special anonymization needed
- Can cite your own arXiv preprint
- arXiv posting is encouraged for reproducibility

## Rebuttal Period

ICLR has a mandatory rebuttal period where authors can respond to reviews.

### Rebuttal Structure

```latex
\section*{Response to Reviewers}

We thank the reviewers for their thoughtful comments and detailed feedback.

\textbf{Regarding Reviewer X's concern about Y:}
We appreciate this observation. To address this concern, we:

\begin{itemize}
    \item Added new experiments showing Z (see Figure X in this response)
    \item Clarified our approach in the revised paper
    \item Acknowledged this limitation in the conclusion
\end{itemize}

\textbf{Regarding the comparison with method A:}
We have added method A to our comparison. Results show our method
outperforms A by X\% on the primary metric.

\textbf{Regarding the theoretical assumptions:}
The reviewer raises an important point. We have added a more
rigorous analysis in the appendix showing that the assumption can
be relaxed to...
```

### Rebuttal Best Practices

**DO:**
- Thank reviewers for their time
- Address every concern specifically
- Provide new evidence when asked
- Be humble and constructive
- Clarify misunderstandings politely

**DON'T:**
- Be defensive or dismissive
- Argue about scores
- Make excuses
- Promise changes you can't deliver
- Be rude or aggressive

## Camera-Ready Compilation

```latex
% Change from:
\usepackage[submission]{iclr2026_conference}
% To:
\usepackage[final]{iclr2026_conference}
```

For camera-ready:
1. Remove line numbers
2. Add acknowledgments
3. Update author information if needed
4. Ensure all author affiliations are correct
5. Add supplementary materials if needed

### Camera-Ready Checklist

- [ ] Changed to `\usepackage[final]{iclr2026_conference}`
- [ ] All author information complete and correct
- [ ] Acknowledgments section added
- [ ] Funding disclosures included
- [ ] No confidential information remaining
- [ ] PDF compiles without errors

## Formatting Rules

- **Paper size:** US Letter
- **Font:** Times New Roman (automatic)
- **Text:** 10pt
- **Margins:** Standard conference margins
- **Columns:** Two-column format
- **Line spacing:** Check style file defaults

## Submission Process

1. Submit PDF to OpenReview: https://openreview.net/group?id=ICLR.cc/2026/Conference
2. Paper becomes publicly visible with author info
3. Reviewers may be anonymous
4. Author response period available
5. Final camera-ready after acceptance

## Checklist Before Submission

- [ ] Author information clearly visible
- [ ] PDF compiles without errors
- [ ] Abstract is clear and compelling
- [ ] Keywords properly set
- [ ] References in correct format
- [ ] Figures/tables properly formatted
- [ ] No confidential information that shouldn't be public
- [ ] Dual submissions declared on OpenReview
- [ ] All notation defined before use
- [ ] Baselines properly documented
- [ ] Statistical significance tested
- [ ] Ablation studies included
- [ ] Reproducibility details provided
