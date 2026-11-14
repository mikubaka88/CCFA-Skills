# IMC Venue Guide

> Migrated from the legacy `ccf-conference-skills/imc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `imc` |
| Venue family | Networks |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/IMC/usenix-2020-09.sty` |
| Official URL | https://www.imc2026.org |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# IMC 2026 Conference Writing Skill

**CCF-B | Networks | Publisher: ACM/USENIX**
**Conference:** https://www.imc2026.org
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

## Section Organization

IMC papers follow the measurement study structure:

1. **Introduction** — Measurement question, motivation, contributions (enumerate findings)
2. **Background & Methodology** — Measurement context, data collection approach
3. **Data Collection** — Measurement infrastructure, dataset description
4. **Analysis / Findings** — Key measurement results
5. **Discussion** — Implications, limitations, open questions
6. **Related Work** — Prior measurement studies
7. **Conclusion** — Summary and future directions
8. References
9. Appendix (optional)

## Measurement Study Conventions

IMC is a premier venue for Internet measurement research:

### Measurement Methodology

```latex
\section{Measurement Methodology}

We measure DNS resolver behavior using a distributed
measurement infrastructure:
\begin{itemize}
  \item \textbf{Platform}: 500 vantage points across
    80 countries
  \item \textbf{Duration}: 3 months of continuous measurement
  \item \textbf{Method}: Active probing of top 10,000 domains
  \item \textbf{Ethics}: Approved by our IRB, no user data collected
\end{itemize}

\subsection{Measurement Traces}
We collect:
\begin{itemize}
  \item DNS query-response pairs (anonymized)
  \item RTT measurements from each vantage point
  \item Resolver IP addresses (city-level geolocation only)
\end{itemize}
```

### Data Analysis

```latex
\section{Measurement Results}

\subsection{Key Finding 1: CDN Concentration}
We find that 65\% of DNS resolution goes through just
5 resolver operators:
\begin{itemize}
  \item Google (32.1\%)
  \item Cloudflare (18.4\%)
  \item Quad9 (7.8\%)
  \item OpenDNS (4.3\%)
  \item CleanBrowsing (2.8\%)
\end{itemize}
This concentration has implications for DNS security
and privacy.
```

## Figures and Tables

- Ensure grayscale legibility
- Include measurement topology and data distribution plots
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/vantage-points}
  \caption{Geographic distribution of our 500 measurement
    vantage points. Points are sized by measurement volume.
    We achieve coverage in 80 countries with at least
    3 vantage points per country for robustness.}
  \label{fig:vantage}
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
