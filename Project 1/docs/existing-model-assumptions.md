# SMR — labelled assumptions for Lab 09

**Question:** What are five years of your company's statements worth, built from assumptions you can defend, and how do you know the statements are right?

**Company-specific line:** NuScale's valuation depends on whether commercialization produces profitable reactor projects before spending and dilution consume the value available to each share.

This application produces five linked annual statements and one **conditional downside value**. It is a services-only scenario followed by wind-down at December 31, 2030. Wind-down is an analyst modelling choice, not an announced company plan. It is neither a market price target nor a lower bound on value. Successful commercialization could be worth much more; higher spending, claims, or worse recoveries could leave less.

The balance-sheet measurement date is December 31, 2025, with information from the report published February 26, 2026. This is a retrospective annual-report exercise, not an estimate using only information public on December 31, and not a September 2026 valuation. Later quarterly reports are outside this case.

## Filing anchors

- [2025 Form 10-K — SEC](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm): F-4 opening balance sheet; F-5 operating costs; F-8 depreciation and cash flow; Note 9 ENTRA1; Note 14 awards; Note 15 tax agreement; Note 17 commitments.
- [2024 Form 10-K — company annual-report archive](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html): statements of operations and cash flows.
- [2023 Form 10-K — company annual-report archive](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html): statements of operations and cash flows.

USD millions, converted from filing amounts in thousands:

| Historical anchor | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Revenue | 22.810 | 37.045 | 31.479 |
| Gross profit | 3.849 | 32.108 | 11.431 |
| Operating cash flow | -183.254 | -108.666 | -459.610 |

Historical revenue and margins are volatile; constant growth is a scenario assumption, not a statistical finding. The 2023 and 2024 values were cross-checked against their respective annual reports. Forecast starting balances use the 2025 report's presentation.

## Forecast assumptions

Every row below is an **analyst judgment** unless explicitly labelled history. None is labelled management guidance. Figures and formulas are editable in `smr_proforma.py`; numerical settings are centralized in `Assumptions` or named constants.

| Input | Setting | Reason and limitation |
|---|---|---|
| Services revenue | 31.479 each year; 0% growth | Hold the latest annual scale without presuming new module sales. This still assumes replacement service work is won; it is not contracted backlog. Sensitivity: -10% / +10% annual growth. |
| Gross margin | 11.431 / 31.479 = 36.31% | History-derived ratio, forecast judgment to repeat it. Does not extrapolate the unusually high 2024 margin. |
| Recurring operating expense anchor | 45.532 + (609.825 - 507.393) + 45.645 = 193.609 | History-derived normalization: remove the identified ENTRA1 expense, retain other costs. No claim that every remaining expense is recurring. |
| Cash operating costs | 193.609 - 1.004 - 0.177 = 192.428 annually | Subtract historical D&A and model it separately. Hold costs flat, implying active cost control despite inflation; test 2% inflation. |
| Compensation | Cash equivalent for future compensation; no future SBC addback | Historical stock compensation remains in the expense anchor and is treated as future cash pay. This avoids treating employee awards as free funding. Existing awards are included separately in the share allowance. Simplified economic statements, not a GAAP SBC vesting forecast. |
| ENTRA1 cash settlement | 259.884 in 2026 | History: settle the opening payable, with no new expense. No repeat of the prior-year charge. |
| New ENTRA1 milestones | Zero | Conditional on no additional triggering projects. Must be replaced alongside any commercialization revenue scenario; not an assumption that successful module sales incur no milestone cost. |
| Long-lead materials | Add 6.929 in 2026 and 41.938 in 2027 | History: disclosed purchase commitment schedule. Cash outflow is capitalized to materials; zero further discretionary purchases. No materials sales in this services-only case. |
| Other purchase/service/marketing commitments | Included within recurring cash operating costs | Avoid adding ordinary contract spending twice. Assumes the retained expense budget covers those obligations; amounts capitalized to materials and opening ENTRA1 settlement are separate. |
| Receivables/prepaids | Opening balance / opening revenue ratios | Constant balances in the flat-revenue case; changes consume/release operating cash in sensitivities. All receivables treated as an operating proxy, including the small investment-related portion. |
| Ordinary liabilities | Hold 39.077 constant | Model ongoing replacement of paid obligations, with no incremental supplier financing. Includes all opening liabilities other than the separately settled ENTRA1 payable. Settle this balance at wind-down. |
| Capex | 0.508 annually | History-informed maintenance assumption; a module production case would need different reinvestment. |
| Depreciation / amortization | 1.004 / 0.177, each capped at the opening asset balance | Simple run-off convention; new capex starts depreciation in the following year. Prevents negative assets. |
| Other assets | Hold at 45.868 | Includes restricted cash, IPR&D, goodwill and other assets; no optimistic fair-value uplift. Terminal recoveries are specified separately. |
| Investments | Sell 450.754 at carrying value in 2026 | Assumed liquidity at par, not a forecast of realized market prices. Separate investing cash flow; not revenue or an operating cash inflow. |
| Investment return | 3% on estimated average available liquidity | Judgment, not a sourced September 2026 yield. Known January ENTRA1 payment reduces the interest base before accrual. |
| Cash tax | 0.342 foreign allowance plus 25% of positive pretax income | Losses generate no refund or deferred-tax asset. All default forecast years lose money. No claimed value for NOLs. |
| Financing/distributions | Zero debt, new capital, buybacks and dividends | Feasibility condition, not guaranteed funding availability. Minimum cash is 25; script refuses a scenario that breaches it instead of silently inserting financing. |
| Discount rate | 15%; test 10% / 20% | Required equity return chosen for a risky conditional outcome; not a measured CAPM/WACC estimate. No claim that discounting alone prices commercialization probabilities. |
| Terminal treatment | Wind-down after 2030; zero going-concern value | Avoid capitalizing negative cash flows forever. This assumption defines the case and is its largest limitation. |
| Recoveries | Cash 100%; receivables 80%; everything else 0% | No assumed proceeds from materials, IP, prepaid costs, PP&E or restricted cash. Recovery percentages are judgments, not appraisals. |
| Closure costs | Additional 50 | Covers incremental closure burden beyond recorded liabilities; unverified planning allowance. Test 100. |
| Additional terminal claims | Zero by default; test 100 | Contingent legal, contract and tax-agreement termination claims are not fully quantified. A zero setting is a scenario condition, not a finding that no claims exist. |

