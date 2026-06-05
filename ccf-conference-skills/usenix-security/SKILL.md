---
name: usenix-security
description: Writing and formatting guidance for USENIX Security Symposium papers. Use when drafting, formatting, or submitting to USENIX Security 2026. Critically, USENIX Security is NOT double-blind — author identities are visible. Covers usenix-2020-09.sty format with article class, \maketitles command (not \maketitle), single-column layout, 10pt font requirement, bibliography with plain style, security-specific writing conventions (threat models, attack descriptions, formal security proofs, ethics statement for sensitive experiments), 16-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# USENIX Security Writing Guide

**CCF-A | Security | Publisher: USENIX Association**
**Conference:** https://www.usenix.org/conference/usenixsecurity26
**Template:** `ccf-latex-templates/USENIX-Security/`

> **IMPORTANT:** USENIX Security is NOT double-blind — author identities are visible to reviewers.

## Document Setup

### Template Files
- Main template: `USENIX-Security/` folder
- Primary style: `usenix-2020-09.sty`
- Older style variants: `usenix2019_v3.1.tex`, `usenix2019_v3.sty`

### Required LaTeX Structure

```latex
\documentclass[11pt]{article}
\usepackage{usenix-2020-09}

% Optional packages
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}

\begin{document}

% IMPORTANT: Use \maketitles (NOT \maketitle)
\maketitles

\begin{abstract}
Your abstract here — typically 150-250 words summarizing motivation,
problem, approach, and results.
\end{abstract}

% Main content
\section{Introduction}
...

% Bibliography: plain style
\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### Key Formatting Requirements
- **Document class**: `article` (NOT `acmart` or `IEEEtran`)
- **Font size**: 10pt (enforced by `usenix-2020-09.sty`)
- **Layout**: Single-column
- **Title command**: `\maketitles` — USENIX-specific command replacing standard `\maketitle`

## Page Limits

- **16 pages** maximum for USENIX Security 2026
- References and appendices do NOT count toward the page limit
- Balance technical depth with readability

## Submission Requirements

### Double-Blind Status
**USENIX Security is NOT anonymous.** Do NOT remove author information. Author names, affiliations, and acknowledgments may be included in the submission.

### Submission Format
- Submit a single PDF file
- Ensure all figures are embedded
- Verify font embedding for compatibility

---

## Security-Specific Writing Conventions

### Threat Model Section (Critical)

Every security paper must include a clear threat model:

```latex
\section{Threat Model}
We consider a network adversary who can:

