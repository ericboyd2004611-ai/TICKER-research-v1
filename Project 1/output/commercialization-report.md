# NuScale commercialization scenarios — AI-generated draft

**Conditional scenario valuations, not company guidance or a validated market price target.**

Default: sale at the end of 2036 for six times normalized next-year operating EBITDA
after a full milestone-fee burden. This is an analyst exit assumption, not a sourced
peer multiple or guaranteed buyer price. Zero/4x/6x/8x/10x sensitivities are shown.

September 1, 2026 close boundary. June financial observations and a judgmental
$40m July–August cash-use allowance form the opening liquidity proxy.
Intervening filings, ownership changes and contingent claims are not fully audited.

USD millions and shares in millions, except USD/share. All results are calculated;
edit `data/commercialization-scenarios.json`, then run `python3 build_scenarios.py`.

## Scenario comparison

| Scenario | Implied value/share | First funding year | Net equity funding | New shares, diagnostic | Existing holder fraction, diagnostic |
|---|---:|---|---:|---:|---:|
| Delayed | $0.00 | 2032 | 2,631.7 | 420.8 | 51.1% |
| Central illustrative | $0.00 | 2031 | 2,608.0 | 417.0 | 51.3% |
| Stronger execution | $6.77 | 2030 | 42.5 | 6.8 | 98.5% |

**Illustrative scenario envelope: $0.00–$6.77/share.**
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
| terminal_method | exit_multiple |
| exit_ebitda_multiple | 6.0 |
| authorized_class_a_shares_m | 662.0 |
| minimum_cash_m | 50.0 |
| funding_issue_price_fraction_market | 0.7 |
| equity_issuance_fee | 0.03 |
| additional_equity_claims_m | 0.0 |
| historical_pma_first_tranche_m | 507.393 |
| historical_pma_cash_paid_2025_m | 247.509 |
| historical_pma_fraction_paid_2025 | 0.5 |
| pma_annual_escalation | 0.05 |
| module_price_annual_growth | 0.02 |
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

PMA fee scale is an inference from the 2025 cash installment and cohort, not a
contract quote. First-cohort tranche 1 is treated as sunk; remaining tranches are paid
two and one years before delivery. Later cohorts pay all tranches. The terminal
run rate uses the full fee burden. Contracts, timing and repeatability need verification.

The modeled fee increases 5% every year from its inferred 2025 base, reflecting
the agreement floor; future CPI above 5% would require a larger adjustment.
Module selling prices grow 2% annually from the stated 2026 assumption. A negotiated
cap is redacted. Equal price/fee growth is not assumed. Contract slot/invoice timing
is simplified; fixed lead years do not reproduce all legal payment conditions.

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

The default operating exit equals the assumed multiple times positive normalized
next-year EBITDA, after a full milestone-fee burden. Nonpositive EBITDA receives
zero operating sale value; this is not a liquidation appraisal. Cash is not part
of the operating multiple. It is added once in the corporate equity bridge.
The perpetuity method remains optional and rejects growth below fee escalation;
a mathematically valid perpetuity would still need independent economic support.

A separate existing-holder method assumes all proceeds arrive on exit and uses
forecast closing cash plus operating sale value, less claims/debt, divided by final
shares and discounted. It does not subtract FCFF again. Because fixed-price raises
differ from fair-value financing, this conditional result can differ from the DCF.
Subscription checks compare that terminal payoff at each raise date with the
assumed issue price. They flag funding assumptions the model does not support.
The share-capacity screen includes current economic interests and gross awards;
it is a proxy, not a legal determination of issuance capacity.

This engine provides simplified economic income, balance-sheet and cash-flow statements.
They are not GAAP forecasts. Legacy nonliquid assets and liabilities are held constant;
the assumed pre-valuation burn reduces cash and equity together. Forecast equity
rolls forward from economic net income plus net equity funding, never as a plug.
The old linked-statement downside remains separate until dates and assumptions reconcile.

## Enterprise-to-equity bridge

| Scenario | PV explicit FCFF | PV terminal | EV | Opening liquidity | Claims | Equity before floor | Shares |
|---|---:|---:|---:|---:|---:|---:|---:|
| Delayed | -1,898.0 | 0.0 | -1,898.0 | 1,853.0 | 0.0 | -45.0 | 439.139 |
| Central illustrative | -2,035.8 | 0.0 | -2,035.8 | 1,853.0 | 0.0 | -182.8 | 439.139 |
| Stronger execution | -855.8 | 1,976.7 | 1,120.9 | 1,853.0 | 0.0 | 2,973.9 | 439.139 |

