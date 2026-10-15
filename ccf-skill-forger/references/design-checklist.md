# Design Checklist

## Intake

Collect only the details that affect the skill:

- Goal: What task should future Codex sessions become better at?
- Triggers: What would the user naturally say that should activate this skill?
- Examples: What are 2-3 realistic requests the skill should handle?
- Inputs: Which files, APIs, tools, credentials, or domain facts are involved?
- Output: What should the completed work look like?
- Risk: What mistakes would be costly, destructive, or hard to notice?

If examples are missing, invent likely examples and proceed unless the domain is high-stakes or the wrong scope would create unwanted files, network calls, credentials, or destructive actions.

## Naming And Location

- Normalize names to lowercase hyphen-case, such as `pdf-redline` or `gh-pr-review`.
- Prefer short verb-led names when natural, such as `draft-contracts`, `query-metrics`, or `build-plugins`.
- Check the target directory before creating the skill.
- Avoid names that collide with system skills or are too broad, such as `helper`, `coding`, or `skill-creator`.
- Place personal skills in `$CODEX_HOME/skills` when set, otherwise `~/.codex/skills`.
- Do not write expanded home directories, usernames, drive-specific local paths, or machine-specific skill roots into committed files. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or non-identifying placeholders.

## Resource Decision

Choose the smallest structure that solves repeated work:

| Need | Put It In | Reason |
| --- | --- | --- |
| Short workflow or decision rules | `SKILL.md` | Loaded after trigger and cheap to read |
| Long docs, schemas, policies, examples | `references/` | Loaded selectively when needed |
| Repeatable or fragile operations | `scripts/` | Executable and deterministic |
| Templates, fonts, images, boilerplate | `assets/` | Used as files, not context |

Avoid `README.md`, changelogs, installation guides, or broad explanatory documents unless the runtime explicitly requires them. A skill is for agent execution, not general documentation.

## Frontmatter

For Codex skills, keep YAML frontmatter to:

```yaml
---
name: skill-name
description: "What the skill does and exactly when to use it."
---
```

For CCFA family skills, also preserve this metadata block unless the user explicitly requests a family-policy change:

```yaml
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
```

Make the `description` do all trigger work:

- Include task verbs and user phrases.
- Mention important file types, tools, platforms, or domains.
- Include update/review/validate triggers if the skill supports them.
- Do not rely on a "When to use" body section, because the body loads only after the skill is selected.

## Body

Keep the body actionable:

- Start with the operating principle or quick workflow.
- Use imperative instructions.
- Reference bundled resources with relative paths.
- Keep the entry compact and front-load the primary trigger and its nearest routing boundary. Measure entry size and mode-specific reference loading; being under 500 lines alone is not evidence of efficient context use.
- Move variant-specific details into one-level-deep files under `references/`.
- Include command snippets only when they are reusable and safe.

## Validation

For meaningful workflow changes, use a small representative set of real requests to compare the existing and candidate behavior: correct routing, necessary prerequisites, unsupported assertions, artifact quality, and user rework. Include at least one should-not-trigger case for changed routing. Keep inputs and evaluation criteria stable, review outputs without version labels when practical, and record latency/calls/tokens only when actually observed. Static assertions are not evidence of a model-quality gain. Run this during maintenance; do not add a benchmark or extra judge to every user task. Optional enhancements should be checked both enabled and disabled, including explicit instructions overriding saved defaults.

### Bounded Candidate Improvement

Use only during authorized skill maintenance, when the optional `maintenance_evolution` preference or a current explicit request enables it. Keep ordinary fixes and required validation separate from this extra comparison.

1. Name the observed failure, permitted edit surface, current usable baseline, representative cases, acceptance conditions, and available budget. Reuse the current task directory and version control or an existing authorized baseline; do not snapshot unrelated files or overwrite concurrent user edits.
2. Produce at most one additional candidate rule revision per maintenance task. Derive it from concrete failure evidence, not generic prompt expansion. Keep evaluation cases and acceptance fixed for this comparison; the candidate must not edit its own judge or weaken a failing check.
3. Compare routing, prerequisite completion, supported claims, deliverable quality, and avoidable calls/rework. Include relevant boundary cases below. Record only observed latency/token/call data; a longer instruction or passing schema check is not evidence of better reasoning. Use the existing `independent_review` preference if a further independent assessment is useful; do not create another automatic critic loop.
4. Retain the candidate when the relevant evidence supports it; if it regresses, keep the usable baseline and the concise unresolved finding. Roll back only this task's changes after checking current file ownership and intervening edits. Never use repository-wide reset/clean as a recovery shortcut. More candidates or rounds require an explicit scope and budget; renaming a task does not reset the limit.
5. If the user changes the objective or a check itself is demonstrably wrong, version the corrected acceptance and rerun affected comparisons. For an optional continuity record, correcting a mistaken acceptance condition against the unchanged user request is `intent_correction`; a newly requested standard is `user_instruction`. Fix an evaluator implementation without changing the goal when possible; a candidate's poor result alone is not a test defect. Do not compare scores from different criteria as if identical. Maintenance can improve instructions/scripts, not model weights, and never publishes changes without authorization.

For continuity changes, exercise these behavioral boundaries during maintenance, without adding per-task evaluations:

| Case | Expected behavior |
| --- | --- |
| Summary claims a file is verified but the current file/export differs | Inspect the real artifact and affected dependency; repair status and the result before reporting completion. |
| Repeated unchanged failure or ignored material constraint | Narrow the next action, retain the full requested standard, and use an actual relevant check to resume. |
| New evidence contradicts the selected route | Correct the route within scope; do not require approval just to preserve an obsolete plan. |
| User changes the goal, or prior interpretation was wrong | Update current goal/acceptance and keep only applicable prior work; old summaries and delayed contributors cannot override it. |
| Recovery may repeat a completed external action | Check its existing result and authorization before replay; do not duplicate the side effect. |
| Results-pending draft or concept-only idea review | Complete supported content at its requested scope; no invented results, mandatory experiment expansion, or defensive warning appendix. |
| One small edit with current context | Apply the local check; no continuity file, alternative route, or new review call by default. |

### Completion Checks

Check these before finishing:

- Folder name equals frontmatter `name`.
- `name` uses only lowercase letters, digits, and hyphens.
- `description` is non-empty, specific, and trigger-rich.
- `SKILL.md` has no unfinished placeholders.
- Referenced files exist, including sibling resource dependencies in supported installation subsets.
- Parse frontmatter and agent configuration as YAML; preserve the five shared control fields and their types. Validate plugin roots, routing entries, Python syntax, and meaningful behavioral regressions with the existing validators.
- Keep model-specific claims tied to current official sources. Distinguish static validation from a measured model comparison; do not relabel historical evaluation data.
- CCFA family skills preserve the shared `ccf_skill_controls` keys and use `ccf-common` for routing, handoff, privacy, and source-registry policy.
- No committed file contains personal absolute paths, usernames, expanded local skill roots, or machine-specific command examples.
- `ccf-common/scripts/check_path_privacy.py` passes when run at the repository root.
- Optional directories contain only useful files.
- Scripts, if any, were executed on a representative example.
- `agents/openai.yaml`, if present, matches the skill and uses a correct `$skill-name` default prompt.
