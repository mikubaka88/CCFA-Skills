---
name: ppopp
description: Writing and formatting guidance for PPoPP (ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming) papers. Use when drafting, formatting, or submitting to PPoPP 2026. Covers ACM acmart sigplan format with anonymous review mode, parallel programming-specific writing conventions (algorithm correctness, complexity analysis, experimental methodology), page limits, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# PPoPP 2026 Conference Writing Skill

**CCF-A | Architecture | Publisher: ACM**
**Conference:** https://ppopp26.sigplan.org/
**Template:** `PPoPP/acmart.cls` (ACM acmart, SIGPLAN format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigplan,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigplan]{acmart}
\acmConference[PPoPP 2026]{31st ACM SIGPLAN Symposium on Principles...}
               {February 22--26, 2026}{Montreal, Canada}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
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
\usepackage{newalg}             % Alternative algorithm formatting
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Not permitted |

PPoPP enforces a strict 12-page limit. There is **no appendix** and no supplementary materials in the traditional sense. All essential content must fit within the 12-page limit.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names anywhere in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs and external links
4. Clear PDF metadata
5. Do not include acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

PPoPP papers typically follow one of two patterns depending on whether the contribution is primarily theoretical or experimental:

### Theory-First Paper Structure

1. **Introduction** — Problem, contributions (state all theorems/lemmas as contributions)
2. **Background & Preliminaries** — Formal definitions, notation, related formalisms
3. **Algorithm / Program Transformation** — Full formal description with pseudocode
4. **Correctness Proof** — Theorems, lemmas, proofs establishing correctness
5. **Complexity Analysis** — Time/space bounds, work/span (or depth) analysis
6. **Related Work** — Comparison with prior algorithms and proofs
7. **Conclusion** — Summary and open problems
8. References

### Experimental Paper Structure

1. **Introduction** — Problem, contributions (enumerate algorithmic/performance contributions)
2. **Background & Motivation** — Why parallelization matters, challenges
3. **Algorithm Design** — Practical parallel algorithm with sufficient detail
4. **Implementation** — System-level details, optimizations, porting effort
5. **Evaluation** — Benchmarks, experimental setup, performance results
6. **Related Work** — Comparison with related parallel frameworks
7. **Conclusion**
8. References

## Algorithm Environments

PPoPP papers heavily use algorithm formatting. Use the `algorithm` + `algorithmic` packages:

```latex
\begin{algorithm}[t]
  \caption{Work-stealing task scheduler}
  \label{alg:steal}
  \begin{algorithmic}[1]
    \REQUIRE $n$ workers, task graph $G$
    \ENSURE All tasks completed

    \STATE $w \leftarrow \Call{GetWorkerID}{}$
    \WHILE{$\neg$\Call{AllDone}{$G$}}
      \STATE $t \leftarrow \Call{Steal}{w}$  \COMMENT{Take from random victim}
      \IF{$t \neq \text{null}$}
        \STATE $\Call{Execute}{t}$
      \ENDIF
    \ENDWHILE
  \RETURN
  \end{algorithmic}
\end{algorithm}
```

For termination, use `\WHILE`, `\FOR`, `\IF` with `\ELSIF`/`\ELSE`.

## Correctness and Complexity

PPoPP values rigorous correctness arguments. Present them formally:

```latex
\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}

\begin{theorem}[Work-stealing correctness]
  \label{th:steal}
  All tasks in $G$ are executed, and no task is executed twice.
\end{theorem}

\begin{Proof}
  % formal proof ...
\end{Proof}
```

For parallel complexity, analyze in terms of:
- **Work**: total operations across all processors
- **Span (Depth)**: longest chain of dependencies
- **Speedup**: $T_1 / T_p$ for $p$ processors

```latex
\begin{restatable}{theorem}{spanbound}
  \label{th:span}
  The algorithm has span $O(\log n)$ with high probability.
\end{restatable}
```

## Figures and Tables

- Use vector formats (.pdf) for all plots and diagrams
- Ensure grayscale legibility
- Number figures/tables sequentially
- Captions should state what to observe and why it matters

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/scaling}
  \caption{Strong scaling on 16-core machine. Our algorithm achieves
    near-linear speedup up to 8 cores, outperforming the
    state-of-the-art by $2.1\times$ at 16 cores.}
  \label{fig:scaling}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{bandis2024}      % Bandis et al. (2024)
\citep{bandis2024}      % (Bandis et al. 2024)
```

All references must list **all authors** by full name.

## Formatting Rules

- **Format:** ACM sigplan (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## PPoPP Writing Conventions

- **Algorithmic detail**: Present sufficient pseudocode for reproducibility; the algorithm should be implementable from the description
- **Correctness arguments**: Prove correctness, not just claim it; include lemmas that break down the argument
- **Complexity analysis**: Always provide work and span/depth bounds; compare with known bounds from related work
- **Experimental methodology**: Use established benchmarks where available; report variance across runs; state hardware platform and OS
- **No supplementary appendix**: all essential content must fit within 12 pages

## Submission Checklist

- [ ] 12 pages or fewer (strict — no appendix)
- [ ] `\documentclass[sigplan,review,anonymous]`
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Algorithm pseudocode is complete and self-contained
- [ ] All theorems/lemmas have proofs
- [ ] Work/span analysis provided
- [ ] References list all authors

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
