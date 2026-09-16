---
name: ccf-common
description: "Required shared preflight for every CCFA skill after ccf-humanization: apply routing, scope, prerequisites, evidence rules, handoffs, and artifact contracts. Also maintain and audit these shared rules. Research deliverables remain with their specialist owners."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: references/
---

# CCF Common

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before applying these shared controls, activate [ccf-humanization](../ccf-humanization/SKILL.md) unless its baseline is already active. Apply this entry once, then continue specialist work; do not recursively re-enter either preflight. Reuse applicable rules across contributors.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](references/routing.md); avoid unrelated stages and duplicate reports.

## Core Rule

This is the shared control module activated before every CCFA specialist, after `ccf-humanization`. It sets the task's scope, integrating owner, relevant prerequisites, evidence boundaries, and file paths while specialist skills produce research deliverables. Applying these controls does not run the maintenance workflow or require a governance report.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `references/handoff-modes.md`. On a direct invocation, ensure Humanization's baseline has been read before applying these controls. Do not recursively restart either preflight. Reuse applicable rules across contributors and read only the shared references needed for the current decision.

## Family Preflight

Resolve the requested result, scope/permissions, integrating owner, and missing or reusable prerequisites. Use `references/routing.md` for collaboration and `references/handoff-modes.md` for transitions. Apply evidence/privacy rules when handling sources or private material, artifact rules before file work, and review standards when assessing. Reuse loaded rules and known paths; create no intake form or state file merely to activate this skill. Continue the specialist task once the applicable controls are established. Reserve the maintenance workflow below for actual family-maintenance requests.

## Shared Controls

Load only the references needed for the current preflight decision or maintenance task:

- `references/routing.md`: Use to resolve which CCFA skill owns a request and to avoid trigger overlap.
- `references/task-modes.md`: Use for exploratory/quick/standard depth, authorization-aware continuation, selective context, host-supported parallel work, and GPT-6 adaptation.
- `references/review-output-standards.md`: Use to keep numeric scoring, multi-reviewer panels, score-change conditions, and visible output quality consistent.
- `references/handoff-modes.md`: Use to interpret `metadata.ccf_skill_controls.handoff_question_mode`.
- `references/privacy-and-evidence.md`: Use when handling manuscripts, reviews, rebuttals, private drafts, literature searches, or evidence claims.
- `references/source-registry.yaml`: Use as the shared source inventory for venue rules, review methods, exemplar records, and research-workflow references.
- `references/ccf-a-venue-map.md`: Use when a non-writing skill needs venue-family mapping without depending on `ccf-paper-writer`.
- `references/skill-trigger-registry.yaml`: Use as the canonical trigger registry; compare descriptions and agent prompts with the same ownership boundaries.
- `references/artifact-contracts.md`: Use whenever a skill creates or revises files; it defines ownership, canonical paths, minimal intermediate-file generation, overwrite-in-place defaults, task-scoped cleanup, and required retained history.
- `references/ccfa-yaml-contract.md`: Use for the shared `ccfa.yaml` project-state schema.

## Maintenance Workflow

1. Follow the current user scope and existing authorization before defaults; for no-new-files maintenance, edit existing surfaces only. When editing any CCFA family skill, preserve the `metadata.ccf_skill_controls` block and keep its keys aligned with `references/handoff-modes.md`.
2. Use `references/routing.md` before adding new trigger language to prevent overlapping ownership.
3. Use `references/task-modes.md` before changing checklist strictness, quick polishing, standard review, or output contracts.
4. Use `references/review-output-standards.md` before changing scorecards, reviewer panels, score-risk language, or final output self-check rules.
5. Use `references/privacy-and-evidence.md` before adding any browsing, citation, novelty, scoring, experiment-result, compression, or rebuttal instruction.
6. Use `references/artifact-contracts.md` before changing generated filenames, revision behavior, report folders, caches, attempt archives, or ledgers. Default to one canonical artifact per deliverable, one stable working directory per task/artifact, and cleanup of task-created disposable files before delivery. Preserve required evidence and other tasks' files.
7. Never commit personal absolute paths, usernames, expanded home directories, private local skill roots, or machine-specific command examples. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or non-identifying placeholders.
8. Put new public sources in `references/source-registry.yaml`; do not duplicate long URL lists in sibling `source-notes.md` files. Local references must use repo-relative or non-identifying `local:`/`repo:` identifiers, not machine paths.
9. Run `scripts/check_sources.py` after source-registry edits. The script reports issues only and must not rewrite registry files.
10. Run `scripts/check_v04.py` for family metadata, registry, script syntax, referenced resources, and regression checks; then run `scripts/check_path_privacy.py` before finalizing CCFA-family changes that touch docs, examples, source records, scripts, diagrams, or release files.

## Output Contract

For ordinary preflight, return control to the specialist without a separate report. When auditing or updating CCFA skills, report:

```text
Routing impact:
Handoff mode impact:
Private-material safety:
Source-registry changes:
Score-risk language changes:
Validation result:
```
