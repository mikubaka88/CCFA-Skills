# ICDE Venue Guide

> Migrated from the legacy `ccf-conference-skills/icde/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `icde` |
| Venue family | DB |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/ICDE/IEEEtran.cls` |
| Official URL | https://icde2026.github.io |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# ICDE 2026 Conference Writing Skill

**CCF-A | DB | Publisher: IEEE**
**Conference:** https://icde2026.github.io
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

## Section Organization

ICDE papers typically follow a data engineering paper structure:

1. **Abstract** — Concise summary
2. **Introduction** — Problem, motivation, contributions (enumerate explicitly)
3. **Background & Preliminaries** — System model, definitions
4. **Problem Definition** — Formal problem statement
5. **Proposed Approach** — Core technical contribution
6. **Implementation** — System details, complexity
7. **Experimental Evaluation** — Benchmarks, comparisons, analysis
8. **Related Work**
9. **Conclusion**
10. References
11. Appendix (optional)

## Theorem Environments

ICDE papers often include formal reasoning:

```latex
\theoremstyle{plain}
\newtheorem{definition}{Definition}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem{property}{Property}
```

## Figures and Tables

- Grayscale legibility required
- Number sequentially
- Use `booktabs` for tables (no vertical rules)
- IEEE convention: figures at top, tables at bottom

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system}
  \caption{System architecture of the proposed data integration
    framework showing the query processor, optimizer, and
    data sources components.}
  \label{fig:system}
\end{figure}

\begin{table}[t]
  \caption{Experimental results on TPC-H benchmark.}
  \label{tab:results}
  \begin{tabular}{cccc}
    \toprule
    Query & Baseline (s) & Ours (s) & Speedup \\
    \midrule
    Q1 & 12.3 & 4.1 & 3.0x \\
    Q2 & 8.7 & 2.9 & 3.0x \\
    Q3 & 15.2 & 5.8 & 2.6x \\
    \bottomrule
  \end{tabular}
\end{table}
```

## References

IEEE uses the `cite` package and numeric citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Citations are numeric:
\cite{garcia2008db}
% Or: \citep{} from natbib if loaded
```

## Content Checklist

- [ ] Grayscale-legible figures
