# Venue Adapters

Use this file after identifying the target CCF A family. Treat it as a writing-priority selector, not as a substitute for the official call for papers.

## Universal CCF A Review Priorities

For any CCF A target, make these visible:

1. Contribution: what new knowledge, capability, method, result, or theoretical insight does the paper add?
2. Significance: why should this venue's audience care now?
3. Soundness: are assumptions, derivations, implementation details, and experiments technically credible?
4. Evidence: does each major claim have a corresponding experiment, proof, analysis, or user study?
5. Clarity: can an expert reviewer reconstruct the problem, method, and evidence without guessing?
6. Positioning: are strongest prior methods, baselines, and limitations handled honestly?
7. Reproducibility: are datasets, metrics, protocols, artifacts, hyperparameters, and evaluation settings sufficiently specified?

## AI, ML, CV, NLP

Target venues include AAAI, NeurIPS, ICML, ICLR, ACL, CVPR, ICCV.

Writing emphasis:

- State the core challenge and contribution early; reviewers should not wait until Method to learn what is new.
- Connect insight -> mechanism -> measurable benefit.
- Make the contribution sound non-obvious without hiding concrete implementation.
- Use strong baselines, ablations, and clear claim-evidence alignment.
- For CV and multimodal papers, treat figures and qualitative results as primary evidence.
- For NLP papers, clarify task/data assumptions, linguistic or semantic claims, annotation quality, evaluation validity, and ethical concerns.
- For ML papers, distinguish empirical novelty from conceptual, theoretical, or algorithmic novelty.

Common reviewer questions:

- Is the contribution new enough for this venue?
- Are gains meaningful across datasets and settings?
- Are comparisons fair and recent?
- Are ablations enough to justify the proposed modules?
- Does the method scale and generalize?
- Are limitations and failure modes acknowledged?

## Data, Mining, Retrieval

Target venues include SIGMOD, VLDB, ICDE, SIGKDD, SIGIR.

Writing emphasis:

- Make the problem setting concrete: workload, data scale, query/user scenario, deployment constraint, or retrieval task.
- Explain why existing systems or algorithms fail under this setting.
- Show both effectiveness and efficiency when relevant.
- Describe indexes, data structures, optimization objectives, pipelines, or system components in enough detail to reproduce.
- Use large-scale or realistic datasets; avoid toy-only evidence.
- Tie experiments to claims about accuracy, latency, throughput, scalability, robustness, or user utility.

Common reviewer questions:

- Is the problem important and realistic?
- Does the method beat strong baselines under fair protocol?
- Does it scale?
- Are system tradeoffs and complexity clear?

## Systems, Architecture, Networks, Storage

Target venues include SOSP, OSDI, NSDI, SIGCOMM, MobiCom, INFOCOM, FAST, ASPLOS, ISCA, MICRO, HPCA, SC, EuroSys, HPDC, PPoPP, ATC.

Writing emphasis:

- Start from a real bottleneck, workload, deployment pain, or architectural constraint.
- Make design goals explicit before introducing the design.
- Explain why simple alternatives fail.
- Describe implementation details, system architecture, assumptions, and overheads.
- Use realistic workloads, ablations, sensitivity studies, and end-to-end evaluation.
- Present failure modes and operational boundaries honestly.

Common reviewer questions:

- Is this a real systems problem or a narrow benchmark artifact?
- Are assumptions realistic?
- Does the design improve the right bottleneck?
- Is implementation detail sufficient?
- Are performance gains robust under changing workloads?

## Security And Cryptography

Target venues include CCS, S&P, USENIX Security, NDSS, CRYPTO, EUROCRYPT.

Writing emphasis:

- Define threat model, attacker capability, defender assumptions, and scope before claims.
- For measurement or attack papers, show real-world impact and responsible handling.
- For defenses, explain security guarantees, deployment constraints, bypasses, and false positives/negatives.
- For cryptography, prioritize formal definitions, security proof structure, assumptions, and theorem readability.
- Include ethics, disclosure, data handling, and harm-reduction notes when relevant.

Common reviewer questions:

- Is the threat model meaningful?
- Is the attack or defense novel and practically important?
- Are claims over-scoped?
- Are ethics and disclosure handled?

## Software Engineering, Programming Languages, Formal Methods

Target venues include ICSE, FSE, ASE, ISSTA, PLDI, POPL, OOPSLA, FM, CAV, LICS.

Writing emphasis:

- Define the program/property/language/tool problem precisely.
- Explain the gap in existing tools, analyses, proofs, or developer workflows.
- For empirical SE, describe datasets, tasks, baselines, metrics, and threats to validity.
- For PL/FM/theory-heavy work, include intuitive proof roadmaps before dense formalism.
- Make soundness, completeness, scalability, and usability tradeoffs explicit.

Common reviewer questions:

- Is the formal claim correct and useful?
- Is the tool or technique evaluated on meaningful programs or benchmarks?
- Are threats to validity explicit?

## HCI, CSCW, Ubiquitous Computing

Target venues include CHI, CSCW, UbiComp, UIST.

Writing emphasis:

- State human problem, population, context, and design goal before system details.
- Connect research questions to study design.
- Report participants, procedures, measures, analysis, limitations, and ethics clearly.
- For systems, make interaction design and user value central, not just technical novelty.
- For qualitative work, explain coding, themes, triangulation, and researcher reflexivity when applicable.

Common reviewer questions:

- Are research questions important?
- Is the study design appropriate?
- Are claims supported by data?
- Are ethical and population limitations handled?

## Graphics, Visualization, Multimedia

Target venues include SIGGRAPH, IEEE VIS, ACM MM, VR.

Writing emphasis:

- Make visual or perceptual improvement inspectable through high-quality figures.
- Explain representation, rendering, interaction, or multimedia pipeline clearly.
- Combine quantitative metrics with qualitative examples and user/perceptual studies when needed.
- Highlight cases where the method changes what users can see, understand, or do.

Common reviewer questions:

- Is the visual result materially better?
- Are comparisons fair and high quality?
- Does the method generalize beyond cherry-picked examples?

## Theory

Target venues include STOC, FOCS, SODA, LICS, CAV.

Writing emphasis:

- State problem, model, assumptions, and result precisely.
- Put theorem contributions early, with intuition before proof detail.
- Explain why the result is surprising or technically difficult.
- Relate to known lower bounds, barriers, algorithms, proof techniques, and open problems.

Common reviewer questions:

- Is the theorem correct and nontrivial?
- Does the result improve or clarify the state of the art?
- Is the proof readable enough to audit?

## Venue Plan Template

Use this compact plan before drafting:

```text
Target venue:
Venue family:
Audience expectation:
Likely reviewer questions:
Contribution type:
Evidence package:
Risk points:
Writing priorities:
Reference papers to analyze:
```
