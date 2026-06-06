# RAID Venue Guide

> Migrated from the legacy `ccf-conference-skills/raid/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `raid` |
| Venue family | Security |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/RAID/llncs.cls` |
| Official URL | https://raid2026.cs.ucalgary.ca |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# RAID 2026 Conference Writing Skill

**CCF-B | Security | Publisher: Springer**
**Conference:** https://raid2026.cs.ucalgary.ca
**Template:** `RAID/llncs.cls` (Springer LNCS format)

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

RAID follows LNCS guidelines with approximately 30 pages (including references). Check the specific Call for Papers for the current year's limit.

## Anonymity Requirements

RAID uses double-blind review:

1. No author names or affiliations in submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (e.g., GitHub repos, dataset pages)
4. Clear PDF metadata
5. Remove acknowledgments from submission

## Camera-Ready Differences

After acceptance:

1. Add complete author information with affiliations
2. Include acknowledgments
3. Add footnote for contact author
4. Ensure PDF/A compliance for Springer publication

## Section Organization

RAID papers follow the security research structure:

1. **Introduction** — Attack/defense problem, contributions (enumerate contributions)
2. **Background & Threat Model** — System model, adversary capabilities
3. **Related Work** — Prior detection/prevention approaches
4. **Proposed Approach** — Core contribution (detection method or attack)
5. **Implementation / Experimental Results** — Evaluation setup, datasets, results
6. **Discussion** — Limitations, ethical considerations
7. **Conclusion** — Summary
8. References

## Security Research Conventions

### Threat Model

```latex
\section{Threat Model}

We consider an attacker who:
\begin{itemize}
  \item Can deploy malicious code on enterprise endpoints
  \item Attempts to persist on the system for long-term access
  \item Uses living-off-the-land techniques to evade detection
  \item Can compromise up to 5\% of endpoints in the network
\end{itemize}

We assume the defender has:
\begin{itemize}
  \item Endpoint detection agents on all corporate machines
  \item Centralized logging infrastructure
  \item No prior knowledge of the attack campaign
\end{itemize}
```

### Attack Analysis

```latex
\section{Attack Analysis}

\subsection{Ransomware Behavioral Model}
We analyze the typical ransomware attack sequence:
\begin{enumerate}
  \item \textbf{Initial access}: Phishing email or exploit kit
  \item \textbf{Lateral movement}: Pass-the-hash, WMI, RDP
  \item \textbf{Privilege escalation}: Exploits or credential dumping
  \item \textbf{Data exfiltration}: Encrypted staging before encryption
  \item \textbf{Encryption}: Mass file encryption with victim's key
  \item \textbf{Extortion}: Ransom note and payment instructions
\end{enumerate}
```

### Detection Methodology

```latex
\section{Detection Approach}

We propose a machine learning-based detector called \textbf{RansomGuard}
that identifies ransomware based on file system behavior:

\subsection{Features}
We extract 50 behavioral features:
\begin{itemize}
  \item File creation rate (files/second)
  \item File overwrite ratio
  \item Encrypted file extension changes
  \item Shadow copy deletion attempts
  \item Network beaconing patterns
\end{itemize}

\subsection{Detection Model}
We train a gradient boosting classifier on:
\begin{itemize}
  \item \textbf{Positive samples}: 10,000 ransomware samples
    from VirusTotal and Malware Bazaar
  \item \textbf{Negative samples}: 50,000 normal system
    activity traces from enterprise endpoints
\end{itemize}
```

## Evaluation

```latex
\section{Evaluation}

We evaluate RansomGuard on:
\begin{itemize}
  \item \textbf{Test dataset}: 5,000 ransomware samples (new
    variants not in training set)
  \item \textbf{Baselines}: Windows Defender, Sysmon rules,
    Elastic ML detection
\end{itemize}

\subsection{Results}
\begin{center}
\begin{tabular}{lccc}
  \toprule
  System & Precision & Recall & F1 \\
  \midrule
  Windows Defender & 0.89 & 0.72 & 0.80 \\
  Sysmon rules & 0.95 & 0.45 & 0.61 \\
  Elastic ML & 0.78 & 0.88 & 0.83 \\
  \textbf{RansomGuard} & \textbf{0.94} & \textbf{0.91} & \textbf{0.92} \\
  \bottomrule
\end{tabular}
\end{center}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Include attack flow diagrams, detection system architecture, and evaluation plots

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/detection-system}
  \caption{RansomGuard detection pipeline: (a) endpoint agent
    collecting file system events, (b) feature extraction module
    computing behavioral indicators, (c) ML classifier producing
    real-time alerts. The system achieves median detection time
    of 23 seconds from attack start.}
  \label{fig:system}
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
- [ ] Evaluation methodology described
- [ ] Baseline comparisons included
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared

## Camera-Ready Checklist

- [ ] Add author information and affiliations
- [ ] Add acknowledgments
- [ ] Verify PDF/A compliance
- [ ] Check figure quality
