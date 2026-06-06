# CCFA Architecture

CCFA is a CCF/NeurIPS-style paper-project workflow family. v0.4.2 keeps the runtime surface small: each stage has one clear owner, and helper capabilities live as modes under that owner.

## Layers

| Layer | Runtime skills |
| --- | --- |
| Setup | `ccf-project-scaffolder` |
| Planning | `ccf-pipeline-orchestrator` |
| Idea | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| Evidence | `ccf-literature-searcher`, `ccf-experiment-designer` |
| Manuscript | `ccf-paper-writer` |
| Review | `ccf-paper-reviewer` |
| Audit | `ccf-integrity-auditor` |
| Submission | `ccf-submission-checker` |
| Post-review | `ccf-rebuttal-writer` |
| Governance | `ccf-common`, `ccf-skill-forger` |

## Relationship Model

```text
project -> planning -> idea -> literature -> experiments
        -> writing -> review -> integrity audit -> submission
        -> rebuttal / revision / resubmission
```

The family is deliberately not one giant all-purpose skill. It is also no longer a large pile of tiny helpers. Each owner can run multiple modes:

- `ccf-paper-writer`: drafting, polishing, compression, paper-derived presentation.
- `ccf-paper-reviewer`: scientific review, writing review, format-facing critique.
- `ccf-integrity-auditor`: claim audit, numeric audit, citation audit.
- `ccf-experiment-designer`: experiment design, result templates, real-result figures/tables.
- `ccf-submission-checker`: venue format, package check, artifact/reproducibility readiness.
- `ccf-rebuttal-writer`: rebuttal, revision ledger, response letter, resubmission plan.
- `ccf-skill-forger`: skill maintenance, docs, generated SVG diagrams, release validation.

## Venue Branch

Venue knowledge remains reference-only:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`

Use `ccf-paper-writer` for venue-aware manuscript text. Use `ccf-submission-checker` for venue compliance, template, page limit, anonymity, camera-ready, and submission package questions.

## Source Of Truth

`SKILL.md` is authoritative. Audit indexes:

- `docs/SKILLS_CATALOG.md`
- `docs/NAMING_AND_MERGE_AUDIT.md`
- `ccf-common/references/routing.md`
- `ccf-common/references/skill-trigger-registry.yaml`
