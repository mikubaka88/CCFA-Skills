# Writing Execution

Use the local execution helper for a substantial manuscript revision, a long session that needs reliable continuation, or contributions from several agents. A self-contained paragraph edit keeps the ordinary direct-edit route; do not create a packet, ledger, or review call merely to polish a sentence.

The helper prepares context and applies checked edits. It does not call a model, search the web, establish scientific truth, or replace Humanization, Common, the writer, the reviewer, or the integrity auditor. Existing permissions, preferences and source-verification rules still apply. `ccfa.yaml` and personal preference formats are unchanged.

For the optional red `results_pending_draft` control, `prepare` reads user preferences and any explicit `--project` overrides without writes. Pass `--results-pending on|off` to reuse Common's already resolved value or a current task choice. `on` injects conditional-draft and mandatory alignment instructions into draft/results/consistency guidance; it does not change context selection, budgets, or source trimming. A results-pending packet remains an editing/review aid, not a completed alignment check. Ordinary complete-paper requests do not imply permission for anticipated analysis.

## Prepare Only The Material Needed

Start with the current manuscript and its established paths. Inspect its actual section IDs before choosing a target:

```bash
python ccf-paper-writer/scripts/writing_runtime.py inspect --manuscript path/to/paper.md
python ccf-paper-writer/scripts/writing_runtime.py prepare --manuscript path/to/paper.md --target SECTION_ID --mode draft
```

The default output goes to stdout. When another contributor or a later session needs the same packet, save one current copy under the established task directory, for example `ccfa-workfiles/writing/paper-short-title/build/writing-packet.json`. Reuse that path instead of creating a packet per agent or iteration. Preparation does not modify the manuscript.

The inventory supports local Markdown and literal LaTeX headings. Each section stops at the next heading of any level; select the actual subsection IDs as well when revising a chapter group. LaTeX macros and `\input` files are not expanded: inspect the actual included files rather than assuming they were read. Binary documents retain their existing document/PDF workflow.

For a substantial rewrite, recover the target's scientific message and the whole-paper relationship from the supplied research and current text. A compact brief can carry them:

```json
{
  "message": "Explain how the representation retains distinctions needed by the downstream task.",
  "throughline": "The paper connects the lost distinction, the representation change, and the observed task behavior."
}
```

Pass the existing brief with `--brief path/to/brief.json`; do not ask the user to fill in a new form when these facts are already available. Optional terminology and protected literals guide the writer in preserving names and facts; they are not automatic lexical locks. Do not invent a throughline to make a weak or incomplete scientific argument appear complete. Section titles alone are a navigation map, not a recovered whole-paper argument.

Use `--sources path/to/sources.json` for selected local source excerpts. Each declaration identifies its path, role and target use, with optional line bounds. Keep factual support distinct from writing exemplars: an exemplar can guide explanation or language without supplying the current paper's scientific claims. Substantive drafting continues to reuse matched originals and search for additional well-written originals under the existing writing preference. This helper does not replace that retrieval or make every selected text a verified source.

The source list is a JSON array. Paths are relative to that list's directory. Use UTF-8 text sources such as actual results, extracted paper passages, SVG or plotting code; do not pass binary PDFs/images as text. For example, after inspecting the real files and section IDs:

```json
[
  {"id": "main-results", "path": "results.csv", "kind": "measurement", "used_by": ["results", "figure:main"]},
  {"id": "related-passage", "path": "paper-excerpt.md", "kind": "exemplar", "used_by": ["related-work"], "start_line": 3, "end_line": 8}
]
```

Bounds must identify actual lines, not the illustrative values above. Include both the section and figure/table IDs when the same data support them; the helper does not infer those relationships. Multiple windows from the same file can use distinct source IDs. An undeclared relationship is unknown, rather than automatically unaffected.

```bash
python ccf-paper-writer/scripts/writing_runtime.py prepare --manuscript path/to/paper.md --target SECTION_ID --mode related-work --brief path/to/brief.json --sources path/to/sources.json
```

