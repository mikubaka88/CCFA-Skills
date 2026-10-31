# Content behavior smoke tests

Run this small suite during maintenance after deterministic checks. It does not
run during ordinary writing, idea development or review, and no helper calls a
model service.

Use the same model, reasoning configuration, supplied materials and budget for
each version. Give a fresh agent the prepared task input and the selected
version's skill files, without grading anchors, the rubric, desired answers or
suspected defects. Keep each task in a separate context. Use supplied materials
without browsing; do not install packages or run training in these probes. Record
actual outputs and any exposed tool/usage information. Missing token receipts
remain unknown; character counts are not token measurements.

Prepare model-facing inputs; keep the assessor's copy of the suite separate:

```bash
python evaluation/behavioral/evaluate_outputs.py --prepare
python evaluation/behavioral/evaluate_outputs.py --suite evaluation/behavioral/tasks-integration.json --prepare
```

The second suite adds five terse requests: a method change across a manuscript,
technical prose without an explicit word-preservation hint, negative results
against an optimistic draft, continuation after a conflicting compressed plan,
and codebase choice under GPU/time constraints. Its manuscript task includes an
unevaluated revision and measurements from the old configuration; the result
must keep those identities distinct. It complements the original four tasks in
`tasks.json`; archived 0.12.0 smoke outputs remain valid for their original suite.

Save each version's actual answers as one JSON object mapping task IDs to text,
then run the matching checker:

```bash
python evaluation/behavioral/evaluate_outputs.py --outputs path/to/answers.json
python evaluation/behavioral/evaluate_outputs.py --suite evaluation/behavioral/tasks-integration.json --outputs path/to/integration-answers.json
```

The checker verifies literal factual anchors and optional groups of alternative
spellings only. It does not score prose, understand numerical attribution, prove
that results were not invented, or enforce a wording template. A reversed
baseline/method comparison can retain every anchor and still be wrong. Fields
such as `forbids_fabricated_results` become questions for semantic assessment,
not automatic success claims. The report leaves `quality_score` null and lists
each task's ungraded `semantic_outcomes_to_check`.

Give anonymous actual outputs, task inputs, outcome questions and the rubric
to an independent reader for semantic assessment. Check meaning, logical
progression, empty defensive framing, scientific uncertainty, closing emphasis
and distinct mechanisms. Do not penalize legitimate technical words. Inspect
actual task completion and calls rather than rewarding a mandated tool order.

Four tasks and one trial per version are a smoke comparison, with no statistical
claim about general writing, model degradation or research productivity. Keep
capability evaluation separate from the deterministic regression suite. An
additional independent judge is optional outside a requested evaluation budget.
The new suite is ready for future comparisons; adding its tasks and passing the
evaluator's own tests does not constitute a model run or a measured quality gain.