## Operating exit and financing conditions

| Scenario | Normalized exit EBITDA | Operating sale value | Existing-holder exit PV/share | Share capacity exceeded? | All assumed subscriptions supported? |
|---|---:|---:|---:|---|---|
| Delayed | -577.0 | 0.0 | $0.01 | True | False |
| Central illustrative | -87.3 | 0.0 | $0.01 | True | False |
| Stronger execution | 1,396.2 | 8,377.3 | $5.24 | False | True |

## Exit-multiple sensitivity - corporate DCF value/share

| Scenario | Zero operating exit | 4x | 6x | 8x | 10x |
|---|---:|---:|---:|---:|---:|
| Delayed | $0.00 | $0.00 | $0.00 | $0.00 | $0.00 |
| Central illustrative | $0.00 | $0.00 | $0.00 | $0.00 | $0.00 |
| Stronger execution | $2.27 | $5.27 | $6.77 | $8.27 | $9.77 |

## Central schedule sensitivity — value/share

| Discount rate | $150m/module | $200m/module | $250m/module |
|---|---:|---:|---:|
| 10% | $0.00 | $0.00 | $2.21 |
| 15% | $0.00 | $0.00 | $2.11 |
| 20% | $0.00 | $0.44 | $2.15 |

## What would justify the reference market price?

Holding the central delivery schedule, 35% gross margin and other inputs fixed,
the model requires about **$386.5m supplier revenue/module**
to reproduce the $9.21 reference share price.
This is an assumption hurdle, not a forecast or evidence a customer will pay it.
It must be checked against actual contracts, competitive economics and any price cap.

## Five-percentage-point module-margin downside

AI-generated automated sensitivity; not the required independent locked prediction.

| Scenario | Base value/share | Stressed value/share | Stressed net funding |
|---|---:|---:|---:|
| Delayed | $0.00 | $0.00 | 2,953.4 |
| Central illustrative | $0.00 | $0.00 | 3,730.7 |
| Stronger execution | $6.77 | $3.34 | 721.6 |

## Delayed annual cash-flow schedule

| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 0 | 1.7 | 0.0 | -79.1 | 0.0 | 0.7 | 0.0 | -79.6 | 0.0 | 1,773.4 |
| 2027 | 0 | 5.0 | 0.0 | -243.8 | 0.0 | 2.0 | 0.0 | -245.1 | 0.0 | 1,528.4 |
| 2028 | 0 | 5.0 | 0.0 | -248.9 | 0.0 | 2.0 | 0.0 | -249.9 | 0.0 | 1,278.4 |
| 2029 | 0 | 5.0 | 0.0 | -254.1 | 0.0 | 2.0 | 0.0 | -254.9 | 0.0 | 1,023.5 |
| 2030 | 0 | 5.0 | 0.0 | -259.4 | 0.0 | 2.0 | 0.0 | -260.0 | 0.0 | 763.4 |
| 2031 | 0 | 5.0 | 129.0 | -393.7 | 0.0 | 2.0 | 0.0 | -394.2 | 0.0 | 369.2 |
| 2032 | 0 | 5.0 | 328.9 | -599.0 | 0.0 | 2.0 | 0.0 | -599.5 | 280.2 | 50.0 |
| 2033 | 6 | 1,038.8 | 487.6 | -453.0 | 0.0 | 31.2 | 103.4 | -585.9 | 585.9 | 50.0 |
| 2034 | 6 | 1,071.5 | 725.3 | -689.9 | 0.0 | 32.1 | 3.3 | -717.8 | 717.8 | 50.0 |
| 2035 | 12 | 2,180.2 | 761.5 | -401.7 | 0.0 | 65.4 | 110.9 | -565.5 | 565.5 | 50.0 |
| 2036 | 12 | 2,247.2 | 799.6 | -431.2 | 0.0 | 67.4 | 6.7 | -482.3 | 482.3 | 50.0 |

Terminal normalized FCFF: -653.2; NONPOSITIVE_EXIT_EBITDA_ZERO_OPERATING_EXIT.

### Linked economic statements and checks

| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | -79.148 | -78.927 | -0.663 | 0.000 | 1,930.045 | 35.536 | 1,894.509 | 0.000 |
| 2027 | -243.803 | -243.050 | -2.000 | 0.000 | 1,686.242 | 35.536 | 1,650.706 | 0.000 |
| 2028 | -248.948 | -247.946 | -2.000 | 0.000 | 1,437.294 | 35.536 | 1,401.758 | 0.000 |
| 2029 | -254.142 | -252.940 | -2.000 | 0.000 | 1,183.152 | 35.536 | 1,147.616 | 0.000 |
| 2030 | -259.395 | -258.034 | -2.000 | 0.000 | 923.757 | 35.536 | 888.221 | 0.000 |
| 2031 | -393.708 | -392.218 | -2.000 | 0.000 | 530.049 | 35.536 | 494.513 | 0.000 |
| 2032 | -599.042 | -597.451 | -2.000 | 280.232 | 211.239 | 35.536 | 175.703 | 0.000 |
| 2033 | -453.041 | -554.749 | -31.165 | 585.914 | 344.112 | 35.536 | 308.576 | 0.000 |
| 2034 | -689.944 | -685.640 | -32.145 | 717.785 | 371.953 | 35.536 | 336.417 | 0.000 |
| 2035 | -401.744 | -500.125 | -65.405 | 565.530 | 535.739 | 35.536 | 500.203 | 0.000 |
| 2036 | -431.234 | -414.867 | -67.416 | 482.282 | 586.787 | 35.536 | 551.251 | 0.000 |

## Central illustrative annual cash-flow schedule

| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 0 | 1.7 | 0.0 | -79.1 | 0.0 | 0.7 | 0.0 | -79.6 | 0.0 | 1,773.4 |
| 2027 | 0 | 5.0 | 0.0 | -243.8 | 0.0 | 2.0 | 0.0 | -245.1 | 0.0 | 1,528.4 |
| 2028 | 0 | 5.0 | 111.4 | -360.4 | 0.0 | 2.0 | 0.0 | -361.4 | 0.0 | 1,167.0 |
| 2029 | 0 | 5.0 | 284.1 | -538.3 | 0.0 | 2.0 | 0.0 | -539.1 | 0.0 | 627.9 |
| 2030 | 6 | 1,303.9 | 421.2 | -226.0 | 0.0 | 39.1 | 129.9 | -393.6 | 0.0 | 234.3 |
| 2031 | 6 | 1,341.9 | 626.5 | -428.9 | 0.0 | 40.3 | 3.8 | -464.1 | 279.8 | 50.0 |
| 2032 | 12 | 2,731.8 | 793.3 | -119.0 | 0.0 | 82.0 | 139.0 | -324.8 | 324.8 | 50.0 |
| 2033 | 12 | 2,809.8 | 1,036.1 | -349.7 | 0.0 | 84.3 | 7.8 | -413.2 | 413.2 | 50.0 |
| 2034 | 18 | 4,295.0 | 1,493.2 | -300.1 | 0.0 | 128.8 | 148.5 | -537.7 | 537.7 | 50.0 |
| 2035 | 18 | 4,415.3 | 1,791.8 | -574.6 | 0.0 | 132.5 | 12.0 | -661.6 | 661.6 | 50.0 |
| 2036 | 24 | 6,000.2 | 1,881.4 | -124.8 | 0.0 | 180.0 | 158.5 | -390.8 | 390.8 | 50.0 |

Terminal normalized FCFF: -288.8; NONPOSITIVE_EXIT_EBITDA_ZERO_OPERATING_EXIT.

### Linked economic statements and checks

| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | -79.148 | -78.927 | -0.663 | 0.000 | 1,930.045 | 35.536 | 1,894.509 | 0.000 |
| 2027 | -243.803 | -243.050 | -2.000 | 0.000 | 1,686.242 | 35.536 | 1,650.706 | 0.000 |
| 2028 | -360.374 | -359.371 | -2.000 | 0.000 | 1,325.868 | 35.536 | 1,290.332 | 0.000 |
| 2029 | -538.277 | -537.075 | -2.000 | 0.000 | 787.592 | 35.536 | 752.056 | 0.000 |
| 2030 | -225.962 | -354.492 | -39.118 | 0.000 | 561.630 | 35.536 | 526.094 | 0.000 |
| 2031 | -428.946 | -423.831 | -40.257 | 279.787 | 412.471 | 35.536 | 376.935 | 0.000 |
| 2032 | -119.016 | -242.824 | -81.954 | 324.777 | 618.232 | 35.536 | 582.696 | 0.000 |
| 2033 | -349.678 | -328.947 | -84.295 | 413.243 | 681.797 | 35.536 | 646.261 | 0.000 |
| 2034 | -300.053 | -408.878 | -128.849 | 537.727 | 919.471 | 35.536 | 883.935 | 0.000 |
| 2035 | -574.625 | -529.141 | -132.460 | 661.601 | 1,006.447 | 35.536 | 970.911 | 0.000 |
| 2036 | -124.848 | -210.824 | -180.005 | 390.829 | 1,272.428 | 35.536 | 1,236.892 | 0.000 |

