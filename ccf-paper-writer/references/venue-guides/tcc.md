# TCC Venue Guide

> Migrated from the legacy `ccf-conference-skills/tcc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `tcc` |
| Venue family | Security |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/TCC/llncs.cls` |
| Official URL | https://tcc.iacr.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# TCC 2026 Conference Writing Skill

**CCF-B | Security | Publisher: Springer**
**Conference:** https://tcc.iacr.org/2026
**Template:** `TCC/llncs.cls` (Springer LNCS format)

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

TCC follows LNCS guidelines with approximately 30 pages (including references). Check the specific Call for Papers for the current year's limit.

## Anonymity Requirements

TCC uses double-blind review:

1. No author names or affiliations in submission
2. Use third person for self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (e.g., ePrint links with author names)
4. Clear PDF metadata
5. Remove acknowledgments from submission

## Camera-Ready Differences

After acceptance:

1. Add complete author information with affiliations
2. Include acknowledgments
3. Add footnote for contact author
4. Ensure PDF/A compliance for Springer publication

## Section Organization

TCC papers follow the theoretical cryptography structure:

1. **Introduction** — Problem, contributions (enumerate contributions)
2. **Technical Overview** — High-level summary of the approach
3. **Preliminaries** — Definitions, notation, complexity classes
4. **Main Results** — Core theoretical contribution
5. **Technical Details** — Proofs, constructions, lower bounds
6. **Related Work / Discussion** — Positioning against prior work
7. **References**

TCC papers emphasize **mathematical rigor** and **precise complexity assumptions**.

## Theoretical Cryptography Conventions

TCC focuses on complexity-theoretic foundations:

### Complexity Assumptions

```latex
\section{Preliminaries}

\subsection{Complexity Assumptions}
We rely on the following assumptions:

\begin{assumption}[Decisional Diffie-Hellman (DDH)]
Given a prime $p$, generator $g$ of $\mathbb{G}_q$,
and tuple $(g^a, g^b, g^c) \in \mathbb{G}_q^3$, the
DDH assumption states that:
\begin{align}
  \Pr[\mathcal{A}(g^a, g^b, g^{ab}) = 1] - 
  \Pr[\mathcal{A}(g^a, g^b, g^c) = 1] \leq \negl(\lambda)
\end{align}
for all PPT adversaries $\mathcal{A}$.
\end{assumption}

Weaker assumptions (used in some constructions):
\begin{itemize}
  \item \textbf{CDH}: Computational Diffie-Hellman
  \item \textbf{DLOG}: Discrete logarithm
  \item \textbf{LWE}: Learning with Errors
\end{itemize}
```

### Protocol Composition

```latex
\section{Protocol Construction}

\subsection{Universal Composability}
We prove our protocol UC-secure in the $\mathcal{F}_{\text{CRS}}$
hybrid model. The protocol proceeds in three phases:

\begin{enumerate}
  \item \textbf{Commit phase}: The sender commits to the message
    using a statistically binding commitment scheme
  \item \textbf{Open phase}: The sender reveals the opening
    using a zero-knowledge proof
  \item \textbf{Verify phase}: The receiver verifies the proof
\end{enumerate}

\subsection{Theorem [Main Result]}
\textbf{Protocol $\Pi$ UC-realizes the ideal functionality
$\mathcal{F}_{\text{OT}}$ in the $\mathcal{F}_{\text{CRS}}$-
hybrid model, assuming DDH.}

\begin{Proof sketch}
We construct an efficient simulator $\Sim$:
\begin{itemize}
  \item $\Sim$ intercepts all messages from the environment
    $\mathcal{Z}$ to the adversary $\mathcal{A}$
  \item $\Sim$ extracts the committed values from the
    statistically binding commitments using the rewinding technique
  \item $\Sim$ programs the CRS to extract the witness for
    the zero-knowledge proof
  \item $\Sim$ forwards the extracted values to $\mathcal{F}_{\text{OT}}$
    and simulates the receiver's view
\end{itemize}
The indistinguishability follows from the DDH assumption...
\end{Proof sketch}
```

### Lower Bounds

```latex
\section{Lower Bounds}

\subsection{Theorem [Main Lower Bound]}
\textbf{Any black-box construction of [primitive] from
[assumption] requires at least $\Omega(n^2)$ communication.}

\begin{Proof}
Assume there exists a black-box construction $\Pi$ achieving
the claimed functionality with $o(n^2)$ communication.
We show this leads to a contradiction with [known lower bound]:

\begin{enumerate}
  \item Consider an adversary $\mathcal{A}$ that interacts with
    $\Pi$ and makes $q$ queries to the protocol
  \item By the black-box lower bound technique of [CITATION],
    $\mathcal{A}$ can recover the secret using $q \cdot \text{poly}(n)$
    time
  \item If $q = o(n^2)$, then total time is $o(n^3)$, which
    contradicts the assumed $\Omega(n^3)$ hardness of [problem]
\end{enumerate}
\end{Proof}
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Include complexity hierarchies, reduction diagrams, and comparison tables

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/hierarchy}
  \caption{Complexity hierarchy of cryptographic assumptions.
    Arrows indicate implication (stronger $\to$ weaker).
    Dashed boxes indicate post-quantum assumptions.
    Our new assumption $\Pi$ lies in the shaded region,
    incomparable with LWE but implied by DDH.}
  \label{fig:hierarchy}
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
- [ ] Complexity assumptions precisely stated
- [ ] Proofs are complete and rigorous
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References in LNCS format

## Camera-Ready Checklist

- [ ] Add author information and affiliations
- [ ] Add acknowledgments
- [ ] Verify PDF/A compliance
- [ ] Check figure quality
