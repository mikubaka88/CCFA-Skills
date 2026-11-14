# IEEE S&P Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/ieee-sp/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `ieee-sp` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `TBD - verify official template` |
| Official URL | https://sp2026.ieee-security.org/cfpapers.html |
| Last verified | 2026-10-30: named 2026 submission snapshot only. |
| Source status | Official CFP checked for the snapshot; domain examples are writing guidance. |

## Usage Boundary

- Use the named policy snapshot only for its year/track/stage; use domain examples as writing guidance.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Before applying format changes, reuse or obtain verified official requirements through `ccf-submission-checker`; keep supplied verified templates.

## IEEE S&P 2026 research/SoK submission snapshot

Checked 2026-10-30 against the [official 2026 CFP](https://sp2026.ieee-security.org/cfpapers.html).

- Anonymous review: omit identifying author information and acknowledgments; anonymize artifacts too.
- Research submissions: up to 13 pages of text plus 5 pages of references/appendices, at most 18 total. The CFP specifies a separate SoK reference exception; check the selected paper type rather than applying one budget to both.
- Use US Letter and the official `conference,compsoc` IEEEtran 1.8b template. Do not load IEEEtran as a package or add a USENIX formatting overlay.
- Include `Ethics considerations`; include `LLM usage considerations` when applicable. These sections have specific accounting and disclosure rules in the CFP.

Use the official template linked by that CFP. The old handwritten LaTeX skeleton has been removed because it mixed incompatible class/package and abstract commands.

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
11. **Ethics considerations** — Required for 2026; report actual facts
12. **LLM usage considerations** — When applicable, using actual usage details
13. **References**

## Figure and Table Guidelines

### Security Figures
- Threat model diagrams
- System architecture
- Protocol flows
- Attack visualizations

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
4. Check the verified final-publication page budget
5. Ensure PDF compliance
6. Use the submission or final-publication portal named by the official instructions

## Common Mistakes to Avoid

1. Applying a page budget from another paper type or year
2. Missing threat model section
3. Insufficient formal treatment
4. Weak evaluation
5. Not following IEEE citation format

## Useful Resources

- [IEEE S&P 2026 Author Information](https://sp2026.ieee-security.org)
- [IEEE S&P 2026 Call for Papers](https://sp2026.ieee-security.org/cfpapers.html)
- Publisher: IEEE Computer Society
