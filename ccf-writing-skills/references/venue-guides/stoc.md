# STOC Venue Guide

> Migrated from the legacy `ccf-conference-skills/stoc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `stoc` |
| Venue family | Theory |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/STOC/acmart.cls` |
| Official URL | https://www.acm.org/stoc2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# STOC 2026 Conference Writing Skill

**CCF-A | Theory | Publisher: ACM**
**Conference:** https://www.acm.org/stoc2026
**Template:** `STOC/acmart.cls` (ACM acmart, sigplan format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\acmConference[STOC 2026]{STOC '26: 2026 ACM Symposium on Theory of Computing}
               {June 14--18, 2026}{Chicago, IL, USA}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amstext}           % For theorem text formatting
\usepackage{graphicx}
\usepackage{balance}
\usepackage{cleveref}
\usepackage{mathrsfs}          % For script/math fonts (e.g., \mathscr)
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted |

STOC enforces a 12-page limit for the main body. References do not count toward the limit. Appendix is permitted but reviewers are not required to read it.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, personal pages, GitHub links
4. Clear PDF metadata
5. Remove acknowledgments
6. Do not include a "Note Added" or "Previous Version" reference to prior work

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore all author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

STOC papers focus heavily on proofs and formal analysis:

1. **Abstract** — Theorem statements, brief proof idea
2. **Introduction** — Problem, previous results, our contribution (enumerate theorems)
3. **Technical Overview** — Proof ideas without full details (helps reviewers)
4. **Preliminaries** — Definitions, notation, known results
5. **Main Technical Sections** — Proofs organized by theorem
6. **Applications / Extensions** — Optional concrete applications
7. **References**
8. Appendix (optional: omitted proofs, additional experiments)

## Theorem Environments

STOC uses rigorous theorem environments from amsthm:

```latex
\theoremstyle{plain}
\newtheorem{main}{Theorem}  % Main results numbered prominently
\newtheorem*{main*}{Main Theorem}  % Unnumbered for emphasis

\theoremstyle{plain}
\newtheorem{definition}[main]{Definition}
\newtheorem{claim}[main]{Claim}
\newtheorem{fact}[main]{Fact}
\newtheorem{observation}[main]{Observation}
\newtheorem{property}[main]{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}

% Proof environment from amsthm:
\begin{main}
  \label[main]{thm:gap-detection}
  There is no algorithm that, given a graph $G$ and parameters
  $\epsilon > 0$ and $k \in \mathbb{N}$, decides whether $G$ has
  a vertex cover of size at most $k$ or whether every vertex cover
  has size at least $(1+\epsilon)k$, in time $n^{o(k)}$.
\end{main}

\begin{Proof}
  We prove by reduction from the $k$-Clique problem.
  Given an instance $(H, k)$ of $k$-Clique, we construct a graph $G$
  such that... [full proof]
\end{Proof}
```

## Proof Structure

STOC proofs should be structured and readable:

```latex
\section{Gap-Hardness for Vertex Cover}
\label{sec:gap-hardness}

\begin{main*}[Gap-Hardness for Vertex Cover]
  There is no algorithm that distinguishes between:
  \begin{itemize}
    \item $\mathbf{YES}$: $G$ has a vertex cover of size at most $k$
    \item $\mathbf{NO}$: Every vertex cover has size at least $(1+\epsilon)k$
  \end{itemize}
  with success probability $2/3$ in time $n^{o(k)}$.
\end{main*}

\begin{Proof}[Proof Sketch]
  We reduce from the $k$-Clique problem. Given $(H, k)$:
  \begin{enumerate}
    \item Construct a graph $G$ whose vertex cover problem encodes
      whether $H$ contains a $k$-clique.
    \item Show that if $H$ has a $k$-clique, then $G$ has a vertex
      cover of size $n - \binom{k}{2}$.
    \item Show that if $H$ has no $k$-clique, then every vertex cover
      of $G$ has size at least $n - \binom{k}{2} + \epsilon n$.
    \item Use the PCP theorem to amplify the gap.
  \end{enumerate}
  The reduction runs in time $n^{O(1)}$ and preserves the gap.
  Full details appear in \autoref{app:reduction}.
\end{Proof}
```

## Proof by Reduction Template

Many STOC papers use reduction-based proofs:

```latex
% Standard reduction proof structure:
\section{Upper Bound}

\begin{main}
  \label[main]{thm:upper-bound}
  There exists an algorithm $\mathcal{A}$ that solves problem $P$
  in time $T(n)$ with error probability at most $\epsilon$.
\end{main}

\begin{Proof}
  \textbf{Algorithm $\mathcal{A}$.} The algorithm proceeds as follows:
  \begin{enumerate}
    \item [Step 1:] Sample a random set $S \subseteq [n]$ of size
      $|S| = O(\frac{1}{\epsilon^2} \log \frac{1}{\delta})$.
    \item [Step 2:] For each $i \in S$, compute $f(x_i)$.
    \item [Step 3:] Return the majority vote of $\{f(x_i) : i \in S\}$.
  \end{enumerate}

  \textbf{Analysis.} We show that with probability at least $1-\delta$,
  the majority vote equals the true answer. [Full analysis...]
\end{Proof}
```

## Figures and Tables

STOC papers use minimal figures but can include diagrams for reductions:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.8\linewidth]{figs/reduction}
  \caption{Reduction from $k$-Clique to Gap-VC.
    Vertices in the constructed graph correspond to
    (a) vertices of $H$, (b) edges of $H$, and (c) auxiliary
    gadgets enforcing the clique structure.
    Edge groups are color-coded by type.}
  \label{fig:reduction}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{arora2009computational}  % Arora and Barak (2009)
\citep{arora2009computational}   % (Arora and Barak 2009)
```

## Formatting Rules

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum, Times New Roman
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in
- **Theorems:** Clearly labeled and prominently numbered

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[sigplan, review, anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Main theorems clearly stated in Introduction
- [ ] Proofs complete and rigorous
- [ ] References list all authors

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
