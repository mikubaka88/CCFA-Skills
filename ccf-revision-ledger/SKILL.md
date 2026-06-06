---
name: ccf-revision-ledger
description: "Maintain a reviewer-comment to action to manuscript-location to status ledger for revisions, rebuttals, resubmissions, and camera-ready changes. Use for tracking review responses and manuscript edits. Do not replace rebuttal drafting."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Revision Ledger

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Maintain traceability between each comment, decision, manuscript edit, owner, status, and evidence. Keep the ledger factual and auditable.

## Inputs

Reviewer comments, rebuttal draft, manuscript locations, diff notes, and ccfa.yaml if present.

## Workflow

1. Identify quick or standard mode from the request, available artifacts, and deadline pressure.
2. Check `../ccf-common/references/skill-trigger-registry.yaml` for ownership boundaries before absorbing adjacent work.
3. Read `ccfa.yaml` when it exists. If absent, continue with supplied artifacts and report that project-state tracking is unavailable.
4. Execute only this skill's owned task. Mark missing evidence, stale venue rules, missing files, or authorization gaps explicitly.
5. Produce the output contract below and name the next owning skill when handoff is needed.

## Quick And Standard Modes

- Quick mode: answer the narrow request with the minimum relevant checklist and a compact risk note.
- Standard mode: produce the full table/checklist, artifact-state notes, boundary checks, and handoff recommendations.

## Output Contract

Revision ledger table, unresolved comment list, action status, and handoff notes.

## Handoff

Use `ccf-conference-paper-rebuttal` for response prose and `ccf-writing-skills` for manuscript edits.

## Forbidden

Do not write final rebuttal claims that are not backed by completed or planned manuscript actions.
