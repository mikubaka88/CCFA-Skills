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

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse existing paths; otherwise use `output/ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Core Rule

Operate as the project coordinator and workflow planner. Clarify the goal, map the current stage, update or read `ccfa.yaml`, define gates, and name the next owner skill. Specialist skills own downstream outputs. For a plan-only request, return the plan. For explicitly requested end-to-end execution, coordinate the authorized owners through completion rather than stopping after naming the next skill. Follow `../ccf-common/references/task-modes.md`: if the user asks for a short plan, checklist, YAML update, table, or narrative roadmap, use that visible shape instead of forcing a fixed report.

Apply `ccf-humanization` within the owning writing stage when producing manuscript or final publication-facing prose/captions. Reuse its policy and prior decisions; do not repeat a separate preflight at every handoff. Raw experiment planning and visual rendering without prose skip it.

Follow `../ccf-common/references/handoff-modes.md` and `../ccf-common/references/artifact-contracts.md`. Later user corrections normally steer the active project: preserve valid completed work, update affected requirements, and continue. Do not invent completed stages or automatic background jobs.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available; if absent, continue with supplied artifacts. Do not require setup or create project state merely to route work; disclose its absence only when it limits requested tracking.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Assign requested deliverables to owners using `../ccf-common/references/routing.md`. Select only necessary stages and distinguish helper work from a transfer to the next artifact's owner. Apply Humanization only at a relevant prose stage.
5. Define the gate: required input, output artifact, pass condition, blocker, and handoff.
6. Use the continuity/return contract in `../ccf-common/references/handoff-modes.md`: carry current scope, evidence/version, canonical paths, edit ownership, and the exact next action. Update existing `ccfa.yaml` stage/gate fields only when state maintenance is authorized; preserve unrelated fields and schema. A planning-only request proposes changes without writing.
7. Integrate helper results before continuing. Advance a gate from actual evidence, preserve completed work, and keep blocked dependencies separate from executable stages. Finish once the requested outputs and relevant checks are complete; do not cycle through owners without new input or an unresolved action.

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
