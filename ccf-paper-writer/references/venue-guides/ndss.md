# NDSS 2026 Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/ndss/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ndss` |
| Venue family | Security |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/NDSS/bare_conf_NDSS2026.tex` |
| Official URL | https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/ |
| Last verified | 2026-10-30: named 2026 submission snapshot only. |
| Source status | Official CFP checked for the snapshot; domain examples are writing guidance. |

## Usage Boundary

- Use the named policy snapshot only for its year/track/stage; use domain examples as writing guidance.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Before applying format changes, reuse or obtain verified official requirements through `ccf-submission-checker`; keep supplied verified templates.

## NDSS 2026 technical-paper submission snapshot

Checked 2026-10-30 against the [official 2026 CFP](https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/).

- Anonymous review: omit author names and affiliations; remove identifying text, figures and links. Cite prior work in the third person where possible.
- Main text: at most 13 pages, excluding the optional `Ethics Considerations` section, references and appendices. When included, that section precedes references.
- Use the official NDSS 2026 template, US Letter and two columns; Times text must be at least 10 points with at least 11-point leading.

The bundled `ccf-latex-templates/NDSS/bare_conf_NDSS2026.tex` is a template candidate, not authority to combine unrelated publisher styles. Match it to the official target bundle; do not add a USENIX overlay from this old guide.

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

For real-world vulnerabilities, report the actual disclosure status and timeline. Keep only events that occurred; distinguish pending actions from completed ones. Do not assume a 90-day deadline, vendor confirmation, patch release or CVE assignment. Preserve review anonymity when reporting these details.

```latex
\section{Responsible Disclosure}
[Describe the actual disclosure status.]
\begin{itemize}
    \item [Actual date]: [Documented action or response]
    \item [Actual date]: [Next documented action or response, if any]
\end{itemize}
[Any pending steps and the applicable coordination arrangements.]
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
10. **Ethics Considerations** — When included, immediately before references
11. **References**
12. **Appendix** (optional) — Additional proofs and evaluations

## Figure and Table Guidelines

### Network Security Figures
- Protocol sequence diagrams (show message flow)
- System architecture diagrams
- Attack flow diagrams
- Packet captures or network traces (if applicable)

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
- [ ] Page accounting matches the verified final-publication requirements
- [ ] References properly formatted
- [ ] Figures in final format

## Common Mistakes to Avoid

1. Using a template not matched to the target year and track
2. Including identifying author information during anonymous review
3. Exceeding page limits
4. Forgetting threat model section
5. Not following IEEE reference format
6. Missing responsible disclosure timeline (for real vulnerabilities)
7. Overclaiming security guarantees
8. Insufficient evaluation of proposed defenses

## Checklist Before Submission

- [ ] Official template and anonymity match the verified target requirements
- [ ] Threat model clearly stated
- [ ] Security analysis provided
- [ ] Responsible disclosure timeline included (if applicable)
- [ ] Performance overhead evaluated
- [ ] Comparison with related work
- [ ] Limitations discussed
- [ ] Page count within limits
- [ ] References in IEEE format
- [ ] All figures properly formatted
