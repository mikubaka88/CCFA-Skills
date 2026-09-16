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

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Activate Humanization and Common before all experiment work, including raw protocol planning and evidence schemas. When producing publication prose/tables/captions or changing executable experiments, load `../ccf-humanization/references/experiment-discipline.md` as applicable, minimize smoke tests to unique changed critical paths, and verify complete method configurations for reported comparisons. These detailed checks are conditional; the family baseline is not. Describe the method and scientifically relevant configuration without exposing internal approval status. Keep unresolved version decisions outside publication artifacts without hiding material facts.

## Core Rule

Design the smallest sufficient experiment package that distinguishes the central hypothesis from plausible alternatives. Use supplied specifications for planned methods; verify complete configurations for reported full-method comparisons. Build result tables and evidence-bound figure specs only from supplied real values or explicit placeholders. Never fabricate numbers, improvements, significance, benchmark ranks, or user-study outcomes. Do not expand protocols with repetitive smoke tests or implausible defensive cases. Publication-grade layout, palette, caption placement, and render QA belong to `ccf-visual-composer`. Follow the user's requested output shape: experiment plan, table, LaTeX table, figure spec, ablation list, or execution queue.

## Modes

- `design`: datasets, baselines, metrics, ablations, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `TBD` placeholders.
- `result-presentation`: result tables, figure evidence plans, chart specs, caption facts, and missing-value markers from supplied real results.

## Workflow

1. Identify the requested output after both family preflights. Raw protocol planning and evidence schemas use Humanization's baseline without a manuscript rewrite. Select detailed prose/experiment checks only when applicable, and establish claims and available evidence before method-version checks.
2. Extract the storyline from the idea or draft. Reuse the supplied claim/mechanism description. Read `../ccf-paper-writer/references/storyline-blueprint.md` only when the central claim needs clarification, not for an already specified result table.
3. Map every major claim to sufficient evidence, dataset/workload, confirmed baseline, metric, and mechanism-relevant ablation. Add robustness or failure tests only when observed, plausible, claim-relevant, or venue-required; do not enumerate remote defensive cases.
4. Resolve missing dataset, baseline, metric, or protocol provenance through `ccf-literature-searcher` before fixing dependent comparisons. Verify compatibility with the central claim. For a consequential unresolved claim-to-test mismatch, request a focused `ccf-paper-reviewer` check and integrate its findings; do not create a full review report for a protocol question. Mark unavailable evidence instead of guessing.
5. Load `references/evidence-design.md` for substantive protocol design or `references/result-templates.md` for table/schema work. Do not load both for a small task unless both are needed.
6. For result presentation, preserve units, seeds, confidence intervals, dataset names, metric direction, and confirmed method version/configuration. Mark missing values explicitly; never fill them with simplified runs.
7. If executable experiment code is actually changed, retain only non-duplicative smoke tests for those critical paths. Planning or formatting alone does not call for smoke tests. Keep them outside publication evidence and do not use them as substitutes for full experiments.
8. Use `ccf-visual-composer` when the requested deliverable includes visual composition, layout, or rendering. Supply real values, units, uncertainty, metric direction, and caption facts; integrate and check the returned figure/table. A raw evidence schema does not require rendering.
9. Before finalizing reported comparisons, reconcile claims, numbers, and configurations; use `ccf-integrity-auditor` for material unresolved conflicts. Use `ccf-paper-writer` for needed manuscript prose and `ccf-submission-checker` when package readiness is in scope. These are conditional contributions, not stages to run for every plan.

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
