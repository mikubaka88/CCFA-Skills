---
name: crypto
description: Writing and formatting guidance for CRYPTO (International Cryptology Conference) papers. Use when drafting, formatting, or submitting to CRYPTO 2026. Covers Springer LNCS llncs.cls format with splncs04 bibliography style, double-blind anonymity, 30-page limit (LNCS standard), formal security proofs, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CRYPTO 2026 Conference Writing Skill

**CCF-A | Security | Publisher: Springer**
**Conference:** https://crypto.iacr.org/2026
**Template:** `CRYPTO/llncs.cls` (Springer LNCS format)

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

CRYPTO follows LNCS guidelines with approximately 30 pages (including references). Check the specific Call for Papers for the current year's limit.

## Anonymity Requirements

CRYPTO uses double-blind review:

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

CRYPTO papers follow the cryptographic research structure:

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

CRYPTO papers emphasize formal security proofs and theoretical depth:

### Security Definitions

```latex
\section{Preliminaries}

\subsection{Cryptographic Primitives}
A \textbf{digital signature scheme} $\Sigma = (\Gen, \Sign, \Ver)$
consists of three PPT algorithms:

\begin{itemize}
  \item $\Gen(1^\lambda) \to (\vk, \sk)$: Key generation
  \item $\Sign(\sk, m) \to \sigma$: Signing
  \item $\Ver(\vk, m, \sigma) \to \{0,1\}$: Verification
\end{itemize}

\subsection{Security Definitions}
We define strong EUF-CMA security:

\begin{definition}[Strong Existential Unforgeability under CMA]
A signature scheme $\Sigma$ is strongly EUF-CMA secure if
for all PPT adversaries $\mathcal{A}$:
\begin{align}
  \Adv{\text{EUF-CMA}}{\Sigma}(\lambda) = 
  \Pr[\text{Forge}_{\mathcal{A}}(\lambda) = 1] \leq \negl(\lambda)
\end{align}
where Forge$_{\mathcal{A}}$ is the experiment where $\mathcal{A}$
gets $\vk$ and access to a signing oracle, and wins if it
outputs a valid $(m^*, \sigma^*)$ pair where $m^*$ was never
queried to the signing oracle.
\end{definition}
```

### Proof Structure

```latex
\section{Security Analysis}

\subsection{Theorem (EUF-CMA Security)}
\textbf{Scheme $\Sigma$ achieves EUF-CMA security under the
CDH assumption.}

\begin{Proof}
We prove this by reduction to the CDH problem.

Suppose there exists an adversary $\mathcal{A}$ that breaks $\Sigma$.
We construct a reduction $\mathcal{B}$ that solves CDH:

\begin{enumerate}
  \item $\mathcal{B}$ receives $(g, g^a, g^b)$ from its CDH challenger.
  \item $\mathcal{B}$ runs $\Gen(1^\lambda)$ to get $(\vk, \sk)$,
    but programs the verification key to be $vk = g^a$.
  \item $\mathcal{B}$ runs $\mathcal{A}$ with $\vk$ and
    answers signing queries by...
  \item When $\mathcal{A}$ outputs a forgery $(m^*, \sigma^*)$,
    $\mathcal{B}$ extracts...
  \item $\mathcal{B}$ outputs $g^{ab}$ as the CDH solution.
\end{enumerate}

The reduction succeeds because...
\end{Proof}
```

## Performance Analysis

```latex
\section{Instantiation}

We instantiate our construction over a BN curve:
\begin{center}
\begin{tabular}{lcc}
  \toprule
  Operation & Time & Communication \\
  \midrule
  Sign & 0.8 ms & -- \\
  Verify & 1.2 ms & -- \\
  Total & 2.0 ms & 64 bytes \\
  \bottomrule
\end{tabular}
\end{center}
Our scheme is the fastest post-quantum signature of
its class, achieving 2.5$\times$ speedup over the
previous best construction.
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure readability at LNCS margins
- Include protocol diagrams and reduction graphs

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/construction}
  \caption{Our signature scheme: (a) key generation, (b) signing
    algorithm showing the hash-and-sign structure, (c) verification.
    All operations are performed in the group $\mathbb{G}$
    of order $q$.}
  \label{fig:construction}
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
