---
name: cav
description: Writing and formatting guidance for CAV (International Conference on Computer Aided Verification) papers. Use when drafting, formatting, and submitting to CAV 2026. Covers Springer LNCS llncs class, CAV page limits (16 pages), double-blind anonymity, theorem environments for formal verification, proof by induction/reduction arguments, and Springer camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CAV 2026 Conference Writing Skill

**CCF-A | Theory | Publisher: Springer (LNCS)**
**Conference:** https://cavconference.org/2026
**Template:** `ccf-latex-templates/CAV/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass{article}

% Springer LNCS setup:
\usepackage{llncs}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amstext}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{url}
\usepackage{cleveref}
\usepackage{listings}

% For review: remove author info
% For camera-ready: restore in LNCS format
```

### Required Packages

```latex
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amstext}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{url}
\usepackage{cleveref}
\usepackage{listings}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **16 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

## Anonymity Requirements

CAV uses double-blind review:

1. Remove all author names and affiliations from the submission
2. Use "Anonymous" as author during submission
3. Third-person self-citations: "Smith et al. showed..." not "we showed..."
4. Anonymize all URLs, GitHub links, project pages
5. Clear PDF metadata
6. Remove acknowledgments

## Section Organization

CAV papers follow a formal verification paper structure:

1. **Abstract** — Theorem statements, brief verification methodology
2. **Introduction** — Problem, verification challenge, contributions
3. **Background & Preliminaries** — Formal definitions, notation
4. **Technical Approach** — Verification algorithm, encoding, reduction
5. **Proof of Correctness** — Theoretical guarantees
6. **Implementation & Experimental Results** — Tool, benchmarks, comparisons
7. **Related Work**
8. **Conclusion**
9. References
10. Appendix (optional)

## Theorem Environments

CAV uses standard theorem environments:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem*{invariant}{Invariant}
\newtheorem*{property}{Property}

% Example with label:
\begin{definition}[Transition System]
  \label[definition]{def:ts}
  A \emph{transition system} $TS$ is a tuple
  $(S, S_0, R, L)$ where $S$ is a finite set of states,
  $S_0 \subseteq S$ is the set of initial states,
  $R \subseteq S \times S$ is the transition relation, and
  $L: S \to 2^{AP}$ is a labeling function.
\end{definition}
```

## CAV-Specific Writing Conventions

### Introduction Structure

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation
Verification of [system/class] is challenging because [reasons].
Errors in such systems can lead to [consequences].

% Paragraph 2: Gap in prior work
Existing verification techniques face limitations:
\begin{itemize}
    \item [Technique A] achieves [benefit] but requires [limitation].
    \item [Technique B] handles [case] but scales poorly to [scale].
\end{itemize}

% Paragraph 3: Our approach
In this paper, we propose a new approach that addresses these challenges.
Our key insight is that [insight].

% Paragraph 4: Contributions (numbered)
Our main contributions are:
\begin{itemize}
    \item We present a new verification algorithm for [problem] with [benefit].
    \item We prove the algorithm's correctness and complexity.
    \item We implement the approach in a tool and evaluate on benchmarks.
\end{itemize}
```

### Verification Proofs

CAV proofs typically involve invariant arguments or reduction proofs:

```latex
\section{Correctness Proof}

\begin{main*}[Soundness]
  \label[main*]{thm:soundness}
  The verification algorithm of \autoref{sec:algorithm}
  returns \texttt{SAFE} only if the program $P$ satisfies
  the specification $\varphi$.
\end{main*}

\begin{Proof}
  We prove by induction on the number of refinement steps.

  \textbf{Base Case.} Initially, the abstract domain $D_0$ contains
  exactly the set of reachable states, so $D_0 \models \varphi$
  implies $P \models \varphi$.

  \textbf{Inductive Step.} Assume that after $i$ refinement steps,
  $D_i \models \varphi$ implies $P \models \varphi$.
  The $(i+1)$-th refinement $D_{i+1}$ adds constraints that are
  logically implied by $D_i$. Therefore...

  By induction, when the algorithm terminates with $D_n \models \varphi$,
  we have $P \models \varphi$.
\end{Proof}
```

### Reduction Proofs

```latex
\begin{main*}[Reduction to SAT]
  \label[main*]{thm:reduction}
  The model checking problem for [class] is polynomial-time
  reducible to SAT.
\end{main*}

\begin{Proof}
  We construct a formula $\varphi$ such that:
  \[
  M \models \varphi \iff M \models \text{SPEC}
  \]
  The construction proceeds as follows:
  \begin{enumerate}
      \item Encode each variable $x_i$ as a fresh propositional variable.
      \item Encode each transition as a clause.
      \item Encode the property as a propositional formula.
  \end{enumerate}
  The size of $\varphi$ is $O(n^2)$ where $n$ is the size of $M$.
\end{Proof}
```

## Implementation Description

CAV papers require implementation details:

```latex
\section{Implementation}
We implemented our approach in a tool called \toolname.
\toolname{} is built on top of the \zthree{} SMT solver
and uses the following key data structures:

\begin{itemize}
  \item \textbf{Constraint graph:} A directed graph where nodes
    represent program variables and edges represent dependency relations.
  \item \textbf{Abstraction cache:} A hash map from program locations
    to abstract states, enabling efficient join operations.
\end{itemize}

The tool consists of approximately 15,000 lines of OCaml code
and exposes a command-line interface compatible with the SV-COMP format.
```

## Experimental Evaluation

CAV evaluation uses standard benchmarks:

```latex
\section{Experimental Evaluation}
We evaluated \toolname{} on the SV-COMP 2025 benchmark suite
and compared it against two state-of-the-art tools:
Spacer~\citep{padhi} and FreqHorn~\citep{horn}.

\begin{table}[t]
  \caption{Results on SV-COMP benchmark (1,234 benchmarks).
    Timeout set to 300s. Best results in bold.}
  \label{tab:results}
  \begin{tabular}{lcccccc}
    \toprule
    Category & \toolname & Spacer & FreqHorn \\
    \midrule
    Control flow & 145/150 & 142/150 & 138/150 \\
    Concurrency & \textbf{89/100} & 82/100 & 76/100 \\
    Arrays & \textbf{203/220} & 198/220 & 189/220 \\
    \midrule
    \textbf{Total} & \textbf{437/470} & 422/470 & 403/470 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References

Springer LNCS uses numeric citations:

```latex
\bibliographystyle{splncs04}
\bibliography{references}

% Numeric citations
\cite{clarke2000model}
```

## Formatting Rules

- **Format:** Springer LNCS (single-column, article)
- **Paper size:** A4
- **Body font:** 10pt
- **Margins:** 2.5cm all sides
- **References:** Numbered, appear at end of paper

## Submission Checklist

- [ ] 16 pages or fewer (main body)
- [ ] Author information removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] Formal correctness proofs included
- [ ] Implementation described
- [ ] SV-COMP or standard benchmarks used

## Camera-Ready Checklist

- [ ] Restore author information in LNCS format
- [ ] Add institution addresses
- [ ] Follow Springer's camera-ready instructions
- [ ] Ensure A4 paper size
