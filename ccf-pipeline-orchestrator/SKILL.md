---
name: ccf-pipeline-orchestrator
description: "Plan or coordinate CCF research stages, goals, gates, artifacts, and ccfa.yaml state. Use for 任务拆解, 流程规划, project status, and explicitly requested end-to-end coordination. Specialist skills own research outputs; ccf-project-scaffolder owns folder/template creation."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Pipeline Orchestrator

## Family File Contract

Before file work, reuse canonical paths and one task/artifact working directory; default to project-root `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place, preserve inputs, and use UTF-8 with Chinese-text checks. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for naming, ownership, and task-created cleanup; handoffs inherit these paths.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Integrate necessary specialist contributions under one owner; reuse valid prerequisites and verify affected results. Follow the [cooperation routes](../ccf-common/references/routing.md) without duplicate reports.

## Core Rule

Operate as the project coordinator and workflow planner. Clarify the goal, map the current stage, update or read `ccfa.yaml`, define gates, and name the next owner skill. Specialist skills own downstream outputs. For a plan-only request, return the plan. For explicitly requested end-to-end execution, coordinate the authorized owners through completion rather than stopping after naming the next skill. Follow `../ccf-common/references/task-modes.md`: if the user asks for a short plan, checklist, YAML update, table, or narrative roadmap, use that visible shape instead of forcing a fixed report.

Ensure Humanization and Common are active before planning and every contributing skill. Reuse their applicable rules at handoffs. Apply Humanization's detailed prose modes within authorized writing stages; raw planning and rendering still receive its baseline without a manuscript-edit workflow.

Follow `../ccf-common/references/handoff-modes.md` and `../ccf-common/references/artifact-contracts.md`. Later user corrections normally steer the active project: preserve valid completed work, update affected requirements, and continue. Do not invent completed stages or automatic background jobs.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available; if absent, continue with supplied artifacts. Do not require setup or create project state merely to route work; disclose its absence only when it limits requested tracking.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Assign integrating owners using `../ccf-common/references/routing.md`. Work backward from the requested outcome to missing prerequisites and material checks, including upstream work not named by the user. Distinguish bounded contributions from next-artifact ownership; carry both active preflights throughout and apply detailed Humanization modes when relevant. Preserve explicit scope limits.
5. Define each applicable gate through its required evidence, output, pass condition, blocker, and responsible skill. Mark prerequisites satisfied, missing, conflicting, or outside scope; reuse valid ones and resolve missing/conflicting ones before advancing dependent conclusions. Tool completion alone does not pass a gate.
6. Use `../ccf-common/references/handoff-modes.md` and, for long tasks or recovery, `../ccf-common/references/continuity.md`: carry the current goal, justified route, evidence/version, canonical paths, work status, and exact next action. Reconcile actual artifacts after lost context before resuming or replaying side effects. Apply explicit user changes and evidence-backed corrections within scope. Update existing `ccfa.yaml` stage/gate fields only when state maintenance is authorized; preserve unrelated fields and schema. A planning-only request proposes changes without writing.
7. Integrate specialist results, resolve conflicts against source evidence, and check affected downstream conclusions. Advance gates from actual evidence; preserve valid completed work and continue independent stages around a blocker. Reopen only changed dependencies or unresolved findings. Finish when requested outputs and applicable prerequisites/checks are complete, or identify the precise dependent result that remains incomplete.

## Adaptive Output Contract

Put the requested artifact first: roadmap, next-step decision, task list, handoff packet, or `ccfa.yaml` patch instructions. Use the full structure below only for standard planning, ambiguous multi-stage projects, or when the user asks for a complete coordination report.

```text
Project goal:
Current stage:
Known artifacts:
Missing artifacts:
Gate decision:
Next owner skill:
Handoff packet:
ccfa.yaml update:
Risks / blockers:
```