## Stronger execution annual cash-flow schedule

| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 0 | 1.7 | 0.0 | -79.1 | 0.0 | 0.7 | 0.0 | -79.6 | 0.0 | 1,773.4 |
| 2027 | 0 | 5.0 | 106.1 | -349.9 | 0.0 | 2.0 | 0.0 | -351.2 | 0.0 | 1,422.2 |
| 2028 | 0 | 5.0 | 382.0 | -631.0 | 0.0 | 2.0 | 0.0 | -632.0 | 0.0 | 790.3 |
| 2029 | 6 | 1,596.8 | 685.3 | -302.7 | 0.0 | 47.9 | 159.2 | -508.6 | 0.0 | 281.7 |
| 2030 | 12 | 3,264.3 | 1,017.9 | 18.5 | 4.6 | 97.9 | 166.7 | -240.3 | 8.6 | 50.0 |
| 2031 | 18 | 5,009.4 | 1,363.6 | 350.5 | 87.6 | 150.3 | 174.5 | -33.9 | 33.9 | 50.0 |
| 2032 | 24 | 6,834.0 | 1,741.4 | 676.4 | 169.1 | 205.0 | 182.5 | 172.3 | 0.0 | 222.3 |
| 2033 | 24 | 7,017.1 | 2,031.6 | 428.4 | 107.1 | 210.5 | 18.3 | 175.4 | 0.0 | 397.7 |
| 2034 | 30 | 8,960.4 | 2,346.5 | 864.6 | 216.1 | 268.8 | 194.3 | 293.8 | 0.0 | 691.5 |
| 2035 | 30 | 9,196.2 | 2,687.8 | 585.9 | 146.5 | 275.9 | 23.6 | 280.5 | 0.0 | 972.0 |
| 2036 | 36 | 11,263.9 | 2,822.2 | 1,251.8 | 312.9 | 337.9 | 206.8 | 561.8 | 0.0 | 1,533.8 |

Terminal normalized FCFF: 721.8; ASSUMED_EXIT_MULTIPLE.

### Linked economic statements and checks

| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | -79.148 | -78.927 | -0.663 | 0.000 | 1,930.045 | 35.536 | 1,894.509 | 0.000 |
| 2027 | -349.923 | -349.169 | -2.000 | 0.000 | 1,580.123 | 35.536 | 1,544.587 | 0.000 |
| 2028 | -630.979 | -629.976 | -2.000 | 0.000 | 949.144 | 35.536 | 913.608 | 0.000 |
| 2029 | -302.684 | -460.663 | -47.904 | 0.000 | 646.461 | 35.536 | 610.925 | 0.000 |
| 2030 | 13.853 | -142.353 | -97.929 | 8.588 | 668.901 | 35.536 | 633.365 | 0.000 |
| 2031 | 262.875 | 116.388 | -150.281 | 33.893 | 965.669 | 35.536 | 930.133 | 0.000 |
| 2032 | 507.329 | 377.340 | -205.019 | 0.000 | 1,472.998 | 35.536 | 1,437.462 | 0.000 |
| 2033 | 321.266 | 385.933 | -210.513 | 0.000 | 1,794.264 | 35.536 | 1,758.728 | 0.000 |
| 2034 | 648.430 | 562.584 | -268.813 | 0.000 | 2,442.694 | 35.536 | 2,407.158 | 0.000 |
| 2035 | 439.409 | 556.387 | -275.886 | 0.000 | 2,882.103 | 35.536 | 2,846.567 | 0.000 |
| 2036 | 938.842 | 899.686 | -337.918 | 0.000 | 3,820.945 | 35.536 | 3,785.409 | 0.000 |

## Evidence and review

Financial observations: [source ledger](../docs/verified-starting-point-draft.md).
PMA scale/tranches: [June 2026 10-Q, Note 9](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm).
Escalation, installments and redacted cap: [PMA Sections 1(c), 1(d), 1(g)](https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm).
Actual inputs, full-precision results, hashes and sensitivities: `commercialization-output.json`.
No final buy/sell recommendation is inferred from unapproved scenario assumptions.
