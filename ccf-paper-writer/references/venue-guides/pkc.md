# PKC Venue Guide

> Migrated from the legacy `ccf-conference-skills/pkc/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-venue-format-guide`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `pkc` |
| Venue family | Security |
| CCF tier | CCF-B |
| Template path | `ccf-latex-templates/PKC/llncs.cls` |
| Official URL | https://pkc.iacr.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# PKC 2026 Conference Writing Skill

**CCF-B | Security | Publisher: Springer**
**Conference:** https://pkc.iacr.org/2026
**Template:** `PKC/llncs.cls` (Springer LNCS format)

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

PKC follows LNCS guidelines with approximately 30 pages (including references). Check the specific Call for Papers for the current year's limit.

## Anonymity Requirements

PKC uses double-blind review:

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

PKC papers follow the cryptographic research structure:

1. **Introduction** — Problem, contributions (enumerate contributions)
2. **Technical Overview** — High-level summary of the approach
3. **Preliminaries** — Definitions, notation, hardness assumptions
4. **Main Construction** — Core cryptographic construction
5. **Security Analysis** — Proofs, reductions, formal security definitions
6. **Performance / Comparison** (if applicable) — Efficiency analysis
7. **Related Work** — Positioning against prior cryptographic constructions
8. **Conclusion** — Summary
9. References

## Public-Key Cryptography Conventions

PKC emphasizes formal security proofs for public-key primitives:

### Security Definitions

```latex
\section{Preliminaries}

\subsection{Key Encapsulation Mechanisms}
A KEM $\Pi = (\Gen, \Enc, \Dec)$ consists of:
\begin{itemize}
  \item $\Gen(1^\lambda) \to (\ek, \dk)$: Key generation
  \item $\Enc(\ek) \to (k, c)$: Encapsulation
  \item $\Dec(\dk, c) \to k$: Decapsulation
\end{itemize}
The ciphertext $c$ is public; $k$ is the session key.

\subsection{CCA Security}
We define IND-CCA2 security:

\begin{definition}[IND-CCA2 Security]
A KEM $\Pi$ is IND-CCA2 secure if for all PPT
adversaries $\mathcal{A}$:
\begin{align}
  \Adv{\text{IND-CCA2}}{\Pi}(\lambda) = 
  \Pr[\Game_0^{\mathcal{A}}(\lambda) = 1] \\
  - \Pr[\Game_1^{\mathcal{A}}(\lambda) = 1] \leq \negl(\lambda)
\end{align}
where $\Game_b$ is defined as...
\end{definition}
```

### Proof Structure

```latex
\section{Security Analysis}

\subsection{Theorem (IND-CCA2 Security)}
\textbf{Our KEM $\Pi$ achieves IND-CCA2 security under
the NTRU assumption.}

\begin{Proof}
We prove this via a sequence of games.

\medskip
\noindent\textbf{Game 0.} Original IND-CCA2 experiment
with bit $b$ and decryption oracle access.

\medskip
\noindent\textbf{Game 1.} We replace $\Dec(\dk, c)$ with
$\Dec(\dk, c) = \bot$ for all ciphertexts $c \neq c^*$,
where $c^*$ is the challenge ciphertext.

\medskip
\noindent\textbf{Game 2.} We modify the key generation to
sample $\ek, \dk$ from the NTRU challenger. The encapsulation
uses the public key from the NTRU instance.

\medskip
\noindent\textbf{Reduction.} We show that an adversary
distinguishing $\Game_1$ from $\Game_2$ yields a solver for NTRU.
The reduction programs the random oracle and forwards
the NTRU challenge appropriately.

Thus, $\Adv{\text{IND-CCA2}}{\Pi} \leq \Adv{\text{NTRU}}{\mathcal{B}} + \negl(\lambda)$.
\end{Proof}
```

## Performance Analysis

```latex
\section{Efficiency}

We compare our construction with prior works:

\begin{center}
\begin{tabular}{lcccc}
  \toprule
  Scheme & Public Key & Ciphertext & Encaps & Decaps \\
  \midrule
  NewHope & 1,824 B & 2,048 B & 7.8 $\mu$s & 7.2 $\mu$s \\
  Kyber & 800 B & 768 B & 5.1 $\mu$s & 4.8 $\mu$s \\
  \textbf{Ours} & \textbf{640 B} & \textbf{672 B} & \textbf{3.9 $\mu$s} & \textbf{3.6 $\mu$s} \\
  \bottomrule
\end{tabular}
\end{center}
Our scheme achieves 30\% smaller keys and 2$\times$
faster encapsulation than Kyber.
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Include reduction diagrams and efficiency comparisons

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/reduction}
  \caption{Sequence of games for the security reduction.
    $\Game_0$ is the original IND-CCA2 experiment.
    Each transition is proven via standard game-hopping
    techniques. The final reduction to NTRU is tight,
    with only a constant factor overhead.}
  \label{fig:reduction}
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
