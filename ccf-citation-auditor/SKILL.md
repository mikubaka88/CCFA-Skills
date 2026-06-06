---
name: ccf-citation-auditor
description: "Verify already cited papers and BibTeX entries: existence, metadata, DOI/arXiv/venue correctness, citation-context support, duplicate keys, stale references, and suspicious unsupported citations. Use for bibliography and citation-context audit. Do not use for broad literature search or finding many new related papers."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Citation Auditor

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Audit citations already present in the manuscript or `.bib`. Use online verification when metadata or existence matters, but avoid broad discovery unless handed off.

## Inputs

Manuscript citation contexts, `.bib` files, cited paper list, and target venue style.

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

Citation issue table, metadata fixes, unsupported-context warnings, and handoff notes for missing related work.

## Handoff

Use `ccf-literature-search` when the task requires new papers or prior-art discovery.

## Forbidden

Do not add citations merely to appear comprehensive, and do not certify a citation without checking enough metadata.
