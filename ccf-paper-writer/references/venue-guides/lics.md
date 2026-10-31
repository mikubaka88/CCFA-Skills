# LICS Venue Guide

> Migrated from the legacy `ccf-conference-skills/lics/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `lics` |
| Venue family | Theory |
| CCF tier | CCF-A |
| Template path | `ccf-latex-templates/LICS/IEEEtran.cls` |
| Official URL | https://lics.siglogic.org/2026 |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# LICS 2026 Conference Writing Skill

**CCF-A | Theory | Publisher: IEEE (joint with ACM)**
**Conference:** https://lics.siglogic.org/2026
**Historical template:** See the local path above for examples only; it is not a verified target submission bundle.

## Section Organization

LICS papers follow a logic-in-CS paper structure:

1. **Abstract** — Theorem statements, brief proof idea
2. **Introduction** — Problem, context in logic/CS, contributions (enumerate theorems)
3. **Preliminaries** — Formal definitions, notation, background
4. **Technical Sections** — Proofs organized by theorem/result
5. **Related Work** — Comparison with related logical systems and results
6. **Conclusion**
7. References
8. Appendix (optional)

## Theorem Environments

LICS uses standard theorem environments with emphasis on formal logic:

```latex
\theoremstyle{plain}
\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{corollary}{Corollary}
\newtheorem*{proposition}{Proposition}
\newtheorem*{fact}{Fact}
\newtheorem*{claim}{Claim}

\theoremstyle{plain}
\newtheorem*{definition}{Definition}
\newtheorem*{property}{Property}
\newtheorem*{invariant}{Invariant}

% For proofs:
\newtheorem*{proof}{Proof}

% Example:
\begin{definition}[Kripke Structure]
  \label[definition]{def:kripke}
  A \emph{Kripke structure} $M$ over a set $AP$ of atomic propositions
  is a tuple $(S, S_0, R, L)$ where:
  \begin{itemize}
    \item $S$ is a non-empty set of states,
    \item $S_0 \subseteq S$ is the set of initial states,
    \item $R \subseteq S \times S$ is a total transition relation, and
    \item $L: S \to 2^{AP}$ is a labeling function.
  \end{itemize}
\end{definition}
```

## Logic-Specific Proofs

### Sequent Calculus Proofs

```latex
\usepackage{bussproofs}

\section{Soundness of the Calculus}

\begin{main*}[Soundness]
  Every derivable sequent $\Gamma \vdash \Delta$ is valid.
\end{main*}

\begin{Proof}
  By induction on the structure of the derivation.
  We show that each inference rule preserves validity.

  \begin{prooftree}
    \AxiomC{$\Gamma, A \vdash \Delta$}
    \RightLabel{(\textit{Left\;$\to$})}
    \UnaryInfC{$\Gamma \vdash A \to B, \Delta$}
  \end{prooftree}

  By the induction hypothesis, $\Gamma, A \vdash \Delta$ is valid,
  meaning that for all valuations $v$, if $v \models \Gamma$ and $v \models A$,
  then $v \models \Delta$. We need to show that if $v \models \Gamma$,
  then $v \models A \to B$ or $v \models \Delta$...
\end{Proof}
```

### Typed Lambda Calculus

The `\inferrule` example uses `mathpartir`; `amsthm` and `amsmath` do not define that command. Load it only if compatible with the project template.

```latex
\section{Typed Lambda Calculus with References}

\subsection{Syntax}
The syntax of types and terms is defined as follows:

\[
\begin{array}{lcl}
  \tau & ::= & \alpha \mid \tau \to \tau \mid \text{ref}(\tau) \mid \tau \times \tau \\
  e & ::= & x \mid \lambda x{:}\tau. e \mid e\, e \mid \\
    &     & \text{ref}(e) \mid !e \mid e := e \mid \\
    &     & (e, e) \mid \pi_i(e)
\end{array}
\]

\subsection{Typing Rules}
\begin{mathpar}
  \inferrule*[right=(Var)]
    {x{:}\tau \in \Gamma}
    {\Gamma \vdash x : \tau}

  \inferrule*[right=(Abs)]
    {\Gamma, x{:}\tau_1 \vdash e : \tau_2}
    {\Gamma \vdash \lambda x{:}\tau_1. e : \tau_1 \to \tau_2}

  \inferrule*[right=(App)]
    {\Gamma \vdash e_1 : \tau_2 \to \tau \\ \Gamma \vdash e_2 : \tau_2}
    {\Gamma \vdash e_1\, e_2 : \tau}
\end{mathpar}
```

## References

IEEE uses numeric citations:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Numeric citations
\cite{abramsky1993handbook}
```

## Figures and Tables

LICS papers use minimal figures, primarily for proof trees and diagrams:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.8\linewidth]{figs/game-semantics}
  \caption{Game semantic interpretation of the implication
    $A \to B$. Player (P) moves in $A$ and Opponent (O) moves in $B$.
    The play continues until a winning condition is met.}
  \label{fig:game-sem}
\end{figure}
```

## Content Checklist

- [ ] Main theorems clearly stated
- [ ] Proofs complete and rigorous
- [ ] Logic notation properly formatted
