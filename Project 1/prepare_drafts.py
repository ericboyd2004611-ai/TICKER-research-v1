"""Generate review drafts from executed output; never invent personal evidence."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    p = json.loads((ROOT / 'output/commercialization-output.json').read_text())
    results = p['results']
    values = [r['value_per_share'] for r in results]
    table = '\n'.join(f"| {r['name']} | ${r['value_per_share']:.2f} | ${r['funding_net_m']:,.1f}m | {r['first_funding_year'] or 'None'} |" for r in results)
    envelope = f'${min(values):.2f}-${max(values):.2f}'
    hurdle = p['reverse_scenario']['solved_module_price_m']
    common_label = '**AI-GENERATED DRAFT | October 19, 2026 | Student review pending**'
    memo = f'''# NuScale (SMR): watch / defer

{common_label}

## Decision and committee ask

Retain SMR on the watchlist; do not initiate a position on this evidence package.
The intended user is a long-horizon, high-risk-tolerance investment committee with
no current holding. Request a contract-economics and financing review before any
purchase decision. This is an AI-generated proposal based on the student's stated
starting thesis, not an approved recommendation or order to trade.

## What the application establishes

The locally runnable component connects editable commercial assumptions to
linked economic statements, FCFF, an enterprise-to-equity bridge, and a funding
diagnostic. The proposed analysis boundary is September 1, 2026 close. Historical
observations retain their actual measurement dates; pre-valuation cash use is
explicitly assumed rather than reported.

| Scenario | Conditional DCF/share | Net funding needed | First funding year |
|---|---:|---:|---|
{table}

The {envelope} envelope includes an assumed end-2036 operating sale at six times
normalized next-year EBITDA after full milestone fees. This is an analyst
assumption, not a verified peer or buyer quote. Zero/4x/6x/8x/10x exit sensitivities
are included. Zero modeled equity is not proof the stock is worthless; assumed
sale proceeds do not establish market value. No probability-weighted target is assigned.

## Strongest decision evidence

The contract exhibit requires at least 5% annual milestone-payment escalation
and redacts the supplier-price cap [1]. That weakens the first AI draft, which
held fees flat. The corrected model applies the escalation floor. Module prices,
margins, payment leads, and delivery schedules remain scenario assumptions.
Commercial progress alone does not resolve the net economics of a supplier order.

## Material sensitivities

The stronger-execution case is the only supplied case with positive modeled
equity value. A five-percentage-point module-margin reduction cuts it from
${results[2]['value_per_share']:.2f} to ${p['margin_stress'][2]['value_per_share']:.2f}/share
and increases net funding from ${results[2]['funding_net_m']:,.1f}m to
${p['margin_stress'][2]['funding_net_m']:,.1f}m. Under the central schedule, the
one-input reverse calculation requires about ${hurdle:.0f}m of 2026-base supplier
revenue per module to reproduce $9.21 with the assumed operating exit. That is a model
hurdle, not evidence of a feasible contract price.

## Conditions, monitoring and reversal

Proposed analyst policy: reconsider initiation only with verified binding net
contract economics, a quarterly cash plan that maintains a $50m buffer under a
20% operating-cost shock and 12-month delivery delay, and a sourced full valuation
at least 25% above the then-current market price. The buffer and 25% hurdle are
analyst choices, not covenants or company guidance.

The student analyst monitors each quarterly filing and material contract or
financing announcement, reviewing the latter within five business days. Escalate
to do-not-initiate if a 12-month funding gap has no supportable financing route
or verified net contract contribution is nonpositive. Withdraw valuation claims
if sources or ownership cannot reconcile. A cash-model flag is not a default.

## Limits and evidence

The package does not yet verify every intervening filing, reconcile all award and
contingent-claim terms, establish a quantitative peer valuation, or support a
market exit. Fixed-price dilution is shown separately and is not deducted
again from FCFF value; a separate terminal-payoff method values that financing
condition. Existing NuScale Lab 11 prediction/results are preserved and mapped.
Their original timing/tool-boundary evidence still requires confirmation. See
Validation-and-AI-Use for named AI use, source corrections and actual checks.

Sources: [1] SEC PMA, Sections 1(c), 1(d), 1(g):
https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm
[2] Financial source ledger: docs/verified-starting-point-draft.md.
[3] Executed analysis: output/commercialization-output.json and report.
'''
    (ROOT / 'docs/decision-memo.md').write_text(memo)
    edition_a_paragraphs = '\n\n'.join((ROOT / 'docs/edition-a-submitted-text.txt').read_text().splitlines())
    research = f'''# Research evolution

{common_label}

## Edition A baseline status

The student identifies the Lab 03 research-baseline text supplied in this
conversation as Edition A and reports that the professor approved submitting it
as text instead of a PDF. That approved format is used here; no separate original
Edition A PDF is requested. The text is preserved in docs/edition-a-submitted-text.txt.
Its existing wording, including its TEST ARTIFACT label, is retained rather than edited.

Two screenshots in docs show Lab 03 Attempt 1, a 25/25 grade, and September 1,
2026, 2:31-2:34 PM. They corroborate the dated lab attempt and grade. The format
approval and identification of the submitted text are the student's account;
the assistant has not independently retrieved the Brightspace answer or approval.

A correction belongs after the preserved baseline, never inside a rewritten
baseline. This document packages the accepted text format; it does not recreate
an earlier PDF or invent a separate submission receipt.

## Edition A - student-supplied submitted text

{edition_a_paragraphs}

## Proposed dated correction addendum

October 19, 2026: the supplied baseline's December 31, 2025 valuation date relied
on a later-published annual report. Edition B uses September 1, 2026 close as an
explicit retrospective analysis boundary. This close follows the lab's pictured
end time and must not be represented as information available during that lab.

The first commercialization draft also omitted contractual payment escalation.
That assistant error is corrected in the current engine and retained in the
superseded evidence directory. Its former $0.51/$1.36/$8.41 values are obsolete.
The first growing-perpetuity assumption was unsupported and has been disabled.
The current model instead uses a six-times operating exit assumption, with
zero/4x/6x/8x/10x alternatives. This completes a conditional valuation while
retaining uncertainty about the market price of the residual business.

## Edition B: current decision and user

Proposed watch/defer for an investment committee with no position. The student
originally described a high-risk-tolerance, long-horizon analyst. No approved buy
recommendation is inferred from unverified assumptions or omitted residual value.

## A-to-B reconciliation proposal

| Item | Earlier supplied material | Current draft | Driver and evidence |
|---|---|---|---|
| Thesis | Watch/defer | Provisionally unchanged | Student initial view plus AI-assisted contract and model review |
| Evidence date | December 2025 with later disclosures | September 1 close, dated observations | AI identified look-ahead risk; source ledger |
| Shares | Historical EPS denominator distinguished from forward shares | Dated interests plus gross-award proxy | Model/source reconciliation; final ownership audit open |
| Commercial economics | Contracts, funding and margins unresolved | Explicit assumed prices, margins, delivery and fee schedules | AI implementation; data/commercialization-scenarios.json |
| Downside | Services-only wind-down case | Separate old-date case plus new margin/cash stresses | Existing coursework plus AI-generated tests |
| Terminal | No established sustainable franchise | Explicit assumed operating exit and zero-exit sensitivity | Avoid unsupported perpetuity; show residual-value uncertainty |
| AI output | Prior assistance disclosed in supplied report | Accept/modify/reject decisions still await student | The assistant corrected its own draft; no student independent check claimed |

This table compares the preserved student-supplied text. The student should identify
which changes came from their own work, instruction, peers or AI.

## Consequential AI check

The assistant's flat-fee draft failed a primary-source contract check. Reading
PMA Section 1(c) revealed the escalation floor. The model was modified, its
original output retained, and an escalation regression added. This demonstrates
an actual assistant correction; it is not a claim the student independently
performed the check. Student disposition remains pending.

## What changed, and why?

The proposed recommendation remains watch/defer, but its support is narrower and
more explicit: commercial opportunities cannot substitute for verified net
supplier economics, and the model no longer presents unsupported perpetual value.
The conditional exit-based envelope is {envelope}/share. Contract prices and
the exit multiple remain assumptions. Funding is conditional, and model tests
establish internal consistency rather than forecast truth.

Existing NuScale Lab 11 prediction, changed input, results and reconciliation are
preserved and mapped in docs/lab11-evidence-map.md. Their original timing and tool
boundary are documentary checks, not an assumption that the exercise was never
done. Remaining ownership evidence is listed in HANDOFF.md. No separate original
Edition A PDF is outstanding.
'''
    (ROOT / 'docs/research-evolution.md').write_text(research)
    validation = f'''# Validation and AI use

{common_label}

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
moves from ${results[2]['value_per_share']:.2f} to
${p['margin_stress'][2]['value_per_share']:.2f}/share including the assumed operating sale.
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
'''
    (ROOT / 'docs/validation-and-ai-use.md').write_text(validation)
    # Scripts are rehearsal material. They are not transcripts of recordings.
    scripts = {
      1: '''# Video 1 rehearsal script - AI-generated draft

Target: under 3 minutes. Planned cue times, not actual recording timestamps.
Verify every first-person statement against your own records before recording.

0:00-0:35 | Show the preserved Edition A text and supporting lab screenshots.
My starting position was watch/defer. I wanted evidence that NuScale could turn
commercial interest into profitable, fundable supplier contracts. My actual
submitted baseline is preserved as text. My professor approved the text submission
format; the screenshots show the lab attempt and grade.

0:35-1:15 | Show docs/research-evolution.md and the current report.
Edition B makes the information date explicit and separates the old services-only
wind-down scenario from the commercialization assumptions. The output is a
conditional valuation with an assumed operating exit. Alternative multiples and
the zero-exit case show residual-value uncertainty. The thesis stays watch/defer.

1:15-2:10 | Show the PMA source and superseded output.
One material AI output required correction. The assistant initially held milestone
payments flat. The contract's escalation clause contradicted that assumption.
The corrected code applies the floor, preserves the old draft and adds a test.
The assistant performed this check; before representing it as my own verification
I need to inspect the primary source and reproduce the calculation independently.

2:10-2:45 | State actual AI disposition after personally reviewing.
The assistant generated code and drafts. I must state which suggestions I accepted,
modified or rejected and why, using evidence I can navigate and explain. The
existing NuScale Lab 11 prediction/results are preserved in the package. Their
original timing and tool boundary need confirmation from the original lab record.
Do not represent this rehearsal script as the independent exercise.
''',
      2: '''# Video 2 rehearsal script - AI-generated draft

Target: under 5 minutes. Planned cue times, not actual recording timestamps.

0:00-0:40 | Open README and the repository folder.
This component supports an initiate, defer or decline decision. It runs locally
with Python and no API key. The terminal interface reads frozen output; the
calculation engine is separate from the display.

0:40-1:35 | Open the two JSON input files and src/commercialization.py.
Reported inputs and forecast assumptions live in separate files. The model uses
an explicit 2026 stub, delivery revenue, service revenue, operating costs,
advance milestone payments, capex and incremental working capital. Every module
price and delivery path is an analyst assumption awaiting evidence.

1:35-2:30 | Run python3 build_scenarios.py, then python3 app.py bridge.
FCFF is operating income less tax, plus depreciation, less investment and working
capital. The bridge adds opening liquidity once and includes an assumed operating
sale. Negative cash flow is already charged in value, so fixed-price financing
shares are shown as a separate diagnostic rather than deducted again.

2:30-3:35 | Run PYTHONPATH=src python3 -m unittest discover -s tests -v.
Show the cash known answer, linked statement checks and PMA escalation test.
Explain one assertion directly in the code. Tests establish financial invariants;
they cannot prove an assumed module price or future funding availability.
Show the exact actual test count from this run rather than reading an old count.

3:35-4:30 | Open the independent record and the source correction.
The designated locked exercise requires my own prediction and an AI-closed run.
Existing Lab 11 records are preserved without manufacturing timing evidence. The biggest financial limitations
are hidden contract pricing, payment timing, ownership changes and unsupported
residual value. A clean-environment rehearsal is recorded separately; another
person's cold run still requires an actual participant.

4:30-4:50 | Show output/commercialization-report.md and app summary.
The visible report can be inspected without running code. Its inputs, source
hashes and precise results are preserved in JSON, with annual statements in CSV.
''',
      3: f'''# Video 3 live demonstration rehearsal - AI-generated draft

Target: under 5 minutes, with live product demonstration as the main delivery.
Planned cue times only. Record yourself; no actual transcript is claimed here.

0:00-0:40 | Run python3 app.py summary.
My proposed committee action is watch/defer. I am not requesting an initiation
on unverified supplier economics. The application compares three explicit paths
and reports financing needs. Its {envelope} envelope assumes a six-times operating
exit. The application also shows zero and alternative exit multiples.

0:40-1:50 | Run python3 app.py scenario --scenario central.
Show where advance milestone payments occur before revenue, and identify the
first funding year from the displayed results. These schedules explain why an
order announcement can increase cash needs before it generates cash receipts.
Timing and economics remain assumptions, not promised orders.

1:50-2:50 | Run python3 app.py sensitivity, then python3 app.py reverse.
Show the margin stress and required supplier-price hurdle. Explain that moving
the assumption does not establish a feasible contract price. The redacted price
cap and actual net supplier economics remain essential missing evidence.

2:50-3:50 | Run python3 app.py monitoring.
Reconsider initiation only with verified binding net economics, a fundable
stressed cash plan and a supported full value at least 25% above the current price.
The cash buffer and margin-of-safety rule are proposed analyst thresholds, not
company covenants. Review quarterly and after material financing or contract news.

3:50-4:40 | Finish on summary and state the committee ask.
Keep the company on the watchlist and authorize further contract and financing
review. Escalate to do-not-initiate if an upcoming funding gap has no supportable
route or verified net contribution is nonpositive. These tests support a cautious
decision process; an assumed exit remains subject to market and contract evidence.
'''}
    for number, text in scripts.items():
        (ROOT / f'docs/video-{number}-rehearsal-script.md').write_text(text)
    print('Generated memo, research-evolution draft and three rehearsal scripts.')


if __name__ == '__main__':
    main()
