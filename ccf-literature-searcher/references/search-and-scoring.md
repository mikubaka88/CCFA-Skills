# Literature Search And Scoring

Use this file for source selection, source-quality exclusions, paper classification, and quality scoring.

## Standalone Search Depth And Handoffs

Choose the scope under Common's task modes. For standalone work, the former planning ranges remain available: exploratory 10-20 screened candidates and 5-10 final papers/clusters; quick 6-10 screened and 3-6 final; standard 15-30 screened and 8-15 final. They are starting budgets, not quotas. Follow a user-requested breadth, stop once the requested evidence is covered, and broaden for a concrete gap. A helper lookup retrieves only the sources needed for its question and returns to the owner without a standalone report.

For each included paper retain identity/link, version/publication status, contribution type, inspected source locations and relevance. Use the taxonomy and scoring anchors below only as needed; omit unrequested score columns and empty generic sections. Keep source evidence distinct from the model's inference. An unverified inaccessible lead may represent missing coverage but cannot establish overlap, quality or missing experiments.

Match the handoff to the receiving decision:

- Writing: the supported prior-art claim, original passage/location, closest-work grouping and citation identity; preserve factual support separately from writing exemplars.
- Idea development: source-backed observations, mechanism primitives, assumptions, protocol anchors and useful gap/conflict relations, including foundational, conflicting or analogous-field work when relevant. Do not send only authors' limitations or recent lexical neighbors.
- Idea review: inspected conceptual overlap, remaining difference and novelty/source coverage.
- Monitoring: watch queries, tracked sources/competitors and dated changes.
- Experiments: dataset, baseline, metric and protocol identity.
- Paper review: decisive related-work or benchmark evidence and its actual location.

Return only the relevant records and recoverable anchors, not copied whole abstracts or a compulsory package for every skill. Reuse a canonical search folder when persistence is needed; `report-template.md` defines its current files. Group overlapping needs before retrieval and derive Markdown/CSV views from one screened set.

## Query Cost And Reuse

Reuse the effective `extended_search` preference from Common; it governs optional expansion beyond the requested evidence coverage, not verification required to support a claim. Batch identifiers through an available API and request only fields needed at this stage: identity/date/URL for screening, abstracts for relevance, and original sections for substantive claims. Do not fetch full citation graphs or author profiles merely because an endpoint returns them. Resolve an ambiguous identity before merging DOI/arXiv/title records; never collapse different versions or supplementary material blindly.

Use the existing source cache and record the source version, inspected pages/sections, and relevant finding IDs in the current report. A changed source invalidates its dependent interpretation, not unrelated verified references. An unchanged cached PDF does not establish that no newer paper/version exists; freshness-sensitive searches still check current primary records. Preserve a relevant evidence excerpt and its anchor instead of repeatedly copying a full extraction across skills. Keep a model-generated interpretation distinct from the source passage.

For unresolved tables, formulas, or reading order, inspect the affected source page first. Additional OCR/visual enrichment follows `enhanced_document_parsing`; process only relevant uncertain pages unless whole-document coverage is necessary. Do not start a new vector database, download a parser model, or invoke a description model for every figure by default. Use host-provided tools before optional new integrations.

## Source Tiers

Use sources according to what they establish:

- Scientific claims: inspect the actual paper, relevant supplementary material, or primary dataset/code/protocol artifact. Official proceedings and publishers such as ACL Anthology, CVF Open Access, PMLR, ACM Digital Library, IEEE Xplore, USENIX, VLDB, AAAI/OJS, SIAM, and Springer/LIPIcs can host these sources; arXiv and OpenReview identify particular preprint or submission versions.
- Discovery and identity: DBLP, Semantic Scholar, OpenAlex, Crossref, DOI landing pages, and venue lists help locate or verify bibliographic records. Record existence, citation counts, or acceptance metadata do not establish a method's validity or reported result.
- Project pages, benchmark leaderboards, and dataset pages support claims about their actual release, protocol, or listed measurements. Inspect the linked paper or artifact for deeper mechanism or comparison claims.
- Original technical reports from research groups and labs can provide mechanisms, observations, and implementation detail. Inspect the report and associated artifacts; keep its release/version and review status explicit. An influential institution is not a substitute for inspecting the claimed finding.
- Strong journals and transactions when the field is journal-centered: JMLR, TPAMI, TOG, TKDE, TDSC, TOSEM, TSE, TODS, CACM, IEEE/ACM Transactions, Nature/Science family only when relevant.

Link final claims to the inspected source and preserve its version/status. A page's official host alone does not establish that the relevant method or result was inspected.

## Hard Exclusions

Exclude:

- MDPI domains, journals, proceedings, PDFs, and special issues.
- Predatory or low-signal venues with no clear review standard.
- Untraceable PDFs without title, authors, venue, or stable link.
- Substantive claims or quality scores based only on search snippets. An identifiable, relevant paper may remain an unverified retrieval lead while the missing primary source is named.

Apply the shared exclusions within the user's current instructions. An explicit request to inspect a named source is already a user-directed exception unless a higher-priority rule prohibits it; do not ask for the same authorization again. Keep source status and verified content distinct, and do not generalize one requested exception to unrelated recommendations.

## Search Strategy

