---
name: focs
description: Writing and formatting guidance for FOCS (IEEE Symposium on Foundations of Computer Science) papers. Use when drafting, formatting, or submitting to FOCS 2026. Covers IEEEtran LaTeX class, FOCS page limits (12 pages), double-blind anonymity, theory-specific theorem/proof structure, and IEEE camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# FOCS 2026 Conference Writing Skill

**CCF-A | Theory | Publisher: IEEE**
**Conference:** https://focs2026.eecs.stanford.edu
**Template:** `FOCS/IEEEtran.cls` (IEEEtran, conference format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[conference]{IEEEtran}

% Author block for anonymous submission:
\author{
  \IEEEauthorblockN{Anonymous Author}
  \IEEEauthorblockA{
    \IEEEauthorrefmark{1}Anonymous Institution\\
    anonymous@institution.edu}
}

% === CAMERA-READY MODE ===
\documentclass[conference]{IEEEtran}
% Restore full author/affiliation information
% Add conference-specific copyright notice
```

### Required Packages

```latex
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amstext}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{balance}
\usepackage{cleveref}
\usepackage{mathrsfs}          % For script fonts (\mathscr)
\usepackage{mathtools}         % Additional math tools
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted |

FOCS enforces a 12-page limit for the main body. References and appendix do not count toward the limit.

## Anonymity Requirements

FOCS uses double-blind review:

1. Remove or replace author names/affiliations in the submission
2. Use "Anonymous" as author during submission
3. Third-person self-citations: "Smith et al. showed..." not "we showed..."
4. Anonymize all URLs, GitHub links, personal pages
5. Clear PDF metadata
6. Remove acknowledgments
7. Do not reference prior versions of the paper by title

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations
2. Add the conference-specific copyright notice provided by IEEE
3. Ensure Xplore-compatible PDF (CMYK colors, embedded fonts)
4. Submit via IEEE PDF eXpress

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

## Formatting Rules

- **Format:** IEEE conference (single-column)
- **Paper size:** US Letter
- **Body font:** 10pt minimum
- **Margins:** 1" all sides
- **Xplore-compatible PDF**: CMYK colors, embedded fonts

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] Author information removed/anonymized
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] Main theorems clearly stated
- [ ] Proofs complete and rigorous
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Restore author information
- [ ] Add IEEE copyright notice
- [ ] Generate Xplore-compatible PDF
- [ ] Use CMYK colors for figures
- [ ] Embed all fonts
- [ ] Submit via IEEE PDF eXpress
