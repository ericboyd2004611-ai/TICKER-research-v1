# NuScale commercialization scenarios — AI-generated draft

**Illustrative assumptions, not company guidance or a validated fair-value range.**

September 1, 2026 close boundary. June financial observations and a judgmental
$40m July–August cash-use allowance form the opening liquidity proxy.
Intervening filings, ownership changes and contingent claims are not fully audited.

USD millions and shares in millions, except USD/share. All results are calculated;
edit `data/commercialization-scenarios.json`, then run `python3 build_scenarios.py`.

## Scenario comparison

| Scenario | Implied value/share | First funding year | Net equity funding | New shares, diagnostic | Existing holder fraction, diagnostic |
|---|---:|---|---:|---:|---:|
| Delayed | $0.51 | 2032 | 1,753.6 | 280.4 | 61.0% |
| Central illustrative | $1.36 | 2031 | 867.1 | 138.7 | 76.0% |
| Stronger execution | $8.41 | None | 0.0 | 0.0 | 100.0% |

**Illustrative scenario envelope: $0.51–$8.41/share.**
No probabilities or weighted target are assigned. A zero result is a modeled
equity floor, not proof the stock is worthless. Current-holder value assumes
future funding on fair terms; the fixed-price financing diagnostic does not
establish those terms. An infeasible funding path invalidates the scenario.

## Inputs that define the answer

| Scenario | Price/module | Gross margin before PMA | Deliveries 2027–2036 |
|---|---:|---:|---|
| Delayed | 150 | 30% | 0, 0, 0, 0, 0, 0, 6, 6, 12, 12 |
| Central illustrative | 200 | 35% | 0, 0, 0, 6, 6, 12, 12, 18, 18, 24 |
| Stronger execution | 250 | 40% | 0, 0, 6, 12, 18, 24, 24, 30, 30, 36 |

**Every scenario price, margin, schedule and forecast parameter is an AI-generated analyst assumption.**
These are neither disclosed orders nor customer contract economics. Stronger execution
is a deliberately optimistic comparator, not a statistical confidence bound.

| Common setting | Value |
|---|---|
| valuation_date | 2026-09-01 |
| first_forecast_year | 2027 |
| last_forecast_year | 2036 |
| assumed_july_august_cash_use_m | 40.0 |
| annual_cash_opex_m | 240.0 |
| opex_growth | 0.02 |
| annual_existing_services_revenue_m | 5.0 |
| existing_services_margin | 0.35 |
| installed_module_annual_service_revenue_m | 2.0 |
| installed_services_margin | 0.5 |
| capex_fraction_revenue | 0.03 |
| minimum_annual_capex_m | 2.0 |
| opening_ppe_m | 3.323 |
| depreciation_fraction_opening_ppe | 0.2 |
| incremental_nwc_fraction_revenue | 0.1 |
| cash_tax_rate | 0.25 |
| discount_rate | 0.15 |
| terminal_growth | 0.025 |
| minimum_cash_m | 50.0 |
| funding_issue_price_fraction_market | 0.7 |
| equity_issuance_fee | 0.03 |
| additional_equity_claims_m | 0.0 |
| historical_pma_first_tranche_m | 507.393 |
| historical_pma_cohort_modules | 72 |
| pma_first_tranche_fraction | 0.15 |
| pma_binding_fraction | 0.35 |
| pma_purchase_fraction | 0.5 |
| pma_binding_lead_years | 2 |
| pma_purchase_lead_years | 1 |

## Method and limitations

FCFF = EBIT − cash tax + depreciation − capex − change in incremental working capital.
Module revenue equals delivered units × assumed supplier revenue/module; this is
not total nuclear power-plant construction cost. Installed-base service income starts
the year after delivery. Costs exclude fuel/pass-through complexity and interest income.
The model has an actual-day stub to December 2026 and year-end full-year cash flows.

PMA fee scale is an inference from the historical first tranche and cohort, not a
contract quote. First-cohort tranche 1 is treated as sunk; remaining tranches are paid
two and one years before delivery. Later cohorts pay all tranches. The terminal
run rate uses the full fee burden. Contracts, timing and repeatability need verification.

PV of explicit FCFF plus PV of terminal operating value gives enterprise value.
Add the opening unrestricted liquidity proxy once, subtract reported debt and the
editable additional-claims allowance, then divide by the June gross-award share proxy.
Operating commitments and leases are assumed within the cash-cost/reinvestment forecasts;
that mapping is not yet reconciled contract by contract. A zero claims allowance
does not mean there are no contingent or tax-agreement claims.

