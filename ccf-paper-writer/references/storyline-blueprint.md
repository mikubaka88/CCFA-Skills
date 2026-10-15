# Storyline Blueprint

Use this for full-manuscript organization, substantial introductions, or explicitly requested storyline design. Ordinary polishing and bounded abstracts use the compact arc in the writer entry.

CCF-A writing should make the paper's scientific logic easy for reviewers to reconstruct. A storyline is not an outline, a marketing angle, or a list of modules. It is the coherent explanatory logic that makes the research necessary, plausible, evidenced, and worth remembering. Several connected motivations, observations, and claims can serve one theme; do not reduce a task, benchmark, and method contribution to one module.

For new drafts, `materials-to-manuscript.md` controls material status, pending results, and content before page fitting. Evidence maps below distinguish available support from planned tests; a planned evidence ladder is not a set of observed findings.

## Storyline Definition

A scientific storyline is the paper's coherent scientific argument:

```text
scientific origin -> knowledge gap -> scientific tension -> fundamental question -> core insight -> method mechanism -> evidence ladder -> bounded claim
```

The storyline must answer:

- Why does this problem matter before the method exists?
- What does the field still not understand, measure, prove, or build?
- What root reason makes existing approaches insufficient?
- What insight changes the way the problem should be attacked?
- How does the method implement that insight?
- Which evidence tests the claim, rather than merely decorating the paper?
- What can be claimed honestly, and where does the claim stop?

Do not start a storyline from the method name, module list, benchmark score, or fashionable technique. Start from the scientific origin.

## Global Story Fields

Fill these first. Mark unknowns instead of inventing them.

```text
Target venue:
Venue family:
Paper type:
Research materials available:
Scientific origin:
Field trajectory:
Largest unknown:
Why this unknown matters:
Existing methods/paradigms:
Unresolved gap:
Root scientific/technical reason for the gap:
Fundamental scientific question:
Core insight:
Proposed method/mechanism:
Contribution type(s):
Evidence ladder:
Expected central claim:
Material assumptions or observed limitations:
Unresolved evidence decisions:
Novelty status: searched / partially searched / user-provided / unsearched
```

## Multi-Expert Storyline Generation Framework

Use the full framework only when multiple substantially different storylines are needed for an explicitly requested comparison or redesign. For ordinary drafting or local polishing, use the compact story fields and section roles below.

### Stage 0: Material And Boundary Intake

Before generating variants, prepare a shared packet:

```text
Research goal:
Current draft/idea:
Method sketch:
Experiments/results supplied:
Closest-work status:
Target venue/audience:
What must stay fixed:
What may be reframed:
Evidence that cannot be invented:
Open unknowns:
```

Hard rules:

- Do not invent results, prior art, datasets, baselines, reviewer reactions, or novelty evidence.
- If novelty or frontier trend is central and unsearched, mark it as `needs-search`.
- If an attractive story requires unsupported evidence, keep it as a possible direction, not as the final story.

### Stage 1: Independent Expert Storyline Generation

Develop distinct candidate storylines before synthesis. Use independent subagents only when the host permits them and the task benefits from separate perspectives; otherwise describe the output as role-based analysis, not independent reviews.

Each expert must output a candidate with:

```text
Research motivation:
Fundamental scientific question:
Core insight:
Experimental logic:
Method organization:
Expected scientific claim:
```

#### Expert 1: Frontier Innovation Expert

Goal: find innovation opportunities from recent trends, cross-disciplinary frontiers, and future directions.

Tasks:

- Identify emerging research hotspots or paradigm shifts.
- Look for important unsolved scientific questions.
- Propose story directions that differ from common paper templates.
- Avoid merely rebranding an existing narrative pattern.

Output:

```text
Emerging scientific opportunity:
Novel perspective:
Potential breakthrough storyline:
```

#### Expert 2: Fundamental Science Expert

Goal: reveal the root scientific problem behind the work.

Must answer:

- Why is this problem important?
- What cognition, mechanism, measurement, theory, or design understanding is missing?
- What basic understanding changes if this work is true?

Output:

```text
Fundamental question:
Scientific gap:
Core insight:
```

#### Expert 3: Domain Expert

Goal: keep the story faithful to real scientific and technical logic.

Checks:

- Whether the method actually addresses the scientific question.
- Whether experiments support the core position.
- How the work differs from existing work.
- Whether there are logical holes or hidden assumptions.

Output:

```text
Scientific validation:
Technical reasoning:
Potential limitations:
```

#### Expert 4: Scientific Storytelling Expert

Goal: turn the discovery into an engaging scientific argument.

Design:

- How to open the problem.
- How to create scientific tension.
- How to order experiments as a logic chain.
- How to form a strong but bounded claim.

Output:

```text
Story arc:
Narrative structure:
Presentation strategy:
```

#### Expert 5: Critical Reviewer

Goal: simulate a strict top-venue reviewer.

Checks:

- Whether the story is truly novel.
- Whether it is only a repackaging of existing work.
- Whether it over-explains or overclaims.
- Whether any key logical connection is missing.

