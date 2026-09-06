# Strict Idea Review Protocol

Use for concept judgment, novelty assessment, investment decisions, comparison, and standard idea review. Natural requests such as “这个思路靠谱吗”, “值得做吗”, “创新够不够”, and “逻辑有没有硬伤” request assessment even without the words score or review.

## Scope

Default to the research problem, prior-art difference, insight, mechanism, and contribution. Review these even when they are embedded in a full manuscript. Do not evaluate experiment completion, results, baselines, ablations, datasets, statistical significance, code release, or paper formatting unless the user requests that extension. Missing experiments do not justify a low score, rejection, or a mandatory follow-up question.

Distinguish conceptual soundness from empirical validation. A contradictory assumption is reviewable now; whether an untested mechanism performs well remains a hypothesis and is not an automatic defect.

## Grounding

For standard novelty judgments, verify the closest public work unless browsing is forbidden or no public-safe query is possible. Query public problem and method terms under `../../ccf-common/references/privacy-and-evidence.md`. Reuse already verified sources; do not retrieve a fixed number of papers to fill a quota.

Read the relevant method or claim before asserting overlap. For each decisive source record its link, what it already does, the overlap, and the remaining conceptual difference. Mark coverage as searched, partially searched, supplied-only, or unsearched. A lack of retrieval is uncertainty; a demonstrated overlap is a finding.

## Output Selection

Use `detailed` by default, including natural assessment requests such as “靠谱吗” and “值得做吗”. Use `brief` only when the user explicitly asks for 简要版, 简短, 快速概览, 只给结论, brief, concise, or a restrictive length/output format. A rough seed, one idea, limited evidence, or “不用打分” does not imply brief output. Output detail and evidence-search depth are separate choices.

Use the concept-specific sections below to organize the assessment, conceptual ratings, and development priorities. Translate headings to the user's language and preserve an explicit user schema.

## Detailed Version — Default

Develop each applicable section using the supplied concept and inspected prior art. A detailed report should contain substantive judgments and their basis, not just an outline or an unexplained scorecard. Keep unavailable inputs in one scope note and do not invent content to populate sections.

### 1. 思路信息与评审范围 / Idea Information

Identify the idea, source version, intended problem and audience, and prior-art coverage. State concept-only scope once. Do not add submission, experiment, or implementation-completeness gates.

### 2. 总体判断与发展潜力 / Verdict And Potential

Lead with accept-to-develop, revise, pivot-with-rescue-route, abandon, or needs-literature-search. Explain the deciding reasons and separate current concept quality, development potential, and confidence. This judgment concerns further research, not conference acceptance.

### 3. 问题定义与研究价值 / Problem And Value

Assess whether the problem is specific, the bottleneck meaningful, the assumptions appropriate, and the intended benefit scientifically valuable. Explain who would benefit and what remains unclear without inventing an application or resource constraint.

### 4. 核心洞察与贡献拆解 / Insight And Contribution

Reconstruct problem → insight → mechanism → intended contribution. Identify the non-obvious idea, what is merely an implementation component, and what the community would learn if the concept were realized. Planned effects remain hypotheses.

### 5. 最近工作与创新差异 / Prior Art And Novelty

Inspect decisive closest work and explain what remains after subtracting known contributions.

| Closest work / source | Existing idea or mechanism | Overlap | Remaining conceptual difference | Judgment |
| --- | --- | --- | --- | --- |

Unsearched novelty stays uncertain; do not treat an empty comparison table as low novelty. If sources are unavailable, give the coverage limit and the precise comparison still needed instead of invented rows.

### 6. 方法机制、假设与逻辑 / Mechanism And Assumptions

Explain how the proposed intervention could address the bottleneck, whether components are necessary and compatible, and whether assumptions support the conclusion. Use a derivation or counterexample when it resolves a conceptual question. Distinguish a demonstrable contradiction from an untested hypothesis; do not demand experiments or a completed proof to make this distinction.

### 7. 主要优势与可保留成分 / Strengths

Number the substantive merits, anchor them in the idea or a verified source, and explain their significance. Identify ingredients worth preserving even if another part needs revision. Do not invent praise or force a minimum count.

### 8. 主要缺陷与概念风险 / Conceptual Concerns

Assign stable IDs. For each material concern, give the exact claim or assumption, inspected basis, why it matters, severity, and the smallest conceptual repair. Distinguish a known flaw from missing definitions or unanswered questions. Missing experiments, results, baselines, or ablations are outside this section's default scope.

### 9. 多视角意见与综合判断 / Perspectives And Synthesis

Use `expert-panel.md` for problem/field, prior-art, mechanism/logic, and contribution/audience perspectives. Give distinct findings and a reasoned synthesis; do not repeat each full criticism or force disagreement. No experiment reviewer is included by default. Label single-agent perspectives honestly.

### 10. 六维评分与置信度 / Concept Ratings

Use the six conceptual dimensions and weights in `rubric.md`, with evidence or concern IDs, deductions, change conditions, assessed-weight coverage, and confidence. Apply `calibration.md` consistently. Unassessed criteria are not zero. For a no-score request, retain qualitative judgments for the same applicable dimensions instead of dropping this analysis or switching to brief output.

### 11. 关键问题与改判条件 / Questions And Change Conditions

Identify definitions, assumptions, prior-art distinctions, or concept choices that could change the verdict. Separate answerable clarifications from actual conceptual redesign. Do not replace these with a mandatory experimental plan or an acceptance prediction.

### 12. 概念修改优先级与发展建议 / Development Priorities

| ID | Priority | Conceptual refinement | What it preserves or repairs | Judgment-change condition |
| --- | --- | --- | --- | --- |

Explain the most useful next conceptual refinement and any meaningful rescue route. Recommendations are not authorization to rewrite the idea unless development was also requested. Preserve concern IDs and status on re-review; keep historical rubric changes explicit.

An explicitly requested experiment or feasibility assessment appears as a separate extension after the conceptual report. It does not silently change these six scores. Detailed output alone never authorizes that extension.

## Brief Version — Explicit Request

Use five compact blocks, unless an exact user format takes precedence:

1. **判断 / Verdict:** conceptual recommendation and development potential.
2. **主要优点 / Strengths:** the most consequential merits and their basis.
3. **关键问题 / Concerns:** decisive conceptual flaws or unanswered questions with anchors.
4. **评分概览与置信度 / Ratings:** an applicable score summary or qualitative judgment, plus novelty/source coverage.
5. **下一步 / Next Step:** the conceptual clarification or repair most likely to change the verdict.

Keep the same concept-only boundary and evidence standards. A brief presentation can summarize a standard literature-grounded assessment; a user-requested quick scan has narrower coverage and must not be labeled a full novelty review. Do not infer either brevity or a shallow search from a short user prompt alone.

## Revision And Persistence

Preserve concern IDs, source versions, and the agreed rubric. Check whether the changed problem or mechanism resolves the previous objection; do not move from concept quality to submission completeness during re-review. Generate one output version unless both are requested. When saving a report, switch detailed/brief in the same canonical artifact instead of making automatic duplicate files.
