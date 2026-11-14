# USENIX Security Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/usenix-security/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `usenix-security` |
| Venue family | Security |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/USENIX-Security/` |
| Official URL | https://www.usenix.org/conference/usenixsecurity26/call-for-papers |
| Last verified | 2026-10-30: named 2026 submission snapshot only. |
| Source status | Official CFP checked for the snapshot; domain examples are writing guidance. |

## Usage Boundary

- Use the named policy snapshot only for its year/track/stage; use domain examples as writing guidance.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Before applying format changes, reuse or obtain verified official requirements through `ccf-submission-checker`; keep supplied verified templates.

## USENIX Security 2026 submission snapshot

Checked 2026-10-30 against the [official 2026 CFP](https://www.usenix.org/conference/usenixsecurity26/call-for-papers).

- Anonymous review: remove identifying author information, acknowledgments and artifact links without removing the template's author space.
- Main text: at most 13 pages. Follow it with `Ethical Considerations` and `Open Science` appendices, at most one page each, before references. Initial references and optional appendices are unlimited; the final paper has a 20-page total limit.
- Use the unmodified official Security 2026 bundle: US Letter, two columns, 10-point Times Roman with 12-point leading. Do not substitute a generic older USENIX sample.

The bundled `ccf-latex-templates/USENIX-Security/` files remain historical examples. Their style defines `\maketitle`, not `\maketitles`. Obtain the target official bundle for a new submission; preserve an already verified project template.

## Security-Specific Writing Conventions

### Threat Model Section (Critical)

For attack, defense, or security-guarantee claims, define the relevant adversary, assets, capabilities, and assumptions. Measurement, human-subject, or synthesis work should state its applicable scope and assumptions without inventing a system adversary. The following is an example for a network-adversary setting:

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

### Ethical Considerations and Open Science

For the 2026 submission, both appendices are required before references. Fill them from actual research records and the applicable ethics requirements. Do not infer IRB exemption, approval, absence of harm, assigned CVEs or a universal disclosure deadline. Include applicable topics and distinguish completed actions from plans.

```latex
\section{Ethical Considerations}
\textbf{Affected parties and risks:} [Relevant stakeholders, possible
effects of the research, and observed issues.]
\textbf{Review and consent:} [Actual review, approval, exemption or consent
status and its basis, where applicable.]
\textbf{Mitigation and disclosure:} [Actions taken, actual dates and
responses, remaining risks, and any pending steps.]

\section{Open Science}
[List the artifacts needed to assess the contributions and their
anonymous review-access locations; explain any unavailable artifacts.]
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
10. **Ethical Considerations** — Required appendix for 2026
11. **Open Science** — Required appendix for 2026
12. **References**
13. **Additional appendices** (optional) — Proofs and additional evaluation

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
    \item [Documented disclosure action, only if completed and relevant.]
\end{itemize}

% Paragraph 5: Roadmap
The remainder of this paper is organized as follows...
```

## Figure and Table Guidelines

### Figure Best Practices
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
1. Use the official bundle matched to the accepted year and final-publication stage
2. Include all author names and affiliations
3. Add acknowledgments section (if applicable)
4. Verify page numbers and formatting
5. Ensure PDF/A compliance if required
6. Submit through the USENIX conference management system

### Camera-Ready Checklist

- [ ] All author information complete
- [ ] Acknowledgments section added
- [ ] Funding disclosures included
- [ ] Page accounting matches the verified final-publication requirements
- [ ] All figures in final format
- [ ] References properly formatted

## Common Mistakes to Avoid

1. Replacing the official template with an incompatible legacy skeleton
2. Applying a page budget from another year or submission stage
3. Leaving identifying information in the review submission
4. Altering the official layout to fit more content
5. Forgetting to define security assumptions clearly
6. Omitting applicable disclosure facts or presenting planned actions as completed
7. Overclaiming security guarantees
8. Insufficient evaluation of proposed defenses

## Checklist Before Submission

- [ ] Template, anonymity and page accounting match the verified target requirements
- [ ] Threat model clearly defined
- [ ] Security analysis included
- [ ] Responsible disclosure timeline (if applicable)
- [ ] Performance overhead evaluated
- [ ] Comparison with related work
- [ ] Limitations discussed
- [ ] References properly formatted
- [ ] All figures properly formatted
