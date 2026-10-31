# FAST Venue Guide

> Migrated from the legacy `ccf-conference-skills/fast/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `fast` |
| Venue family | Systems |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/FAST/usenix-2020-09.sty` |
| Official URL | https://www.usenix.org/conference/fast26 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# FAST 2026 Conference Writing Skill

**CCF-A | Systems | Publisher: USENIX**
**Conference:** https://www.usenix.org/conference/fast26
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

## Section Organization

FAST papers follow the systems paper structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, prior approaches and their limits
3. **Design/Approach** — Core technical contribution with rationale
4. **Implementation** — System details, complexity, challenges solved
5. **Evaluation** — Rigorous experimental methodology, baselines, sensitivity analysis
6. **Related Work** — Thorough positioning against prior art
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Storage Systems Conventions

FAST papers typically cover:
- File systems and storage architectures
- Storage performance and reliability
- Distributed storage systems
- Storage security and privacy
- New storage technologies (NVMe, persistent memory, etc.)

### Performance Evaluation

```latex
\section{Evaluation}
We evaluate our file system using:
\begin{itemize}
  \item \textbf{Benchmarks}: fio, IOzone, Filebench
  \item \textbf{Workloads}: synthetic and real-world traces
  \item \textbf{Metrics}: throughput (ops/sec), latency (usec), bandwidth (MB/s)
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all diagrams
- Ensure grayscale legibility — reviewers often print in B&W
- Self-contained captions: describe what to observe and why it matters
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/design-arch}
  \caption{Architecture overview: (a) metadata server layout,
    (b) data plane organization. Our design reduces metadata
    lookup latency by 3x compared to the baseline.}
  \label{fig:arch}
\end{figure}
```

## References

```latex
\bibliographystyle{plain}
\bibliography{references}

% Citations:
~\cite{smith2023}        % [1]
```

Use `plain` bibstyle with numerical citations.

## Content Checklist

- [ ] References properly formatted
- [ ] Figures legible in grayscale
