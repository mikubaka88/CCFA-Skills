---
name: ccf-integrity-auditor
description: "Audit manuscript integrity: claim-support alignment, result-to-claim consistency, numeric consistency, citation-context support, terminology consistency, figure/table-to-text consistency, and unsupported overclaims. Use for evidence audits and internal consistency before submission. Do not use for full scientific review or broad literature search."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Integrity Auditor

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Trace each important claim to supplied evidence and each numerical statement to supplied results. Mark unsupported items instead of fixing by invention.

## Inputs

Manuscript text, figures/tables/results, claims list or ccfa.yaml, and optional bibliography.

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

Claim-evidence matrix, numeric consistency findings, risk severity, required owner skill, and suggested safe edits.

## Handoff

Use `ccf-citation-auditor` for bibliography verification and `ccf-conference-reviewer` for full scientific review.

## Forbidden

Do not score acceptance, invent missing evidence, or claim that an experiment supports a result not supplied.
