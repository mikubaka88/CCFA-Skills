# ICASSP Venue Guide

> Migrated from the legacy `ccf-conference-skills/icassp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icassp` |
| Venue family | Signal Processing |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/ICASSP/IEEEtran.cls` |
| Official URL | https://2026.ieeeicassp.org/ |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# ICASSP 2026 Conference Writing Skill

**CCF-B | Signal Processing | Publisher: IEEE**
**Conference:** https://2026.ieeeicassp.org/
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

## Abstract

Describe the problem, method and key results in a concise paragraph. Use the abstract environment and length required by the verified target template.

## Section Organization

Standard ICASSP paper structure:
1. Abstract
2. Introduction — Problem, motivation, contributions
3. Background / Prior Work
4. Proposed Method / System
5. Experiments / Evaluation
6. Conclusion
7. References

## Figures and Tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figure}
  \caption{Figure caption here (lowercase, period at end).}
  \label{fig:label}
\end{figure}
```

- Use vector formats (.pdf) where possible
- Caption **below** figures, **above** tables
- Number figures and tables sequentially
- Ensure figures are legible in grayscale

## References (IEEEtran)

IEEE numbered citation style:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Inline citations:
\cite{key1, key2}      % [1], [2]
```