The prepared view retains the target and neighboring excerpts, together with applicable source positions and factual constraints. A recovered whole-paper relationship comes from the brief; the helper does not infer one from section titles. These have different roles: write from the science and the reader's path; use the constraints internally to avoid changing facts. Do not turn source IDs, completion states or preparation fields into manuscript sentences. Include a material condition where it changes the scientific meaning. Check marked omissions and read a necessary dependency before relying on it.

`--max-chars N` bounds the serialized `context` JSON in characters. Guidance and identity metadata occupy additional space; this is not a total-packet limit or a measured token count. The helper never shortens the target or scientific brief. Optional excerpts may be shortened with explicit omitted locations, which remain unread until retrieved. If the necessary context cannot fit, select a coherent smaller scope or retrieve the specific dependency. Keep one owner responsible for integrating the argument; target IDs do not imply one agent per paragraph.

## Apply A Localized Edit And Follow Its Impact

The packet carries the current source identity and authorized target. Return a localized patch in its actual schema, then apply it against that packet:

```bash
python ccf-paper-writer/scripts/writing_runtime.py apply --packet path/to/writing-packet.json --patch path/to/patch.json
python ccf-paper-writer/scripts/writing_runtime.py impact --packet path/to/writing-packet.json
```

A changed manuscript requires refreshed context and reconciliation with the current text. Never force an older patch over an independently edited version. Preserve citations, labels, equations, numbers, source format and accepted passages outside the edit. An authorized change to a protected fact needs a new factual basis and refreshed preparation, not a workaround that removes the protection.

Use the impact view to find relations that may need checking: definitions used elsewhere, the adjacent transition, claims repeated in an abstract or conclusion, and corresponding tables or figures. It is a selection aid, not proof that the remaining paper has been checked. Review the actual affected text and its dependencies once; broaden only when a finding changes the scope. The reviewer diagnoses, the writer revises, the integrity auditor resolves evidence or numerical conflicts, and the visual composer owns figure edits.

## Select One Prompt Module

`prepare` automatically injects the selected module into the packet. Default mode is `draft`; `related-work`, `results`, and `consistency` select the corresponding module. Read or inject only the applicable block, not this whole guide or every mode. A consistency packet supports read-only assessment; it does not grant manuscript-edit permission or trigger an independent agent.

<!-- prompt:draft -->
Write the authorized target in the user's requested language and source format. Use its scientific message, the whole-paper throughline and necessary neighboring passages to develop a connected explanation. Preserve the actual role of conceptual, theoretical and interpretive passages; not every paragraph describes an engineering operation.

Use selected original passages for applicable argument and language organization. Keep factual support, technical meanings, citations and protected content intact. Internal source IDs, preparation fields and work status do not supply the manuscript narrative. Material uncertainty belongs where it affects the claim. Preserve supported strength and the author's sentence-final synthesis or broader significance.

Return the localized edit in the packet's patch schema, bound to its source identity and target. Do not revise unrelated sections or start a new experiment. If a necessary fact is missing, leave only the dependent assertion unresolved and complete the supported writing.
<!-- /prompt:draft -->

<!-- prompt:related-work -->
Organize the authorized passage around the scientific question and the ideas, assumptions, mechanisms or capabilities that explain the closest work. Use the whole-paper throughline and neighboring passages to connect this account to the paper. Topic count and paragraph count follow the material.

Describe what the original sources actually establish and how the relevant relationships differ. Retain informative attribution and ordinary citation syntax. A good writing exemplar supplies explanatory technique, not borrowed scientific claims or distinctive sentences. Do not require every group to end in a limitation, a denial or a superiority claim.

Return only the authorized edit in the packet's patch schema. Preserve source identities internally, citation keys in the manuscript and the difference between an observed contribution and a proposed direction. Do not broaden retrieval merely to reach a source quota.
<!-- /prompt:related-work -->

