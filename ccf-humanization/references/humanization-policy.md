# Humanization Policy

## Manuscript Standard

Write from the scientific work itself: the problem, insight, mechanism, observations, and what they establish. Use the strongest wording supported by the supplied evidence. Write for a reader trying to understand the work. Do not draft an answer to an imagined hostile reviewer and then decorate it as a paper.

Humanization preserves technical precision, equations, citation keys, terminology, numerical results, relevant assumptions, negative findings, reproducibility details, and mandatory disclosures. It is not detector-evasion or a license to strengthen evidence. A direct sentence can express uncertainty accurately.

## Sentence Decision

For each sentence that sounds defensive, recover its scientific payload before editing:

1. Identify the observation, mechanism, assumption, comparison, or inference it contributes.
2. If it contains a supported fact, state that fact directly with the scope needed to interpret it.
3. If it contains a genuine uncertainty, state what remains unresolved and why. Retain calibrated verbs such as `may` or `suggests` when the evidence warrants them.
4. If deleting it loses no scientific information, delete it. Do not replace it with another disclaimer or an advisory warning.
5. If resolving it requires an unknown result, a new experiment, or a change to the research claim, ask only about that decision and continue unaffected work.

Ordinary authorized editing includes preserving material facts, removing rhetorical padding, and rewriting a claim to accurately express its supplied evidence. These edits do not need a second approval. A factual limitation already supplied by the user is scientific content, not a warning to be kept out of the paper.

## Defensive Patterns And Repairs

These examples illustrate edits, not factual claims about the user's research. Apply a rewrite only when its scientific content is supported; brackets stand for supplied details.

| Pattern | Defensive wording | Repair |
| --- | --- | --- |
| Imagined objection | To address potential reviewer concerns, we include an ablation. | The ablation isolates the contribution of [component]. |
| Apologetic contribution | Although our method is merely a simple extension, it remains useful. | Describe the changed operation and the capability it provides. Remove the apology. |
| Denial-led positioning | We do not claim to solve the general problem; our goal is only to study [setting]. | We study [problem] in [setting]. |
| Repeated caveat | It should be emphasized that these results do not guarantee universal generalization. | State the evaluated setting once. Keep a specific generalization gap only if it changes interpretation. |
| Assurances without information | We carefully ensure a fair and rigorous comparison. | All methods use [the supplied common split and evaluation protocol]. |
| Unnecessary contrast | This is not a replacement for [unrelated system], but rather [method]. | Describe [method] and its inputs and outputs. Retain a contrast only when it distinguishes real alternatives. |
| Stacked hedging | These preliminary results might potentially suggest that [claim]. | Use the one level of uncertainty justified by the evidence: [Observation] suggests [interpretation]. |
| Defensive paragraph ending | Nevertheless, the method is not without limitations. | End on the paragraph's scientific takeaway. Discuss a material limitation at its relevant location. |
| 中文审稿预判 | 为避免审稿人质疑，我们额外加入了消融实验。 | 消融实验检验了[组件]对[能力]的作用。 |
| 中文自我降格 | 尽管这只是一个简单改进，我们并不试图解决所有问题。 | 说明改动的机制、研究问题和适用设置。 |
| 中文空泛保证 | 需要强调的是，我们不能保证该方法在所有情况下都有效。 | 写明实际评估条件；仅保留有依据且影响结论的外推限制。 |
| 中文流程旁白 | 为确保论文严谨性，此处仅报告经过确认的完整版本。 | 直接写方法名称、科学上相关的配置和实际结果。 |

Do not mechanically delete `not`, `only`, `may`, `however`, `limited`, or their Chinese equivalents. Negation can define a method, `only` can specify an experimental control, and contrast can explain a causal mechanism. Rewrite the rhetorical function, not a blacklist of words.

## Paragraph And Section Discipline

Give each paragraph a scientific purpose and a retained message. Develop the reason, operation, or evidence that supports it. End where that point is complete; do not append a caution, future-work sentence, or novelty disclaimer to every paragraph.

- Abstract: explain the problem, contribution, mechanism, and decisive evidence. Express scope in the task or result statement. A separate limitations sentence is needed only when omission would materially misrepresent the central finding or the venue requires it.
- Introduction and related work: establish the actual technical difference from the closest work. Do not pre-empt accusations of incrementalism or dismiss prior work to make the contribution appear larger.
- Method: describe operations, assumptions, and relevant configurations. Do not repeatedly justify why the design should be acceptable to a reviewer.
- Experiments: state the test, observation, and supported interpretation. Replace promises of fairness or robustness with actual protocol and measurements. Separate observations from causal explanations not established by the test.
- Discussion and limitations: give each material boundary a specific consequence. Do not enumerate unobserved deployment hazards or generic threats unrelated to the claim.
- Conclusion: state what was established and why it matters within the studied setting. Future work and caveats are optional, not a required closing ritual.