Choose queries for the requested role: closest-work verification, explanation of a phenomenon, transferable mechanism, or a practical requirement. Use relevant query forms:

```text
"<task>" "<method>" benchmark
"<task>" "<closest baseline>" "dataset"
"<problem phrase>" site:openaccess.thecvf.com OR site:proceedings.mlr.press
"<method phrase>" OpenReview NeurIPS ICLR ICML
"<topic>" DBLP SIGMOD SIGCOMM SOSP CCS CHI PLDI STOC
"<information constraint or invariant>" "<operation>"
"<unexplained observation>" "analysis" OR "technical report"
```

Choose a compact source set that answers the current question. Current closest work establishes overlap and timing; an older foundational result, a technical report, a conflicting observation, or an analogous field may supply a better explanation or mechanism. Do not impose year, venue, or paper-count quotas. A survey helps map a field; inspect the relevant original for a substantive claim. When source selection feeds creative exploration, pass its relationship to the question instead of ranking only by topical similarity.

## Opportunity Mapping

When the search is for early direction scouting, classify each cluster as one or more of:

- `crowded but open`: many papers exist, but a measurable failure mode, setting, or assumption remains weak.
- `covered central claim`: the same problem, mechanism, and evidence path are already present; the idea needs a new angle.
- `benchmark gap`: the field lacks a dataset, protocol, metric, stress test, workload, or evaluation standard.
- `mechanism gap`: papers report performance but do not explain why the method works or fails.
- `deployment/system gap`: real constraints, cost, latency, robustness, privacy, security, or user workflow are under-tested.
- `theory/analysis gap`: empirical results exist but formal understanding, bounds, or diagnostics are missing.
- `negative-result opportunity`: common assumptions fail, and a careful diagnostic or falsification paper may be valuable.

For a `covered central claim`, explain the overlap. Include a reframing only when it changes a meaningful problem, mechanism, or evidence contribution; a popular topic alone does not make the broader direction unproductive. Use only the fields needed to communicate the decision:

```text
What is covered:
Why direct novelty is weak:
Supported next step: substantive reframing / specific unresolved question / stop this candidate
Evidence needed to decide, if unresolved:
```

If no valuable distinction is supported, say so and return to the idea owner. Do not invent an extra module or treat a venue change as scientific novelty. Stopping this candidate does not discard the user's broader research objective.

## Paper-Type Taxonomy

Classify each included paper:

- `pure benchmark`: primary contribution is dataset, benchmark, workload, protocol, evaluation suite, or leaderboard.
- `pure method`: primary contribution is method, algorithm, model, system design, proof, or analysis.
- `method + benchmark`: introduces a method and a new dataset/benchmark/protocol that both matter.
- `survey`: synthesizes prior work.
- `system/tool`: primary contribution is implementation, infrastructure, deployment, or usable tool.
- `theory/proof`: primary contribution is theorem, bound, proof technique, or formal model.
- `other`: use only with a short explanation.

## Scoring

Use 1-5 anchors unless the user asks for another scale.

Score paper quality separately from idea viability and overlap. A high-quality close paper may reduce direct novelty while also revealing a better problem boundary, baseline, benchmark, or unresolved assumption. Weak empirical support does not erase a disclosed mechanism's prior existence, and overlap alone does not establish that the broader problem is solved. Explain which inspected claim, method, or evidence matches.

Insight:

- 5: clear, non-obvious insight that changes how the problem is understood.
- 4: strong idea with a specific mechanism or framing.
- 3: useful but incremental insight.
- 2: mostly engineering assembly or standard framing.
- 1: unclear or weak insight.

Completeness:

- 5: the contribution's definitions, method/protocol/proof, appropriate evidence, material boundaries, reproducibility, and positioning are well covered.
- 4: strong coverage with minor missing details.
- 3: adequate but with visible gaps.
- 2: partial; important design or evidence details missing.
- 1: incomplete or hard to audit.

Experimental numeric evidence:

- 5: strong, fair, multi-setting numerical evidence with appropriate baselines and analysis.
- 4: solid numerical evidence with minor weaknesses.
- 3: adequate numbers but limited settings, baselines, or statistics.
- 2: weak numbers, narrow protocol, or unclear fairness.
- 1: the paper makes an empirical claim that its inspected numerical evidence does not support.
- `N/A benchmark`: use for pure benchmark papers; instead write a benchmark-quality note.
- `N/A` with a reason: numerical evidence is not applicable to the contribution, such as a proof-only result. Assess its proof or other relevant support under completeness.
- `not assessed`: the relevant results were not inspected or are unavailable. This is a coverage limit, not evidence of poor quality.

Benchmark-quality note for `pure benchmark`:

```text
Benchmark scope:
Task realism:
Metric validity:
Baseline coverage:
Adoption or reproducibility signal:
Known limitation:
```

Screening/relevance label, separate from scientific quality:

- `A`: high-priority evidence for the assigned role, such as closest work, a decisive counterexample, or a mechanism-bearing inspiration.
- `B`: useful supporting, comparison, or inspiration material.
- `C`: background only or weak fit.
- `Risk`: a candidate with a specific unresolved overlap question that could change the novelty judgment; this is a reading priority, not a verdict.

Do not convert scores into acceptance probability.
