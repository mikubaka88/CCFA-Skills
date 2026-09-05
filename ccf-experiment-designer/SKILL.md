---
name: ccf-experiment-designer
description: "Design CCF experiment protocols and evidence schemas: datasets, baselines, metrics, ablations, and result-table contents. Use for 设计实验, 消融, benchmark planning, and 结果表证据结构. Preserve real values. Table styling/rendering belongs to ccf-visual-composer; broad retrieval belongs to ccf-literature-searcher."
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

Design the smallest sufficient experiment package that distinguishes the central hypothesis from plausible alternatives. Use supplied specifications for planned methods; verify complete configurations for reported full-method comparisons. Build result tables and evidence-bound figure specs only from supplied real values or explicit placeholders. Never fabricate numbers, improvements, significance, benchmark ranks, or user-study outcomes. Do not expand protocols with repetitive smoke tests or implausible defensive cases. Publication-grade layout, palette, caption placement, and render QA belong to `ccf-visual-composer`. Follow the user's requested output shape: experiment plan, table, LaTeX table, figure spec, ablation list, or execution queue.

## Modes

- `design`: datasets, baselines, metrics, ablations, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `TBD` placeholders.
- `result-presentation`: result tables, figure evidence plans, chart specs, caption facts, and missing-value markers from supplied real results.

## Workflow

1. Identify the requested output first. For raw protocol planning, dataset/baseline/metric selection, or evidence schemas, skip Humanization. Apply its preflight only to manuscript prose or final publication tables/captions. Establish the central claims and available evidence before any method-version check.
2. Extract the storyline from the idea or draft. Reuse the supplied claim/mechanism description. Read `../ccf-paper-writer/references/storyline-blueprint.md` only when the central claim needs clarification, not for an already specified result table.
3. Map every major claim to sufficient evidence, dataset/workload, confirmed baseline, metric, and mechanism-relevant ablation. Add robustness or failure tests only when observed, plausible, claim-relevant, or venue-required; do not enumerate remote defensive cases.
4. If datasets or baselines are unknown, use public-safe search or hand off to `ccf-literature-searcher`; mark uncertainty instead of guessing.
5. Load `references/evidence-design.md` for substantive protocol design or `references/result-templates.md` for table/schema work. Do not load both for a small task unless both are needed.
6. For result presentation, preserve units, seeds, confidence intervals, dataset names, metric direction, and confirmed method version/configuration. Mark missing values explicitly; never fill them with simplified runs.
7. If executable experiment code is actually changed, retain only non-duplicative smoke tests for those critical paths. Planning or formatting alone does not call for smoke tests. Keep them outside publication evidence and do not use them as substitutes for full experiments.
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

For file outputs, follow `../ccf-common/references/artifact-contracts.md`: resolve existing project paths first, keep generated working files under one stable task/artifact directory, and update canonical files in place. Load this shared policy only when files are written and it is not already in context.
