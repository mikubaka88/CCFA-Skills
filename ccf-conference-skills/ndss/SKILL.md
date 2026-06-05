---
name: ndss
description: Writing and formatting guidance for NDSS (Network and Distributed System Security Symposium) papers. Use when drafting, formatting, or submitting to NDSS 2026. NDSS is NOT double-blind. Covers the bare_conf_NDSS2026.tex template with IEEEtran conference class, USENIX styling overlay, author block formatting, security-specific conventions including threat models, responsible disclosure, 16-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# NDSS 2026 Writing Guide

**CCF-A | Security | Publisher: ISOC (Internet Society)**
**Conference:** https://www.ndss-symposium.org/ndss2026
**Template:** `ccf-latex-templates/NDSS/bare_conf_NDSS2026.tex`

> **IMPORTANT:** NDSS is NOT double-blind — author identities are visible to reviewers.

## Document Setup

### Template Files
- Main template: `NDSS/bare_conf_NDSS2026.tex`
- Also uses: `usenix-2020-09.sty` for USENIX-style overlay
- IEEEtran.cls required

### Required LaTeX Structure

```latex
\documentclass[conference]{IEEEtran}
\usepackage{usenix-2020-09}  % NDSS overlays USENIX styling

% Optional packages
\usepackage{graphicx}
\usepackage{cite}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}

\begin{document}

% Title
\title{Your Paper Title}

% Author blocks — NDSS uses IEEE author format
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

\maketitle

\begin{abstract}
Your abstract here — summarize motivation, problem, approach, and results.
\end{abstract}

% Main content
\section{Introduction}
...

% References: IEEE style
\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

### Key Formatting Requirements
- **Document class**: `IEEEtran` with `[conference]` option
- **Layout**: Single-column (USENIX-style overlay)
- **Title**: Standard `\maketitle` with IEEE author blocks
- **Author format**: `\IEEEauthorblockN{}` and `\IEEEauthorblockA{}`

## Page Limits

- **16 pages** maximum for NDSS 2026
- References do NOT count toward the page limit
- Appendices may be included after references

## Submission Requirements

### Double-Blind Status
**NDSS is NOT anonymous.** Author information should be included. Reviewers see author identities.

### Submission Format
- Submit a single PDF file
- Ensure all fonts are embedded
- Use hyperref for clickable links in PDF

---

## Security-Specific Writing Conventions

### Network Security Focus
NDSS papers typically focus on:
- Network protocol vulnerabilities
- Distributed system security
- Protocol design and analysis
- Real-world attack demonstrations
- Measurement studies of security phenomena

### Threat Model Section (Critical for Security Papers)

The threat model is the foundation of any security paper. Structure it clearly:

```latex
\section{Threat Model}
We assume an adversary with the following capabilities:

