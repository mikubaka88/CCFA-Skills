<p align="center">
  <a href="https://trendshift.io/repositories/151023?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-151023" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/151023/daily?language=TeX" alt="mikubaka88%2FCCFA-Skills | Trendshift" width="250" height="55"/></a> <a href="https://trendshift.io/repositories/151023?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-151023" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/151023/weekly?language=TeX" alt="mikubaka88%2FCCFA-Skills | Trendshift" width="250" height="55"/></a>
</p>

<div align="center">

<h1>CCFA-Skills</h1>

**A skill family for shaping the research storyline of CCF-A papers.**

[Simplified Chinese](README.md) · [English](README.en.md) · [Traditional Chinese](README.zh-TW.md)

**[Latest updates · v0.11.0](#latest-updates)**

<img src="assets/ccfaskills.png" alt="CCFA-Skills logo" width="560">

---

*“The structure of the prose becomes the structure of the scientific argument.”*<br>
George D. Gopen and Judith A. Swan, [*The Science of Scientific Writing*](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html)

*“The very process of science is centered around communication.”*<br>
Yann LeCun and James M. Manyika, [*Learning Abstractions*](https://www.amacad.org/publication/daedalus/learning-abstractions-conversation-yann-lecun)

</div>

## Table of contents

- [Quick start](#quick-start)
- [Why a family of skills](#why-a-family-of-skills)
- [The family and its 17 core skills](#the-family)
- [Day and night controls](#day-and-night-controls)
- [From idea to submission](#from-idea-to-submission)
- [Visual examples](#visual-examples)
- [Keeping the writing natural](#keeping-the-writing-natural)
- [Figures that remain editable](#figures-that-remain-editable)
- [Distinct roles, shared story](#distinct-roles-shared-story)
- [Repository and maintenance](#repository)
- [Latest updates](#latest-updates)
- [Star history](#star-history)

At two in the morning, the experiment finally finishes. The new result is better than expected, yet reopening the manuscript reveals the harder problem. The sharp question that began the project is buried beneath related work. The method section no longer quite matches the mechanism in the code. A new experiment answers the previous review, but pulls the argument in another direction. Every part seems to have improved, while the paper as a whole has become less clear.

Many promising projects are weakened not by a poor idea, but by what happens to that idea over time. Literature accumulates, result tables expand, and the author repeatedly switches between researcher, writer, and reviewer. The original insight gradually disappears beneath local revisions. One long prompt cannot reliably preserve all these relationships because retrieval must remain faithful to sources, experiments to protocols, writing to the argument, and review to independent judgment.

CCFA-Skills grew from this problem. We treat a paper as a research storyline that must remain coherent while it changes, not as a document waiting to be filled. Seventeen specialized skills accompany the work from idea, literature, and experiments to writing, visualization, review, rebuttal, and submission. As the work passes between them, the link between question, evidence, and conclusion remains intact, so the paper can evolve without forgetting why it deserved to be written.

<p align="center">
  <img src="assets/ccfa-skills-hero.svg" alt="CCFA-Skills family overview" width="100%">
</p>

## Quick start

Choose the agent you use:

[Codex](docs/getting-started/CODEX.md) · [Claude Code](docs/getting-started/CLAUDE_CODE.md) · [Cursor](docs/getting-started/CURSOR.md) · [Gemini CLI](docs/getting-started/GEMINI_CLI.md) · [Other agents](docs/getting-started/OTHER_AGENTS.md) · [Automatic updates](docs/getting-started/AUTO_UPDATE.md)

One-line installation for Codex:

```powershell
npx skills add mikubaka88/CCFA-Skills --global --agent codex --skill '*' --yes --copy
```

Then describe the research problem in ordinary language:

```text
Review and rank these three ideas, and identify the most likely rejection reason for each.
Find recent work, benchmarks, and published baselines for temporal visual reasoning.
Design the main experiments, ablations, and robustness evidence for this paper without inventing results.
Rewrite the method section in a CVPR style while preserving equations, terminology, and citations.
Draw the method architecture, create an aesthetic draft first, and then ask whether to rebuild it as PPTX.
```

## Why a family of skills

The difficulties of paper research are connected, but they do not require the same kind of reasoning.

| What researchers encounter | How CCFA-Skills responds |
|---|---|
| Retrieval, experiments, writing, and review compete inside one conversation | The skill best suited to the current question leads; adjacent capabilities join only when useful |
| Literature facts, experimental values, and manuscript claims drift apart | Sources, experiment design, and whole-paper consistency remain distinct responsibilities |
| A revision begins to sound like a review response full of caveats and internal status language | Writing forms the argument; Humanization restores direct and natural academic prose |
| Each review round changes its focus, obscuring whether the manuscript actually improved | Current publication readiness and progress over the previous version are considered separately |
| Architecture figures are either plain box diagrams or attractive but impossible to edit | A content-aware visual draft comes first, followed by optional SVG, PDF, or PPTX reconstruction |
| More installed skills create more noise instead of better work | Only capabilities relevant to the present question enter the conversation |

## What we value

- **The research question comes before the tool.** Judging an idea is different from developing it. Designing evidence is different from drawing a figure. Each step remains centered on the question it must answer.
- **Evidence keeps its provenance.** Literature, protocols, values, claims, figures, and citations do not collapse into plausible prose. A missing fact stays missing until it is found or verified.
- **A paper should sound academic, not defensive.** Humanization removes ritual caveats, mechanical enumeration, excessive em dashes, and internal process language while preserving material limitations and disclosures.
- **Review remains independent from revision.** The Reviewer judges; the Writer revises. Diagnosis comes before repair, so the manuscript does not argue with its own evaluation.
- **Scientific figures should explain and invite attention.** Quantitative plots remain reproducible. Method figures first explore a visual language suited to their content, then become editable when the user chooses.
- **Exemplars provide direction rather than a template.** When users supply target papers, CCFA learns their narrative rhythm, paragraph roles, and evidence organization without copying sentences or forcing one style onto every project.

## The family

![CCFA-Skills family architecture](assets/ccfa-skills-architecture.svg)

Every CCFA task activates `ccf-humanization` first, then `ccf-common`, before the specialist, including retrieval, review, visuals, experiments, and maintenance. Humanization keeps communication direct and evidence-faithful; Common applies scope, collaboration, evidence, and file rules. Reuse active rules across contributors and refresh only changed or missing context. Detailed rewriting and experiment checks depend on the actual task, without duplicate preflight reports. Specialists retain ownership and integrate necessary contributions.

### The 17 core skills

| Research moment | Skill | What it contributes |
|---|---|---|
| Family coordination | `ccf-common` | Understands requests, coordinates responsibilities, and protects evidence and privacy boundaries |
| Project direction | `ccf-pipeline-orchestrator` | Clarifies goals, stages, decisive milestones, and the next move |
| Project beginning | `ccf-project-scaffolder` | Prepares the paper workspace, templates, and research-material structure |
| Idea judgment | `ccf-idea-reviewer` | Judges idea value, novelty, and mechanism; excludes experiments by default |
| Idea development | `ccf-idea-optimizer` | Turns a rough direction into a problem, insight, method, and evidence path |
| Literature search | `ccf-literature-searcher` | Finds related work, datasets, benchmarks, and published baselines |
| Frontier tracking | `ccf-literature-monitor` | Watches new papers, nearby work, and changes in the field |
| Experiment design | `ccf-experiment-designer` | Designs main comparisons, ablations, robustness studies, and result structures |
| Integrity | `ccf-integrity-auditor` | Checks claims, values, terminology, figures, and citations together |
| Paper review | `ccf-paper-reviewer` | Provides independent scientific review, version comparison, and readiness judgment |
| Paper writing | `ccf-paper-writer` | Drafts, rewrites, polishes, and compresses manuscript text |
| Academic voice | `ccf-humanization` | Removes defensive and mechanical prose without weakening rigor |
| Author response | `ccf-rebuttal-writer` | Organizes rebuttals, response letters, and revision records |
| Scientific visuals | `ccf-visual-composer` | Creates plots, visual tables, method figures, and editable versions |
| Submission | `ccf-submission-checker` | Checks templates, page limits, anonymity, PDFs, and supplementary material |
| Exemplar learning | `ccf-paper-to-exemplar` | Distills controllable writing patterns from papers supplied by the user |
| Family maintenance | `ccf-skill-forger` | Improves skills, resolves conflicts, and validates releases |

The complete responsibility map:

![Skill catalog by responsibility](assets/ccfa-skills-catalog.svg)

## Day and night controls

When you are tightening an abstract, you may want a quick edit. Three days before submission, you may be happy to wait for another assistant to check the key conclusions. The day and night configurator lets you make those choices and remembers them for later.

![The CCFA-Skills local configurator](assets/configurator-preview.png)

*The actual local configuration page. Adjust the options in your browser, then click “Save preferences” to apply them.*

Start with **Light**, **Balanced**, or **Deep**, then adjust any of the seven enhancements. The page supports Simplified Chinese, Traditional Chinese, and English, with light, dark, and system themes. **☾ Off** skips unrequested extra work, **☀ On** adds the enhancement to relevant tasks, and **Auto** enables it when a specific need arises. Each card explains what the extra work involves and why it may use more tokens or take longer.

From the repository root, run this command with Python 3.10+; no extra dependencies are needed:

```bash
python ccf-common/scripts/preferences.py serve
```

Your browser will open the local configurator. These three examples are useful starting points. Choose a preset, adjust it to suit your work, and save:

| What you are working on | Settings to try | Where the extra effort goes |
|---|---|---|
| **Everyday editing:** clarify an abstract or shorten a method paragraph | Choose **Light**, which turns all seven optional enhancements off | Focus on the requested edit, with fewer unrequested second reviews, figure alternatives, and process reports |
| **Before submission:** check for gaps in key conclusions or citations | Start with **Balanced** and enable **Independent second review**. Enable **Additional process reports** if you need a handoff record | Another pass over relevant evidence and, when selected, a written record. Both add tokens and waiting time. Independent review requires a host that supports actual independent execution |
| **Exploring an idea:** test whether a selected direction has a better underlying mechanism | Start with **Balanced**, set **Alternative route comparison** to **Auto**, and leave **Broader supplementary search** on **Auto** | Add one alternative when an unresolved choice is worth comparing, with further search focused on a specific evidence gap |

**Deep** suits stages where you want to invest more in relevant tasks. It enables independent review, broader search, extra figure candidates, and process reports, with the other three enhancements on Auto. You can start there and turn off anything you do not need. Actual usage depends on your material, model, and tools, so the page explains likely costs without promising fixed savings.

To give a paper its own settings, start the configurator with its directory. Replace the example path with yours:

```bash
python ccf-common/scripts/preferences.py serve --project "path/to/paper"
```

Choose **Personal defaults** or **This project** before saving. Personal defaults carry into future tasks. Explicit project settings take priority, while unset options continue to inherit. You might keep everyday work light and enable independent review only for a paper nearing submission. Preferences live outside installed skill folders and survive skill updates.

**These switches control additional effort only.** Even with Light selected, an explicitly requested full review, several research directions, and necessary verification still happen. The Humanization → Common preflight always applies. Opening the page does not call a model or start a research task.

<details>
<summary>Configuration files and offline use</summary>

Personal preferences live at `$CODEX_HOME/ccfa/preferences.json`, or `~/.codex/ccfa/preferences.json` if `CODEX_HOME` is unset. Project settings live at `.ccfa/preferences.json` inside the paper directory. An installed copy can run its own `ccf-common/scripts/preferences.py`. Add `--no-browser` to print the local launch URL without opening a browser.

After downloading the repository, you can also open the [static configuration page](ccf-common/assets/configurator/index.html) to import, edit, and export JSON. That page exports a file only. Rename the export to `preferences.json` and place it in the appropriate directory above to apply it. See the [preference contract](ccf-common/references/preferences.md) for details.

</details>

## From idea to submission

![Default research journey](assets/ccfa-skills-workflow.svg)

This is not a pipeline that everyone must enter at the beginning. You may arrive with a half-formed idea, a result table that resists interpretation, a method reviewers repeatedly misunderstand, or a PDF that is nearly ready to submit. CCFA-Skills begins where you are and brings in only the help that matters there.

## Visual examples

These are research visuals rather than release-announcement graphics. Each figure uses a visual language suited to its reading context.

### Paper method architecture

The figure below extracts the computational relationships from `output/DynTrace.pdf` and uses a layered layout to explain the mechanism and information flow. Inputs and visual processing sit at the bottom, geometry-grounded evidence and the DTV/DTG branches form the middle, and token integration, the MLLM, and the answer appear at the top. Connections follow computational dependencies so readers can trace the complete method.

![Paper method architecture](assets/visual-showcase/dyntrace-paper-mechanism-llava4d-reference.png)

**How it was made:** The DynTrace paper was distilled into mechanism relationships and representation–operation pairs. GPT Image 2 then generated a layered architecture draft, followed by a check that the method remained complete. The displayed artifact is a PNG visual draft; after composition approval, it can be rebuilt as semantic SVG, vector PDF, or native-object PPTX.

<details>
<summary>Reference figure, source, and composition principles</summary>

![LLaVA-4D Figure 2 reference](assets/visual-showcase/references/llava-4d-figure-2-iclr-2026.png)

Reference: Hanyu Zhou and Gim Hee Lee, [*LLaVA-4D: Embedding SpatioTemporal Prompt into LMMs for 4D Scene Understanding*](https://arxiv.org/abs/2505.12253), Figure 2; see also the [OpenReview page](https://openreview.net/forum?id=URpbmVEsqB). The screenshot is included only for non-commercial study of academic composition and visual style. Copyright remains with the authors; please contact the maintainer for removal if it raises any rights concern.

- A paper figure should make its inputs, representations, operations, branches, integration, and output easy to follow.
- Video frames, optical flow, masks, 3D trajectories, DT-Tokens, and the temporal graph carry method meaning rather than decoration.
- Ordinary English uses natural capitalization; Qwen3-VL, WAFT, SAM3, DTV, DTG, MLLM, 3D, and 4D retain their canonical forms.

</details>

### PPT/Poster

The two earlier visual explorations remain below. They are better suited to slides, project posters, and README overviews, so they are not presented as top-conference method figures.

#### GPT Image 2 concept draft

![GPT Image 2 concept draft](assets/visual-showcase/dyntrace-method-architecture-gpt-image-2.png)

**How it was made:** The three-stage DynTrace method was translated into a vivid visual story built around video, trajectories, and graph structure, then explored with GPT Image 2.

#### Reference-guided PPT/Poster

![Reference-guided PPT/Poster](assets/visual-showcase/dyntrace-ppt-poster-reference-driven.png)

**How it was made:** Reference composition principles were added to the three-stage content so that headings, color fields, and visual anchors would read naturally in a presentation or poster.

### Data-analysis figures

The following figures come from reproducible `ccf-visual-composer` drawing recipes. Their values demonstrate visual forms and are not reported paper findings.

| Composite figure | Heatmap |
|---|---|
| ![Composite figure](assets/visual-showcase/showcase-13-composite-analysis-dashboard.svg) | ![Heatmap](assets/visual-showcase/showcase-03-evidence-coverage-heatmap.svg) |
| **Volcano plot** | **Bar chart** |
| ![Volcano plot](assets/visual-showcase/showcase-11-volcano-candidate-screen.svg) | ![Bar chart](assets/visual-showcase/showcase-10-grouped-benchmark-bars.svg) |
| **Slopegraph** | **Radial chart** |
| ![Slopegraph](assets/visual-showcase/showcase-02-revision-lift-slopegraph.svg) | ![Radial chart](assets/visual-showcase/showcase-06-readiness-radial-scorecard.svg) |

More examples are available in [`assets/visual-showcase/`](assets/visual-showcase/).

## Keeping the writing natural

`ccf-paper-writer` can learn from exemplars chosen by the user. It studies how an effective paper frames its problem, unfolds its method, arranges evidence, and controls pace. It does not copy source sentences or turn one paper into a template for every field.

`ccf-humanization` checks what scientific information each sentence contributes: state supported facts directly, qualify genuine uncertainty accurately, and delete empty defenses. It removes imagined reviewer objections, apologies for the contribution, repeated caveats, ritual endings, and internal status narration. Paragraphs do not need an appended limitation or future-work sentence. Observed failures, scope conditions, reproducibility details, and required disclosures remain visible; only concrete unresolved scientific decisions need a separate warning.

Route by the requested judgment: “Is this direction worth pursuing?” uses `ccf-idea-reviewer` without needing an explicit score request; “Does this manuscript support its conclusions?” uses `ccf-paper-reviewer`. A full PDF can still receive concept-only review. Idea ratings cover problem value, novelty, insight, mechanism, elegance, and audience fit; experiments are assessed separately only when requested.

Structured review reports use detailed output by default and brief output on explicit request. Manuscript reports develop contributions, strengths, concerns, prior art, method and evidence, reviewer perspectives, ratings, and action priorities. Idea reports develop problem value, novelty, mechanism logic, and development advice; experiments are outside their default scope. Findings carry specific evidence locations and stable IDs for revision tracking. Percentile ranks require a real comparable corpus. See the [manuscript report format](ccf-paper-reviewer/references/fixed-output-format.md) and [idea-review protocol](ccf-idea-reviewer/references/strict-idea-review.md).

Full manuscript reviews keep 14 ordered sections, writing reviews keep 9, and explicitly requested brief reports use 5 blocks. The generic scientific scorecard has seven criteria: novelty, soundness, evidence, significance, clarity, reproducibility, and ethics/limitations. Evidence expectations follow contribution type; confidence and source coverage are separate. Markdown reports can be checked directly for section order, rating fields, and concern-ID references. Explicit venue or user formats retain priority.

Manuscript re-review answers two different questions:

![Review and revision scoring](assets/ccfa-skills-review-boundaries.svg)

- **Is the current manuscript ready for its target venue?** This measures the remaining distance to the publication standard.
- **Did the revision make genuine progress?** This compares what the new version resolved and what new problems it may have introduced.

## Figures that remain editable

![Visual delivery](assets/ccfa-skills-artifacts.svg)

Quantitative figures begin with reproducible code and traceable data. Method, system, and architecture figures usually begin with GPT Image 2 exploring a visual language that suits the content. Requested editable SVG, vector PDF, or PPTX deliverables continue under the existing authorization; additional formats can be offered when useful. Existing editable figures are revised in their authoring source, with only affected exports rebuilt; local text, color, spacing, value, or format changes do not restart image generation. Common concepts use a coherent open-source icon family, while method-specific scientific objects can be drawn together in the initial draft and isolated as assets when reuse or editing requires it. In PPTX, text, boxes, nodes, and connectors remain native objects wherever possible, so the final figure can still be meaningfully revised.

Figure aspect ratio follows the content and paper placement, with no default square. Allocate space to the main mechanism before placing compact modules, illustrations, and connectors. Align peer edges, text baselines, and ports across groups, and inspect unused regions. Set a consistent type scale at final paper width: Times New Roman by default, or Comic Sans MS for a requested comic treatment. Keep essential scientific labels while removing repeated explanation and ornamental numbers.

Five coordinated presets cover formal mechanisms, soft mechanisms, visual evidence, geometric flows, and compact comic illustrations, alongside seven additional palettes. Venue context helps select a preset; actual template requirements take precedence. These are design suggestions, not official conference styles. Each preset coordinates type, strokes, grouping, and color, while each reference has a specific region or property to guide. Pixel gaps are generation targets; requested editable outputs enforce live fonts and coordinates. Local edits check attached connectors and protected regions, with current artifacts organized per figure.

When a user does not want GPT Image 2 or explicitly prefers code-first drawing, `ccf-visual-composer` uses a pure-SVG route and labels it clearly.

## Distinct roles, shared story

![Skill collaboration boundaries](assets/ccfa-skills-routing.svg)

Each artifact has an owner responsible for integration and delivery. Other skills contribute according to prerequisites and quality needs; role boundaries support necessary collaboration:

| Your request | Responsible skill | What it deliberately avoids |
|---|---|---|
| Is this idea worthwhile, novel, or coherent? Score or compare ideas | `ccf-idea-reviewer` | Concept review by default; missing experiments do not lower its score |
| Develop one rough idea | `ccf-idea-optimizer` | Does not make ranking its primary goal |
| Find benchmarks and published results | `ccf-literature-searcher` | Does not invent an experiment conclusion |
| Choose baselines, metrics, and ablations | `ccf-experiment-designer` | Does not alter or fabricate results |
| Review, score, and diagnose | `ccf-paper-reviewer` | Does not rewrite the manuscript while judging it |
| Rewrite, polish, and compress | `ccf-paper-writer` | Does not change the scientific problem, method, or conclusion without authorization |
| Draw figures, tables, and PPTX | `ccf-visual-composer` | Does not choose datasets, metrics, or values |

## Repository

```text
CCFA-Skills/
├── ccf-common/                 # Shared family guidance
├── ccf-*/SKILL.md              # Entry points for 17 skills
├── ccf-*/references/           # References read when needed
├── ccf-*/scripts/              # Reproducible operations
├── assets/                     # README visuals and figure examples
├── evaluation/                 # Regression and ablation results
├── tools/build_ccfa_diagrams.py
└── 实验结果.md
```

Longer guidance lives in `references/`, while repeatable work belongs in `scripts/`. Iterative artifacts keep stable names so that a new version replaces the previous one instead of leaving behind a trail of indistinguishable attempts.

Work backward from the result to its prerequisites: closest-work evidence before novelty judgments, claims and citation support before substantive writing, and data semantics/topology before scientific rendering. Use the relevant skills to resolve missing, conflicting, or stale evidence; reuse valid checks. Verify affected arguments after substantial revisions and integrate fixes before delivery. Concept review still does not require completed experiments. Internal contributions return focused findings; requested reviews retain their fixed templates and full scoped coverage. Save tokens on repeated retrieval, duplicate reports, irrelevant references, and repeated intake, while completing necessary groundwork. See [cooperation routes](ccf-common/references/routing.md) and [handoff rules](ccf-common/references/handoff-modes.md).

The file contract leads all 17 skill entrypoints. Explicit paths, this artifact's existing mappings, and established task folders take priority. New tasks use a dedicated project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, outside generic `output/` folders. Examples include `figures/method-overview/`, `reviews/paper-short-title/`, and `literature/retrieval-memory/`. If the name belongs to unrelated material, use a stable `ccfa-workfiles-<project-id>/` rather than merging or overwriting contents.

Create `source/` (reusable authoring files), `assets/` (reference/icon assets), `cache/` (downloads/extractions), and `build/` (current previews/logs) only when needed. Skills working on the same artifact share its directory and update current files. Avoid ambiguous new names such as `temp`, `misc`, or `final-final`. Remove only verified disposable files created by the task; retain original evidence, editable sources, requested outputs, and necessary comparison baselines. Failed builds preserve usable results. Existing folders are not migrated to adopt the new default; see the [artifact contract](ccf-common/references/artifact-contracts.md).

Chinese output uses explicit UTF-8 I/O with optional BOM support on input. Shell pipes, Unicode filenames, and glyph coverage are checked separately. Family validation includes Chinese and uncommon-character regressions and reports decoding errors rather than masking them with replacement characters. Figures retain the chosen Latin font and use an available CJK fallback.

<a id="latest-updates"></a>

## Latest updates: keep long projects on course and give good ideas room to grow

**v0.11.0 · 2026-10-15**

You are a few weeks into a research project. The conversation keeps growing, and the assistant keeps answering, but it gradually loses sight of why you started. You bring in more assistants, only to find that they have read the same papers and returned similar answers. A paragraph finally looks polished, yet its argument is still hard to follow.

This update grew out of those moments. We want CCFA-Skills to help researchers carry work through: remember the important decisions, build on what is already done, and leave room for ideas worth trying. That gives you more time to judge whether the question matters, whether the evidence is convincing, and whether the next step is worth taking.

### Resilience: remember the purpose as the conversation grows

Suppose your original request was to find a promising research direction within your current compute budget. Several rounds later, the assistant has added modules and experiments until the plan is beyond your resources. Each step has an explanation, but together they have taken the work away from your goal.

Long tasks can now keep a short record of your goal, important constraints, current approach, and next action. When changing direction, accepting another assistant's work, or recovering context, the assistant checks that record. If an answer goes off course, it returns to actual files and evidence, preserves sound work, and resumes with a small step that can be checked. New evidence can still justify a change of direction, with a clear explanation of why.

This is our practical approach to degraded or inconsistent model behavior: make goals harder to lose and errors harder to carry forward. The [continuity rules](ccf-common/references/continuity.md) describe how it works.

### Multiple agents: give each assistant a useful question to answer

When exploring a direction, assistants can first develop mechanisms independently and then exchange relevant evidence. When checking a paper, one can verify citations while another examines numbers and conclusions, with one person or agent responsible for bringing the findings back into the manuscript. Each contributor has a concrete question and returns sources that can be checked.

This release makes that division of work explicit. Independent tasks can run in parallel, while closely connected arguments keep one author responsible for coherence. Shared files have a clear owner, and findings from an older version are checked before reuse. Hosts that support multiple agents can use these rules to coordinate the work and integrate results once the evidence is sufficient. See [task modes](ccf-common/references/task-modes.md) and [handoffs](ccf-common/references/handoff-modes.md).

### Personal preferences: spend time on what matters to you now

The same researcher needs different help at different stages. A sentence edit should be straightforward. An unexplained result may deserve a few more papers. Before submission, an independent look at the central claims may be worth the wait.

The [day and night configurator](#day-and-night-controls) makes those preferences visible, adjustable, and reusable. Keep a light default for daily work and add review or retrieval for a particular paper. Each of the seven enhancements explains what it adds and how it may affect tokens and time. The page supports three languages and light and dark themes. The examples above show settings for everyday editing, submission checks, and idea exploration.

### Ideas and writing: make each revision move the substance forward

A new module should explain what it changes and what would be lost without it. Ideas shown to be unworkable can be dropped, while promising hypotheses can first be distinguished through theory, counterexamples, or observations. We removed conflicting instructions that forced another rescue attempt or repeated scoring, giving exploration room to move beyond small variations while keeping a chosen direction steady.

Writing starts with the paragraph's point. It checks whether one sentence gives a reason, evidence, or an inference for the next, then improves order and wording. This release adds diagnostics for English and Chinese semicolons and clusters of `rather than`, helping locate passages where the argument may be hard to follow. Necessary scientific comparisons and limitations stay intact. See [idea development](ccf-idea-optimizer/SKILL.md), [prose guidance](ccf-paper-writer/references/prose-quality-guardrails.md), and [Humanization](ccf-humanization/SKILL.md).

### Files and context: pick up where you left off

After editing a figure or moving to another skill, you should still be able to find its source and current result. Skills now share clearly named working directories, update current files during ordinary revisions, and pass along the locations of relevant evidence. Original material, editable sources, and useful validation records are retained. Disposable files are cleaned up within the task that created them. Detailed instructions load when needed, reducing repeated copies of the entire history. See [Repository](#repository) for directory examples.

The update keeps the 17-skill family and existing review structure, with the relevant structural and scenario checks passing. We hope that the next time you open your project, you can reconnect with the work sooner and save your attention for the questions worth solving.

[Full changelog](CHANGELOG.md) · [Earlier ICLR 2027 adaptation](ccf-paper-writer/references/venue-guides/iclr.md)

## Maintenance and validation

```powershell
python ccf-common\scripts\check_v04.py
python ccf-common\scripts\check_path_privacy.py
python ccf-common\scripts\check_markdown_links.py
python ccf-common\scripts\check_sources.py
python ccf-common\scripts\test_preferences.py
python ccf-common\scripts\test_continuity.py
node --check ccf-common/assets/configurator/app.js
node ccf-common/scripts/test_configurator.js
```

These checks validate the static structure of all 17 skills, configuration and reference paths, and existing script regressions. They do not replace comparisons of actual model quality or token use. Experiment and efficiency results are summarized in [实验结果.md](实验结果.md).

`0.11.0` has passed structural and scenario checks. Performance gains under actual model degradation still need validation, and the linked historical experiments do not measure token or quality gains for current models.

## Commitments

- Never invent experimental results, citations, method components, or venue rules.
- Read only the private manuscript or unpublished material needed for the task.
- Use external retrieval and image generation with user authorization and minimal disclosure.
- Respect the user's decision to disable any skill.
- Explain the rubric, comparison target, evidence, and uncertainty behind every automated score.

## Acknowledgments

Thanks to [Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) for contributing to the open ecosystem of academic-writing skills.

## Star history

[![GitHub Stars](https://img.shields.io/github/stars/mikubaka88/CCFA-Skills?style=flat-square&label=Stars)](https://github.com/mikubaka88/CCFA-Skills/stargazers)

<a href="https://www.star-history.com/?repos=mikubaka88%2FCCFA-Skills&amp;type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mikubaka88/CCFA-Skills&amp;type=Date&amp;theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mikubaka88/CCFA-Skills&amp;type=Date" />
    <img alt="GitHub star history for CCFA-Skills" src="https://api.star-history.com/svg?repos=mikubaka88/CCFA-Skills&amp;type=Date" width="800" />
  </picture>
</a>

The chart updates through Star History and the count badge through Shields.io. Service and GitHub image caches can delay changes; the chart is typically cached for about 24 hours, so it is not a second-by-second live feed. Click the chart for the interactive page.

[View the 2026-08-13 historical snapshot (available offline)](assets/ccfa-skills-star-history.svg)
