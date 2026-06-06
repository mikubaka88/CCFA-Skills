# ISSTA Venue Guide

> Migrated from the legacy `ccf-conference-skills/issta/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `issta` |
| Venue family | SE |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/ISSTA/acmart.cls` |
| Official URL | https://issta.org/issta2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# ISSTA 2026 Conference Writing Skill

**CCF-A | SE | Publisher: ACM**
**Conference:** https://issta.org/issta2026
**Template:** `ccf-latex-templates/ISSTA/acmart.cls` (ACM acmart, SIGCONF format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\setcopyright{acmlicensed}
\acmConference[ISSTA 2026]{Proceedings of the 35th ACM SIGSOFT International Symposium
  on Software Testing and Analysis}{July 12--16, 2026}{Seoul, South Korea}
\acmISBN{978-X-XXXX-XXXX-X/26/07}
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
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
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

Standard ISSTA paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background/Motivation** — Context, testing/analysis foundations
3. **Approach/Method** — Core technical contribution
4. **Implementation** — Tool details, optimizations
5. **Evaluation** — Experimental methodology, benchmarks, results
6. **Discussion** — Threats to validity, limitations
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## ISSTA-Specific Writing Conventions

### Introduction Structure for Testing Papers

```latex
\section{Introduction}
% Paragraph 1-2: Problem and motivation
Testing [software/system] is challenging because [reasons].
Current testing techniques fail to [gap].
This is particularly problematic for [impact].

% Paragraph 3: Gap in prior work
Prior work on [testing problem] has explored [approaches].
However, these approaches [limitation].

% Paragraph 4: Our approach
In this paper, we propose a novel approach that [key contribution].
Our approach addresses [challenge] by [technical mechanism].

% Paragraph 5: Contributions (numbered)
Our main contributions are:
\begin{itemize}
    \item We propose [Name], a novel testing approach that [benefit].
    \item We implement [tool] supporting [capabilities].
    \item We evaluate on [benchmarks] showing [results].
    \item We make our [artifacts] publicly available.
\end{itemize}
```

### Testing-Specific Terminology

```latex
\section{Background}

\subsection{Testing Problem}
We focus on testing [system type] for [property].
The challenge is that [specific difficulty].

\subsection{Existing Techniques}
\textbf{Coverage-based testing:} [Description]
\textbf{Fuzzing:} [Description]
\textbf{Symbolic execution:} [Description]
```

## Theorem Environments

ISSTA papers may include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{property}{Property}
\newtheorem{invariant}{Invariant}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
```

## Code Listings

```latex
% Inline code:
The test generator uses \lstinline!KLEE! for symbolic execution.

% Code blocks:
\begin{lstlisting}[language=C, caption={Test case generation pseudocode}, label={lst:gen}]
void generate_tests(Function *f) {
    KTestObject *args = klee_gen_inputs(f);
    KTest *ktest = ktest_create();
    
    for (int i = 0; i < MAX_PATHS; i++) {
        State *s = execute_function(f, args);
        if (s->error) {
            record_bug(s->error_type, ktest);
        }
        args = klee_gen_inputs(f);  // New random inputs
    }
}
\end{lstlisting}
```

## Evaluation Standards for Testing Papers

```latex
\section{Evaluation}
We evaluate [Name] through experiments addressing:

\textbf{RQ1 (Effectiveness):} How effective is [Name] at detecting [bugs]?

\textbf{RQ2 (Efficiency):} How efficient is [Name] compared to [baselines]?

\textbf{RQ3 (Scalability):} How does [Name] scale to [larger systems]?

\subsection{Subjects}
We evaluate on [benchmark suite]:

\begin{table}[h]
  \caption{Benchmark subjects.}
  \label{tab:benchmarks}
  \centering
  \begin{tabular}{lrrr}
    \toprule
    Subject & LOC & Tests & Source \\
    \midrule
    Program A & 5,000 & 120 & Real-world \\
    Program B & 12,000 & 340 & OSS \\
    \bottomrule
  \end{tabular}
\end{table}

\subsection{Results}
\autoref{tab:results} shows effectiveness results.
\autoref{fig:scalability} shows scalability analysis.
```

### Bug Detection Evaluation

```latex
\begin{table}[h]
  \caption{Bug detection comparison. TP=true positives, FP=false positives.}
  \label{tab:results}
  \centering
  \begin{tabular}{lcccccc}
    \toprule
    \multirow{2}{*}{Tool} & \multicolumn{2}{c}{Effectiveness} &
      \multicolumn{2}{c}{Efficiency} & \multirow{2}{*}{Time} \\
    \cmidrule(lr){2-3}\cmidrule(lr){4-5}
          & TP & FP & TP/hr & FP/hr & (s) \\
    \midrule
    Baseline & 42 & 18 & 12.3 & 5.2 & 342 \\
    \textbf{Ours} & \textbf{58} & \textbf{12} & \textbf{17.1} & \textbf{3.5} & \textbf{339} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Figures and Tables

- Use vector formats (.pdf) where possible
- Ensure figures are legible in grayscale
- Number figures and tables sequentially
- Captions should be descriptive and self-contained

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

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author/anonymization info removed
- [ ] No self-identifying URLs or citations
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`
- [ ] Research questions clearly stated
- [ ] Comparison with state-of-the-art
- [ ] Limitations discussed

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add `\setcopyright{acmlicensed}` (or appropriate)
- [ ] Fill `\acmConference`, `\acmISBN`, `\acmDOI`, `\acmPrice`
- [ ] Restore author names and affiliations
- [ ] Include page numbers (`\settopmatter{printfolios=true}`)
