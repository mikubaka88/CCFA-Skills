# Skill-Family Maintenance

Load for actual skill maintenance after Humanization and Common, not for routine research preflight. Paths below are relative to this reference unless a command explicitly names the skill root.


1. Follow the current user scope and existing authorization before defaults; for no-new-files maintenance, edit existing surfaces only. When editing any CCFA family skill, preserve the `metadata.ccf_skill_controls` block and keep its keys aligned with [handoff-modes.md](handoff-modes.md).
2. Use [routing.md](routing.md) before adding new trigger language to prevent overlapping ownership.
3. Use [task-modes.md](task-modes.md) before changing checklist strictness, quick polishing, standard review, or output contracts.
4. Use [review-output-standards.md](review-output-standards.md) before changing scorecards, reviewer panels, score-risk language, or final output self-check rules.
5. Use [privacy-and-evidence.md](privacy-and-evidence.md) before adding any browsing, citation, novelty, scoring, experiment-result, compression, or rebuttal instruction.
6. Use [artifact-contracts.md](artifact-contracts.md) before changing generated filenames, revision behavior, report folders, caches, attempt archives, or ledgers. Default to one canonical artifact per deliverable, one stable working directory per task/artifact, and cleanup of task-created disposable files before delivery. Preserve required evidence and other tasks' files.
7. Never commit personal absolute paths, usernames, expanded home directories, private local skill roots, or machine-specific command examples. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or non-identifying placeholders.
8. Put new public sources in `source-registry.yaml`; do not duplicate long URL lists in sibling `source-notes.md` files. Local references must use repo-relative or non-identifying `local:`/`repo:` identifiers, not machine paths.
9. Run `ccf-common/scripts/check_sources.py` from the repository root after source-registry edits. The script reports issues only and must not rewrite registry files.
10. Run `ccf-common/scripts/check_v04.py` from the repository root for family metadata, registry, script syntax, referenced resources, and regression checks; then run `ccf-common/scripts/check_path_privacy.py` before finalizing CCFA-family changes that touch docs, examples, source records, scripts, diagrams, or release files.

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
