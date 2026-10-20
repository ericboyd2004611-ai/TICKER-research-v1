# Edition B — AI-generated working draft

**Current Edition B: [research-evolution.md](research-evolution.md).**
This earlier planning draft is superseded by the contract correction and the
current research-evolution PDF. Flat-fee outputs and perpetual terminal credit
are no longer used. Retained below as planning context only.

Not a final submission. Prepared with Codex on October 19, 2026. All proposed
interpretations below require the student's review and independent checks.
The actual submitted Edition A remains the baseline; this file does not replace it.

## Proposed decision framing

Advise a committee with no position whether to initiate, defer, or decline an SMR
investment. Retain watch/defer as the student's starting thesis, pending completion
of a sourced valuation range. No numerical fair-value conclusion is established.

## Proposed changes to reconcile with the actual Edition A

| Item | Earlier material supplied in chat | Proposed Edition B treatment | Reason |
|---|---|---|---|
| Information date | December 2025 date alongside later disclosures | September 1, 2026 close | Align the evidence boundary; disclose later-than-lab timing |
| Historical inputs | Annual baseline and subsequent company report | Separate reported observation dates from analysis date | Avoid presenting stale balances as contemporaneous |
| Share basis | Weighted-average EPS shares identified as historical only | Dated economic-interest and award bridge | Match a stock of equity value with ownership at a point in time |
| Valuation method | Earlier negative-FCFF exercise; services-only downside | Keep downside as one case; build commercialization separately | Existing cases do not establish full going-concern value |
| Position | Watch/defer | Provisionally unchanged | Completion and review of evidence are required before a final call |

## Commercialization model to build next

Implementation update: `build_scenarios.py` and `src/commercialization.py` now
execute delayed, central and stronger cases with an explicit FCFF bridge,
advance PMA payments, working capital, funding diagnostics and normalized
terminal cash flow. `output/commercialization-report.md` shows the results.
All forecast assumptions remain AI-generated and unapproved. The financing
diagnostic is not a second dilution deduction from the FCFF valuation.

Use separately labeled analyst assumptions for module delivery dates, units,
net selling economics, milestone payments, recurring services, operating costs,
reinvestment, taxes, working capital and financing. Preserve the distinction
between a commercial opportunity, binding order, delivery and cash collection.

Create delayed, central and stronger-execution cases. Assign no probabilities
until the student can explain their evidence basis. If contract economics cannot
be sourced, use explicit break-even/reverse-valuation scenarios and identify
what would have to become true; do not present assumed economics as fact.

The old downside's $0.1063/share is a conditional annual-model result, not a
September fair-value estimate or downside floor. Do not combine it mechanically
with the new financial starting point.

## Student review fields

Pending: disposition of this draft, independently checked inputs, accepted or
rejected assumptions, final recommendation, monitoring thresholds and committee ask.
The required locked prediction remains a separate student-authored AI-off exercise.
