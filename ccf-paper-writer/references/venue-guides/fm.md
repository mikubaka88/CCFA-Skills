# FM Venue Guide

> Migrated from the legacy `ccf-conference-skills/fm/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `fm` |
| Venue family | SE |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/FM/llncs.cls` |
| Official URL | https://formal-methods-26.weebly.com |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# FM Conference Writing Skill

**CCF-A | SE | Publisher: Springer**
**Conference:** https://formal-methods-26.weebly.com
**Template:** `FM/llncs.cls` (Springer LNCS)

## Document Setup

### Preamble Structure

```latex
\documentclass{llncs}

\usepackage{llncsdoc}

\usepackage{makeidx}           % Author-generated index
\usepackage{aliascnt}           % Alias counters for theorem environments

% Additional packages commonly used:
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
| Main paper | **21 pages** (consult CFP) |
| References | No specific limit |

FM typically allows 21 pages for the main paper. Exact limits should be verified from the current Call for Papers as they may vary by year.

## Anonymity Requirements

FM may use single-blind review (author names visible to reviewers). Check the current CFP:

1. If single-blind: Author names may appear in the submission
2. If double-blind: Remove identifying information, use third person for self-citations
3. Anonymize URLs where required
4. Remove PDF metadata that reveals authorship

## Camera-Ready Differences

When preparing camera-ready after acceptance:

1. Ensure all author information is complete and correctly formatted
2. Add acknowledgments if desired
3. Finalize the bibliography
4. Follow Springer's guidelines for final submission

## Section Organization

Standard FM paper structure:

1. **Introduction** — Problem, motivation, contributions
2. **Background/Preliminaries** — Technical foundations
3. **Formal Foundation** — Core formalism, definitions
4. **Technical Development** — Main results, proofs
5. **Case Study/Application** — Practical validation
6. **Related Work** — Positioning against prior art
7. **Conclusion** — Summary and future work
8. References

## Theorem Environments

FM papers heavily rely on formal definitions and proofs:

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

\theoremstyle{note}
\newtheorem*{remark}{Remark}
```

Use `\qed` (from amsthm) to close proofs.

## Formal Semantics

FM papers typically include formal semantics using inference rules:

```latex
\usepackage{mathpartir}

% Typing rules:
\infersection{Type Soundness}
\inferrule{
  \Gamma \vdash e : \tau \\
  e \step e'
}{
  \Gamma \vdash e' : \tau
}
```

## Code Listings

```latex
% Inline code:
The transition system uses \lstinline!State! as the configuration type.

% Code blocks:
\begin{lstlisting}[caption={State transition function}, label={lst:trans}]
type State = (Location, Valuation)

transition :: State -> Action -> State
transition (loc, val) act = case act of
    Assign x e -> (loc, val[x := eval e val])
    Goto l     -> (l, val)
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
  \includegraphics[width=0.9\linewidth]{figs/model}
  \caption{State machine model of the system.}
  \label{fig:model}
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

- [ ] Page count within limits
- [ ] `\documentclass{llncs}`
- [ ] Author info correct (single-blind) or removed (double-blind)
- [ ] No self-identifying URLs if double-blind
- [ ] PDF metadata cleared if required
- [ ] Figures legible in grayscale
- [ ] Compiles with `pdflatex`

## Camera-Ready Checklist

- [ ] Complete author information
- [ ] Finalize acknowledgments
- [ ] Verify bibliography format
- [ ] Check figure quality
