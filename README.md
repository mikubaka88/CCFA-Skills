<div align="center">

# CCFA Skills

### A governed `ccf-*` skill family for CCF paper projects.

<p>
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

CCFA Skills is a local Codex skill family for CCF-style research projects. It covers the full paper lifecycle: project setup, workflow planning, idea shaping, literature search, experiment design, manuscript writing, review, audits, submission checks, rebuttal, resubmission, and presentation.

The current naming pass makes every runtime skill easier to route: names use `ccf-<object>-<role/action>`, with `ccf-common` kept as the governance exception. `ccf-revision-ledger` has been merged into `ccf-rebuttal-writer` so response promises and manuscript actions stay in one post-review workflow.

![Architecture](assets/ccfa-skills-architecture.svg)

## Install

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cp -r CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

For an existing checkout:

```bash
git pull origin main
cp -r ccf-* "$CODEX_HOME/skills/"
```

Plugin manifests are available at `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`.

## Skill Map

- `ccf-project-scaffolder`: Creates project folders, copies/selects templates, and initializes ccfa.yaml.
- `ccf-pipeline-orchestrator`: Coordinates project stages, gates, artifacts, and handoffs.
- `ccf-workflow-planner`: Clarifies goals, constraints, scope, success criteria, and next skill.
- `ccf-idea-optimizer`: Turns rough directions into problem-gap-insight-method-evidence plans.
- `ccf-idea-reviewer`: Scores, ranks, compares, and triages early ideas.
- `ccf-literature-searcher`: Finds related work, prior art, datasets, benchmarks, and citation evidence.
- `ccf-experiment-designer`: Designs datasets, baselines, metrics, ablations, robustness tests, and result templates.
- `ccf-paper-writer`: Plans, drafts, revises, and polishes manuscript text while preserving evidence scope.
- `ccf-paper-compressor`: Shortens paper text to word/page limits without changing claims or results.
- `ccf-scientific-reviewer`: Runs full scientific manuscript review, scoring, simulated reviewers, and AC/meta-review.
- `ccf-writing-reviewer`: Reviews paragraph logic, writing clarity, consistency, LaTeX/format, and presentation risks.
- `ccf-integrity-auditor`: Audits claim-support, result-to-claim, numeric, terminology, and figure/table consistency.
- `ccf-citation-auditor`: Verifies existing citations, BibTeX metadata, paper existence, and citation-context support.
- `ccf-figure-table-builder`: Builds and audits figures, LaTeX tables, captions, SVG/PDF assets from real results.
- `ccf-artifact-packager`: Prepares artifact and reproducibility package plans, env notes, seeds, licenses, and README.
- `ccf-venue-format-guide`: Answers venue LaTeX, template, page-limit, anonymity, and camera-ready format questions.
- `ccf-submission-checker`: Checks LaTeX/PDF builds, page limits, anonymity, fonts, metadata, templates, and policy freshness.
- `ccf-rebuttal-writer`: Writes rebuttals, author responses, response letters, revision summaries, and revision ledgers.
- `ccf-resubmission-adapter`: Adapts an existing paper to a new venue under conservative no-new-experiment defaults.
- `ccf-paper-presenter`: Converts a paper into slides, poster, talk script, figure narration, and Q&A bank.
- `ccf-common`: Shared routing, trigger registry, handoff modes, source registry, privacy policy, and artifact contracts.
- `ccf-skill-forger`: Creates, updates, validates, and audits CCFA/Codex skills and family governance.

## Family Relationship

```text
ccf-project-scaffolder -> ccf-pipeline-orchestrator -> ccf-workflow-planner
  -> ccf-idea-optimizer -> ccf-idea-reviewer
  -> ccf-literature-searcher -> ccf-experiment-designer
  -> ccf-paper-writer -> ccf-paper-compressor
  -> ccf-scientific-reviewer / ccf-writing-reviewer
  -> ccf-integrity-auditor / ccf-citation-auditor
  -> ccf-figure-table-builder / ccf-artifact-packager
  -> ccf-venue-format-guide / ccf-submission-checker
  -> ccf-rebuttal-writer / ccf-resubmission-adapter / ccf-paper-presenter
```

![Workflow](assets/ccfa-skills-workflow.svg)

## Venue Branch

The old per-venue runtime skills remain migrated into:

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

Use `ccf-venue-format-guide` for venue requirements, `ccf-paper-writer` for manuscript content, `ccf-writing-reviewer` for writing/format critique, and `ccf-submission-checker` for actual package checks.

## Naming Migration

- `ccf-brainstorming` -> `ccf-workflow-planner`: Clearer role name; avoids overlap with generic brainstorming.
- `ccf-literature-search` -> `ccf-literature-searcher`: Aligns with role/action naming.
- `ccf-writing-skills` -> `ccf-paper-writer`: Replaces plural family-style name with a single owning role.
- `ccf-conference-reviewer` -> `ccf-scientific-reviewer`: Names the review type, not the venue layer.
- `ccf-conference-writing-reviewer` -> `ccf-writing-reviewer`: Keeps writing review distinct from scientific review.
- `ccf-conference-paper-rebuttal` -> `ccf-rebuttal-writer`: Names the output responsibility.
- `ccf-conference-guides` -> `ccf-venue-format-guide`: Clarifies it handles venue format only.
- `ccf-paper-project-scaffold` -> `ccf-project-scaffolder`: Aligns with role/action naming.
- `ccf-artifact-reproducibility` -> `ccf-artifact-packager`: Clarifies owned artifact output.
- `ccf-revision-ledger` -> `merged into ccf-rebuttal-writer`: Ledger tracking is part of post-review response accountability.
- `ccf-paper-talk` -> `ccf-paper-presenter`: Clarifies presentation ownership.
- `ccf-forge-skills` -> `ccf-skill-forger`: Avoids plural skill-family wording.

## More Diagrams

![Catalog](assets/ccfa-skills-catalog.svg)

![Routing](assets/ccfa-skills-routing.svg)

![Artifacts](assets/ccfa-skills-artifacts.svg)

![Review Boundaries](assets/ccfa-skills-review-boundaries.svg)

See `docs/SKILLS_CATALOG.md`, `docs/ARCHITECTURE.md`, and `docs/NAMING_AND_MERGE_AUDIT.md` for the full routing and merge rationale.