Negative FCFF is already deducted in the DCF. Funding receipts stay out of enterprise
value, and diagnostic new shares do not dilute the DCF denominator a second time.
Funding diagnostics assume issuance at 70% of the reference market price, 3% fees,
and a $50m cash floor. Availability is not guaranteed; only year-end cash is tested.
Liquid investments are assumed saleable at carrying value with no investment return.

Terminal value requires positive normalized FCFF and discount rate above growth.
A nonpositive terminal run rate is assigned zero going-concern terminal value,
with no separate liquidation recovery; that case needs a different closure analysis.
Terminal margins, module cadence, service mix and reinvestment are simplifying
steady-state assumptions and can dominate the result.

This engine provides simplified economic income, balance-sheet and cash-flow statements.
They are not GAAP forecasts. Legacy nonliquid assets and liabilities are held constant;
the assumed pre-valuation burn reduces cash and equity together. Forecast equity
rolls forward from economic net income plus net equity funding, never as a plug.
The old linked-statement downside remains separate until dates and assumptions reconcile.

## Enterprise-to-equity bridge

| Scenario | PV explicit FCFF | PV terminal | EV | Opening liquidity | Claims | Equity before floor | Shares |
|---|---:|---:|---:|---:|---:|---:|---:|
| Delayed | -1,629.1 | 0.0 | -1,629.1 | 1,853.0 | 0.0 | 223.9 | 439.139 |
| Central illustrative | -1,465.1 | 211.2 | -1,253.9 | 1,853.0 | 0.0 | 599.1 | 439.139 |
| Stronger execution | -215.4 | 2,054.6 | 1,839.2 | 1,853.0 | 0.0 | 3,692.2 | 439.139 |

## Central schedule sensitivity — value/share

| Discount rate | $150m/module | $200m/module | $250m/module |
|---|---:|---:|---:|
| 10% | $0.00 | $1.50 | $5.97 |
| 15% | $0.00 | $1.36 | $3.46 |
| 20% | $0.65 | $1.60 | $2.79 |

## What would justify the reference market price?

Holding the central delivery schedule, 35% gross margin and other inputs fixed,
the model requires about **$393.3m supplier revenue/module**
to reproduce the $9.21 reference share price.
This is an assumption hurdle, not a forecast or evidence a customer will pay it.
It must be checked against actual contracts, competitive economics and any price cap.

## Five-percentage-point module-margin downside

AI-generated automated sensitivity; not the required independent locked prediction.

| Scenario | Base value/share | Stressed value/share | Stressed net funding |
|---|---:|---:|---:|
| Delayed | $0.51 | $0.34 | 2,023.6 |
| Central illustrative | $1.36 | $0.20 | 1,767.1 |
| Stronger execution | $8.41 | $5.53 | 37.7 |

## Delayed annual cash-flow schedule

| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 0 | 1.7 | 0.0 | -79.1 | 0.0 | 0.7 | 0.0 | -79.6 | 0.0 | 1,773.4 |
| 2027 | 0 | 5.0 | 0.0 | -243.8 | 0.0 | 2.0 | 0.0 | -245.1 | 0.0 | 1,528.4 |
| 2028 | 0 | 5.0 | 0.0 | -248.9 | 0.0 | 2.0 | 0.0 | -249.9 | 0.0 | 1,278.4 |
| 2029 | 0 | 5.0 | 0.0 | -254.1 | 0.0 | 2.0 | 0.0 | -254.9 | 0.0 | 1,023.5 |
| 2030 | 0 | 5.0 | 0.0 | -259.4 | 0.0 | 2.0 | 0.0 | -260.0 | 0.0 | 763.4 |
| 2031 | 0 | 5.0 | 98.7 | -363.4 | 0.0 | 2.0 | 0.0 | -363.9 | 0.0 | 399.5 |
| 2032 | 0 | 5.0 | 239.6 | -509.7 | 0.0 | 2.0 | 0.0 | -510.1 | 160.6 | 50.0 |
| 2033 | 6 | 905.0 | 338.3 | -343.9 | 0.0 | 27.1 | 90.0 | -459.3 | 459.3 | 50.0 |
| 2034 | 6 | 917.0 | 479.2 | -489.4 | 0.0 | 27.5 | 1.2 | -511.4 | 511.4 | 50.0 |
| 2035 | 12 | 1,829.0 | 479.2 | -223.2 | 0.0 | 54.9 | 91.2 | -358.3 | 358.3 | 50.0 |
| 2036 | 12 | 1,853.0 | 479.2 | -225.7 | 0.0 | 55.6 | 2.4 | -264.0 | 264.0 | 50.0 |

Terminal normalized FCFF: -359.4; NO_GOING_CONCERN_TERMINAL_VALUE.