## Ownership and terminal distribution

The conservative denominator is **346.764728 million**: year-end Class A 318.480601 + exchangeable LLC interests 19.413185 + RSUs 4.184488 + options 4.686454. Figures are from the 2025 balance sheet and award notes.

The model values consolidated economic interests as if the LLC interests were exchanged. Class B voting shares are not independently valuable shares added on top of those interests. There is no separate deduction for book NCI, which would double-count this allocation. This is a simplified if-converted allocation, not a legal liquidation waterfall.

All outstanding options are included without exercise proceeds even when out of the money. This deliberately conservative gross-award allowance is **not** treasury-stock-method dilution or an option valuation. It avoids overstating per-share value but should be refined for a decision-grade estimate. The old 163.731673 million weighted-average EPS denominator is not used.

Terminal proceeds = ending cash + recoverable assets - remaining recorded liabilities - closure costs - additional terminal claims, floored at zero. Discount that single shareholder distribution for five years, then divide by the economic share allowance. Operating losses have already consumed terminal cash. Subtracting their PV again, or adding opening liquidity again, would double-count.

Tax-receivable-agreement acceleration, termination and liquidation consequences require separate review. No tax benefit is valued here and no TRA cash payment is assumed; that does not establish that wind-down could occur free of a claim. The additional-claims sensitivity makes part of this uncertainty visible. Do not treat this result as a guaranteed liquidation recovery.

## What this changes from the ABG and earlier SMR exercises

There is no dealer inventory turnover, floor-plan borrowing, recurring share repurchase, or ABG terminal-debt addback. Long-lead materials and the ENTRA1 cash settlement get separate schedules. Equity accumulates forecast income, cash rolls forward through all three cash-flow sections, and accounting checks must pass independently.

The earlier negative-FCFF perpetual-growth result is superseded **only for this conditional scenario**. A complete going-concern SMR valuation still needs credible contract timing, net project margins after milestone payments, capital needs, funding terms, ownership dilution, tax-agreement cash flows and a sustainable terminal business. This model does not infer module pricing or probability of success from preliminary agreements.

## Run and inspect

From `Week 05`:

```sh
python smr_proforma.py --write-report
python lab09.py
python lab09.py --abg
```

`SMR_Five_Year_Results.md` is generated from the same calculations as terminal output. It includes the income statement, balance sheet, cash flow statement, valuation bridge and sensitivities. `proforma.py` remains the ABG reference.

Suggested checkout wording: “I valued a services-only SMR downside case using five linked statements and discounted residual shareholder proceeds. My assumptions are labelled, all statements reconcile, and I explicitly settle the opening ENTRA1 payable. My result excludes successful reactor commercialization, so it is a conditional scenario value rather than my final fair-value estimate for SMR.”
