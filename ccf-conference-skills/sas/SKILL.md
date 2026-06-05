---
name: sas
description: Writing and formatting guidance for SAS (International Static Analysis Symposium). Use when drafting, formatting, or submitting to SAS. Covers Springer llncs.cls document class, two-column format, page limits, static analysis conventions, program verification, theorem/proof environments, camera-ready preparation, and Springer LNCS bibliography style.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# SAS Conference Writing Skill

**CCF-B | SE | Publisher: Springer**
**Conference:** https://sas.myqen.com
**Template:** `SAS/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass{llncs}

\usepackage{llncsdoc}

\usepackage{makeidx}           % Author-generated index
\usepackage{aliascnt}           % Alias counters for theorem environments

% Additional packages commonly used in static analysis papers:
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

SAS typically allows 16 pages for the main paper. Exact limits should be verified from the current Call for Papers as they may vary by year.

## Anonymity Requirements

SAS uses single-blind review (author names visible to reviewers):

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

Standard SAS paper structure:

1. **Introduction** — Problem, motivation, contributions
2. **Background/Preliminaries** — Static analysis foundations
3. **Analysis/Approach** — Core analysis technique
4. **Technical Development** — Algorithm, soundness proofs
5. **Implementation** — Tool details, optimizations
6. **Experimental Evaluation** — Benchmarks, results
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future work
9. References

## Theorem Environments

SAS papers rely heavily on formal definitions and proofs:

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

## Inference Rules

SAS papers frequently use inference rules:

```latex
\usepackage{mathpartir}

% Semantics rule:
\infersection{Assignment}
\inferrule{
  \langle e, \sigma \rangle \Downarrow v
}{
  \langle x := e, \sigma \rangle \Rightarrow \sigma[x \mapsto v]
}

% Type system rule:
\infersection{Variable}
\inferrule{
  \Gamma(x) = \tau
}{
  \Gamma \vdash x : \tau
}
```

## Code Listings

```latex
% Inline code:
The fixpoint solver uses \lstinline!widening! to ensure termination.

% Code blocks:
\begin{lstlisting}[language=Python, caption={Worklist algorithm for static analysis}, label={lst:worklist}]
def analyze(cfg):
    worklist = Queue()
    for node in cfg.nodes:
        worklist.put(node)

    while not worklist.empty():
        node = worklist.get()
        old_state = node.state
        new_state = transfer(node, old_state)
        node.state = old_state ⊔ new_state  # Join
        if node.state != old_state:
            for succ in cfg.succ(node):
                worklist.put(succ)
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
  \includegraphics[width=0.9\linewidth]{figs/analysis-flow}
  \caption{Control flow graph and analysis data flow.}
  \label{fig:cfg}
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