### Linked economic statements and checks

| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | -79.148 | -78.927 | -0.663 | 0.000 | 1,930.045 | 35.536 | 1,894.509 | 0.000 |
| 2027 | -243.803 | -243.050 | -2.000 | 0.000 | 1,686.242 | 35.536 | 1,650.706 | 0.000 |
| 2028 | -248.948 | -247.946 | -2.000 | 0.000 | 1,437.294 | 35.536 | 1,401.758 | 0.000 |
| 2029 | -254.142 | -252.940 | -2.000 | 0.000 | 1,183.152 | 35.536 | 1,147.616 | 0.000 |
| 2030 | -259.395 | -258.034 | -2.000 | 0.000 | 923.757 | 35.536 | 888.221 | 0.000 |
| 2031 | -363.378 | -361.889 | -2.000 | 0.000 | 560.378 | 35.536 | 524.842 | 0.000 |
| 2032 | -509.723 | -508.131 | -2.000 | 160.583 | 211.239 | 35.536 | 175.703 | 0.000 |
| 2033 | -343.870 | -432.197 | -27.150 | 459.347 | 326.716 | 35.536 | 291.180 | 0.000 |
| 2034 | -489.421 | -483.853 | -27.510 | 511.363 | 348.657 | 35.536 | 313.121 | 0.000 |
| 2035 | -223.194 | -303.477 | -54.870 | 358.347 | 483.810 | 35.536 | 448.274 | 0.000 |
| 2036 | -225.721 | -208.413 | -55.590 | 264.003 | 522.093 | 35.536 | 486.557 | 0.000 |

## Central illustrative annual cash-flow schedule

| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 0 | 1.7 | 0.0 | -79.1 | 0.0 | 0.7 | 0.0 | -79.6 | 0.0 | 1,773.4 |
| 2027 | 0 | 5.0 | 0.0 | -243.8 | 0.0 | 2.0 | 0.0 | -245.1 | 0.0 | 1,528.4 |
| 2028 | 0 | 5.0 | 98.7 | -347.6 | 0.0 | 2.0 | 0.0 | -348.6 | 0.0 | 1,179.8 |
| 2029 | 0 | 5.0 | 239.6 | -493.7 | 0.0 | 2.0 | 0.0 | -494.5 | 0.0 | 685.2 |
| 2030 | 6 | 1,205.0 | 338.3 | -177.7 | 0.0 | 36.1 | 120.0 | -332.4 | 0.0 | 352.8 |
| 2031 | 6 | 1,217.0 | 479.2 | -324.8 | 0.0 | 36.5 | 1.2 | -354.1 | 51.4 | 50.0 |
| 2032 | 12 | 2,429.0 | 577.9 | -8.4 | 0.0 | 72.9 | 121.2 | -188.5 | 188.5 | 50.0 |
| 2033 | 12 | 2,453.0 | 718.8 | -154.5 | 0.0 | 73.6 | 2.4 | -204.7 | 204.7 | 50.0 |
| 2034 | 18 | 3,677.0 | 986.6 | -5.4 | 0.0 | 110.3 | 122.4 | -202.8 | 202.8 | 50.0 |
| 2035 | 18 | 3,713.0 | 1,127.5 | -148.9 | 0.0 | 111.4 | 3.6 | -213.6 | 213.6 | 50.0 |
| 2036 | 24 | 4,949.0 | 1,127.5 | 271.1 | 67.8 | 148.5 | 123.6 | -6.2 | 6.2 | 50.0 |

Terminal normalized FCFF: 111.9; POSITIVE_NORMALIZED_RUN_RATE.

### Linked economic statements and checks

| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | -79.148 | -78.927 | -0.663 | 0.000 | 1,930.045 | 35.536 | 1,894.509 | 0.000 |
| 2027 | -243.803 | -243.050 | -2.000 | 0.000 | 1,686.242 | 35.536 | 1,650.706 | 0.000 |
| 2028 | -347.608 | -346.606 | -2.000 | 0.000 | 1,338.634 | 35.536 | 1,303.098 | 0.000 |
| 2029 | -493.744 | -492.542 | -2.000 | 0.000 | 844.890 | 35.536 | 809.354 | 0.000 |
| 2030 | -177.657 | -296.296 | -36.150 | 0.000 | 667.233 | 35.536 | 631.697 | 0.000 |
| 2031 | -324.753 | -317.634 | -36.510 | 51.381 | 393.860 | 35.536 | 358.324 | 0.000 |
| 2032 | -8.351 | -115.593 | -72.870 | 188.463 | 573.973 | 35.536 | 538.437 | 0.000 |
| 2033 | -154.481 | -131.141 | -73.590 | 204.731 | 624.223 | 35.536 | 588.687 | 0.000 |
| 2034 | -5.356 | -92.446 | -110.310 | 202.756 | 821.623 | 35.536 | 786.087 | 0.000 |
| 2035 | -148.922 | -102.212 | -111.390 | 213.602 | 886.303 | 35.536 | 850.767 | 0.000 |
| 2036 | 203.344 | 142.270 | -148.470 | 6.200 | 1,095.847 | 35.536 | 1,060.311 | 0.000 |