State a recurring scope condition at its natural location and use cross-references where needed. Restate it only when the reader would otherwise misinterpret a local result. Do not spread the same disclaimer through the abstract, contributions, captions, experiments, and conclusion.

## Consolidated Writing Constraints

- Begin with the scientific subject. Remove throat-clearing openers such as `It is important to note that`, `It is worth mentioning that`, `需要强调的是`, and `值得注意的是` when the following clause can stand directly.
- Use familiar, precise academic language. Keep one canonical technical term instead of cycling through synonyms for stylistic variation.
- Do not force every argument into exactly three items. Choose structure from the content, preserving required enumerations and study questions.
- Prefer zero em dashes in newly written or revised prose; allow at most three in a full paper, excluding direct quotations. LaTeX `---` counts in prose. Preserve numeric ranges, minus signs, citation keys, commands, and code.
- Use varied sentence rhythm where it helps the argument. Regular procedure descriptions and parallel experimental comparisons may remain regular. Five sentences within a five-word length band, similar paragraph lengths, and more than two semicolons per 1,000 words are review signals, not mandatory rewrites.
- Check inflated or vague terms such as `groundbreaking`, `pivotal`, `comprehensive`, `robust`, and `novel` against a concrete meaning and evidence. Retain standard terms such as `robust optimization` when technically correct.
- Every strong claim needs an evidence path. Replace an unsupported broad assertion with the precise supported claim; do not surround it with reassurance, disclaimers, or unsupported stronger verbs.
- Preserve the user's Markdown/LaTeX structure unless restructuring is requested. Do not insert internal warnings, hidden comments, prompt notes, or workflow metadata into manuscript files.

## Method Status Versus Academic Description

Method identity checks are internal. For reported experimental comparisons, verify identity and scientifically relevant configuration against supplied records or inspectable sources. For a literature description, use the cited paper; for a proposed method, use the supplied specification and distinguish planned evaluation from completed results. Do not demand a runnable checkpoint merely to explain a theoretical method, cite prior work, or draft from a supplied design.

Write `Transformer Base with six encoder and six decoder layers` when supported. Do not write `the confirmed full Transformer Base version`. Mention releases, revisions, and checkpoints when they distinguish experiments or support reproduction, not as badges of approval. `experiment-discipline.md` owns the full-method comparison rule and legitimate ablation exception.

## Unfavorable Information

If an unfavorable fact is observed, verified, and material to the claims, comparison fairness, reproducibility, ethics, or required disclosure, do not conceal it. Preserve it in direct scientific language within the authorized edit. For example, an observed failure on [condition] belongs with the relevant result; an untested scenario does not become an observed failure.

Discard speculative drawbacks and generic risk narration with no decision-relevant evidence. Do not recreate them as a long warning appendix outside the manuscript. Use a warning only for a concrete unresolved scientific decision or a material fact the available evidence cannot resolve.

## Warning-Only Boundary

For a warning-only issue:

1. Name the affected claim, evidence gap, and the smallest decision needed.
2. Explain the consequence briefly and propose a concrete action.
3. Make no source edit solely to encode that warning, no hidden comment, and no configuration change. Do not invent a replacement result or conceal an established fact.
4. Pause only the dependent claim or change until the user resolves the decision; continue already authorized, unaffected work. Reuse prior authorization when it covers the exact change.

Warnings are not the default output of humanization. Return the requested artifact first; include a short warning only when one remains. Exact-output requests keep their schema; use an allowed field or seek the one essential clarification rather than inserting an extra section.

## SHA-256 And Checksum Rule

Do not add SHA-256, checksum files, hashes, or hash-based identity as generic writing, deduplication, provenance, or confirmation requirements. Use method names, versions, configurations, dataset splits, checkpoint labels, and repository revisions when relevant.

Preserve hashing when it is the research object, an implemented dependency, or an external distribution/submission requirement. Do not remove a scientifically necessary operation for style.

## Humanization Acceptance Check

Read the revised prose once for its scientific argument, before counting surface patterns:

- The paragraph's main subject is the research, not reviewer opinion or authorial defensibility.
- Each retained qualification changes interpretation; empty caveats and repeated scope reminders are gone.
- Uncertainty matches the evidence without stacked hedging or inflated certainty.
- Assumptions, material negative results, protocol facts, and mandatory disclosures remain accurate.
- Scientific identity and configuration replace confirmation/status narration.
- Terminology, citations, numbers, equations, and requested structure are preserved.
- The em-dash preference and context-dependent pattern signals have been checked.

For full sections or papers, use `ccf-paper-writer/scripts/check_prose_quality.py` for candidate locations. Fix real problems; keep justified scientific language even when a pattern matches. A clean script result alone does not establish natural prose, correctness, or publication readiness.
