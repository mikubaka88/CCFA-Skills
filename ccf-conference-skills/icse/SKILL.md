---
name: icse
description: Writing and formatting guidance for ICSE (ACM/IEEE International Conference on Software Engineering). Use when drafting, formatting, and submitting to ICSE 2026. Covers ACM acmart with sigconf format, anonymous double-blind review mode, ICSE page limits (14 pages), software engineering conventions, research and technical papers, theorem environments, code listings, camera-ready preparation with DOI/ISBN, and ACM-Reference-Format citations.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ICSE 2026 Conference Writing Skill

**CCF-A | SE | Publisher: ACM/IEEE**
**Conference:** https://conf.researchr.org/track/icse-2026/icse-2026-papers
**Template:** `ccf-latex-templates/ICSE/acmart.cls` (ACM acmart, SIGCONF format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\setcopyright{acmlicensed}
\acmConference[ICSE 2026]{Proceedings of the 48th ACM/IEEE International Conference
  on Software Engineering}{May 17--23, 2026}{Vancouver, Canada}
\acmISBN{978-X-XXXX-XXXX-X/26/05}
\acmDOI{10.1145/XXXXXXX}
\acmPrice{}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{algorithm}
\usepackage[noend]{algorithmic}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{cleveref}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **14 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. Do not include author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize URLs (e.g., GitHub repositories, institutional links)
4. Remove PDF metadata that reveals authorship
5. Do not include acknowledgments

## Section Organization

Standard ICSE paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background/Motivation** — Context, related work positioning
3. **Approach/Method** — Core technical contribution
4. **Implementation/Development** — System details, tool support
5. **Evaluation** — Experimental methodology, results, comparison
6. **Discussion** — Threats to validity, limitations
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## ICSE-Specific Writing Conventions

### Introduction Structure for SE Papers

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
Software engineering increasingly faces challenges in [area].
Current approaches to [problem] suffer from [limitation].
This is particularly problematic because [impact].

% Paragraph 3: Gap in prior work
Prior work has addressed [aspect] through [approaches].
However, these approaches [gap/motivation for new work].

% Paragraph 4: Our approach
In this paper, we propose a novel approach that [key contribution].
Our approach addresses [challenge] by [technical contribution].

% Paragraph 5: Contributions (numbered)
Our main contributions are:
\begin{itemize}
    \item We propose [Name], a novel approach to [problem] that [benefit].
    \item We implement [tool/system] and demonstrate [evidence].
    \item We conduct an empirical study with [N] practitioners showing [result].
    \item We make our [artifacts] publicly available.
\end{itemize}
```

### Research Type Classifications

ICSE distinguishes between research types:

**Solution Papers:**
```latex
\section{Approach}
We propose a novel approach called [Name] that addresses [problem].
The approach consists of three main components...

\section{Implementation}
We implemented [Name] as a [tool/library/framework]...
```

**Empirical Papers:**
```latex
\section{Study Design}
We conducted a [type] study following [methodology].

\subsection{Participants}
We recruited [N] [population] through [recruitment method].

\subsection{Procedure}
The study consisted of [phases] conducted over [timeframe].

\subsection{Data Collection}
We collected [types of data] using [methods].
```

## Theorem Environments

ICSE papers may include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{property}{Property}
\newtheorem{invariant}{Invariant}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
```

## Code Listings

```latex
% Inline code:
The static analyzer uses \lstinline!Soot! for bytecode analysis.

% Code blocks:
\begin{lstlisting}[language=Python, caption={Linter rule implementation}, label={lst:rule}]
class ResourceLeakRule(LinterRule):
    def analyze_function(self, func: ast.FunctionDef):
        resource_calls = []
        for node in ast.walk(func):
            if isinstance(node, ast.Call):
                if self.is_resource_alloc(node):
                    resource_calls.append(node.func.id)
        return ResourceLeakWarning(func.name, resource_calls)
\end{lstlisting}
```

## Evaluation Standards

```latex
\section{Evaluation}
We evaluate [Name] through [type of evaluation]:

\subsection{Research Questions}
We investigate the following research questions:
\begin{itemize}
    \item \textbf{RQ1:} [Question]
    \item \textbf{RQ2:} [Question]
\end{itemize}

\subsection{Study Setup}
\textbf{Subjects/Dataset:} [Description]
\textbf{Metrics:} [List metrics]
\textbf{Baselines/Comparison:} [Methods compared]

\subsection{Results}
\autoref{tab:results} shows the results for RQ1...
Results for RQ2 are shown in \autoref{fig:graph}...
```

### Quantitative Evaluation

```latex
\begin{table}[h]
  \caption{Comparison of defect detection tools on [dataset].}
  \label{tab:results}
  \centering
  \begin{tabular}{lcccccc}
    \toprule
    \multirow{2}{*}{Tool} & \multicolumn{2}{c}{Precision} &
      \multicolumn{2}{c}{Recall} & \multicolumn{2}{c}{F1} \\
    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
          & Mean & SD & Mean & SD & Mean & SD \\
    \midrule
    Tool A & 0.72 & 0.05 & 0.68 & 0.04 & 0.70 & 0.03 \\
    Tool B & 0.81 & 0.03 & 0.74 & 0.06 & 0.77 & 0.04 \\
    \textbf{Ours} & \textbf{0.85} & \textbf{0.02} & \textbf{0.79} & \textbf{0.03} & \textbf{0.82} & \textbf{0.02} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Figures and Tables

- Use vector formats (.pdf) where possible
- Ensure figures are legible in grayscale
- Number figures and tables sequentially
- Captions should be descriptive and self-contained

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/approach}
  \caption{Overview of the proposed approach showing the main phases:
    (1) input processing, (2) analysis, (3) result generation.}
  \label{fig:approach}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

Each reference must list **all authors** — do not use "et al." in the bibliography.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, no page limit

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author/anonymization info removed
- [ ] No self-identifying URLs or citations
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`
- [ ] Research questions clearly stated
- [ ] Evaluation methodology sound
- [ ] Threats to validity discussed

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add `\setcopyright{acmlicensed}` (or appropriate)
- [ ] Fill `\acmConference`, `\acmISBN`, `\acmDOI`, `\acmPrice`
- [ ] Restore author names and affiliations
- [ ] Include page numbers (`\settopmatter{printfolios=true}`)
- [ ] Add acknowledgments if desired
