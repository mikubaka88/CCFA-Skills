# Content behavior smoke tests

Run this small suite during maintenance after deterministic checks. It does not
run during ordinary writing, idea development or review, and no helper calls a
model service.

Use the same model, reasoning configuration, supplied materials and budget for
each version. Give a fresh agent the suite and the selected version's skill
files, without the desired answer or suspected defect. The tasks request no
browsing; they test supplied-content writing and mechanism development. Record
actual outputs and any exposed tool/usage information. Missing token receipts
remain unknown; character counts are not token measurements.

Save each version's answers as one JSON object mapping task IDs to text, then:

```bash
python evaluation/behavioral/evaluate_outputs.py --outputs path/to/answers.json
```

The checker verifies a few factual anchors only. It does not score prose or
enforce a wording template. Give anonymous outputs, task inputs and the rubric
to an independent reader for semantic assessment. Check meaning, logical
progression, empty defensive framing, scientific uncertainty, closing emphasis
and distinct mechanisms. Do not penalize legitimate technical words. Inspect
actual task completion and calls rather than rewarding a mandated tool order.

Four tasks and one trial per version are a smoke comparison, with no statistical
claim about general writing, model degradation or research productivity. Keep
capability evaluation separate from the deterministic regression suite. An
additional independent judge is optional outside a requested evaluation budget.
