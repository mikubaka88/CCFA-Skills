#!/usr/bin/env python3
"""Check the local ICML 2027 submission package."""
from yearly_submission import VenuePolicy, main


POLICY = VenuePolicy(
    name="ICML",
    year=2027,
    package="icml2027",
    bibliography_style="icml2027",
    dimensions=(612, 792),
    size_name="US Letter",
    policy_records=("icml-2027-author-instructions", "icml-2027-author-ai"),
    policy_checked="2026-11-25",
    review_budgets={"research": 8},
    review_modes=(frozenset(),),
    final_modes=(frozenset({"accepted"}),),
    independent_options=frozenset({"nohyperref"}),
    section_titles={
        "impact_statement": frozenset({"impact statement"}),
        "ai_disclosure": frozenset({"ai disclosure statement", "ai use statement"}),
    },
    manual_review=("icml_submission", "Check contribution type, actual AI use, profiles, quotas and reviewer eligibility"),
    manual_final=("icml_camera_ready", "Check final limits and metadata, registration and lay summary"),
    sections_may_follow_references=frozenset({"ai_disclosure"}),
    other_style_pattern=r"icml\d{4}",
)


if __name__ == "__main__":
    raise SystemExit(main(POLICY, __doc__))
