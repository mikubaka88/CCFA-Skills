---
name: ccf-paper-presenter
description: "Convert a completed or near-completed CCF paper into slides, poster, talk script, elevator pitch, figure narration, and Q&A bank. Use for presentation preparation. Do not perform pre-submission scientific review."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Presenter

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Translate the paper into a presentation artifact while preserving claims, evidence, limitations, and target audience.

## Inputs

Paper draft, figures/tables, venue/session type, talk duration, audience, and required output format.

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

Slide/poster outline, talk script, Q&A bank, figure narration, timing plan, and asset checklist.

## Handoff

Use `ccf-paper-writer` only if manuscript text itself must be revised.

## Forbidden

Do not present speculative results as completed or use this skill to bypass scientific review.
