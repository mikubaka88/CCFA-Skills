---
name: vmcai
description: Writing and formatting guidance for VMCAI (International Conference on Verification, Model Checking, and Abstract Interpretation). Use when drafting, formatting, or submitting to VMCAI. Covers Springer llncs.cls document class, two-column format, page limits, program analysis and verification conventions, theorem/proof environments, camera-ready preparation, and Springer LNCS bibliography style.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# VMCAI Conference Writing Skill

**CCF-B | SE | Publisher: Springer**
**Conference:** https://vmcai.sigplan.org
**Template:** `VMCAI/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass{llncs}

\usepackage{llncsdoc}

\usepackage{makeidx}           % Author-generated index
\usepackage{aliascnt}           % Alias counters for theorem environments

% Additional packages commonly used in program analysis papers:
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{mathpartir}         % For inference rules
\usepackage{listings}
\usepackage{graphicx}
```

### Springer LNCS Document Class

The `llncs.cls` is based on `article.cls` with Springer-specific formatting. Key options:

- `envcountreset` — Reset theorem counters per section
- `citeauthoryear` — Enable author-year citations
- `runningheads` — Enable running heads

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper | **16 pages** (consult CFP) |
| References | No specific limit |

VMCAI typically allows 16 pages for the main paper. Exact limits should be verified from the current Call for Papers as they may vary by year.

## Anonymity Requirements

VMCAI uses single-blind review (author names visible to reviewers):

1. Author names may appear in the submission
2. Anonymize URLs where appropriate
3. Remove PDF metadata that reveals institutional affiliations if required
4. No explicit anonymization of self-citations required (check CFP)

## Camera-Ready Differences

When preparing camera-ready after acceptance:

1. Ensure all author information is complete and correctly formatted
2. Add acknowledgments if desired
3. Follow Springer's guidelines for final submission
4. Finalize the bibliography

## Section Organization

Standard VMCAI paper structure:

1. **Introduction** — Problem, motivation, contributions
2. **Background/Preliminaries** — Static analysis foundations
3. **Abstract Interpretation** — Abstract domain, transfer functions
4. **Technical Development** — Algorithm, soundness proofs
5. **Implementation** — Tool details, optimizations
6. **Experimental Evaluation** — Benchmarks, results
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## Theorem Environments

VMCAI papers rely heavily on formal definitions and proofs:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem{example}{Example}
\newtheorem{property}{Property}

\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{proposition}{Proposition}
\newtheorem*{corollary}{Corollary}

\theoremstyle{plain}
\newtheorem*{invariant}{Invariant}
\newtheorem*{soundness}{Soundness}

\theoremstyle{note}
\newtheorem*{remark}{Remark}
```

Use `\qed` (from amsthm) to close proofs.

## Abstract Interpretation

VMCAI papers typically involve abstract interpretation:

```latex
% Galois connection:
\[
  \alpha \dashv \gamma : C \overleftrightarrow{\quad} A
\]

% Abstract transfer function:
\[
  \唐代{PC}{f}(\法语{a}) = \bigvee \{ \alpha(f(\gamma(\代理{a}))) \mid \代理{a} \in \gamma(\法语{a}) \}
\]
```

## Code Listings

```latex
% Inline code:
The widening operator \lstinline!\nabla! accelerates fixpoint computation.

% Code blocks:
\begin{lstlisting}[language=C, caption={Transfer function for assignment}, label={lst:assign}]
AbsState assign(AbsState s, Var x, Expr e) {
    // Evaluate e over abstract state s
    AbsVal v = eval(e, s);
    // Update abstract state: x maps to v
    return update(s, x, v);
}
\end{lstlisting}
```

## Figures and Tables

- Use vector formats (.pdf) where possible
- Ensure figures are legible in grayscale
- Number figures and tables sequentially
- Captions should be descriptive and self-contained

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.9\linewidth]{figs/lattice}
  \caption{Abstract domain lattice structure.}
  \label{fig:lattice}
\end{figure}
```

## References (Springer LNCS)

Springer LNCS uses a numbered bibliography style:

```latex
\bibliographystyle{splncs04}
\bibliography{references}

% Citations:
\cite{smith2023}        % [1]
\citep{smith2023}       % [1] (natbib)
```

## Formatting Rules

- **Format:** Springer LNCS (two-column, single-spaced)
- **Paper size:** A4
- **Margins:** Template defaults
- **Body font:** 9pt or 10pt (template default)
- **References:** Small font, numbered, no page limits

## Submission Checklist

- [ ] Page count within limits (16 pages typical)
- [ ] `\documentclass{llncs}`
- [ ] Author info correct
- [ ] PDF metadata appropriate
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Complete author information
- [ ] Finalize acknowledgments
- [ ] Verify bibliography format
- [ ] Check figure quality
