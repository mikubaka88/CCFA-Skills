# CHES Venue Guide

> Migrated from the legacy `ccf-conference-skills/ches/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ches` |
| Venue family | Security |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/CHES/llncs.cls` |
| Official URL | https://ches.iacr.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CHES 2026 Conference Writing Skill

**CCF-B | Security | Publisher: Springer**
**Conference:** https://ches.iacr.org/2026
**Template:** `CHES/llncs.cls` (Springer LNCS format)

## Document Setup

### Preamble Structure

```latex
\documentclass[runningheads]{llncs}

% Required packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{url}
\usepackage{hyperref}
```

### Required Packages

```latex
\documentclass[runningheads]{llncs}
\usepackage{graphicx}           % Figures
\usepackage{amsmath}            % Math
\usepackage{amssymb}            % Symbols
\usepackage{url}                % URLs in references
\usepackage{hyperref}           % Clickable links
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper | **30 pages** (LNCS standard) |
| References | Included in page count |
| Appendix | Typically included |

CHES follows LNCS guidelines with approximately 30 pages (including references). Check the specific Call for Papers for the current year's limit.

## Anonymity Requirements

CHES uses double-blind review:

1. No author names or affiliations in submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (e.g., GitHub repos, ePrint links)
4. Clear PDF metadata
5. Remove acknowledgments from submission

## Camera-Ready Differences

After acceptance:

1. Add complete author information with affiliations
2. Include acknowledgments
3. Add footnote for contact author
4. Ensure PDF/A compliance for Springer publication

## Section Organization

CHES papers follow the hardware security structure:

1. **Introduction** — Problem, contributions (enumerate contributions)
2. **Background & Threat Model** — Side-channel leakage model, adversary capabilities
3. **Related Work** — Prior countermeasures and analysis techniques
4. **Proposed Design / Analysis** — Core contribution (countermeasure or attack)
5. **Implementation / Experimental Results** — Measurement setup, evaluation
6. **Security Analysis** — Formal analysis, leakage bounds
7. **Conclusion** — Summary
8. References

## CHES-Specific Conventions

### Side-Channel Leakage Model

```latex
\section{Threat Model}

We consider a side-channel adversary who can:
\begin{itemize}
  \item Measure power consumption during cryptographic operations
  \item Mount template attacks with $N$ profiling traces
  \item Recover the first $k$ bits of the secret key with
    probability $p$
\end{itemize}

We assume the $t$-threshold probing model where the adversary
can inspect at most $t$ intermediate values simultaneously.
Our countermeasure achieves $t$-probing security.
```

### Hardware Implementation

```latex
\section{Hardware Implementation}

We implement our protected AES engine in 65nm CMOS:
\begin{itemize}
  \item \textbf{Technology}: TSMC 65nm standard cell library
  \item \textbf{Area}: 0.85 mm$^2$ (including RNG and control)
  \item \textbf{Clock frequency}: 100 MHz
  \item \textbf{Power consumption}: 45 mW @ 100 MHz
  \item \textbf{Throughput}: 1.28 Gbps (AES-128)
\end{itemize}

\subsection{Leakage Assessment}
We perform leakage assessment using:
\begin{itemize}
  \item \textbf{Test Vector Leakage Assessment (TVLA)}:
    $|t| = 3.2 < 4.5$ (passes the threshold)
  \item \textbf Welch's $t$-test}: No fixed vs. random
    data-dependent leakage detected
\end{itemize}
```

### Attack Evaluation

```latex
\section{Experimental Results}

We evaluate our attack on an ARM Cortex-M4 implementation:
\begin{itemize}
  \item \textbf{Target}: AES-128 in counter mode
  \item \textbf{Measurement}: ChipWhisperer Lite with 500MS/s
  \item \textbf{Traces}: 10,000 power traces
  \item \textbf{Key recovery}: Full 128-bit key in 2.3 seconds
\end{itemize}

Against our countermeasures:
\begin{itemize}
  \item \textbf{Without masking}: Key recovered with 5,000 traces
  \item \textbf{With 1st-order masking}: 50,000 traces insufficient
  \item \textbf{With 2nd-order masking}: No key recovery with
    100,000 traces
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Include oscilloscope traces, chip layouts, and measurement setups

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/power-trace}
  \caption{Power consumption trace during AES S-box lookup:
    (a) unprotected implementation showing clear data-dependent
    leakage, (b) our masked implementation with uniform power
    consumption. The $y$-axis shows current in mA, $x$-axis
    shows time in $\mu$s.}
  \label{fig:power-trace}
\end{figure}
```

## References (Springer LNCS)

```latex
\bibliographystyle{splncs04}
\bibliography{references}

% Citations:
\cite{doe2025}          % [1]
```

## Formatting Rules

- **Format:** Springer LNCS (single-column, typeset)
- **Paper size:** A4
- **Body font:** 10pt typical
- **Margins:** Per LNCS guidelines
- **References:** Numbered, square brackets

## Submission Checklist

- [ ] Page count within LNCS guidelines
- [ ] All author identification removed
- [ ] Third-person self-citations only
- [ ] Threat model clearly defined
- [ ] Implementation details included
- [ ] Experimental methodology described
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared

## Camera-Ready Checklist

- [ ] Add author information and affiliations
- [ ] Add acknowledgments
- [ ] Verify PDF/A compliance
- [ ] Check figure quality
