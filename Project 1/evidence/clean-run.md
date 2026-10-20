# Assistant clean-directory rehearsal

This is an assistant-run reproducibility check, not an outside human review.
Timestamp: 2026-10-20T01:01:47.755785+00:00
Python: 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)]

Commands run with -I -S: isolated mode, with site-package loading disabled.

## python3 -I -S build_scenarios.py

```text
Delayed: illustrative $0.00/share; net funding $2,631.7m
Central illustrative: illustrative $0.00/share; net funding $2,608.0m
Stronger execution: illustrative $6.77/share; net funding $42.5m
Saved report, JSON and CSV in output/. Not a final fair-value range.

```

## python3 -I -S research_bridge.py

```text
Cash and investments: USD 1,892.997 million
June if-converted economic interests: 429,701,540
Gross-award proxy: 439,138,602; not treasury-stock-method dilution
Saved output/research-bridge.json; arithmetic checks passed.

```

## python3 -I -S analysis.py

```text
Exported output/downside-report.md and output/downside-output.json
Conditional downside value/share: 0.1063
Project incomplete: this result is not a full company valuation.

```

## python3 -I -S prepare_drafts.py

```text
Generated memo, research-evolution draft and three rehearsal scripts.

```

## python3 -I -S verify_project.py

```text
test_changed_inputs_cannot_silently_display_old_values (test_application.ApplicationChecks.test_changed_inputs_cannot_silently_display_old_values) ... ok
test_summary_uses_current_frozen_results (test_application.ApplicationChecks.test_summary_uses_current_frozen_results) ... ok
test_year_outside_forecast_is_actionable_error (test_application.ApplicationChecks.test_year_outside_forecast_is_actionable_error) ... ok
test_contractual_fee_escalation_reduces_value (test_commercialization.CommercializationChecks.test_contractual_fee_escalation_reduces_value) ... ok
test_discount_timing_and_bridge (test_commercialization.CommercializationChecks.test_discount_timing_and_bridge) ... ok
test_exit_multiple_adds_only_discounted_operating_sale_value (test_commercialization.CommercializationChecks.test_exit_multiple_adds_only_discounted_operating_sale_value) ... ok
test_funding_price_changes_diagnostic_dilution_not_fcff_value (test_commercialization.CommercializationChecks.test_funding_price_changes_diagnostic_dilution_not_fcff_value) ... ok
test_invalid_inputs_fail (test_commercialization.CommercializationChecks.test_invalid_inputs_fail) ... ok
test_investor_value_does_not_charge_operating_losses_twice (test_commercialization.CommercializationChecks.test_investor_value_does_not_charge_operating_losses_twice) ... ok
test_linked_economic_statements_reconcile_without_equity_plug (test_commercialization.CommercializationChecks.test_linked_economic_statements_reconcile_without_equity_plug) ... ok
test_margin_shock_reduces_value_and_increases_funding (test_commercialization.CommercializationChecks.test_margin_shock_reduces_value_and_increases_funding) ... ok
test_no_operations_equals_cash_less_explicit_claims (test_commercialization.CommercializationChecks.test_no_operations_equals_cash_less_explicit_claims) ... ok
test_standalone_cash_budget_matches_every_year (test_commercialization.CommercializationChecks.test_standalone_cash_budget_matches_every_year) ... ok
test_sunk_first_tranche_is_not_paid_twice (test_commercialization.CommercializationChecks.test_sunk_first_tranche_is_not_paid_twice) ... ok
test_unsupported_terminal_growth_cannot_ignore_fee_escalation (test_commercialization.CommercializationChecks.test_unsupported_terminal_growth_cannot_ignore_fee_escalation) ... ok
test_additional_claim_reduces_distribution_and_equity_cannot_be_negative (test_smr_proforma.SMRChecks.test_additional_claim_reduces_distribution_and_equity_cannot_be_negative) ... ok
test_bad_balance_is_not_silently_plugged (test_smr_proforma.SMRChecks.test_bad_balance_is_not_silently_plugged) ... ok
test_cash_without_interest_matches_independent_cash_budget (test_smr_proforma.SMRChecks.test_cash_without_interest_matches_independent_cash_budget) ... ok
test_insufficient_funding_is_rejected (test_smr_proforma.SMRChecks.test_insufficient_funding_is_rejected) ... ok
test_terminal_bridge_does_not_double_count_cash_or_operating_losses (test_smr_proforma.SMRChecks.test_terminal_bridge_does_not_double_count_cash_or_operating_losses) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.135s

OK

```

