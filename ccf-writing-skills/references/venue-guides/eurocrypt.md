# EUROCRYPT Venue Guide

> Migrated from the legacy `ccf-conference-skills/eurocrypt/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `eurocrypt` |
| Venue family | Security |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/EUROCRYPT/llncs.cls` |
| Official URL | https://eurocrypt.iacr.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# EUROCRYPT 2026 Conference Writing Skill

**CCF-A | Security | Publisher: Springer**
**Conference:** https://eurocrypt.iacr.org/2026
**Template:** `EUROCRYPT/llncs.cls` (Springer LNCS format)

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

EUROCRYPT follows LNCS guidelines with approximately 30 pages (including references). Check the specific Call for Papers for the current year's limit.

## Anonymity Requirements

EUROCRYPT uses double-blind review:

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

EUROCRYPT papers follow the cryptographic research structure:

1. **Introduction** — Problem, contributions (enumerate contributions)
2. **Technical Overview** — High-level summary of the approach
3. **Preliminaries** — Definitions, notation, hardness assumptions
4. **Main Construction / Protocol** — Core cryptographic contribution
5. **Security Analysis** — Proofs, reductions, formal security definitions
6. **Performance / Comparison** (if applicable) — Efficiency analysis
7. **Related Work** — Positioning against prior cryptographic constructions
8. **Conclusion** — Summary
9. References

## Cryptographic Conventions

EUROCRYPT papers emphasize formal security proofs:

### Security Definitions

```latex
\section{Preliminaries}

\subsection{Cryptographic Primitives}
A \textbf{public-key encryption scheme} $\Pi = (\Gen, \Enc, \Dec)$
consists of three algorithms:

\begin{itemize}
  \item $\Gen(1^\lambda) \to (\pk, \sk)$: Key generation
  \item $\Enc(\pk, m) \to c$: Encryption
  \item $\Dec(\sk, c) \to m$: Decryption
\end{itemize}

\subsection{Security Definitions}
We define IND-CPA security:

\begin{definition}[IND-CPA Security]
A PKE scheme $\Pi$ is IND-CPA secure if for all PPT
adversaries $\mathcal{A}$:
\begin{align}
  \Adv{\text{IND-CPA}}{\Pi}(\lambda) = 
  \Pr[\Exp{\text{IND-CPA-0}}{\Pi}(\mathcal{A}) = 1] \\
  - \Pr[\Exp{\text{IND-CPA-1}}{\Pi}(\mathcal{A}) = 1] 
  \leq \negl(\lambda)
\end{align}
where the experiments are defined as follows...
\end{definition}
```

### Proof Structure

```latex
\section{Security Analysis}

\subsection{Theorem (IND-CPA Security)}
\textbf{Scheme $\Pi$ achieves IND-CPA security under the DDH assumption.}

\begin{Proof}
We prove this by a sequence of games:

\medskip
\noindent\textbf{Game 0.} This is the original IND-CPA experiment
with challenge bit $b$.

\medskip
\noindent\textbf{Game 1.} We modify Game 0 by replacing the
DH challenge tuple $(g, g^a, g^b, g^{ab})$ with
$(g, g^a, g^b, g^c)$ where $c \xleftarrow{R} \mathbb{Z}_p$.
By the DDH assumption, this change is indistinguishable.

\medskip
\noindent\textbf{Analysis.} In Game 1, the challenge ciphertext
is independent of the challenge bit $b$, so the adversary's
advantage is exactly 0.

\medskip
\noindent\textbf{Conclusion.} The reduction from DDH shows that
$\Adv{\text{IND-CPA}}{\Pi} \leq \Adv{\text{DDH}}{\mathcal{B}}$,
which is negligible.
\end{Proof}
```

## Performance Analysis

```latex
\section{Efficiency}

\subsection{Concrete Parameters}
We instantiate our scheme with the following parameters:
\begin{center}
\begin{tabular}{lcc}
  \toprule
  Operation & Time & Size \\
  \midrule
  KeyGen & 2.3 ms & 256 bits \\
  Enc & 4.1 ms & 1.2 KB \\
  Dec & 3.8 ms & -- \\
  \bottomrule
\end{tabular}
\end{center}
Our scheme is $2.1\times$ faster than the state-of-the-art
while achieving stronger security guarantees.
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure readability at LNCS margins
- Include protocol diagrams and reduction graphs

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/protocol}
  \caption{Overview of our PAKE protocol. The client and server
    exchange messages in three rounds to establish a shared
    session key. Our protocol achieves UC-security against
    passive adversaries.}
  \label{fig:protocol}
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
- [ ] Formal security definitions included
- [ ] Proofs are complete and rigorous
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References in LNCS format

## Camera-Ready Checklist

- [ ] Add author information and affiliations
- [ ] Add acknowledgments
- [ ] Verify PDF/A compliance
- [ ] Check figure quality
