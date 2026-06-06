---
name: ccf-pipeline-orchestrator
description: "Plan and coordinate CCF paper-project stages, goals, constraints, success criteria, gates, artifacts, handoffs, and ccfa.yaml status across the CCFA family. Use for workflow planning, task decomposition, project status, stage gates, next-skill routing, 任务拆解, 流程规划. Do not perform downstream writing, review, search, experiment design, or rebuttal itself."
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

Operate as the project coordinator and workflow planner. Clarify the goal, map the current stage, update or read `ccfa.yaml`, define gates, and name the next owner skill. Do not perform the downstream skill's work.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available; if absent, continue with supplied artifacts and report that project-state tracking is unavailable.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Classify the next owner: `ccf-project-scaffolder`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, or `ccf-rebuttal-writer`.
5. Define the gate: required input, output artifact, pass condition, blocker, and handoff.
6. Provide `ccfa.yaml` update instructions rather than silently overwriting user project state unless explicitly asked.

## Output Contract

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
