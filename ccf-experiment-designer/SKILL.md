---
name: ccf-experiment-designer
description: "Own experiment evidence semantics: decide datasets, baselines, metrics, ablations, robustness tests, chart evidence, and exactly what rows or columns a result table should contain. Use for experiment design, benchmark planning, supplied-result evidence structure, result-table schema, chart-spec semantics, 设计实验, 对比实验, 消融, 结果表证据结构. Do not search literature as the main deliverable, visually beautify or render an already specified table/figure, improve layout/colors/readability, or invent results."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Designer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Run `ccf-humanization` as the first publication-facing experiment preflight only when this skill produces or revises publication-facing prose, final manuscript tables/captions, or a publication method description. Do not load it for raw protocol planning, dataset/baseline/metric selection, execution queues, or evidence-schema design. When it applies, load `../ccf-humanization/references/experiment-discipline.md`, minimize smoke tests to unique changed critical paths, and allow only internally confirmed full method versions in manuscript text, final tables, captions, and claimed comparisons. In publication-facing wording, name the method and scientifically relevant configuration naturally without exposing confirmation, approval, or readiness status. Put version conflicts or necessary exceptions in a separate user-review warning; do not modify experiment or manuscript files merely to encode the warning.

## Core Rule

Design the smallest sufficient experiment package that tests the paper's central claims with complete method configurations verified by the internal gate. Build result tables and evidence-bound figure specs only from supplied real values or explicit placeholders. Never fabricate numbers, improvements, significance, benchmark ranks, or user-study outcomes. Do not expand protocols with repetitive smoke tests or implausible defensive cases. Publication-grade layout, palette, caption placement, and render QA belong to `ccf-visual-composer`. Follow the user's requested output shape: experiment plan, table, LaTeX table, figure spec, ablation list, or execution queue.

## Modes

- `design`: datasets, baselines, metrics, ablations, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `TBD` placeholders.
- `result-presentation`: result tables, figure evidence plans, chart specs, caption facts, and missing-value markers from supplied real results.

## Workflow

1. Run the `ccf-humanization` experiment preflight, then identify target venue, paper type, central claims, available results, confirmed method identities, and whether the task is planning or presenting results.
2. Extract the storyline from the idea or draft. Use `../ccf-paper-writer/references/storyline-blueprint.md` only as a schema, not as a writing handoff.
3. Map every major claim to sufficient evidence, dataset/workload, confirmed baseline, metric, and mechanism-relevant ablation. Add robustness or failure tests only when observed, plausible, claim-relevant, or venue-required; do not enumerate remote defensive cases.
4. If datasets or baselines are unknown, use public-safe search or hand off to `ccf-literature-searcher`; mark uncertainty instead of guessing.
5. Load `references/evidence-design.md` for venue-family expectations and `references/result-templates.md` for result tables.
6. For result presentation, preserve units, seeds, confidence intervals, dataset names, metric direction, and confirmed method version/configuration. Mark missing values explicitly; never fill them with simplified runs.
7. Retain only non-duplicative smoke tests for changed executable critical paths. Keep them outside publication evidence and do not use them as substitutes for full experiments.
8. Hand off to `ccf-visual-composer` for publication-grade figure/table layout, palettes, panel maps, captions, manuscript integration, and render QA.
9. Hand off to `ccf-paper-writer` for manuscript prose, `ccf-integrity-auditor` for number/claim consistency, and `ccf-submission-checker` for package or artifact readiness.

## Adaptive Output Contract

Return the requested artifact first. For a result table request, output the table. For a figure request, output the evidence-bound figure spec and caption facts, then name `ccf-visual-composer` as next owner for visual composition when needed. For a full experiment-design request, use this default structure:

```text
Mode:
Venue and assumptions:
Claim-evidence matrix:
Dataset / benchmark needs:
Confirmed method / baseline versions:
Baseline matrix:
Main experiments:
Ablations:
Robustness / failure / efficiency:
Smoke scope and deduplication:
Result tables or figure specs:
Missing values:
Execution priority:
No-fabrication status:
Next CCFA owner:
```

## References

- `references/evidence-design.md`: experiment and benchmark design.
- `references/result-templates.md`: fill-in result tables and presentation scaffolds.
- `../ccf-humanization/references/experiment-discipline.md`: confirmed full method gate, simplified-version prohibition, smoke-test scope, and experiment-to-paper checks.
- `../ccf-humanization/references/humanization-policy.md`: warning-only, non-injection, and defensive-case removal policy.