<!-- prompt:results -->
Develop the authorized results passage around the question answered by the supplied observations. Connect the result, its comparison and its interpretation; a list of scores is not the explanation. Use the whole-paper throughline without forcing the observations to support an expected story.

Preserve sample units, denominators, metric directions, intervals, configurations and reported values. Distinguish our measurements, prior reported results, simulations and plans. A missing result remains missing; complete the supported material without drafting a status report or an imagined reviewer response. Keep genuine negative findings and material uncertainty.

Return the localized edit in the packet's patch schema. Do not change values to improve the narrative, infer an untested causal mechanism or add an experiment campaign. A table or figure conflict goes to its existing evidence owner while unaffected writing continues.
<!-- /prompt:results -->

<!-- prompt:consistency -->
Assess the supplied manuscript view without rewriting it. Compare the target and actual affected dependencies for scientific meaning, terminology, definitions, quantities, conditions and narrative transitions. Use source excerpts according to their stated roles; a writing exemplar is not evidence for the current research.

Report concrete findings with a section location, an exact available quotation, the conflicting relation and a useful repair direction. Preserve calibrated uncertainty and the author's supported rhetorical emphasis. Do not invent a defect merely because wording matches a familiar pattern.

State what was actually read. Unseen sections and excerpt-only dependencies remain unchecked; hashes and successful local checks do not establish semantic agreement. Return the requested review shape, with no automatic acceptance score, new experiment request or manuscript patch.
<!-- /prompt:consistency -->

<!-- prompt:pending-results -->
The author has deliberately enabled complete results-pending drafting. In write mode, complete the authorized argument and prospective interpretation with missing quantities left as stable [[PENDING:claim-id]] slots. A conditional passage may use [[PENDING:claim-id|If the measured effect persists, it would support this interpretation.]]. Give the artifact one visible results-pending label. Honor any current request to leave experiments empty. In review mode, assess only; do not write or fill values.

Existing observations, including negative and mixed findings, govern the manuscript. Never invent measurements, completed runs, rankings, statistical significance, citations, mechanisms or qualitative observations. Anticipated analysis must remain conditional, with the consequence of an opposite finding where material; it cannot establish the intended claim. Keep the scientific prose coherent and the author's supported closing significance.

Before delivering a whole draft, automatically inspect abstract, contributions, definitions, methods, result tables, captions, analysis, conclusion and any supplied appendix together. Track pending claim IDs across these locations, distinguish expected from observed outcomes, and resolve conflicting quantities, units, directions, protocols or versions. Repair within scope and recheck affected passages. Do not mark unseen dependencies checked or present internal agreement as empirical support. A local patch checks its affected relations; the whole-draft pass occurs when integrating the completed draft. No extra independent reviewer or experiments are activated. The output remains results-pending until actual outcomes replace all dependent assertions consistently.
<!-- /prompt:pending-results -->

## Reuse Only Matching Review Work

An independent second assessment follows the existing `independent_review` preference or an explicit request and its budget. Ordinary writer checks and required factual corrections remain part of the authorized work. Do not send the same full manuscript once per section or turn a paragraph repair into a standing review loop.

The helper's `review-cache` commands can track an expensive review request and its actual coverage. Use its `--help` for `begin`, `complete`, `lookup` and recovery details. Reuse requires matching content, scope, model and applicable options; pending or excerpt-only work cannot become a completed full review. If a request's execution is uncertain, establish that it stopped before explicitly abandoning it. No cache command starts a model call, and no status label substitutes for reading the text.

Supply the actual model/runtime identity and all review parameters with `--model` and `--options`; include the applied rubric and policy contents or their version hashes in that options object. Hidden host configuration cannot be inferred by this local helper. Coverage describes the actual inspected material: `full` means all prepared targets were read, not that unprovided paper sections or source files were reviewed. Keep unknown and omitted coverage explicit in the existing result.
