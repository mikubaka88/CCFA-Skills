---
name: conext
description: Writing and formatting guidance for CoNEXT (International Conference on emerging Networking EXperiments and Technologies) papers. Use when drafting, formatting, or submitting to CoNEXT 2026. Covers ACM acmart sigconf format with anonymous review mode, networking experiments paper conventions (measurement studies, protocol evaluation, network trace analysis), 12-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CoNEXT 2026 Conference Writing Skill

**CCF-B | Networks | Publisher: ACM**
**Conference:** https://conext2026.sigcomm.org
**Template:** `CoNEXT/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[CoNEXT 2026]{CoNEXT '26: Conference on emerging...}
               {December 7--10, 2026}{Vienna, Austria}
\acmISBN{978-X-XXXX-XXXX-X/XX/XX}
\acmDOI{10.5555/XXXXXXX.XXXXXXX}
```

### Required Packages

```latex
\usepackage[round]{natbib}     % Author-year citations
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{listings}
\lstset{basicstyle=\small\ttfamily}
\usepackage{booktabs}
\usepackage{graphicx}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **12 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

CoNEXT enforces a 12-page limit for the main body. References and appendix do not count.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names anywhere in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub, institutional pages)
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

CoNEXT papers follow the networking experiments structure:

1. **Introduction** — Problem, motivation, contributions (enumerate contributions)
2. **Background & Motivation** — Why the problem matters, existing approaches
3. **Methodology / Design** — Experimental setup, measurement methodology, or system design
4. **Implementation / Data Collection** — System details, trace collection process
5. **Evaluation / Results** — Data analysis, findings, comparison
6. **Discussion** — Implications, limitations, open questions
7. **Related Work** — Positioning against prior art
8. **Conclusion** — Summary and future directions
9. References
10. Appendix (optional)

## Networking Experiments Conventions

CoNEXT focuses on experimental networking research:

### Measurement Methodology

```latex
\section{Methodology}

We collect network measurements from:
\begin{itemize}
  \item \textbf{Platform}: RIPE Atlas probes (10,000+ globally distributed)
  \item \textbf{Duration}: 6 months of continuous measurement
  \item \textbf{Data volume}: 50 GB of raw traceroute and DNS data
\end{itemize}

\subsection{Data Collection}
We measure DNS resolution performance by:
\begin{itemize}
  \item Resolving top 1M domains from Alexa from each probe
  \item Recording resolution time, anycast routing, and CDN selection
  \item Correlating with geolocation and network topology data
\end{itemize}
```

### Protocol Evaluation

```latex
\section{Experimental Evaluation}

We evaluate our proposed QUIC extension through:
\begin{itemize}
  \item \textbf{Testbed}: 20-node testbed with commodity hardware
  \item \textbf{Network conditions}: Emulated using mahimahi
    (variable RTT, loss rate, bandwidth)
  \item \textbf{Baselines}: QUIC (RFC 9000), TCP Cubic, TCP BBR
\end{itemize}

\subsection{Results}
\begin{itemize}
  \item \textbf{Throughput}: 35\% improvement over QUIC in
    high-loss environments
  \item \textbf{Latency}: 20ms reduction in 99th percentile latency
  \item \textbf{Fairness}: Jain's fairness index of 0.94
\end{itemize}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Include network topology and measurement setup diagrams
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/measurement-setup}
  \caption{Measurement infrastructure: (a) RIPE Atlas probe
    distribution (10,234 probes worldwide), (b) measurement
    collection pipeline using Apache Spark. Our methodology
    achieves sub-second temporal resolution and sub-km
    spatial resolution.}
  \label{fig:setup}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{doe2025}      % Doe et al. (2025)
\citep{doe2025}     % (Doe et al. 2025)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 12 pages or fewer (main body)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author identification removed
- [ ] No self-referential citations in first person
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References list all authors
- [ ] Figures legible in grayscale

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
