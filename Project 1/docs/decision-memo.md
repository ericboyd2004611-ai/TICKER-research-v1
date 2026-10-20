# NuScale (SMR): watch / defer

**October 19, 2026 | Modeling choices reviewed and adopted**

## Decision and committee ask

Retain SMR on the watchlist; do not initiate a position on this evidence package.
The intended user is a long-horizon, high-risk-tolerance investment committee with
no current holding. Request a contract-economics and financing review before any
purchase decision. The analysis develops the starting watch/defer thesis; assumptions and limitations are documented below.

## What the application establishes

The locally runnable component connects editable commercial assumptions to
linked economic statements, FCFF, an enterprise-to-equity bridge, and a funding
diagnostic. The analysis boundary is September 1, 2026 close. Historical
observations retain their actual measurement dates; pre-valuation cash use is
explicitly assumed rather than reported.

| Scenario | Conditional DCF/share | Net funding needed | First funding year |
|---|---:|---:|---|
| Delayed | $0.00 | $2,631.7m | 2032 |
| Central illustrative | $0.00 | $2,608.0m | 2031 |
| Stronger execution | $6.77 | $42.5m | 2030 |

The $0.00-$6.77 envelope includes an assumed end-2036 operating sale at six times
normalized next-year EBITDA after full milestone fees. This is an analyst
assumption, not a verified peer or buyer quote. Zero/4x/6x/8x/10x exit sensitivities
are included. Zero modeled equity is not proof the stock is worthless; assumed
sale proceeds do not establish market value. No probability-weighted target is assigned.

## Strongest decision evidence

The contract exhibit requires at least 5% annual milestone-payment escalation
and redacts the supplier-price cap [1]. That weakens the earlier flat-fee calculation, which
held fees flat. The corrected model applies the escalation floor. Module prices,
margins, payment leads, and delivery schedules remain scenario assumptions.
Commercial progress alone does not resolve the net economics of a supplier order.

## Material sensitivities

The stronger-execution case is the only supplied case with positive modeled
equity value. A five-percentage-point module-margin reduction cuts it from
$6.77 to $3.34/share
and increases net funding from $42.5m to
$721.6m. Under the central schedule, the
one-input reverse calculation requires about $387m of 2026-base supplier
revenue per module to reproduce $9.21 with the assumed operating exit. That is a model
hurdle, not evidence of a feasible contract price.

## Conditions, monitoring and reversal

Proposed analyst policy: reconsider initiation only with verified binding net
contract economics, a quarterly cash plan that maintains a $50m buffer under a
20% operating-cost shock and 12-month delivery delay, and a sourced full valuation
at least 25% above the then-current market price. The buffer and 25% hurdle are
analyst choices, not covenants or company guidance.

The monitoring policy calls for reviewing each quarterly filing and material contract or
financing announcement within five business days of release. Escalate
to do-not-initiate if a 12-month funding gap has no supportable financing route
or verified net contract contribution is nonpositive. Withdraw valuation claims
if sources or ownership cannot reconcile. A cash-model flag is not a default.

## WACC, peer context and terminal dependence

The reference CAPM build is 4.75% risk-free + 2.0 beta × 4.14% ERP = 13.03% WACC under all-equity financing. Beta 2.0 is a scenario judgment rather than a measured beta. The original 15% reference remains separate; stronger-case value is $7.68 at 13.03%, versus $6.77 at 15%.

June-balance/September-price peer observations: OKLO EV/Sales 3,409.44× and P/Book 2.18×; BWXT 4.61× and 11.09×. Mechanical SMR gross-award translations are $87.31/$9.99 from OKLO and $4.42/$50.86 from BWXT. These are not a target range: tiny developer sales distort EV/Sales, while mature profitability and accumulated financing distort P/Book. Policy, sources and bridges are in docs/peer-analysis.md and data/peers.json.

The stronger case's PV terminal value is 176.3% of EV, exposing dependence on the assumed exit. Mixed-sign cash flows cause delayed/central monotonicity failures; these are disclosed. WACC–growth grids block 2–3% perpetuities that conflict with the contractual fee floor. No economically supported perpetual-growth base is claimed.

## Limits and evidence

The package does not yet verify every intervening filing, reconcile all award and
contingent-claim terms, or establish a supportable
market exit. Fixed-price dilution is shown separately and is not deducted
again from FCFF value; a separate terminal-payoff method values that financing
condition. Existing NuScale Lab 11 prediction/results are preserved and mapped.
Their original timing/tool-boundary evidence still requires confirmation. See
Validation-and-AI-Use for the assistance disclosure, source corrections and validation results.

Sources: [1] SEC PMA, Sections 1(c), 1(d), 1(g):
https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm
[2] Financial source ledger: docs/verified-starting-point-draft.md.
[3] Executed analysis: output/commercialization-output.json and report.