Output:

```text
Strengths:
Weaknesses:
Improvement suggestions:
```

### Stage 2: Cross-Expert Review

Compare candidate storylines before choosing one. Use 1-5 scores only when useful; always include the reason and the required repair.

Dimensions:

```text
Scientific Depth: Does it reach the root scientific question?
Novelty: Does it create a new cognitive angle, not just a new wording?
Logical Coherence: Do the motivation, mechanism, and evidence support the same research claims?
Narrative Quality: Is there scientific tension and reader curiosity?
Claim Strength: Does the final claim represent the whole work and match evidence?
```

Cross-review format:

```text
Candidate:
Best element:
Scientific Depth:
Novelty:
Logical Coherence:
Narrative Quality:
Claim Strength:
Fatal weakness if any:
Repair needed:
Evidence needed:
Keep / merge / discard:
```

### Stage 3: Chief Scientific Narrative Architect Fusion

The final fusion role is:

```text
Chief Scientific Narrative Architect
```

Responsibility: organize the original materials, candidate interpretations, and review findings around a shared scientific object. Retain related questions and observations when they explain distinct parts of the contribution.

Fusion rules:

1. Establish the shared scientific object and the related questions the work addresses.
2. Retain the observations that explain those questions; do not force one insight when it erases part of the contribution.
3. Organize the method as the natural implementation of the insight.
4. Organize supplied experiments as evidence for the claims, distinguishing planned tests from completed results.
5. Remove candidate fragments that create a second main story.
6. Weaken or mark claims that exceed supplied evidence.
7. Resolve disagreement against the original evidence. Carry a limitation into prose only when it is scientifically material; do not convert hypothetical objections into paper content.

Fusion output:

```text
Unified scientific origin:
Related research questions:
Core insight:
Final story arc:
Method organization:
Evidence ladder:
Central scientific claim:
Subclaims and evidence:
Limitations and boundaries:
Reviewer-risk repairs:
Discarded story fragments and why:
```

## Storyline Expression Logic

Use this expression order for new or rebuilt storylines unless the user intentionally requests a different format.

### 1. Scientific Origin: Why

Start from the root motivation. Do not introduce the method first.

Must answer:

- What is the research background?
- What is the largest current unknown?
- Why is this unknown worth solving now?
- What becomes possible if it is solved?

Structure:

```text
Field trajectory -> unresolved unknown -> consequence of the unknown -> scientific opportunity
```

Good origin statements make the reader feel the problem existed before the authors arrived.

### 2. Knowledge Gap And Scientific Tension

Show the mismatch between what the field can currently do and what it still cannot explain, measure, prove, or deploy.

Must answer:

- What do existing paradigms assume?
- Where do they break down?
- Why is the gap not solved by a straightforward extension?
- What tension makes the paper necessary?

Avoid generic gaps such as "existing methods are inaccurate" or "few works study this." Name the root bottleneck.

### 3. Fundamental Scientific Question

Establish the shared scientific question or coherent set of related questions that drives the paper.

The question should be:

- specific enough to test,
- broad enough to matter,
- connected to the method mechanism,
- answerable by the evidence package.

If several questions are necessary, make their relationships explicit. A common theme does not require discarding distinct task, measurement, and modeling contributions.

### 4. Core Insight: What Changes

The insight is the cognitive turn of the paper. It is not the method name.

It should say:

- what the authors noticed,
- why prior framing missed it,
- why this observation makes the solution plausible,
- what changes in the field's understanding if the observation is correct.

Insight test:

```text
Could a reviewer explain the paper's value in one sentence without listing modules?
```

If not, the insight is not yet sharp.

### 5. Method As Consequence: How

Present the method as the consequence of the insight.

For each module, specify:

```text
Module:
Which part of the insight it implements:
Input:
Operation:
Output:
Why it is necessary:
Validated by:
```

The method order should follow the logic of the insight, not the order in which code was written.

### 6. Evidence Ladder: Why Believe It

Experiments, proofs, analyses, studies, and figures should form a ladder of belief.

Typical order:

1. Establish the phenomenon or failure mode.
2. Validate the main effect against strong baselines.
3. Test the mechanism through ablation, proof, or diagnostic analysis.
4. Test generalization, robustness, scale, or transfer.
5. Explain observed boundary conditions or failure cases when they change the supported interpretation. This is conditional, not a required closing move.

Each evidence item must answer a scientific question:

```text
Reviewer question:
Evidence:
Claim supported:
What would be weakened if this evidence failed:
```

### 7. Claim Construction: What Can Be Said

Build a coherent set of claims expressing the whole contribution. Use a central claim with subclaims when that reflects the work, not as a compulsory restriction. Result-dependent claims remain unasserted until their evidence exists.

Central claim format:

```text
[Mechanism or observation] establishes [supported finding] in [studied setting]. Add a material boundary where needed, not as a mandatory trailing disclaimer.
```

Subclaim map:

```text
Subclaim:
Evidence:
Support strength: strong / adequate / weak / absent
Risk:
Revision action:
```

Do not make the claim stronger than the evidence. If the strongest novelty is a benchmark, measurement, empirical finding, or system insight, claim that directly instead of pretending the method is the main novelty.

### 8. Final Takeaway And Boundary

End with what the community should remember:

- new understanding,
- new capability,
- new measurement,
- new design principle,
- new limitation of prior assumptions.

State a boundary only when it changes interpretation or is required. Preserve actual negative findings without apologetic framing; do not append a generic caution or future-work paragraph.

## Compact Core Story Arc

Use this compact arc for ordinary drafting:

1. The scientific origin makes the problem matter.
2. Existing approaches leave a specific knowledge or capability gap.
3. The gap has a root reason, not merely weak numbers.
4. The paper introduces a core insight that addresses that reason.
5. The method implements the insight through necessary modules or formal steps.
6. Evidence addresses the major claims in the order needed to understand the argument.
7. Material assumptions and observed limits are explained where they affect the finding.

## Contribution Types

Identify which contribution types are actually present:

- New scientific question or problem setting.
- New problem formulation.
- New theoretical result.
- New algorithm or model.
- New system architecture.
- New module in an existing pipeline.
- New empirical finding.
- New dataset, benchmark, evaluation protocol, or measurement.
- New interface, workflow, or user study insight.
- New synthesis that resolves a known tension.

Do not imply a stronger contribution type than the evidence supports.

## Section Story Roles

| Section | Main role | Story check |
| --- | --- | --- |
| Abstract | Compress the entire story | Does it include origin, gap, insight, method, and evidence without overclaiming? |
| Introduction | Build scientific tension and reviewer curiosity | Does the challenge naturally lead to the insight and method? |
| Related Work | Position the research | Does each topic establish the relevant capability, assumption, or closest relationship without a forced superiority ending? |
| Method | Make mechanism auditable | Can reviewers see how the method implements the insight? |
| Experiments | Explain the evidence | Does each empirical claim have support, presented in a logically connected order? |
| Figures/Tables | Make evidence inspectable | Does each visual answer one reviewer question? |
| Limitations | Bound claims | Are limitations honest but not self-defeating? |
| Conclusion | Leave final takeaway | Does it restate what the community now knows or can do? |

## Storyline Checks After Each Section

Run these after writing or revising a section:

1. Paragraph roles:
   - Assign each paragraph one role.
   - Remove or merge paragraphs with unclear roles.
2. Claim-evidence map:
   - List every major claim.
   - Point to evidence in experiments, theorem, analysis, user study, or figure.
   - Mark as `supported`, `needs evidence`, or `overclaim`.
3. Term map:
   - List key terms and abbreviations.
   - Ensure the same concept keeps the same name.
   - Define terms before reuse.
4. Cross-section continuity:
   - Check whether Abstract, Introduction, Method, and Experiments tell the same story.
   - Ensure empirical claims in Introduction have applicable evidence; proposed mechanisms and formal or dataset contributions use their appropriate support. Pending tests do not count as validation.
   - Ensure limitations do not contradict contribution claims.
5. Evidence gaps:
   - Identify concrete unsupported claims or actual review findings relevant to the revision.
   - Resolve them through accurate text or existing evidence; isolate decisions requiring new research. Do not invent likely objections.

## Claim-Evidence Matrix

Use this format:

```text
Claim:
Where stated:
Evidence source:
Evidence strength:
Reviewer risk:
Status: supported / needs evidence / overclaim / unclear
Revision action:
```

## Output Templates

Use these visible templates only when the user asks for storyline planning, generation, diagnosis, or rationale. For ordinary drafting, keep them internal and output the requested manuscript text.

### Multi-Expert Candidates

```text
Expert:
Research motivation:
Fundamental scientific question:
Core insight:
Experimental logic:
Method organization:
Expected scientific claim:
Main risk:
```

### Cross-Review Matrix

```text
Candidate:
Scientific Depth:
Novelty:
Logical Coherence:
Narrative Quality:
Claim Strength:
Keep / merge / discard:
Required repair:
```

### Final Fused Storyline

```text
Scientific Origin:
Scientific Tension:
Fundamental Question:
Core Insight:
Method As Consequence:
Evidence Ladder:
Central Claim:
Boundaries:
Section-Level Expression:
Reviewer-Risk Repairs:
```

## Storyline Failure Signals

Revise when you see:

- The method appears before the reader understands the scientific origin.
- The gap is "existing work has not tried X" without a root reason.
- The insight is only a component name or implementation detail.
- The story has several unrelated main claims.
- The paper sells a module but experiments validate only the whole pipeline.
- The evidence order is a checklist rather than a belief ladder.
- The Abstract claims broad improvement but experiments cover a narrow setting.
- Related Work hides the strongest competitor.
- Experiments introduce claims never promised earlier.
- The conclusion adds new claims.
- Figures show many details but no clear reviewer question.
- The final claim is stronger than the supplied evidence.
