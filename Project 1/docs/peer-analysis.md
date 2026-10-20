# Public-company comparison and cost of capital

CAPM: 4.75% + 2.00 × 4.14% = 13.03% cost of equity.
Weights: equity 100%, financial debt 0%. WACC = 13.03%.
Beta 2.0 is a proposed judgment, not an estimated SMR beta or a student approval. The original 15% scenario remains separately labeled.

## Dated multiples

Price date September 1, 2026; balance sheets June 30, 2026. USD millions except per share. TTM = FY2025 - H1 2025 + H1 2026.

| Company | Market equity | Financial EV | TTM sales | EV / sales | Adjusted EV / sales | Price / book |
|---|---:|---:|---:|---:|---:|---:|
| SMR | 3,957.55 | 2,064.55 | 10.69 | 193.13 | 193.13 | 1.97 |
| OKLO | 7,131.52 | 4,125.42 | 1.21 | 3,409.44 | 3,409.44 | 2.18 |
| BWXT | 14,800.55 | 16,212.24 | 3,513.97 | 4.61 | 4.66 | 11.09 |

## Mechanical peer translation to SMR ($/share)

| Peer | EV/sales: basic | P/book: basic | EV/sales: gross awards | P/book: gross awards |
|---|---:|---:|---:|---:|
| OKLO | 89.22 | 10.21 | 87.31 | 9.99 |
| BWXT | 4.52 | 51.97 | 4.42 | 50.86 |

EV-based translation: peer EV/sales × SMR TTM revenue + June unrestricted liquidity - reported financial debt, divided by indicated economic shares. P/book translation: peer P/book × SMR consolidated common economic book, divided by the same shares. These are June-balance mechanical comparisons, not September cash reconciliations or fair-value estimates.
Conventional financial EV excludes operating leases; adjusted BWXT EV adds pension and postretirement liabilities. Negative book NCI is not treated as a market claim. The entire public-company bridge is a proxy pending September share/claim roll-forwards. No peer median is used.

## Why comps disagree with the DCF

OKLO has only $1.210m of trailing revenue. Its very high EV/sales reflects development expectations divided by a tiny current-sales denominator; applying it to SMR can create an extreme mechanical value. BWXT has established nuclear/defense sales and profitability, so its revenue multiple transfers mature economics to an early-stage supplier. P/book largely compares financing cash and accumulated losses; it does not value reactor IP, future contracts, or future burn. The DCF instead prices an explicit delivery path, milestone fees, reinvestment, funding and an assumed exit. These methods answer different economic questions. Do not average their outputs into a target.

## Discount-rate and terminal dependence

| Scenario | Original 15% / share | CAPM / share | PV terminal / EV | Equity nonincreasing? | EV nonincreasing? |
|---|---:|---:|---:|---|---|
| Delayed | 0.00 | 0.00 | NM: nonpositive EV | False | False |
| Central illustrative | 0.00 | 0.00 | NM: nonpositive EV | False | False |
| Stronger execution | 6.77 | 7.68 | 176.3% | True | True |

Terminal share is PV terminal / EV, not PV terminal / equity. A ratio above 100% reflects negative explicit FCFF. With nonpositive EV it is NM.
Monotonicity holds for a fixed stream of nonnegative cash flows. This development model has mixed-sign flows. The sampled EV diagnostic can fail even when the floored per-share output is flat at zero. Such a failure is disclosed, not removed.

## WACC–growth grids

A Gordon diagnostic is provided separately from the exit-multiple base. With perpetual milestone fees escalating at least 5%, a 2–3% uniform terminal-FCFF growth assumption is blocked. Conditional 5–6% cases impose uniform terminal FCFF growth and remain economically unsupported as long-run forecasts. They are sensitivity cases, not endorsed terminal values.

### Delayed

| WACC / growth | 2.0% | 2.5% | 3.0% | 5.0% | 6.0% |
|---|---:|---:|---:|---:|---:|
| 10.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |
| 13.03% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |
| 15.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |
| 20.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |

### Central illustrative

| WACC / growth | 2.0% | 2.5% | 3.0% | 5.0% | 6.0% |
|---|---:|---:|---:|---:|---:|
| 10.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |
| 13.03% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |
| 15.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |
| 20.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | NM: normalized terminal FCFF is nonpositive | NM: normalized terminal FCFF is nonpositive |

### Stronger execution

| WACC / growth | 2.0% | 2.5% | 3.0% | 5.0% | 6.0% |
|---|---:|---:|---:|---:|---:|
| 10.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | 14.67 | 17.74 |
| 13.03% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | 8.08 | 8.90 |
| 15.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | 6.15 | 6.58 |
| 20.00% | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | BLOCKED: growth below contractual fee escalation | 3.92 | 4.04 |

## Sources and policy

Selection was recorded in docs/peer-policy.md before extracting multiples. This is a new October research step, not a claimed earlier lock. Exact observations, locators and URLs: data/peers.json and data/cost-of-capital.json. Inputs and source hashes: output/valuation-methods.json.
