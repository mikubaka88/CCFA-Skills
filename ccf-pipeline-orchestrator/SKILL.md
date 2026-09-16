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

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

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
6. Use the continuity/return contract in `../ccf-common/references/handoff-modes.md`: carry current scope, evidence/version, canonical paths, edit ownership, and the exact next action. Update existing `ccfa.yaml` stage/gate fields only when state maintenance is authorized; preserve unrelated fields and schema. A planning-only request proposes changes without writing.
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
