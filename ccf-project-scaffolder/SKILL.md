---
name: ccf-project-scaffolder
description: "Create CCF paper project folders, select or copy LaTeX templates, initialize ccfa.yaml, and prepare artifact directories. Use for project scaffolding and reproducible workspace setup. Do not generate research content."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Project Scaffolder

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Create structure and metadata only. Prefer the target venue guide index for template discovery, then initialize `ccfa.yaml` from `assets/ccfa.yaml` with explicit placeholders.

## Inputs

Project name, target venue, output directory, template preference, and optional paper type.

## Workflow

1. Identify quick or standard mode from the request, available artifacts, and deadline pressure.
2. Check `../ccf-common/references/skill-trigger-registry.yaml` for ownership boundaries before absorbing adjacent work.
3. Read `ccfa.yaml` when it exists. If absent, continue with supplied artifacts and report that project-state tracking is unavailable.
4. Execute only this skill's owned task. Mark missing evidence, stale venue rules, missing files, or authorization gaps explicitly.
5. Produce the requested scaffold result and name the next owning skill when handoff is needed.

## Quick And Standard Modes

- Quick mode: answer the narrow request with the minimum relevant checklist and a compact risk note.
- Standard mode: produce the full table/checklist, artifact-state notes, boundary checks, and handoff recommendations.

## Adaptive Output Contract

If files were created or copied, report the directory tree, template paths, initialized `ccfa.yaml`, and next-step handoff. If the user only asks for a dry-run plan or install subset, return that requested shape instead. Do not force a full checklist for a small scaffold command.

## Handoff

Handoff to `ccf-pipeline-orchestrator` for stage management, `ccf-paper-writer` for manuscript work, and `ccf-submission-checker` for build checks.

## Forbidden

Do not invent title, abstract, claims, experiments, or citations unless the user explicitly supplies them.
