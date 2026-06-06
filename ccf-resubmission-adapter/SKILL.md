---
name: ccf-resubmission-adapter
description: "Adapt an already written paper to a new CCF venue, including format mapping, story reframing, reviewer-priority shifts, page-budget planning, and conservative change tracking. Default mode is no-new-experiment and no-bib-edit unless the user explicitly authorizes those changes."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Resubmission Adapter

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Preserve the manuscript's evidence base by default. Use the new venue guide and writing adapter to identify safe framing and formatting changes.

## Inputs

Existing manuscript, old venue, new target venue, reviews if available, and allowed-change policy.

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

Venue adaptation plan, safe text/structure edits, page-budget risks, forbidden changes, and required authorization requests.

## Handoff

Use `ccf-conference-guides`, `ccf-writing-skills`, `ccf-paper-compressor`, and `ccf-submission-checker` as needed.

## Forbidden

Do not add experiments, edit bibliography scope, or change claims beyond supplied evidence unless explicitly authorized.
