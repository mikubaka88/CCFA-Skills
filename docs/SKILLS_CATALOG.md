# CCFA Skills Catalog

This is the public trigger-conflict index for v0.4.0. It lists every installable `ccf-*` skill, its startup condition, exclusion boundary, and expected linkage. If this catalog conflicts with a skill's `SKILL.md`, the `SKILL.md` wins and this catalog should be patched.

| Skill | Startup condition | Do not use for | Linked skills |
| --- | --- | --- | --- |
| `ccf-brainstorming` | Complex research workflow clarification, task decomposition, and skill-routing planning. | Do not optimize ideas, search literature, write, review, or rebut as the primary output. | Most CCFA skills through partial handoff. |
| `ccf-idea-optimizer` | Make rough research directions concrete: problem, method, novelty, and evidence plan. | Do not rank or score ideas as the main job. | ccf-literature-search, ccf-experiment-designer, ccf-writing-skills. |
| `ccf-idea-reviewer` | Strictly score, rank, compare, and triage early research ideas. | Do not polish manuscripts or optimize a single fuzzy idea unless scoring is explicit. | ccf-literature-search, ccf-idea-optimizer. |
| `ccf-literature-search` | Find prior art, related work, datasets, benchmarks, and citation evidence online. | Do not write the paper or audit an already fixed bibliography as the main task. | ccf-idea-optimizer, ccf-idea-reviewer, ccf-experiment-designer, ccf-writing-skills. |
| `ccf-experiment-designer` | Design evaluation protocols, baselines, ablations, metrics, and result table templates. | Do not invent experimental results. | ccf-literature-search, ccf-writing-skills, ccf-figure-table-builder. |
| `ccf-writing-skills` | Plan, draft, revise, polish, and reviewer-proof manuscript text. | Do not change idea scope without confirmation; do not replace full scientific review or rebuttal. | ccf-conference-guides, ccf-paper-compressor, ccf-conference-writing-reviewer, ccf-conference-reviewer. |
| `ccf-paper-compressor` | Reduce paper, section, abstract, related-work, method, or experiment length. | Do not change claims, evidence, results, or limitations. | ccf-writing-skills, ccf-submission-checker. |
| `ccf-conference-reviewer` | Full scientific manuscript review, simulated reviewers, AC/meta-review, scoring, and acceptance-risk diagnosis. | Do not rewrite prose or perform venue-format-only checks. | ccf-writing-skills, ccf-conference-writing-reviewer, ccf-experiment-designer. |
| `ccf-conference-writing-reviewer` | Writing-only review, paragraph logic, consistency, LaTeX/format audit, and presentation risks. | Do not score scientific acceptance as a full reviewer. | ccf-writing-skills, ccf-conference-guides, ccf-submission-checker. |
| `ccf-conference-paper-rebuttal` | Draft rebuttal, author response, response letter, and revision summary after real reviews. | Do not trigger for ordinary manuscript writing. | ccf-revision-ledger, ccf-writing-skills. |
| `ccf-conference-guides` | Query conference LaTeX, template, anonymity, page limit, camera-ready, and venue-format requirements. | Do not write, polish, review, or rebut paper content. | ccf-writing-skills, ccf-conference-writing-reviewer, ccf-submission-checker. |
| `ccf-pipeline-orchestrator` | Coordinate project stages, gates, handoffs, and ccfa.yaml state. | Do not write, review, search, or design experiments itself. | All stage-owning CCFA skills. |
| `ccf-paper-project-scaffold` | Create a paper-project directory, copy templates, and initialize ccfa.yaml. | Do not generate research content. | ccf-pipeline-orchestrator, ccf-writing-skills, ccf-submission-checker. |
| `ccf-integrity-auditor` | Audit claim-support, result-to-claim alignment, numbers, terminology, and evidence consistency. | Do not perform full scientific acceptance review. | ccf-writing-skills, ccf-conference-reviewer, ccf-citation-auditor. |
| `ccf-citation-auditor` | Verify existing citations, BibTeX metadata, existence, and citation-context support. | Do not perform broad literature search for new papers. | ccf-literature-search, ccf-writing-skills. |
| `ccf-submission-checker` | Check LaTeX/PDF build, page limit, anonymity, metadata, fonts, templates, and policy freshness. | Do not polish or rewrite manuscript content. | ccf-conference-guides, ccf-paper-compressor, ccf-writing-skills. |
| `ccf-figure-table-builder` | Generate or audit figures, LaTeX tables, SVG/PDF outputs, and QA from real supplied results. | Do not invent data. | ccf-experiment-designer, ccf-writing-skills, ccf-integrity-auditor. |
| `ccf-artifact-reproducibility` | Prepare artifact checklist, code/data/model release plan, seed/env notes, and reproducibility appendix. | Do not claim reproducibility without evidence. | ccf-experiment-designer, ccf-submission-checker, ccf-writing-skills. |
| `ccf-revision-ledger` | Maintain reviewer-comment to action to manuscript-location to status tracking. | Do not replace rebuttal wording. | ccf-conference-paper-rebuttal, ccf-writing-skills. |
| `ccf-resubmission-adapter` | Adapt an existing manuscript to a new venue under conservative default constraints. | Do not add experiments or edit bibliography unless authorized. | ccf-conference-guides, ccf-writing-skills, ccf-submission-checker. |
| `ccf-paper-talk` | Convert a paper into slides, poster, talk script, Q&A, or presentation plan. | Do not perform pre-submission scientific review. | ccf-writing-skills. |
| `ccf-common` | Shared routing, handoff, task modes, source registry, privacy/evidence, and artifact governance. | Not an ordinary research task skill. | All CCFA skills. |
| `ccf-forge-skills` | Create, update, validate, or audit CCFA/Codex skills and shared controls. | Do not perform research writing or review work. | ccf-common. |

## Venue Guide Rule

The 109 legacy venue runtime skills were migrated into `ccf-writing-skills/references/venue-guides/`. Use `ccf-conference-guides` for format-only questions and `ccf-writing-skills` for manuscript text.
