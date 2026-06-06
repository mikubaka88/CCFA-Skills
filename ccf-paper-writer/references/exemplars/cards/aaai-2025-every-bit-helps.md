# Every Bit Helps

Venue/year: AAAI 2025.
Source: `paper_ref/best-papers/aaai-2025-every-bit-helps.pdf`; AAAI OJS `https://ojs.aaai.org/index.php/AAAI/article/view/33507`.
Use when: writing theory, social choice, multi-agent systems, elicitation, approximation, or parameterized optimality papers.

## Story Pattern

The paper motivates an abstract problem through a concrete allocation scenario, then converts the scenario into a formal tension: ordinal rankings are easy to elicit but lose utility intensity. The central question is parameterized by the number of value queries, and the contribution is to close the gap between known upper and lower bounds.

## Abstract Moves

- Define the formal problem and why weaker information is used.
- State the inefficiency measure before stating the result.
- Tie new bounds to a prior result and a prior lower bound.
- End with the "settles open questions" implication.

## Introduction Moves

- Use a realistic example before formal notation.
- Introduce the metric of success early.
- Give a small history of known query regimes.
- State the exact missing regime as a question.
- Use tables to map previous and new bounds.

## Method Moves

- Put notation after the motivation is clear.
- Separate model definitions from theorem statements.
- Use theorem names and tables as navigation anchors.

## Evidence Moves

- For theory papers, evidence is proof structure plus tightness against lower bounds.
- Emphasize optimality only where upper and lower bounds match.
- Make assumptions visible before theorems so reviewers can audit scope.

## Reusable Techniques

- Turn a parameter sweep into a story: from zero queries to constant queries to logarithmic queries.
- Use examples to make a formal objective intuitive before proving results.
- Present contribution tables early for quick reviewer orientation.

## User Notes

Use this card when the user's result "settles" or tightens a known regime. If the paper only improves constants, avoid the same level of closure language.

## Do-Not-Copy Boundary

Do not reuse the office/allocation example, distortion framing, or optimality language unless the user's paper has matching formal guarantees.