## python3 -I -S app.py summary

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

Scenario              DCF value/share  Net funding  First funding
--------------------  ---------------  -----------  -------------
Delayed               $0.00            $2,631.7m    2032         
Central illustrative  $0.00            $2,608.0m    2031         
Stronger execution    $6.77            $42.5m       2030         

Ask: retain on watchlist; require verified net contract economics and a fundable cash plan.
Prices, margins and exit multiple are assumptions. Funding conditions must also be satisfied.

```

## python3 -I -S app.py scenario --scenario stronger --year 2030

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

Stronger execution
Year  Modules  Revenue   PMA       FCFF     Funding  End cash  BS gap
----  -------  --------  --------  -------  -------  --------  ------
2030  12       3,264.30  1,017.87  -240.28  8.59     50.00     0.00  

Financing shares are a separate fixed-price diagnostic; not a second DCF dilution deduction.
Existing-holder exit PV/share: $5.24
Share-capacity proxy exceeded: False
Funding subscription checks: [{'year': 2030, 'assumed_issue_price': 6.447, 'modeled_value_at_raise': 9.606886110079529, 'subscription_supported_by_model': True}, {'year': 2031, 'assumed_issue_price': 6.447, 'modeled_value_at_raise': 11.046862212922727, 'subscription_supported_by_model': True}]

```

## python3 -I -S app.py sensitivity

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

Discount rate  Module base price  Conditional DCF/share  Net funding
-------------  -----------------  ---------------------  -----------
10%            $150m              $0.00                  $4,258.1m  
10%            $200m              $0.00                  $2,608.0m  
10%            $250m              $2.21                  $1,093.5m  
15%            $150m              $0.00                  $4,258.1m  
15%            $200m              $0.00                  $2,608.0m  
15%            $250m              $2.11                  $1,093.5m  
20%            $150m              $0.00                  $4,258.1m  
20%            $200m              $0.44                  $2,608.0m  
20%            $250m              $2.15                  $1,093.5m  

Five-percentage-point module-margin stress:
Scenario              Stressed conditional DCF/share  Stressed funding
--------------------  ------------------------------  ----------------
Delayed               $0.00                           $2,953.4m       
Central illustrative  $0.00                           $3,730.7m       
Stronger execution    $3.34                           $721.6m         

```

## python3 -I -S app.py exit

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

Operating exit assumption: end-2036 sale; multiple of normalized 2037 EBITDA after full fees.
Scenario              Multiple  DCF/share  Existing-holder exit PV/share
--------------------  --------  ---------  -----------------------------
Delayed               0x        $0.00      $0.01                        
Delayed               4x        $0.00      $0.01                        
Delayed               6x        $0.00      $0.01                        
Delayed               8x        $0.00      $0.01                        
Delayed               10x       $0.00      $0.01                        
Central illustrative  0x        $0.00      $0.01                        
Central illustrative  4x        $0.00      $0.01                        
Central illustrative  6x        $0.00      $0.01                        
Central illustrative  8x        $0.00      $0.01                        
Central illustrative  10x       $0.00      $0.01                        
Stronger execution    0x        $2.27      $0.81                        
Stronger execution    4x        $5.27      $3.77                        
Stronger execution    6x        $6.77      $5.24                        
Stronger execution    8x        $8.27      $6.72                        
Stronger execution    10x       $9.77      $8.20                        

The multiple is an analyst assumption; it is not a verified peer or buyer quote.

```

## python3 -I -S app.py reverse

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

One-input reverse scenario: SOLVED_ILLUSTRATIVE
Reference share price: $9.21
Required 2026-base supplier revenue/module: $386.5m
Held fixed: central delivery cadence, margin, costs, taxes, working capital, fee escalation and discount rate.
The required price is an assumption hurdle; the redacted contract cap is not validated.

```

## python3 -I -S app.py sources

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

Historical financial inputs and precise locators: docs/verified-starting-point-draft.md
Research, boundary and contract correction: docs/source-review.md
Editable assumptions: data/commercialization-scenarios.json
2026 quarterly filing: https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm
2025 PMA: https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm
All module prices, margins and delivery schedules are unapproved analyst assumptions.

```

## python3 -I -S app.py monitoring

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

# Monitoring policy - AI-generated proposal

Created October 19, 2026 for a retrospective September 1 analysis. This was not
a precommitted September 1 rule. Student review and adoption are pending.

Decision user: an investment committee with no existing SMR position.
Proposed action: WATCH / DEFER. No authorization to buy or short is requested.