## Stronger execution annual cash-flow schedule

| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 0 | 1.7 | 0.0 | -79.1 | 0.0 | 0.7 | 0.0 | -79.6 | 0.0 | 1,773.4 |
| 2027 | 0 | 5.0 | 98.7 | -342.5 | 0.0 | 2.0 | 0.0 | -343.7 | 0.0 | 1,429.7 |
| 2028 | 0 | 5.0 | 338.3 | -587.2 | 0.0 | 2.0 | 0.0 | -588.2 | 0.0 | 841.5 |
| 2029 | 6 | 1,505.0 | 577.9 | -232.0 | 0.0 | 45.1 | 150.0 | -426.0 | 0.0 | 415.5 |
| 2030 | 12 | 3,017.0 | 817.5 | 120.5 | 30.1 | 90.5 | 151.2 | -141.3 | 0.0 | 274.2 |
| 2031 | 18 | 4,541.0 | 1,043.0 | 485.7 | 121.4 | 136.2 | 152.4 | 101.7 | 0.0 | 375.9 |
| 2032 | 24 | 6,077.0 | 1,268.5 | 850.9 | 212.7 | 182.3 | 153.6 | 350.4 | 0.0 | 726.3 |
| 2033 | 24 | 6,125.0 | 1,409.4 | 701.7 | 175.4 | 183.8 | 4.8 | 412.7 | 0.0 | 1,139.0 |
| 2034 | 30 | 7,673.0 | 1,550.4 | 1,157.5 | 289.4 | 230.2 | 154.8 | 579.8 | 0.0 | 1,718.8 |
| 2035 | 30 | 7,733.0 | 1,691.3 | 1,014.2 | 253.6 | 232.0 | 6.0 | 646.1 | 0.0 | 2,364.9 |
| 2036 | 36 | 9,293.0 | 1,691.3 | 1,616.8 | 404.2 | 278.8 | 156.0 | 922.9 | 0.0 | 3,287.8 |

Terminal normalized FCFF: 1,088.4; POSITIVE_NORMALIZED_RUN_RATE.

### Linked economic statements and checks

| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | -79.148 | -78.927 | -0.663 | 0.000 | 1,930.045 | 35.536 | 1,894.509 | 0.000 |
| 2027 | -342.463 | -341.710 | -2.000 | 0.000 | 1,587.583 | 35.536 | 1,552.047 | 0.000 |
| 2028 | -587.210 | -586.208 | -2.000 | 0.000 | 1,000.372 | 35.536 | 964.836 | 0.000 |
| 2029 | -232.006 | -380.804 | -45.150 | 0.000 | 768.366 | 35.536 | 732.830 | 0.000 |
| 2030 | 90.381 | -50.827 | -90.510 | 0.000 | 858.747 | 35.536 | 823.211 | 0.000 |
| 2031 | 364.276 | 237.971 | -136.230 | 0.000 | 1,223.023 | 35.536 | 1,187.487 | 0.000 |
| 2032 | 638.150 | 532.672 | -182.310 | 0.000 | 1,861.172 | 35.536 | 1,825.636 | 0.000 |
| 2033 | 526.261 | 596.420 | -183.750 | 0.000 | 2,387.433 | 35.536 | 2,351.897 | 0.000 |
| 2034 | 868.100 | 810.018 | -230.190 | 0.000 | 3,255.533 | 35.536 | 3,219.997 | 0.000 |
| 2035 | 760.654 | 878.066 | -231.990 | 0.000 | 4,016.187 | 35.536 | 3,980.651 | 0.000 |
| 2036 | 1,212.565 | 1,201.693 | -278.790 | 0.000 | 5,228.752 | 35.536 | 5,193.216 | 0.000 |

## Evidence and review

Financial observations: [source ledger](../docs/verified-starting-point-draft.md).
PMA scale/tranches: [June 2026 10-Q, Note 9](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm).
Actual inputs, full-precision results, hashes and sensitivities: `commercialization-output.json`.
No final buy/sell recommendation is inferred from unapproved scenario assumptions.
