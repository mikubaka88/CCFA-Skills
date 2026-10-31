# FOCS Venue Guide

> Migrated from the legacy `ccf-conference-skills/focs/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `focs` |
| Venue family | Theory |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/FOCS/IEEEtran.cls` |
| Official URL | https://focs2026.eecs.stanford.edu |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# FOCS 2026 Conference Writing Skill

**CCF-A | Theory | Publisher: IEEE**
**Conference:** https://focs2026.eecs.stanford.edu
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

## Section Organization

FOCS papers are proof-heavy theory papers:

1. **Abstract** — Main theorem statements, brief proof sketch
2. **Introduction** — Problem, prior results, our contribution (enumerate theorems)
3. **Technical Overview** — Proof ideas and intuition
4. **Preliminaries** — Definitions, notation, known results
5. **Main Technical Sections** — Proofs organized by theorem
6. **Applications / Extensions** — Optional concrete applications
7. **References**
8. Appendix (optional: omitted proofs, additional details)

## Theorem Environments

FOCS uses rigorous theorem environments:

```latex
\theoremstyle{plain}
\newtheorem{main}{Theorem}  % Main results numbered prominently

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem*{proposition}{Proposition}
\newtheorem*{fact}{Fact}
\newtheorem*{claim}{Claim}
\newtheorem{property}{Property}

\newtheorem*{definition}{Definition}
\newtheorem*{invariant}{Invariant}

% Example:
\begin{main}
  \label[main]{thm:gap-detection}
  There is no algorithm that, given a graph $G$ and parameters
  $\epsilon > 0$ and $k \in \mathbb{N}$, decides whether $G$ has
  a vertex cover of size at most $k$ or whether every vertex cover
  has size at least $(1+\epsilon)k$, in time $n^{o(k)}$.
\end{main}
```

## Proof Structure

FOCS proofs should be well-organized with clear structure:

```latex
\section{Gap-Hardness for Vertex Cover}

\begin{main*}[Gap-Hardness]
  There is no algorithm that distinguishes between:
  \begin{itemize}
    \item $\mathbf{YES}$: $G$ has a vertex cover of size at most $k$
    \item $\mathbf{NO}$: Every vertex cover has size at least $(1+\epsilon)k$
  \end{itemize}
  with success probability $2/3$ in time $n^{o(k)}$.
\end{main*}

\begin{Proof}
  We reduce from the $k$-Clique problem.

  \paragraph*{Reduction.} Given an instance $(H, k)$ of $k$-Clique,
  we construct a graph $G$ as follows:
  \begin{enumerate}
    \item For each vertex $v \in V(H)$, create a vertex $v' \in V(G)$.
    \item For each edge $(u, v) \in E(H)$, create a gadget $g_{uv}$...
    \item [Full construction details...]
  \end{enumerate}

  \paragraph*{Completeness.} If $H$ contains a $k$-clique,
  then $G$ has a vertex cover of size $n - \binom{k}{2}$...

  \paragraph*{Soundness.} If $H$ has no $k$-clique,
  then every vertex cover of $G$ has size at least
  $n - \binom{k}{2} + \epsilon n$...

  The reduction runs in time $n^{O(1)}$ and preserves the gap.
\end{Proof}
```

## Algorithm Description

FOCS papers describe algorithms formally:

```latex
\subsection{The Algorithm}
\begin algorithm}[h]
\caption{Approximate Set Cover}
\label[algorithm]{alg:set-cover}
\textbf{Input:} Universe $U$ of size $n$, collection $\mathcal{S}$ of subsets
\textbf{Output:} A set cover $\mathcal{C} \subseteq \mathcal{S}$
\begin{algorithmic}[1]
\STATE $\mathcal{C} \gets \emptyset$
\STATE $U' \gets U$
\WHILE{$U' \neq \emptyset$}
  \STATE Choose $S \in \mathcal{S}$ that maximizes $|S \cap U'|$
  \STATE $\mathcal{C} \gets \mathcal{C} \cup \{S\}$
  \STATE $U' \gets U' \setminus S$
\ENDWHILE
\RETURN $\mathcal{C}$
\end{algorithmic}
\end{algorithm}
```

## Figures and Tables

FOCS papers use minimal figures, primarily for reductions:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.8\linewidth]{figs/reduction}
  \caption{Reduction from $k$-Clique to Gap-VC.
    Vertices in $G$ correspond to vertices and edges of $H$,
    with gadgets enforcing the clique structure.
    Edge types are color-coded: black for vertex vertices,
    red for edge vertices, blue for gadget edges.}
  \label{fig:reduction}
\end{figure}
```

## References

IEEE uses numeric citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Numeric citations
\cite{arora2009computational}
```

## Content Checklist

- [ ] Main theorems clearly stated
- [ ] Proofs complete and rigorous
