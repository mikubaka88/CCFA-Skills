<div align="center">

# CCFA Skills

### A governed `ccf-*` skill family for CCF research paper projects.

<p>
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

CCFA Skills is a local Codex skill family for building, auditing, submitting, revising, and presenting CCF-style research papers. v0.4.0 upgrades the repository from a writing-oriented skill set into a project workflow family with routing governance, artifact contracts, venue-guide integration, validation, plugin manifests, and release-ready documentation.

The design is informed by ARS, nature-skills, and ARIS, but CCFA keeps a stricter separation of responsibilities: idea optimization is not paper review, citation audit is not literature search, venue-format lookup is not writing, and submission checking is not content polishing.

![Architecture](assets/ccfa-skills-architecture.svg)

## Install

Manual install remains supported:

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
cp -r CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

For an existing checkout:

```bash
git pull origin main
cp -r ccf-* "$CODEX_HOME/skills/"
```

Plugin manifests are available at `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` for clients that support plugin installation. Manual copying is kept because it makes local skill visibility and updates explicit.

## v0.4 Architecture

| Layer | Purpose | Main files |
| --- | --- | --- |
| Governance | Routing, trigger registry, privacy/evidence policy, source registry, artifact ownership, validation. | `ccf-common/`, `docs/SKILLS_CATALOG.md`, `AGENT_GUIDE.md` |
| Project state | Create and maintain paper-project structure and `ccfa.yaml`. | `ccf-paper-project-scaffold`, `ccf-pipeline-orchestrator` |
| Research pipeline | Idea, literature, experiment, writing, compression, review, rebuttal, resubmission, and talk workflows. | `ccf-*` skills |
| Venue branch | Conference LaTeX, template, page-limit, anonymity, and camera-ready notes. | `ccf-conference-guides`, `ccf-writing-skills/references/venue-guides/` |
| Release checks | Prefix, frontmatter, shared controls, registry, venue index, SVG, source, and path privacy checks. | `.github/workflows/validate.yml`, `ccf-common/scripts/` |

## Core Chain

```text
ccf-brainstorming
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-search
  -> ccf-experiment-designer
  -> ccf-writing-skills
  -> ccf-paper-compressor
  -> ccf-conference-reviewer
  -> ccf-conference-writing-reviewer
  -> ccf-conference-paper-rebuttal
```

v0.4 adds:

```text
ccf-pipeline-orchestrator
ccf-paper-project-scaffold
ccf-integrity-auditor
ccf-citation-auditor
ccf-submission-checker
ccf-figure-table-builder
ccf-artifact-reproducibility
ccf-revision-ledger
ccf-resubmission-adapter
ccf-paper-talk
ccf-conference-guides
ccf-forge-skills
```

See `docs/SKILLS_CATALOG.md` for the full trigger catalog, exclusion boundaries, and linked skills.

## Venue Branch

`ccf-conference-skills/<venue>/SKILL.md` is no longer an installable runtime layer. Its 109 venue guides were migrated into:

```text
ccf-writing-skills/references/venue-guides/index.md
ccf-writing-skills/references/venue-guides/<venue>.md
```

Use `ccf-conference-guides` for format-only questions such as:

- CVPR page limit
- NeurIPS LaTeX template
- SIGMOD anonymity mode
- camera-ready checklist
- supplementary material rules

Use `ccf-writing-skills` for manuscript content, `ccf-conference-writing-reviewer` for writing/format review, and `ccf-submission-checker` for build/package compliance. Final venue policy must still be verified against the current official venue page.

![Workflow](assets/ccfa-skills-workflow.svg)

## `ccfa.yaml`

v0.4 introduces a shared project-state contract. The fixed top-level fields are:

```text
version
project
target_venue
stage
artifacts
claims
experiments
reviews
revision_ledger
submission_checks
```

`ccf-paper-project-scaffold` creates the file, `ccf-pipeline-orchestrator` may update project stage and gates, and other skills read it or propose updates according to `ccf-common/references/artifact-contracts.md`.

## Validation

Run local checks before release:

```bash
python ccf-common/scripts/check_v04.py
python ccf-common/scripts/check_path_privacy.py .
python ccf-common/scripts/check_sources.py
rg -nP "^name: (?!ccf-)" -g "SKILL.md"
```

GitHub Actions runs the same structural checks on push and pull request.

![Review Boundaries](assets/ccfa-skills-review-boundaries.svg)

## Compatibility

- All installable skill names now use the `ccf-` prefix.
- `forge-skills` was renamed to `ccf-forge-skills`.
- Core research-chain names are preserved.
- Legacy venue runtime skills were removed; use `ccf-conference-guides` and the venue-guide reference branch.
- `SKILL.md` is authoritative. If docs, catalog, or routing files conflict with a skill body, patch the index files.
