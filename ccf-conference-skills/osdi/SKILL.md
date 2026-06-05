---
name: osdi
description: Writing and formatting guidance for OSDI (USENIX Symposium on Operating Systems Design and Implementation) papers. Use when drafting, formatting, and submitting to OSDI 2026. Covers ACM acmart sigplan format with anonymous review mode, camera-ready metadata (DOI/ISBN/price), OSDI-specific page limits (14 pages), theorem environments, code listing conventions, systems-specific evaluation standards, and USENIX conference submission policies.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# OSDI 2026 Conference Writing Skill

**CCF-A | SE/Systems | Publisher: USENIX**
**Conference:** https://www.usenix.org/conference/osdi26
**Template:** `ccf-latex-templates/OSDI/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\setcopyright{usenix}          % or acmlicensed
\acmConference[OSDI 2026]{OSDI '26: 16th USENIX Symposium on...}
                         {July 7--9, 2026}{Seattle, WA, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
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
| Main paper (submission) | **14 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

OSDI enforces a strict 14-page limit for the main body. References and appendix do not count toward this limit, but reviewers are not required to read the appendix.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. Do not include author names anywhere in the submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize URLs (e.g., GitHub repositories)
4. Remove PDF metadata that reveals authorship
5. Do not include acknowledgments

## Camera-Ready Differences

When preparing camera-ready after acceptance:

1. Remove `review` and `anonymous` options from `\documentclass`
2. Add `\setcopyright{usenix}` or appropriate rights mode
3. Fill in `\acmConference` with full conference title and dates
4. Add `\acmISBN`, `\acmDOI`, and `\acmPrice` fields
5. Restore all author names and affiliations
6. Add acknowledgments if desired

## Section Organization

Standard OSDI paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions explicitly)
2. **Background & Motivation** — Context and why the problem matters
3. **Design/Approach** — Core technical contribution
4. **Implementation** — System details, complexity, design decisions
5. **Evaluation** — Experimental methodology, results, comparisons
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future work
8. References
9. Appendix (optional)

## OSDI-Specific Writing Conventions

### Introduction Structure for OSDI Papers

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation
Modern [systems/applications] require [properties].
Current solutions achieve [benefits] but suffer from [limitations].
As [trend] accelerates, these limitations become increasingly problematic.

% Paragraph 2: Why existing approaches fail
Prior systems have addressed [related problems] through [approaches].
However, these systems assume [assumption] and cannot scale to [scenario].
Alternatively, [approaches] achieve [benefit] but require [trade-off].

% Paragraph 3: Our approach
In this paper, we present [Name], a new [system/approach] that achieves [benefit].
The key insight is that [insight].
[Name] consists of [components] that work together to [mechanism].

% Paragraph 4: Contributions (numbered)
This paper makes the following contributions:
\begin{itemize}
    \item We design and implement [Name], a [system] that achieves [properties].
    \item We identify key design principles: [P1], [P2], [P3].
    \item We evaluate [Name] on [workloads] showing [results].
    \item We make our [artifacts] publicly available.
\end{itemize}
```

### Design Section Structure

```latex
\section{Design}

\subsection{Overview}
\autoref{fig:overview} shows the high-level architecture of [Name].
The system consists of [N] main components: [list components].

\subsection{Data Structures}
We use [data structure] to store [information]:
\begin{lstlisting}[language=C++, caption={Core data structure}]
struct Entry {
    Key key;
    Value value;
    uint64_t version;
    // Metadata...
};
\end{lstlisting}

\subsection{Key Algorithms}
The core algorithm operates as follows:
\begin{enumerate}
    \item [Step 1]
    \item [Step 2]
    \item [Step 3]
\end{enumerate}
```

### Implementation Section

```latex
\section{Implementation}
We implemented [Name] in [N] lines of [language].
The implementation required [time] and consists of:

\textbf{Core system:} [description]

\textbf{Supporting components:} [description]

\textbf{Key challenges:} We addressed three main challenges:
\begin{itemize}
    \item \textbf{Challenge 1:} [Description] — [Solution]
    \item \textbf{Challenge 2:} [Description] — [Solution]
    \item \textbf{Challenge 3:} [Description] — [Solution]
\end{itemize}
```