\textbf{Adversary's Goals:} The adversary aims to [achieve X, violate Y property].

\textbf{Adversary's Capabilities:}
\begin{itemize}
    \item \textbf{Network access:} The adversary can intercept, modify, and
    inject network traffic on [channel X].
    \item \textbf{Computational resources:} The adversary has [bounded/unbounded]
    computational power.
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

### Attack/Defense Structure

Organize security papers as follows:

```latex
\section{Introduction}
% Problem statement, motivation, contributions (numbered)

\section{Background}
% Protocol/system overview, relevant prior work

\section{System Design}
% Architecture, protocol details, design rationale

\section{Security Analysis}
% Proof of security, threat model, attack surface analysis

\section{Implementation}
% Prototype details, challenges, optimizations

\section{Evaluation}
% Benchmarks, comparison with alternatives, case studies

\section{Discussion}
% Limitations, deployment considerations, future work

\section{Related Work}
% Positioning against prior security work

\section{Conclusion}
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
\end{itemize}

\subsection{Vulnerability Details}
Describe the vulnerability precisely:
\begin{itemize}
    \item Affected component: [Component X, version Y]
    \item Root cause: [Buffer overflow, race condition, etc.]
    \item CVSS score: [If applicable]
    \item CVE ID: [If assigned]
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

\section{Countermeasures}
Proposed defenses with detailed description.
```

### Responsible Disclosure

For real-world vulnerabilities:

```latex
\section{Responsible Disclosure}
We disclosed this vulnerability to [vendor] on [date].
\begin{itemize}
    \item [Date]: Initial disclosure to [vendor]
    \item [Date]: Vendor acknowledged receipt
    \item [Date]: Vendor confirmed vulnerability
    \item [Date]: Patch released / CVE assigned
    \item [Date]: Public disclosure (90-day deadline met)
\end{itemize}

We worked with [CVE Number] and coordinated disclosure with [vendor].
```

## Section Ordering (Recommended)

1. **Abstract** — 150-250 words
2. **Introduction** — Problem, contributions, roadmap
3. **Background** — System model, relevant protocols, threat model
4. **Design/Approach** — Technical contribution
5. **Implementation** — Prototype, deployment challenges
6. **Evaluation** — Methodology, results, baselines
7. **Related Work** — Context within literature
8. **Discussion** — Limitations, deployment considerations
9. **Conclusion** — Summary
10. **References**
11. **Appendix** — Additional proofs, evaluations

## Figure and Table Guidelines

### Network Security Figures
- Protocol sequence diagrams (show message flow)
- System architecture diagrams
- Attack flow diagrams
- Packet captures or network traces (if applicable)
- Use vector graphics for scalability

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{figs/protocol-flow}
  \caption{Sequence diagram showing the attack flow.
    Dashed lines indicate the attacker's actions.}
  \label{fig:protocol}
\end{figure}
```

### Evaluation Tables

```latex
\begin{table}
  \caption{Performance comparison of security mechanisms.
    All measurements are averages over 1000 runs.}
  \label{tab:perf}
  \centering
  \begin{tabular}{lrrr}
    \toprule
    Mechanism & Overhead & Memory & Security \\
    \midrule
    Baseline & 0ms & 1MB & None \\
    Our System & 2.3ms & 3.2MB & Strong \\
    Related Work & 5.1ms & 8.7MB & Moderate \\
    \bottomrule
  \end{tabular}
\end{table}
```

- Compare against state-of-the-art defenses
- Include quantitative metrics (detection rate, overhead, etc.)
- Use booktabs-style formatting
- Clearly label units and metrics

## Reference Format

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

- IEEE reference style: numbered citations `[1]`, `[2]`
- Full author names (not initials)
- Complete conference/journal names

## Camera-Ready Preparation

1. Use final `bare_conf_NDSS2026.tex` template
2. Include all author information and acknowledgments
3. Verify PDF compliance with NDSS requirements
4. Ensure page numbers are correct
5. Submit through the NDSS paper management system

### Camera-Ready Checklist

- [ ] All author information complete
- [ ] Final PDF with embedded fonts
- [ ] Page count ≤ 16 pages
- [ ] References properly formatted
- [ ] Figures in final format

## Common Mistakes to Avoid

1. Using wrong document class (use IEEEtran conference mode)
2. Missing `\IEEEauthorblockN{}` for author names
3. Exceeding page limits
4. Forgetting threat model section
5. Not following IEEE reference format
6. Missing responsible disclosure timeline (for real vulnerabilities)
7. Overclaiming security guarantees
8. Insufficient evaluation of proposed defenses

## Checklist Before Submission

- [ ] Document class: IEEEtran conference mode
- [ ] USENIX styling included
- [ ] Author information complete (not anonymous)
- [ ] Threat model clearly stated
- [ ] Security analysis provided
- [ ] Responsible disclosure timeline included (if applicable)
- [ ] Performance overhead evaluated
- [ ] Comparison with related work
- [ ] Limitations discussed
- [ ] Page count within limits
- [ ] References in IEEE format
- [ ] All figures properly formatted
