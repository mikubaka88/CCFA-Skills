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

## Core Rule

Operate as the project coordinator and workflow planner. Clarify the goal, map the current stage, update or read `ccfa.yaml`, define gates, and name the next owner skill. Specialist skills own downstream outputs. For a plan-only request, return the plan. For explicitly requested end-to-end execution, coordinate the authorized owners through completion rather than stopping after naming the next skill. Follow `../ccf-common/references/task-modes.md`: if the user asks for a short plan, checklist, YAML update, table, or narrative roadmap, use that visible shape instead of forcing a fixed report.

Place `ccf-humanization` before any handoff that will write manuscript text or create publication-facing experiment artifacts. This priority preflight does not replace the downstream owner and requires no extra handoff question.

Follow `../ccf-common/references/handoff-modes.md` and `../ccf-common/references/artifact-contracts.md`. Later user corrections normally steer the active project: preserve valid completed work, update affected requirements, and continue. Do not invent completed stages or automatic background jobs.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available; if absent, continue with supplied artifacts and report that project-state tracking is unavailable.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Classify the next owner: `ccf-project-scaffolder`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, or `ccf-rebuttal-writer`. Prefix `ccf-humanization` when the output will enter a manuscript or publication-facing experiment artifact.
5. Define the gate: required input, output artifact, pass condition, blocker, and handoff.
6. Resolve canonical input/output and working paths before each file-producing handoff. Reuse the current artifact and hand off changed requirements plus source locations, not duplicated full reports. Keep independent owners from writing the same file concurrently. Update existing `ccfa.yaml` stage/gate fields when project-state maintenance is authorized; preserve unrelated fields and the existing contract. For a planning-only request, propose the update without writing. Reuse existing artifact/state fields for the current goal, evidence locations, completed work, and next step when continuation needs it.

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
