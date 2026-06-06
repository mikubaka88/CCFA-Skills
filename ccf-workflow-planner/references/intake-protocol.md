# Intake Protocol

Use this file to turn an ambiguous user request into a bounded CCFA research task.

## Intake Fields

Collect or infer:

```text
Goal:
Decision to make:
Audience:
Target venue or venue family:
Research stage:
Available materials:
Known constraints:
Success criteria:
Privacy boundary:
Downstream skill candidates:
```

Do not ask for a field if it is clear from local files, pasted text, or the user's prompt. Mark unknowns explicitly.

## Research Stage Values

Use the closest value:

- rough idea,
- idea selection,
- literature grounding,
- experiment planning,
- manuscript drafting,
- manuscript polishing,
- page/word compression,
- writing review,
- rebuttal/author response,
- skill maintenance,
- mixed workflow.

## Missing Information Classes

Classify missing information as:

- `must-know`: changes route, scope, privacy, target venue, or feasibility;
- `useful-to-know`: improves output quality but can be assumed;
- `safe-to-assume`: choose a conservative default and state it.

Ask only for `must-know` information. In quick mode, ask at most one question or proceed with a stated assumption.

## Privacy Boundary

Before any browsing or handoff that could expose private material, classify the user's material:

- public: paper title, published abstract, arXiv/OpenReview link, official venue rule, public dataset or benchmark;
- private: rough idea, manuscript draft, reviewer comments, unpublished result numbers, internal experiment notes;
- mixed: public title plus private draft or internal result interpretation.

Use public-safe queries unless the user explicitly authorizes exact private text in searches.

## Scope Diagnosis

Return one of:

- `single-task`: one CCFA skill can handle the request directly;
- `multi-stage`: several CCFA skills should run in order;
- `too-broad`: split into subprojects before any downstream work;
- `unclear`: one must-know question remains.

When the scope is multi-stage, identify the first stage and the handoff condition for the next stage.
