---
name: ccf-experiment-designer
description: "Design CCF paper evidence packages: datasets, baselines, metrics, ablations, robustness tests, result-table templates, and real-result figure/table presentation. Use for experiment design, benchmark planning, baseline selection, ablation design, result tables, publication figures from supplied numbers, 设计实验, 对比实验, 消融, 结果图表. Do not invent results."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Designer

## Core Rule

Design experiments that test the paper's central claims. Build result tables and publication figures only from supplied real values or explicit placeholders. Never fabricate numbers, improvements, significance, benchmark ranks, or user-study outcomes.

## Modes

- `design`: datasets, baselines, metrics, ablations, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `TBD` placeholders.
- `result-presentation`: LaTeX tables, figure plans, SVG/PDF-ready chart specs, captions, and QA from supplied real results.

## Workflow

1. Identify target venue, paper type, central claims, available results, and whether the task is planning or presenting results.
2. Extract the storyline from the idea or draft. Use `../ccf-paper-writer/references/storyline-blueprint.md` only as a schema, not as a writing handoff.
3. Map every major claim to required evidence, reviewer question, dataset/workload, baseline, metric, ablation, and robustness/failure test.
4. If datasets or baselines are unknown, use public-safe search or hand off to `ccf-literature-searcher`; mark uncertainty instead of guessing.
5. Load `references/evidence-design.md` for venue-family expectations and `references/result-templates.md` for result tables.
6. For result presentation, preserve units, seeds, confidence intervals, dataset names, and metric direction. Mark missing values explicitly.
7. Hand off to `ccf-paper-writer` for manuscript prose, `ccf-integrity-auditor` for number/claim consistency, and `ccf-submission-checker` for package or artifact readiness.

## Output Contract

```text
Mode:
Venue and assumptions:
Claim-evidence matrix:
Dataset / benchmark needs:
Baseline matrix:
Main experiments:
Ablations:
Robustness / failure / efficiency:
Result tables or figure specs:
Missing values:
Execution priority:
No-fabrication status:
Next CCFA owner:
```

## References

- `references/evidence-design.md`: experiment and benchmark design.
- `references/result-templates.md`: fill-in result tables and presentation scaffolds.
