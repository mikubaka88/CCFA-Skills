# CCS Venue Guide

> Migrated from the legacy `ccf-conference-skills/ccs/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ccs` |
| Venue family | Security |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/CCS/acmart.cls` |
| Official URL | https://www.sigsac.org/ccs/CCS2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# CCS 2026 Conference Writing Skill

**CCF-A | Security | Publisher: ACM**
**Conference:** https://www.sigsac.org/ccs/CCS2026
**Template:** `CCS/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf, review, anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[CCS 2026]{CCS '26: 2026 ACM SIGSAC Conference...}
               {October 12--16, 2026}{London, United Kingdom}
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
\usepackage{balance}
\usepackage{cleveref}          % For consistent cross-references
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **16 pages** |
| References | No limit |
| Appendix | Permitted (not counted) |

CCS enforces a 16-page limit for the main body. References and appendix do not count toward this limit. Appendix is for supplementary details only — reviewers are not required to read it.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names or affiliations in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs, GitHub links, personal pages
4. Clear PDF metadata
5. Remove acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore all author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

CCS papers must follow security-specific structure:

1. **Introduction** — Security problem, threat model, contributions (enumerate contributions)
2. **Background & Threat Model** — System model, adversary capabilities, security goals
3. **Attack Description / Problem Statement** — For attack papers: how the attack works; for defense papers: what you are defending against
4. **Design / Defense Mechanism** — Core contribution with formal treatment where applicable
5. **Security Analysis / Proof** — Formal security proofs, reduction arguments, or informal analysis
6. **Implementation** — System details, complexity, integration challenges
7. **Evaluation** — Security analysis, performance overhead, comparison with defenses
8. **Related Work** — Positioning against prior security work
9. **Conclusion**
10. References
11. Appendix (optional)

## Threat Modeling

CCS papers require explicit threat modeling:

```latex
\section{Threat Model}
We consider a network adversary who can:
\begin{itemize}
  \item Intercept and modify packets in transit (MITM capability)
  \item Observe traffic timing and volume
  \item Inject packets into the network
  \item Potentially compromise up to $t$ nodes in the system
\end{itemize}
We assume the adversary cannot break cryptographic primitives,
but can observe all communication on compromised nodes.
\end{itemize}
```

## Security Proofs

Formal security proofs are highly valued in CCS. Use the `amsthm` theorem environment:

```latex
\theoremstyle{plain}
\newtheorem{securityclaim}{Security Claim}
\newtheorem{invariant}{Invariant}

% Reduction-style proof
\begin{securityclaim}[Fork隐私 (Fork Privacy)]
  \label{claim:fork-privacy}
  No polynomial-time adversary $\mathcal{A}$ can distinguish
  between the real execution and an ideal execution where
  transactions are reordered before commitment.
\end{securityclaim}

\begin{Proof}
  We prove by reduction to the DDH assumption.
  % detailed proof ...
\end{Proof}
```

## Attack/Defense Taxonomy

Clearly categorize your contribution:

```latex
\section{Attack Overview}
Our attack, \textbf{SideChannel}, exploits timing variations in
cache eviction policies to extract secret keys. Specifically:
\begin{itemize}
  \item \textbf{Adversary model}: Unprivileged user-space process
  \item \textbf{Attack vector}: Prime+Probe on shared L3 cache
  \item \textbf{Sensitive data}: RSA decryption keys
  \item \textbf{Leakage}: Partial key bits via eviction timing
\end{itemize}
```

## Evaluation

CCS evaluation combines security analysis with performance:

```latex
\section{Evaluation}
We evaluate SideChannel along two dimensions:
\begin{itemize}
  \item \textbf{Attack effectiveness}: Key recovery rate vs. time
  \item \textbf{Defense overhead}: Performance impact of mitigations
\end{itemize}

\begin{table}[t]
  \caption{Key recovery rate after 1,000 measurements.}
  \label{tab:recovery}
  \begin{tabular}{lrr}
    \toprule
    Defense & Success Rate & Overhead \\
    \midrule
    None & 94.2\% & -- \\
    \textbf{Our defense} & 2.1\% & 3.2\% \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Figures and Tables

- Vector formats (.pdf) for diagrams
- Ensure grayscale legibility
- Self-contained captions
- Security figures often use attack trees or protocol diagrams

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/attack-flow}
  \caption{Attack flow: (1) Attacker primes cache set $S$,
    (2) Victim executes, evicting attacker's probe set,
    (3) Attacker probes to detect evictions and recover 1 bit
    of the secret key.}
  \label{fig:attack-flow}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{shamir1979}      % Shamir (1979)
\citep{shamir1979}      % (Shamir 1979)
```

All references must list **every author by full name**.

## Ethics and Responsible Disclosure

CCS expects ethical security research:

1. **No victim harm** — attacks should be evaluated responsibly
2. **Coordinated disclosure** — disclose vulnerabilities to affected vendors before publication
3. **IRB/exemption** — if human subjects are involved, address ethics
4. **Artifacts** — consider releasing proof-of-concept code or evaluation artifacts

```latex
\section{Ethics}
We disclosed the vulnerabilities to affected vendors 90 days
prior to submission. All experiments were conducted on our
own equipment with ethical approval.
```

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 16 pages or fewer (main body)
- [ ] `\documentclass[sigconf, review, anonymous]`
- [ ] All author identification removed
- [ ] Threat model clearly stated
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs
- [ ] Security claims backed by analysis/proofs
- [ ] References list all authors
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
- [ ] Add ethics/disclosure statement if applicable