\textbf{Adversary's Goals:} The adversary aims to [achieve X, violate Y property].

\textbf{Adversary's Capabilities:}
\begin{itemize}
    \item \textbf{Network access:} The adversary can intercept, modify, and
    inject network traffic on [channel X].
    \item \textbf{Computational resources:} The adversary has
    [bounded/unbounded] computational power.
    \item \textbf{Prior knowledge:} The adversary knows [protocol details,
    public keys, etc.].
\end{itemize}

\textbf{Security Goals:} Our system should ensure:
\begin{itemize}
    \item \textbf{Confidentiality:} [What should remain secret]
    \item \textbf{Integrity:} [What should not be tampered with]
    \item \textbf{Availability:} [The system should remain available for...]
\end{itemize}

\textbf{Trust Assumptions:} We assume:
\begin{itemize}
    \item The underlying cryptographic primitives (AES, SHA-256) are secure.
    \item The trusted platform module is correctly implemented.
    \item [Other assumptions...]
\end{itemize}
```

### Attack Description Structure

For papers describing vulnerabilities or attacks:

```latex
\section{Vulnerability Analysis}

\subsection{Background}
Describe the system/protocol being analyzed.

\subsection{Vulnerability Discovery}
How did you find this vulnerability?
\begin{itemize}
    \item Manual code review
    \item Fuzzing with [tool]
    \item Protocol state machine analysis
    \item Symbolic execution with [tool]
\end{itemize}

\subsection{Vulnerability Details}
Describe the vulnerability precisely:
\begin{itemize}
    \item \textbf{Affected component:} [Component X, version Y]
    \item \textbf{Root cause:} [Buffer overflow, race condition, etc.]
    \item \textbf{CVSS score:} [If applicable]
    \item \textbf{CVE ID:} [If assigned]
\end{itemize}

\subsection{Exploitation}
Step-by-step attack procedure:
\begin{enumerate}
    \item Attacker sends [X] to victim...
    \item Victim responds with [Y]...
    \item Attacker exploits [Z]...
\end{enumerate}

\subsection{Impact Assessment}
Real-world impact:
\begin{itemize}
    \item Number of affected users/systems
    \item Potential confidentiality/integrity/availability impact
    \item Attack complexity and prerequisites
\end{itemize}
```

### Formal Security Proofs

For cryptographic or protocol papers:

```latex
\section{Security Analysis}

\begin{securitygame}{EAVESDROP}
The adversary $\mathcal{A}$ interacts with the following experiment:
\begin{enumerate}
    \item Challenger generates key $k \leftarrow \mathcal{K}$
    \item Adversary chooses two messages $m_0, m_1$ of equal length
    \item Challenger samples $b \leftarrow \{0,1\}$, sends $c \leftarrow \text{Enc}_k(m_b)$
    \item Adversary outputs $b'$
\end{enumerate}
The adversary wins if $b' = b$.
\end{securitygame}

\begin{definition}[Semantic Security]
A cipher $(\text{Gen}, \text{Enc}, \text{Dec})$ is semantically secure
if for all PPT adversaries $\mathcal{A}$, there exists a negligible function
$\varepsilon$ such that:
\[
\left| \Pr[\mathcal{A} \text{ wins}] - \frac{1}{2} \right| \leq \varepsilon(n).
\]
\end{definition}

\begin{convergence}
Our protocol achieves the property if the DDH assumption holds.
\end{convergence}
```

### Ethics Statement

Required for papers involving:

```latex
\section{Ethics Statement}
We conducted this research ethically and responsibly.

\textbf{Responsible Disclosure:} We disclosed all vulnerabilities to
affected vendors [90 days] prior to submission. We received the following
responses: [vendor acknowledgments]. CVEs have been assigned: [CVE IDs].

\textbf{Institutional Review:} This research was determined to be exempt
from IRB review as it involved [analysis of publicly available systems /
controlled experiments on our own equipment].

\textbf{No Harm:} Our attacks were evaluated in a controlled environment
and no real users or systems were harmed.
```

## Section Ordering (Recommended)

1. **Abstract** — 150-250 words
2. **Introduction** — Motivation, problem, contributions (4-6 paragraphs)
3. **Background/Threat Model** — System overview, adversary model, assumptions
4. **Design/Approach** — Technical contribution with diagrams
5. **Implementation** — System design, prototype, challenges
6. **Evaluation** — Experimental methodology, results, comparison
7. **Related Work** — Context within existing literature
8. **Discussion/Limitations** — Scope, deployment challenges, future work
9. **Conclusion** — Summary of contributions
10. **References**
11. **Appendix** (optional) — Proofs, additional evaluation, artifacts

### Introduction Structure for Security Papers

```latex
\section{Introduction}
% Paragraph 1: Problem and motivation
Security of [system X] is increasingly important due to [Y].
As [Z] becomes more prevalent, protecting [X] against [threat] is critical.

% Paragraph 2: Gap in prior work
Prior work has addressed [aspect] through approaches A, B, and C.
However, these approaches fail to protect against [new threat] because...

% Paragraph 3: Our attack/discovery
In this paper, we identify a new vulnerability in [system].
Our [attack/method] exploits [specific weakness] to achieve [impact].

% Paragraph 4: Contributions (numbered)
Our main contributions are:
\begin{itemize}
    \item We identify and demonstrate [vulnerability] in [system],
    affecting [scope].
    \item We provide a thorough analysis of the root cause and attack surface.
    \item We design and evaluate countermeasures that [achieve X] with [Y] overhead.
    \item We responsibly disclosed our findings to affected vendors.
\end{itemize}

% Paragraph 5: Roadmap
The remainder of this paper is organized as follows...
```

## Figure and Table Guidelines

### Figure Best Practices
- Use vector graphics (PDF/EPS) over raster images
- Include captions below figures
- Reference figures in text: "Figure~\ref{fig:overview} shows..."
- Ensure sufficient contrast for readability
- Label axes clearly with units

### Security-Specific Figures

```latex
% Attack flow diagram
\begin{figure}
  \centering
  \includegraphics[width=0.9\linewidth]{figs/attack-flow}
  \caption{Attack flow: (1) Attacker primes the cache,
    (2) Victim executes sensitive operation,
    (3) Attacker probes to detect evictions.}
  \label{fig:attack}
\end{figure}

% Protocol sequence diagram
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{figs/protocol}
  \caption{Sequence diagram of the attack. Dashed arrows indicate
    the attacker's actions.}
  \label{fig:protocol}
\end{figure}
```

### Table Best Practices
- Use tables for comparing multiple approaches/metrics
- Include clear column headers
- Add horizontal lines sparingly (booktabs style recommended)
- Reference tables in text

```latex
\begin{table}
  \caption{Performance comparison. All measurements are averages
    over 1000 runs on our test machine.}
  \label{tab:perf}
  \centering
  \begin{tabular}{lrrr}
    \toprule
    Scheme & Latency & Memory & Security \\
    \midrule
    Baseline & 0ms & 1MB & None \\
    Our System & 2.3ms & 3.2MB & Strong \\
    Related Work & 5.1ms & 8.7MB & Moderate \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Reference Format

```latex
\bibliographystyle{plain}
\bibliography{references}
```

- Use BibTeX for managing references
- Check for consistent formatting (authors, titles, venues)
- Prioritize recent work (last 5 years) and seminal papers
- Include full conference names, not just abbreviations

## Camera-Ready Preparation

When preparing camera-ready:
1. Download the latest `usenix-2020-09.sty` from USENIX website
2. Include all author names and affiliations
3. Add acknowledgments section (if applicable)
4. Verify page numbers and formatting
5. Ensure PDF/A compliance if required
6. Submit through the USENIX conference management system

### Camera-Ready Checklist

- [ ] All author information complete
- [ ] Acknowledgments section added
- [ ] Funding disclosures included
- [ ] Page count ≤ 16 pages
- [ ] All figures in final format
- [ ] References properly formatted

## Common Mistakes to Avoid

1. Using `\maketitle` instead of `\maketitles`
2. Exceeding 16 pages in main content
3. Including anonymization efforts (unnecessary for USENIX)
4. Using two-column layout (USENIX is single-column)
5. Forgetting to define security assumptions clearly
6. Not including responsible disclosure timeline
7. Overclaiming security guarantees
8. Insufficient evaluation of proposed defenses

## Checklist Before Submission

- [ ] Document class: article with usenix-2020-09.sty
- [ ] `\maketitles` command used (not \maketitle)
- [ ] Single-column layout
- [ ] 16 pages or fewer
- [ ] Threat model clearly defined
- [ ] Security analysis included
- [ ] Responsible disclosure timeline (if applicable)
- [ ] Performance overhead evaluated
- [ ] Comparison with related work
- [ ] Limitations discussed
- [ ] References properly formatted
- [ ] All figures properly formatted
