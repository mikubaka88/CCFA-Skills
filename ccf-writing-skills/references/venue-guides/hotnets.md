# HotNets Venue Guide

> Migrated from the legacy `ccf-conference-skills/hotnets/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-writing-skills` and `ccf-conference-guides`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `hotnets` |
| Venue family | Networks |
| CCF tier | CCF-C |
| Template path | `ccf-latex-templates/HotNets/acmart.cls` |
| Official URL | https://conext2026.sigcomm.org/hotnets |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Migrated local guide; not independently reverified in v0.4.0. |

## Usage Boundary

- Use this file for LaTeX, page limit, anonymity, template, camera-ready, rebuttal-template, and venue-format details.
- Use `ccf-writing-skills` for actual paper writing and polishing.
- Use `ccf-conference-writing-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Verify current-year official rules before final submission.

## Migrated Venue Notes

# HotNets 2026 Conference Writing Skill

**CCF-C | Networks | Publisher: ACM**
**Conference:** https://conext2026.sigcomm.org/hotnets
**Template:** `HotNets/acmart.cls` (ACM acmart, sigconf format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[sigconf,review,anonymous]{acmart}
\settopmatter{printfolios=true}

% === CAMERA-READY MODE ===
\documentclass[sigconf]{acmart}
\acmConference[HotNets 2026]{HotNets '26: ACM SIGCOMM Workshop on...}
               {December 7--8, 2026}{Vienna, Austria}
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
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **6 pages** |
| References | No limit |
| Appendix | Not typical |

HotNets enforces a strict 6-page limit for the main body. This is intentionally short to encourage focused, thought-provoking presentations.

## Anonymity Requirements

Double-blind review with `anonymous` class option:

1. No author names anywhere in submission
2. Third-person self-citations: "Smith et al. showed..." not "we showed..."
3. Anonymize all URLs (GitHub, institutional pages)
4. Clear PDF metadata
5. Do not include acknowledgments

## Camera-Ready Differences

After acceptance:

1. Remove `review` and `anonymous` options
2. Fill in `\acmConference`, `\acmISBN`, `\acmDOI`
3. Restore author names and affiliations
4. Add appropriate `\setcopyright` mode
5. Enable page numbers with `\settopmatter{printfolios=true}`

## Section Organization

HotNets papers are intentionally brief and provocative:

1. **Introduction** — Problem statement, motivation (why it matters NOW)
2. **Key Insight** — The one key observation or idea (the "hot take")
3. **Opportunity / Challenge** — What this enables or what problem it creates
4. **Preliminary Exploration** (optional) — Initial thoughts, simple experiments, early data
5. **Discussion** — Implications, open questions, call to action
6. References

HotNets values **brevity and clarity** over comprehensiveness.

## HotNets Writing Conventions

HotNets is a workshop for early-stage ideas:

### What Makes a Good HotNets Paper

```latex
\section{Key Insight}

The key insight of this paper is that current Internet routing
is fundamentally incompatible with emerging requirements for
in-network compute:

\textbf{Thesis}: We should replace destination-based routing
with intent-based forwarding where routers execute user-defined
programs.

This is provocative because:
\begin{itemize}
  \item Current IP forwarding is 40+ years old
  \item Router vendors resist any fundamental change
  \item But: The proliferation of programmable data planes
    makes this suddenly feasible
\end{itemize}
```

### Structure Tips

- Lead with the insight: State your key claim in the first paragraph
- No need for full related work survey
- Focus on why this idea matters NOW
- Provoke discussion, not consensus

```latex
\section{Discussion}

We believe this direction opens three promising research questions:
\begin{enumerate}
  \item \textbf{Security}: How do we sandbox user programs
    in programmable routers?
  \item \textbf{Performance}: What is the latency overhead
    of in-network compute?
  \item \textbf{Deployment}: How do we migrate incrementally
    from today's Internet?
\end{enumerate}

We hope this position paper sparks discussion at HotNets
and motivates follow-up work.
```

## Figures and Tables

- Use vector formats (.pdf) for all figures
- Ensure grayscale legibility
- Keep figures simple and communicative
- Tables should have clear column headers and units

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figs/insight}
  \caption{Comparison of (a) current destination-based routing
    and (b) our proposed intent-based forwarding architecture.
    The key difference is that packets carry program identifiers
    rather than destination addresses.}
  \label{fig:insight}
\end{figure}
```

## References (natbib)

```latex
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\citet{doe2025}      % Doe et al. (2025)
\citep{doe2025}     % (Doe et al. 2025)
```

All references must list **every author by full name**.

## Formatting Rules

- **Format:** ACM sigconf (two-column, single-spaced)
- **Paper size:** US Letter
- **Body font:** 9pt minimum
- **References:** 8pt, unlimited pages
- **Margins:** Top/bottom 1in, sides 0.75in, column gap 0.25in

## Submission Checklist

- [ ] 6 pages or fewer (main body)
- [ ] `\documentclass[sigconf,review,anonymous]`
- [ ] All author identification removed
- [ ] Key insight clearly stated in first paragraph
- [ ] No self-referential citations in first person
- [ ] Anonymized all URLs
- [ ] PDF metadata cleared
- [ ] References list all authors

## Camera-Ready Checklist

- [ ] Remove `review` and `anonymous` options
- [ ] Add conference metadata
- [ ] Restore author information
- [ ] Enable page numbers