Owner: student acting as equity analyst. Review each quarterly filing and within
five business days of a material contract, financing or delivery announcement.

Reconsider initiation only when ALL conditions hold:
- Binding orders disclose enough enforceable economics to reconstruct net module
  contribution after milestone payments, supplier costs and working capital.
- The updated quarterly cash plan remains above an analyst-selected $50m cash
  buffer without unsupported funding, including a 20% operating-cost stress and
  12-month delivery delay. The buffer is not a disclosed covenant.
- A sourced valuation including a defensible residual business value exceeds the
  contemporaneous stock price by at least 25%. This margin of safety is a proposed
  analyst rule, not a fact about the company or a calibrated optimal threshold.

Escalate to DO NOT INITIATE if financing needed within 12 months cannot be
supported by committed capacity, or if verified net contract contribution is
nonpositive after the required fees. Withdraw any price claim when the share
bridge or source boundary cannot be reconciled. A liquidity flag is not a
covenant breach, payment default or realized loss.

The current envelope uses an assumed operating exit, with zero and alternative
multiples shown separately. It cannot satisfy the valuation condition until its
contract economics, funding conditions and exit assumption are supported.


```

## python3 -I -S app.py readiness

```text

NUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT
Boundary: September 1, 2026 close | USD millions except USD/share
Proposed action: WATCH / DEFER. Student review pending.
Conditional scenarios with an assumed operating exit; not fair value established by contracts.

# Project 1 handoff

The local application, calculations, executed output and AI-generated document
drafts are prepared for review. This is NOT a complete submission or an approved
fair-value estimate. Do not upload the draft package as if all evidence existed.

## Open first

- output/pdf/Decision-Memo-DRAFT.pdf
- output/commercialization-report.md
- docs/source-review.md
- README.md

## Run

From the Project 1 directory, with Python 3.10 or later:

```sh
python3 build_scenarios.py
python3 app.py --interactive
python3 verify_project.py
```

## Work the assistant completed

- Three editable commercialization scenarios and a reverse economic hurdle.
- Linked economic income, balance-sheet and cash-flow statements, with a
  reconciled equity roll-forward and an explicit enterprise-to-equity bridge.
- Advance milestone payments with the contract escalation floor, financing
  diagnostics, margin stress and price/discount sensitivities.
- A frozen-output terminal interface that rejects stale input/source hashes.
- Review drafts for the memo, research evolution, validation/AI use and videos.
- Local reproducibility checks, PDF rendering checks, a manifest and archive.

The original flat-fee scenario output is preserved as superseded evidence.
The unsupported perpetuity is replaced by an explicit assumed operating sale,
with zero/4x/6x/8x/10x sensitivity. Results are conditional valuations, not verified
market price targets. Funding-capacity and subscriber-economics checks are included.

## Evidence still required from the student

1. Edition A is included as student-supplied text in docs/edition-a-submitted-text.txt
   and the Research-Evolution draft. The student reports the professor approved
   this submission format. No separate original Edition A PDF is required here.
   The screenshots support the lab attempt, grade and time.
2. Existing NuScale Lab 11 prediction, snapshot, results and reconciliation are
   included under evidence/lab11-smr/. See docs/lab11-evidence-map.md. Confirm the
   original timing and tool boundary from the original lab record; a fresh exercise
   is not automatically required.
3. Personal review of material sources, assumptions, model logic and AI dispositions.
4. Three actual recordings, corrected transcripts, real URLs/durations and actual
   timestamp indices. Rehearsal scripts are not transcripts.
5. Repository publication state and the actual source commit are recorded in
   evidence/repository-status.json. Instructional-team access still requires
   confirmation; a successful git connection alone does not establish that access.
6. A real outside-user cold run if required. The assistant's isolated run is
   documented honestly as an assistant rehearsal, not another person's work.

## Finance limitations that remain open

Complete the intervening-event/share audit; verify contract prices, net margins,
invoice/slot timing, investment availability, authorized-share capacity and
contingent/tax claims; validate the assumed operating exit against market evidence. Those facts
cannot be manufactured from redacted terms. No quantitative peer valuation is
claimed. The proposed watch/defer action reflects this evidence boundary.

The syllabus lists October 19, 2026 at 11:59 PM Eastern as the Project 1 deadline;
Brightspace controls detailed requirements and any announced changes.


```

## Result

PASS: all commands succeeded; all three JSON outputs matched byte for byte.
First clean-run failure: none. Outside-user review remains outstanding.
