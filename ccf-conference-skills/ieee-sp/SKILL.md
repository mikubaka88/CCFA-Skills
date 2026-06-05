---
name: ieee-sp
description: Writing and formatting guidance for IEEE S&P (Symposium on Security and Privacy) papers. Use when drafting, formatting, or submitting to IEEE S&P 2026. IEEE S&P is NOT double-blind. Covers IEEEtran conference class with author block formatting, two-column layout, security-specific writing conventions (threat models, formal security proofs, implementation evaluation), 12-page limit, and camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# IEEE S&P Writing Guide

IEEE S&P (Symposium on Security and Privacy) is a **CCF-A security conference** (https://sp2026.ieee-security.org). **IMPORTANT: IEEE S&P is NOT double-blind — author identities are visible to reviewers.** Known for high-quality security and privacy research with rigorous standards.

## Document Setup

### Template Files
- Template folder: `S&P/`
- Document class: `IEEEtran.cls` from the S&P folder
- Mode: `conference` option for two-column format

### Required LaTeX Structure

```latex
\documentclass[conference]{IEEEtran}
\usepackage{IEEEtran}  % Use class from S&P folder

% Optional packages
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}

% Column control if needed
\IEEEoverridewithcntl % For line spacing control

\begin{document}

% Title
\title{Your Paper Title}

% Author blocks — IEEE format
\author{
  \IEEEauthorblockN{Author Name}
  \IEEEauthorblockA{Institution\\Department\\email@example.com}
}

\maketitle

% Two-column begin (IEEE conference format starts two-column here)
\begin{IEEEabstract}
\IEEEabstractnarrowsection
Your abstract content here.
\end{IEEEabstract}

% Main content (single-column at top, then two-column)
\section{Introduction}
...

% References: IEEE style
\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

### Key Formatting Requirements
- **Document class**: `IEEEtran` with `[conference]`
- **Layout**: Two-column (IEEE standard)
- **Font size**: 10pt (IEEE default)
- **Author format**: `\IEEEauthorblockN{}` and `\IEEEauthorblockA{}`

## Page Limits

- **12 pages** maximum for IEEE S&P 2026
- References count within the page limit
- Supplementary materials may be submitted separately

## Submission Requirements

### Double-Blind Status
**IEEE S&P is NOT anonymous.** Author information is visible to reviewers.

### Submission Format
- Single PDF submission
- Ensure PDF/A compliance if required
- Include all figures embedded

## Security-Specific Writing Conventions

### Threat Modeling
Required section structure:
1. **System description**: What is being analyzed?
2. **Trust model**: What does the system trust?
3. **Adversary capabilities**: What can attackers do?
4. **Security goals**: What properties must hold?
5. **Assumptions**: Explicit assumptions about environment

### Formal Security Analysis
For papers with formal components:
- Define security model formally
- State theorems precisely
- Provide complete proofs (or clear proof sketches)
- Include game-based or simulation-based definitions

### Privacy Focus
If paper addresses privacy:
- Define privacy guarantees formally (differential privacy parameters, etc.)
- Discuss adversary models for privacy attacks
- Provide privacy-utility trade-off analysis

### Evaluation Requirements
- Implementation completeness
- Real-world applicability
- Comparison with state-of-the-art
- Limitations and scope

## Section Ordering (Recommended)

1. **Abstract** — Concise summary
2. **Introduction** — Problem, contributions, roadmap
3. **Background/Preliminaries** — Technical background
4. **System/Threat Model** — What is being analyzed, adversary model
5. **Design/Approach** — Technical contribution
6. **Implementation** — Prototype, challenges
7. **Evaluation** — Experiments, results
8. **Related Work** — Context
9. **Discussion/Limitations** — Scope, open questions
10. **Conclusion** — Summary
11. **References**

## Figure and Table Guidelines

### Security Figures
- Threat model diagrams
- System architecture
- Protocol flows
- Attack visualizations
- Use vector graphics

### Evaluation
- Performance overhead measurements
- Accuracy/precision metrics
- Comparison tables
- Ablation studies

## Reference Format

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

- IEEE numbered citation style `[1]`
- Full author names
- Complete venue information
- Prioritize recent and seminal work

## Camera-Ready Preparation

1. Finalize all content
2. Add author acknowledgments
3. Verify two-column layout
4. Check page limits (12 pages)
5. Ensure PDF compliance
6. Submit through IEEE PaperPlaza

## Common Mistakes to Avoid

1. Exceeding 12-page limit
2. Missing threat model section
3. Insufficient formal treatment
4. Weak evaluation
5. Not following IEEE citation format

## Useful Resources

- [IEEE S&P 2026 Author Information](https://sp2026.ieee-security.org)
- [IEEE PaperPlaza](https://paperplaza.net/conferences/)
- Publisher: IEEE Computer Society
