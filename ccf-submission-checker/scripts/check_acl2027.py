#!/usr/bin/env python3
"""Check the local ACL 2027 submission package."""
from yearly_submission import VenuePolicy, main


POLICY = VenuePolicy(
    name="ACL",
    year=2027,
    package="acl",
    bibliography_style="acl_natbib",
    dimensions=(595.276, 841.89),
    size_name="A4",
    policy_records=("acl-2027-main-cfp", "acl-arr-cfp"),
    policy_checked="2026-11-25",
    review_budgets={"long": 8, "short": 4},
    review_modes=(frozenset({"review"}),),
    final_modes=(frozenset(), frozenset({"final"})),
    independent_options=frozenset({"hyperref", "nohyperref"}),
    section_titles={"limitations": frozenset({"limitations"})},
    manual_review=("arr_submission", "Check cycle, Responsible NLP answers, AI assistance, profiles and service registration"),
    manual_final=("acl_commitment", "Check the committed ARR version, decision, author list and final instructions"),
    extra_anonymous_metadata=frozenset({"anonymous acl submission"}),
)


if __name__ == "__main__":
    raise SystemExit(main(POLICY, __doc__))
