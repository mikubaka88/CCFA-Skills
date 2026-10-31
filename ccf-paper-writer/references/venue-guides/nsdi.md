# NSDI Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/nsdi/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `nsdi` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/NSDI` |
| Official URL | https://www.usenix.org/conference/nsdi26/call-for-papers |
| Last verified | 2026-10-30: named 2026 submission snapshot only. |
| Source status | Official CFP checked for the snapshot; domain examples are writing guidance. |

## Usage Boundary

- Use the named policy snapshot only for its year/track/stage; use domain examples as writing guidance.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Before applying format changes, reuse or obtain verified official requirements through `ccf-submission-checker`; keep supplied verified templates.

## NSDI 2026 research-paper submission snapshot

Checked 2026-10-30 against the [official 2026 CFP](https://www.usenix.org/conference/nsdi26/call-for-papers).

- Research papers use anonymous review; follow the CFP's non-destructive anonymization rules. Do not transfer this rule to an operational track without checking that track.
- Main text: at most 12 pages, including figures, tables and footnotes, for submissions and final papers. References and supplementary appendices are outside this limit.
- Use US Letter, two columns and 10-point type with 12-point leading. Keep the official template's text area and column gap.

The bundled `ccf-latex-templates/NSDI/` files are historical examples. USENIX styles use `\maketitle`. Use the verified target template before formatting a manuscript.

## Systems Paper Conventions

NSDI publishes **systems papers** — papers about the design, implementation, and evaluation of practical systems. Key characteristics:

### What Makes a Good NSDI Paper
1. **System evidence**: Claims about an implemented system need actual implementation and evaluation evidence; distinguish proposed design from measured behavior
2. **Design rationale**: Explain why design decisions were made
3. **Practical evaluation**: Show real-world deployment or realistic experiments
4. **Lessons learned**: Insights that benefit the community
5. **Working code**: Preferably open-sourced

### Paper Structure Emphasis

**Introduction** (critical for NSDI):
- Problem statement and motivation
- Key challenges
- Contributions stated at their natural number, with the actual capability, insight, or result identified
- Roadmap of the paper

**Design Section**:
- Design goals and constraints
- Architecture overview
- Component design with rationale
- Design decisions trade-offs

**Implementation Section**:
- Prototype details
- System complexity metrics
- Key implementation challenges
- Deployment considerations

**Evaluation Section**:
- Real-world deployment preferred
- Testbed/simulation acceptable with justification
- Baseline comparison (existing systems)
- Sensitivity analysis
- Performance under stress

## Section Ordering (Recommended)

1. **Abstract** — 150-250 words
2. **Introduction** — Problem, challenges, contributions (4-6 paragraphs)
3. **Background/Motivation** — Context and problem space
4. **Design** — System architecture and components
5. **Implementation** — Prototype details and challenges
6. **Evaluation** — Experiments, results, comparison with baselines
7. **Related Work** — Existing approaches and how this differs
8. **Discussion/Limitations** — Scope, future directions
9. **Conclusion** — Summary
10. **References**
11. **Appendix** (optional) — Additional evaluation and proofs; provide supporting artifacts through the permitted anonymous review channels

## Figure and Table Guidelines

### Systems Diagrams
- Architecture diagrams showing components
- Data flow diagrams
- State machines (if applicable)
- Sequence diagrams for protocols
- Use consistent styling and color schemes

### Evaluation Figures
- Performance graphs with error bars
- Latency/throughput CDFs
- Scalability plots
- Resource utilization over time
- Comparison bar charts

### Table Best Practices
- Use booktabs formatting
- Include baseline comparisons
- Report statistical significance where applicable
- Label units clearly

## Reference Format

```latex
\bibliographystyle{plain}
\bibliography{references}
```

- Author names in standard format
- Full conference proceedings names
- Prioritize recent work and foundational papers

## Camera-Ready Preparation

1. Final review of all content
2. Include author acknowledgments
3. Verify page formatting
4. Ensure figures are high quality
5. Submit through USENIX submission system

## Common Mistakes to Avoid

1. Submitting theory papers (NSDI is for systems)
2. Replacing the verified template with an incompatible legacy skeleton
3. Lightweight evaluation (NSDI expects rigorous evaluation)
4. Missing design rationale (just showing, not explaining)
5. Claiming contributions without sufficient evidence

## Useful Resources

- [NSDI 2026 Call for Papers](https://www.usenix.org/conference/nsdi26/call-for-papers)
- [NSDI Paper Review Guidelines](https://www.usenix.org/conference/nsdi26/reviewing-guidelines)
- Publisher: USENIX Association
