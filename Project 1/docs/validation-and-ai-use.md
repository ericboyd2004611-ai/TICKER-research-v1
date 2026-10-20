# Validation and AI use

**AI-GENERATED DRAFT | October 19, 2026 | Student review pending**

## Decision, version and boundary

Proposed watch/defer for a committee with no SMR position. Analysis boundary:
September 1, 2026 close, later than the pictured Edition A lab time. Research and
draft construction occurred October 19. No September authorship is claimed.
The working record matches the generated draft PDF when rebuilt.

Core environment: Python 3.10+ and standard library. PDF rebuilding uses optional
packages in requirements-docs.txt. Input and source SHA-256 hashes are embedded
in output/commercialization-output.json. The package file inventory provides
file hashes; no Git freeze or LMS receipt is invented.

## Data and convention ledger

Historical observations, units, dates and filing locators are in
docs/verified-starting-point-draft.md and data/research-inputs.json. These are
reported June balances, June awards and July cover shares, not September balances.
The model's assumed $40m lag-period cash use reduces cash and opening equity.
The unrestricted liquidity sum adds each selected category once; restricted
balances are outside it and are not subtracted a second time.

Current valuation uses consolidated economic interests with a gross award
allowance. No book-NCI subtraction is made again. Gross options with no proceeds
are an allowance, not a treasury-stock-method calculation. Equity funding affects
liquidity; its fixed-price dilution diagnostic is separate from FCFF valuation.

Operating commitments and leases are assumed inside forecast costs. This requires
a contract-by-contract mapping before a final value. Additional claims default
to zero as a scenario condition, not a legal conclusion. The engine uses economic
PMA expense timing, not GAAP revenue recognition or a tax opinion.

## Source check and assistant correction

The assistant opened the PMA exhibit, Sections 1(c), 1(d), 1(g), and found the
annual escalation floor and redacted cap. Earlier flat-fee outputs were preserved
and superseded. The revised fee scale is inferred from the 2025 cash installment
and installment allocation. Future fees grow at the 5% floor; higher CPI is not
forecast. Lead-year timing simplifies contractual slots, invoices and contingencies.

An unsupported low-growth perpetuity is disabled. Default operating exit value
is six times positive normalized next-year EBITDA after full milestone fees.
The multiple is an analyst assumption, not a peer benchmark. Zero/4x/6x/8x/10x
alternatives are computed. Negative EBITDA receives zero operating sale value,
not a liquidation appraisal. Quantitative peer validation remains unresolved.

## Validation register

| Claim | Check | Actual disposition | Evidence |
|---|---|---|---|
| Cash is not counted twice | No-operations known answer | PASS | tests/test_commercialization.py |
| Cash follows financial flows | Independent cumulative cash budget | PASS | same test file |
| Statements reconcile | Assets equal claims; equity rolls from income/funding | PASS | same test file |
| Sunk tranche is not paid twice | Single-cohort hand formula with escalation | PASS | same test file |
| Contract escalation matters | Compare escalated vs flat fees | PASS | same test file |
| Funding is not double charged | Financing-price change affects diagnostic shares only | PASS | same test file |
| Margin stress worsens economics | Unfloored equity falls; funding does not fall | PASS | same test file |
| Discount dates are explicit | Recompute actual-day discount factors | PASS | same test file |
| Invalid assumptions fail | Reject bad rates, deliveries and nonfinite inputs | PASS | same test file |
| Unsupported terminal path fails | Reject growth below fee escalation if enabled | PASS | same test file |
| UI displays executed values | Compare CLI summary with frozen output | PASS | tests/test_application.py |
| UI detects stale evidence | Alter copied input and require error | PASS | same test file |
| Invalid year is actionable | Require nonzero exit and valid range | PASS | same test file |
| Old downside invariants | Cash budget, bridge, funding, claims, broken balance | PASS: five checks | tests/test_smr_proforma.py |

Run python3 verify_project.py. Current suite: 20 tests passed. Tests demonstrate
these specific invariants, not the accuracy of commercial forecasts.

## Failure retained and diagnosed

After fee escalation was corrected, one margin test initially failed because it
required strictly lower floored share value even when both outcomes were zero.
Diagnosis: limited-liability flooring masks a worse underlying equity result.
The corrected test requires lower unfloored equity, nonincreasing floored value,
and no reduction in funding. No finance input was tuned to force a passing test.

## Changed-input results - AI-generated, not the locked exercise

The three five-percentage-point module-margin stresses and the full price/discount
grid are preserved in output/commercialization-output.json. Stronger execution
moves from $6.77 to
$3.34/share including the assumed operating sale.
The watch/defer proposal remains because contract pricing and the assumed exit
are unverified, not because the automated test establishes a final price target.

## Reproducibility and access

evidence/clean-run.md records an actual assistant rehearsal in a fresh temporary
directory with site packages disabled. Its command outputs and JSON comparisons
are preserved. This is not a claimed outside-person cold run. A real reviewer
must record their own first failure/resolution if the assignment requires it.
Repository publication state is recorded in evidence/repository-status.json.
Instructional-team and video access remain separate checks; they are not inferred
from an assistant's successful git connection.

## Existing NuScale Lab 11 changed-input evidence

The exercise is not classified as absent. Existing records include a supplied
prediction, input/model snapshot, changed cost-growth input, before/after output,
and reconciliation. They are preserved in evidence/lab11-smr/ and mapped in
docs/lab11-evidence-map.md. Cost growth changes from 0% to 2%; 2030 FCFE moves
from -174.639m to -196.199m. The recorded explanation attributes the 21.560m decline
to 20.028m extra costs and 1.532m lost investment income. Watch/defer remains.

The saved narrative does not independently establish the prediction-lock timestamp
or AI boundary during the original run. This is a documentary check on existing
work, not an automatic requirement to repeat it. Joby comparison evidence is not
substituted for NuScale ownership. No timestamp or attestation is invented.

## Named AI-use register

Tool: Codex; exact model version was not exposed in the task surface. Interaction
date: October 19, 2026. Material uses: workspace audit, source navigation, code,
scenario assumptions, tests, generated outputs, memo/research/validation drafts,
PDF layout, application interface and rehearsal scripts.

Assistant disposition: modified the flat-fee proposal after checking the contract;
withdrew unsupported perpetual terminal credit; qualified every module-price and
delivery assumption. Primary-source checks and deterministic arithmetic are
assistant work. Student accept/modify/reject decisions and independent checks are
still pending and must be recorded truthfully.

Inherited Week 5 work is preserved. Its original AI history must be supplied by
the student. This record does not infer authorship from a test pass, file date,
lab grade or code style. The user's account of grammar assistance is retained as
their account, not independently verified history.

## Limitations, monitoring and kill rules

See docs/monitoring-policy.md. The full event/share audit, net contract economics,
invoice timing, investment liquidity, authorized share capacity, contingent/tax
claims and residual valuation remain open. Assumed equity issuance is not
committed capacity, and end-year cash checks cannot establish intra-year solvency.
No default, legal liability or certain loss is inferred from a model flag.

## Source references

PMA: https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm
June 10-Q: https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm
Source ledger and boundary review: docs/verified-starting-point-draft.md; docs/source-review.md.
