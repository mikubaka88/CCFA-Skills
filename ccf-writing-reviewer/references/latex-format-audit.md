# LaTeX And Format Audit

Use this file when the user provides `.tex`, LaTeX snippets, Overleaf-exported source, ACM/IEEE/CVF/ACL/AAAI/NeurIPS/ICLR style constraints, or asks for format/排版/LaTeX checks.

## Source Inspection

When local files are available, inspect them with fast text search before commenting:

- section structure: `\title`, `\begin{abstract}`, `\section`, `\subsection`, `\paragraph`, `\appendix`;
- references and citations: `\cite`, `\ref`, `\label`, `\bibliography`, `\bibliographystyle`, `\printbibliography`;
- figures and tables: `\begin{figure}`, `\begin{table}`, captions, subfigures, `\resizebox`, `\vspace`, `\hspace`;
- equations and algorithms: `equation`, `align`, `algorithm`, notation definitions, punctuation around displayed math;
- packages and macros: `\usepackage`, `\newcommand`, `\def`, duplicated packages, style-breaking overrides;
- TODOs and placeholders: `TODO`, `??`, `TBD`, `xxx`, `\cite{}`, `\ref{}`.

If compilation is feasible and the user wants format validation, run the local build command or infer from the repo's README/Makefile. Report failures without hiding them.

## Audit Checklist

Check:

1. Venue template: correct class/style, anonymization/camera-ready mode, font size, margins, page limit, appendix handling, and supplemental-material rules.
2. Title/abstract: no undefined acronyms, no overclaiming beyond evidence, no result numbers inconsistent with experiment section.
3. Section order: motivation before method details; method before results; limitations before broad conclusion when needed.
4. Labels/refs: no duplicate labels, undefined refs, orphan labels, wrong figure/table/equation references, or stale section names.
5. Citations: no missing citation keys, no citation-only paragraphs, no overloaded citation lists without comparison text.
6. Equations: notation defined before use, symbols consistent, punctuation correct, equations referenced when central.
7. Figures/tables: captions are self-contained, axes/metrics/datasets named, tables fit without unreadable scaling, and text explains the key takeaway.
8. Algorithms: inputs/outputs defined, variables match method text, steps are not implementation trivia.
9. Typography: avoid excessive bold/italics, manual spacing hacks, overfull-risk long URLs, and inconsistent capitalization.
10. Bibliography: style matches venue, entries are complete enough, and important related work is not hidden in footnotes.

## Required Output

```text
Format verdict:
Blocking compliance issues:
LaTeX/source issues:
Figure/table/caption issues:
Citation/reference issues:
Notation/equation issues:
Suggested checks or build command:
```

Do not fabricate compiler errors. If the source was not compiled, state `not compiled`.
