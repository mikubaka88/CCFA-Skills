---
name: ccf-experiment-designer
description: "Design and interpret CCF experiments: datasets, baselines, metrics, ablations, execution specifications, observed feedback, and result-table contents. Use for 设计实验, 消融, benchmark planning, 实验结果分析, and evidence design within requested autonomous research. Preserve real values. Orchestrator coordinates research-loop execution; visual styling and broad retrieval have separate owners."
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

Before file work, reuse canonical paths and one task/artifact working directory; default to project-root `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place, preserve inputs, and use UTF-8 with Chinese-text checks. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for naming, ownership, and task-created cleanup; handoffs inherit these paths.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Integrate necessary specialist contributions under one owner; reuse valid prerequisites and verify affected results. Follow the [cooperation routes](../ccf-common/references/routing.md) without duplicate reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Activate Humanization and Common before all experiment work, including raw protocol planning and evidence schemas. When producing publication prose/tables/captions or changing executable experiments, load `../ccf-humanization/references/experiment-discipline.md` as applicable, minimize smoke tests to unique changed critical paths, and verify complete method configurations for reported comparisons. These detailed checks are conditional; the family baseline is not. Describe the method and scientifically relevant configuration without exposing internal approval status. Keep unresolved version decisions outside publication artifacts without hiding material facts.

## Core Rule

Design the smallest sufficient experiment package that distinguishes the central hypothesis from plausible alternatives. Use supplied specifications for planned methods; verify complete configurations for reported full-method comparisons. Build result tables and evidence-bound figure specs from supplied real values, checked measurements obtained through authorized execution, or explicit placeholders. Never fabricate numbers, improvements, significance, benchmark ranks, or user-study outcomes. Do not expand protocols with repetitive smoke tests or implausible defensive cases. Publication-grade layout, palette, caption placement, and render QA belong to `ccf-visual-composer`. Follow the user's requested output shape: experiment plan, table, LaTeX table, figure spec, ablation list, or execution queue.

In explicitly requested autonomous research, own the comparison protocol, necessary execution specifications, and interpretation of actual feedback. Return these to `ccf-pipeline-orchestrator`, which coordinates task-owned implementation and real host execution. Separate a failed command from a negative scientific result. Evidence can motivate a different mechanism or search strategy, not merely another module. This collaboration does not add experiment requirements to concept-only idea review.

## Modes

- `design`: datasets, baselines, metrics, ablations, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `\emptycell` in LaTeX or `—` in Markdown; no invented outcomes.
- `result-presentation`: result tables, figure evidence plans, chart specs, caption facts, and missing-value markers from supplied real results or checked measurements from authorized execution.
- `research-iteration`: a discriminating protocol, executable run specification when authorized, and interpretation of observed results for the next research decision; use `references/evidence-design.md`.

## Workflow

1. Identify the requested output after both family preflights. Raw protocol planning and evidence schemas use Humanization's baseline without a manuscript rewrite. Select detailed prose/experiment checks only when applicable, and establish claims and available evidence before method-version checks.
2. Extract the storyline from the idea or draft. Reuse the supplied claim/mechanism description. Read `../ccf-paper-writer/references/storyline-blueprint.md` only when the central claim needs clarification, not for an already specified result table.
3. Map each major claim to sufficient evidence for its contribution type: applicable datasets/workloads, comparison methods, metrics, and a discriminating ablation, analysis, proof, or study. Planned methods use supplied specifications; reported comparisons require verified configurations. Add robustness or failure tests only when they resolve a specific claim or project decision, grounded in an observed issue or a plausible mechanism, or satisfy a verified venue requirement. Plausibility alone does not justify an unrelated test; do not enumerate remote defensive cases.
4. Resolve missing dataset, baseline, metric, or protocol provenance through `ccf-literature-searcher` when it affects a dependent comparison; reuse verified supplied sources first. A plan may identify an unresolved dependency without blocking independent design work. Verify compatibility with the central claim. For a consequential unresolved claim-to-test mismatch, request a focused `ccf-paper-reviewer` check and integrate its findings; do not create a full review report for a protocol question. Mark unavailable evidence instead of guessing, and do not narrow the research goal merely to fit a generic experiment checklist.
5. Load `references/evidence-design.md` for substantive protocol design or `references/result-templates.md` for table/schema work. Do not load both for a small task unless both are needed.
   For a results-pending manuscript, map the supplied design to its table schema without automatically adding experiments. Preserve planned versus completed protocol status, aggregation, and method identity. Leave outcome analysis blank and return the schema to the writer; pending values do not block drafting the rest of the paper. Every added test must answer a specific claim, comparison, or observed issue; omit irrelevant categories rather than filling them to complete a package.
6. For result presentation, preserve units, seeds, confidence intervals, dataset names, metric direction, and confirmed method version/configuration. Mark missing values explicitly; never fill them with simplified runs.
7. If executable experiment code is actually changed, retain only non-duplicative smoke tests for those critical paths. Planning or formatting alone does not call for smoke tests. Keep them outside publication evidence and do not use them as substitutes for full experiments.
   For an authorized research iteration, provide the executable contract and interpret feedback as described in `references/evidence-design.md`. Use supplied or inspected commands, data, environment, and remaining budget; do not guess runnable paths or treat missing inputs as successful execution. Continue independent preparation while a necessary input is unresolved. Return a concrete next comparison or interpretation to the orchestrator rather than launching an unrelated experiment campaign.
8. Use `ccf-visual-composer` when the requested deliverable includes visual composition, layout, or rendering. Supply real values, units, uncertainty, metric direction, and caption facts; integrate and check the returned figure/table. A raw evidence schema does not require rendering.
9. Before finalizing reported comparisons, reconcile claims, numbers, and configurations; use `ccf-integrity-auditor` for material unresolved conflicts. Use `ccf-paper-writer` for needed manuscript prose and `ccf-submission-checker` when package readiness is in scope. These are conditional contributions, not stages to run for every plan.

## Adaptive Output Contract

Return the requested artifact first. For a result table request, output the table. For a figure request, output the evidence-bound figure spec and caption facts, then name `ccf-visual-composer` as next owner for visual composition when needed. For a full experiment-design request, use the applicable fields below. Omit irrelevant or empty categories; smoke scope belongs only to changed executable code, and a handoff appears only when needed. Evidence integrity is a working rule, not a self-certification field.

For research iterations, return the protocol version, actual outcome and evidence location, whether it distinguishes the competing explanations, and the next decision supported by it. A missing result, invalid comparison, or execution error remains distinct from an unfavorable measurement. Do not infer causal success or publication readiness from a single improved metric.

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
Next CCFA owner:
```

## References

- `references/evidence-design.md`: experiment and benchmark design, run specifications, and interpretation during autonomous research.
- `references/result-templates.md`: fill-in result tables and presentation scaffolds.
- `../ccf-humanization/references/experiment-discipline.md`: confirmed full method gate, simplified-version prohibition, smoke-test scope, and experiment-to-paper checks.
- `../ccf-humanization/references/humanization-policy.md`: warning-only, non-injection, and defensive-case removal policy.