## Theorem Environments

OSDI papers commonly use formal reasoning environments:

```latex
\theoremstyle{plain}
\newtheorem{property}{Property}
\newtheorem{invariant}{Invariant}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}      % unnumbered for main theorems
\newtheorem*{lemma}{Lemma}

\theoremstyle{plain}
\newtheorem*{corollary}{Corollary}

\theoremstyle{plain}
\newtheorem*{invariant}{Invariant}
```

## Code Listings

Use `lstinline{}` for inline code and `lstlisting` for blocks:

```latex
% Inline code:
The kernel uses \lstinline!spin_lock_irqsave()! to protect the shared queue.

% Code blocks:
\begin{lstlisting}[language=C, caption={Ring buffer implementation}, label={lst:ringbuf}]
struct ring_buffer {
    void **entries;
    size_t head, tail;
    size_t capacity;
};

bool enqueue(struct ring_buffer *rb, void *item) {
    size_t next = (rb->head + 1) % rb->capacity;
    if (next == rb->tail) return false;  // Full
    rb->entries[next] = item;
    rb->head = next;
    return true;
}
\end{lstlisting}
```

## Sub-subsections

OSDI uses `\paragraph{}` for sub-subsections (no numbering, bold heading followed by inline text):

```latex
\section{Design}
\subsection{Overview}
paragraph{Scheduling Policy}  % This is a sub-subsection
The FCFS policy orders requests by...
```

## Systems Evaluation

```latex
\section{Evaluation}
We evaluate [Name] to answer:

\textbf{RQ1:} How does [Name] perform compared to [baselines]?

\textbf{RQ2:} What is the overhead of [Name]'s mechanisms?

\textbf{RQ3:} How does [Name] scale to [larger workloads]?

\subsection{Experimental Setup}
\textbf{Platform:} [Hardware configuration]
\textbf{Baselines:} [List of comparison systems]

\subsection{Microbenchmarks}
\autoref{fig:micro} shows component-level performance.

\subsection{End-to-End Performance}
\autoref{tab:results} summarizes end-to-end performance.
```

### Performance Results

```latex
\begin{table}[h]
  \caption{End-to-end performance (throughput in ops/sec).
    Best results in \textbf{bold}.}
  \label{tab:results}
  \centering
  \begin{tabular}{lrr}
    \toprule
    System & Throughput & Latency (P99) \\
    \midrule
    Baseline & 10.2K & 2.3ms \\
    Related Work & 8.7K & 3.1ms \\
    \textbf{Ours} & \textbf{18.7K} & \textbf{1.1ms} \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Figures and Tables

- Use vector formats (.pdf, .eps) where possible
- Ensure figures are legible in grayscale (reviewers often print in B&W)
- Number figures and tables sequentially
- Captions should be descriptive and self-contained
- Place tables near their first reference

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/design-overview}
  \caption{System architecture overview showing the interaction
    between the scheduler and worker threads.}
  \label{fig:overview}
\end{figure}
```

## References (natbib)

ACM-Reference-Format bibstyle with author-year citations:

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{smith2023}      % Smith et al. (2023)
\citep{smith2023}      % (Smith et al. 2023)
```

Each reference must list **all authors** — do not use "et al." in the bibliography.

## Formatting Rules

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, no page limit
- **Line spacing:** Single-spaced (template default)

## Submission Checklist

- [ ] 14 pages or fewer (main body)
- [ ] `\documentclass[sigplan,review,anonymous]`
- [ ] All author/anonymization info removed
- [ ] No self-identifying URLs or citations
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`
- [ ] Design rationale explained
- [ ] Implementation challenges discussed

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add `\setcopyright{usenix}` (or appropriate)
- [ ] Fill `\acmConference`, `\acmISBN`, `\acmDOI`, `\acmPrice`
- [ ] Restore author names and affiliations
- [ ] Include page numbers (`\settopmatter{printfolios=true}`)
