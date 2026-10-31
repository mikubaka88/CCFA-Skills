# Frontier Ideation

Use this file when the user provides a fuzzy, broad, or stale-prone idea and wants it concretized or optimized.

## Exploration Rule

Generate distinct explanations or mechanisms before selecting a development route. A field's unmet need and an unexplained phenomenon are both valid starting points. Explain what solving the question would change in practice or understanding; do not invent a customer, immediate application, or leaderboard target for basic research. When literature is available, use `literature-grounded-evolution.md` to connect inspected premises to new inferences. An inferred hypothesis need not already appear in a paper to be worth developing.

Check relevant closest work before making a strong novelty claim. Keep search coverage with the comparison; a search that found no match is not a proof of novelty.

Do not collapse the search space too early. When breadth is useful, consider a direct repair, a changed assumption, or an alternative explanation of the same difficulty. For a requested breakthrough, explore how information, representations, objectives, or computations could change; a safer configuration alone does not answer that request. Use the capability diagnosis in `problem-method-blueprint.md` where relevant. These are thinking aids, not mandatory rows. If no coherent alternative emerges, identify the unresolved premise rather than inventing a breakthrough or substituting an easier goal.

## Varied Inspiration And Candidate Selection

Use this procedure for requested creative or broad exploration. The existing `alternative_routes` preference governs an unsolicited extra comparison after a route has been selected; it does not suppress the breadth the user requested. Extra literature beyond requested coverage follows `extended_search`. Neither setting starts experiments or requires additional agents.

1. Preserve a compact problem statement, explicit constraints, and any already useful route. Separate these from a provisional explanation of the failure.
2. Assemble a small eligible inspiration pool from inspected sources and supplied observations. Vary their relationship to the question: close mechanisms, conflicting findings, older foundational arguments, or a structurally related problem in another field. Select for relevant information, assumptions, and operations; venue prestige, date, and lexical similarity alone do not determine eligibility.
3. When random variation is requested, use a host-supported seeded sample or shuffle among comparable eligible inspirations or transformation operators. Record the seed and selected source IDs in the existing task note when the selection must survive recovery. Reuse that selection on continuation; draw again only for an authorized new exploration or when the current source relationship is exhausted. A seed reproduces the selection, not the model's generated text. If no random tool is available, make a deliberate diverse selection without claiming random sampling. Do not change model temperature or choose the final recommendation by lottery.
4. Form a candidate by stating the changed assumption or operation and the consequence that distinguishes it. For a cross-field transfer, map the objects, information available, invariants, and objective, then identify where that mapping breaks. Shared vocabulary alone is insufficient; a useful analogy need not imply that the original method can be copied unchanged.
5. Compare the candidate set as a set: merge alternatives with the same failure explanation, intervention, and prediction despite different names. Preserve the strongest substantive route. Replace redundant candidates only when an alternative adds a meaningful explanation, capability, or tradeoff; distance or surprise alone does not make a weak idea useful. Finish at the requested breadth and budget instead of repeatedly regenerating until every slot looks novel.

An idea about a practical bottleneck should identify who or what is affected and how current methods miss the requirement. A basic-research idea should identify the unresolved relation, limit, or phenomenon and what resolving it would explain. These are alternative motivations, not two compulsory justification sections.

## Candidate Axes

Vary only the axes that create meaningful differences; do not build a Cartesian product or change every axis at once:

```text
Problem angle:
Root bottleneck:
Target user/community:
Method mechanism:
Data or benchmark:
Evidence type:
Venue family:
Main risk:
```

Useful variation patterns:

- Same problem, simpler mechanism.
- Same method family, sharper problem.
- New benchmark/protocol instead of new model.
- System/tool contribution instead of only algorithmic contribution.
- Theory/analysis contribution that explains an empirical pattern.
- Human-centered or deployment constraint that changes the problem.
- Negative result or diagnostic paper when SOTA chasing is crowded.

For iterative research, keep meaningful parent relationships in the existing research record. A combination should explain the interaction between mechanisms; a transfer should check the original assumptions in the new setting. A single idea card needs no lineage labels or separate bookkeeping file.

## Non-Stale Check

Ask or search:

- Which current papers or technical reports change this question, and which older result still defines its assumptions?
- What datasets or baselines have become standard?
- What failure mode is still not well measured?
- What assumption do recent papers share?
- What result would still be useful if headline performance gains are small?

Complete explicitly requested retrieval. Reuse inspected sources where applicable; if a primary source is unavailable, name the specific unresolved comparison and continue independent development without asserting novelty.

## Coherence Audit

Repair promising candidates when a specific fix can preserve their value. A hard constraint violation, direct contradiction, or clear duplication may be filtered immediately; do not spend a rescue pass on every discarded branch. Separate lack of validation from a demonstrated flaw. Watch for:

- The method requires data the setting cannot provide.
- The benchmark does not test the claimed mechanism.
- Claimed contributions lack a common research question or require incompatible assumptions; connected method, data, and theory contributions may legitimately belong together.
- A fixed intended audience would not benefit from the result; an unspecified venue is not a reason to discard the idea.
- The core insight is only a renamed component.
- Two modules optimize incompatible objectives.

After the audit, develop the selected route and retain a structurally different fallback when useful. For an options request, deliver the requested breadth. Reopen a mechanism when a counterexample, new observation, verified overlap, or changed constraint affects it. Explain which premise changed and preserve the research objective. Repeated low scores or paraphrased criticism alone do not justify either another cosmetic revision or abandoning the goal. Apply Common's continuity progress test across search, reviewer, and optimizer handoffs.

## Rescue Patterns

Consider these when a specific reformulation can preserve the direction's value. They are options, not a required rescue pass for a contradicted, infeasible-under-hard-constraints, or clearly duplicate candidate:

- Keep the important problem and replace a limiting assumption, information flow, interaction mechanism, or measurement perspective. State the causal reason and a prediction that distinguishes the alternative.
- Transfer an explanatory principle from another setting after checking its necessary assumptions; specify what changes in this setting rather than stacking modules.
- Narrow the target setting until the bottleneck is measurable.
- Replace "new model" novelty with a benchmark, protocol, diagnostic, or analysis contribution.
- Keep the problem but simplify the mechanism.
- Keep the method family but change the claim from SOTA improvement to failure-mode explanation, robustness, cost, or deployment constraint.
- Switch venue family when the idea is valuable but not a main-track fit for the named venue.
- Turn a crowded positive-result idea into a negative-result or measurement paper if that would teach the community something.

Choose by the user's contribution goal and decision-relevant potential, not merely by ease of completion. Lowering ambition, changing contribution type, or moving venue is an option to explain when material; it is not an automatic consequence of uncertainty or a poor provisional score.

## Output

Use the requested format. Explain the problem, proposed mechanism, reason it could address the difficulty, and relevant difference from known work. For alternatives, make their different assumptions or predictions easy to compare. State material unknowns where they affect the choice; keep branch labels and audit bookkeeping internal. Include an experiment plan only when requested or needed to answer a specific decision, and distinguish a proposed next observation from a measured result.
