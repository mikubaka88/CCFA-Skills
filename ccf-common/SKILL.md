---
name: ccf-common
description: "Shared governance for the CCFA family: routing, trigger registry, task modes, handoff modes, source registry, privacy/evidence policy, ccfa.yaml, and artifact contracts. Use only when maintaining or auditing CCFA skills; not for ordinary research tasks."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: references/
---

# CCF Common

## Core Rule

This is the shared control module for the CCFA Skills family. Do not use it as a user-facing research assistant module. Use it to keep routing, handoff behavior, source provenance, private-material handling, and score-risk language consistent across `ccf-*` skills and `ccf-skill-forger`.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `references/handoff-modes.md`. This skill provides shared policy only; route ordinary research tasks to the owning skill in `references/routing.md`.

## Shared Controls

Load only the file needed for the current maintenance task:

- `references/routing.md`: Use to resolve which CCFA skill owns a request and to avoid trigger overlap.
- `references/task-modes.md`: Use to interpret quick and standard execution modes across CCFA skills.
- `references/review-output-standards.md`: Use to keep numeric scoring, multi-reviewer panels, score-change conditions, and visible output quality consistent.
- `references/handoff-modes.md`: Use to interpret `metadata.ccf_skill_controls.handoff_question_mode`.
- `references/privacy-and-evidence.md`: Use when handling manuscripts, reviews, rebuttals, private drafts, literature searches, or evidence claims.
- `references/source-registry.yaml`: Use as the shared source inventory for venue rules, review methods, exemplar records, and research-workflow references.
- `references/ccf-a-venue-map.md`: Use when a non-writing skill needs venue-family mapping without depending on `ccf-paper-writer`.
- `references/skill-trigger-registry.yaml`: Use as the v0.4 public trigger registry for routing conflict audits.
- `references/artifact-contracts.md`: Use to decide which skill may read or write each project artifact.
- `references/ccfa-yaml-contract.md`: Use for the shared `ccfa.yaml` project-state schema.

## Maintenance Workflow

1. When editing any CCFA family skill, preserve the `metadata.ccf_skill_controls` block and keep its keys aligned with `references/handoff-modes.md`.
2. Use `references/routing.md` before adding new trigger language to prevent overlapping ownership.
3. Use `references/task-modes.md` before changing checklist strictness, quick polishing, standard review, or output contracts.
4. Use `references/review-output-standards.md` before changing scorecards, reviewer panels, score-risk language, or final output self-check rules.
5. Use `references/privacy-and-evidence.md` before adding any browsing, citation, novelty, scoring, experiment-result, compression, or rebuttal instruction.
6. Never commit personal absolute paths, usernames, expanded home directories, private local skill roots, or machine-specific command examples. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or non-identifying placeholders.
7. Put new public sources in `references/source-registry.yaml`; do not duplicate long URL lists in sibling `source-notes.md` files. Local references must use repo-relative or non-identifying `local:`/`repo:` identifiers, not machine paths.
8. Run `scripts/check_sources.py` after source-registry edits. The script reports issues only and must not rewrite registry files.
9. Run `scripts/check_path_privacy.py` before finalizing CCFA-family changes that touch docs, examples, source records, scripts, diagrams, or release files.

## Output Contract

When auditing or updating CCFA skills, report:

```text
Routing impact:
Handoff mode impact:
Private-material safety:
Source-registry changes:
Score-risk language changes:
Validation result:
```
