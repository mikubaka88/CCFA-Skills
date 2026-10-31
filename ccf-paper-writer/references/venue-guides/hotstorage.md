# HotStorage Writing Guide Venue Guide

> Migrated from the legacy `ccf-conference-skills/hotstorage/SKILL.md` runtime skill during v0.4.0. This file is now reference material for `ccf-paper-writer` and `ccf-submission-checker`, not a standalone skill.

| Field | Value |
| --- | --- |
| Venue slug | `hotstorage` |
| Venue family | TBD |
| CCF tier | TBD |
| Template path | `ccf-latex-templates/HotStorage` |
| Official URL | TBD |
| Last verified | Legacy migration on 2026-06-06; official policy must be rechecked before submission. |
| Source status | Domain guidance retained; obsolete policy blocks removed. Query the target official requirements before formatting. |

## Usage Boundary

- Use this file for domain writing guidance. Annual submission rules are resolved through `ccf-submission-checker`, not copied from historical templates.
- Use `ccf-paper-writer` for actual paper writing and polishing.
- Use `ccf-paper-reviewer` or `ccf-submission-checker` for format audit, depending on whether the task is manuscript-facing or submission-package-facing.
- Match the exact year/track/stage before applying any format change; reuse current verified official rules and preserve supplied verified templates.

## Migrated Venue Notes

# HotStorage Writing Guide

HotStorage (Workshop on Hot Topics in Storage Systems) is a **CCF-B storage workshop** (https://www.usenix.org/conferences/hotstorage). HotStorage is a venue for innovative storage systems research, focusing on hot topics in storage and file systems.

## Storage Systems Writing Conventions

### Storage Focus
HotStorage papers focus on:
- File systems
- Storage architectures
- Data management
- Emerging storage technologies

### Workshop Style
- Shorter, more focused papers
- Novel ideas and preliminary results welcome
- Emphasis on hot topics in storage

### Methodology Requirements
- Describe storage system design clearly
- Report performance metrics
- Include workload characterization
- Discuss limitations

## Section Ordering (Recommended)

1. **Abstract** — 150 words, highlight key contribution
2. **Introduction** — Problem, motivation, contributions
3. **Background** — Storage context
4. **Design/Approach** — System design
5. **Evaluation** — Results and analysis
6. **Related Work** — Positioning within literature
7. **Conclusion** — Summary
8. **References**

## Figure and Table Guidelines

### Storage System Figures
- Architecture diagrams
- Performance charts
- Trace visualizations
- Use vector graphics (PDF)

### Table Best Practices
- Clear headers with units
- Highlight best results
- Include performance metrics

## Reference Format

```latex
\bibliographystyle{plain}
\bibliography{references}
```

- Plain bibliography style
- Numbered citations

## Common Mistakes to Avoid

1. Using wrong document class
2. Using a page budget from another year or track
3. Non-embedded fonts in PDF
4. Missing abstract

## Useful Resources

- [HotStorage 2026 Author Information](https://www.usenix.org/conferences/hotstorage)
- [USENIX LaTeX Guidelines](https://www.usenix.org/conferences/author-resources)
- Publisher: USENIX
