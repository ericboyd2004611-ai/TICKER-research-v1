# Lab 11 — Individual submission summary

## Individual submission summary

### Two-driver sensitivity — visible results

Company: NuScale Power (SMR). Each rate applies annually in 2026–2030, with every other independent input reset to base before each full linked-model run. Outputs and signed changes are **USD millions**. Free cash flow is **FCFE**. Lower/base/higher ranges are labelled judgments: revenue growth −10%/0%/+10%; operating-cost growth −2%/0%/+2%. Detailed range rationales, annual paths and statements appear later in this document.

| Driver | Case | Annual input | 2030 EBIT | Change from base | 2030 FCFE | Change from base |
|---|---|---:|---:|---:|---:|---:|
| Revenue growth | Lower | -10% | -186.186 | -4.681 | -178.687 | -4.048 |
| Revenue growth | Base | 0% | -181.505 | +0.000 | -174.639 | +0.000 |
| Revenue growth | Higher | 10% | -174.526 | +6.979 | -169.325 | +5.314 |
| Operating-cost growth | Lower | -2% | -163.017 | +18.488 | -154.690 | +19.950 |
| Operating-cost growth | Base | 0% | -181.505 | +0.000 | -174.639 | +0.000 |
| Operating-cost growth | Higher | 2% | -201.533 | -20.028 | -196.199 | -21.560 |

**Checks:** All six lower/base/higher runs pass the accounting and minimum-cash checks. The restored base matches the initial base exactly across inputs, every annual statement field and checks. Both base runs produce 2030 EBIT **−181.505M** and FCFE **−174.639M**. Accounting tolerance is **1e-7 USD million**; display rounding is **0.001 USD million**.

**Valuation:** Value per share is unavailable for this exercise because sustainable cash flows and a defensible going-concern valuation remain unresolved. Signed negative FCFE is retained in every year. The saved Lab 10 wind-down illustration is not used as the sensitivity valuation output.

### Reconciled original prediction

The supplied original prediction expected higher costs to reduce FCFE, lost investment income to enlarge the decline, and cost-linked payables to offset it if that linkage existed. The illustrative $230M anchor at 5% versus 7% over four years was explicitly not the actual model. Actual model costs start at 192.428M and grow at 0% versus 2% over five steps. The resulting **20.028M cost increase + 1.532M lost investment income = 21.560M FCFE decline**. Costs explain 92.9% and interest 7.1% of the decline. The original 21.917M illustration overstates the comparable actual cost gap by 1.889M; its proximity to the FCFE result was coincidental. Ordinary liabilities are fixed, so there is no cost-linked payable offset. Taxes are 0.342M in both runs, giving zero tax change despite a nonzero tax level.

### Main driver over the tested ranges

**Over these ranges**, operating-cost growth has the larger span: **38.516M EBIT and 41.510M FCFE**, compared with revenue growth spans of **11.660M EBIT and 9.362M FCFE**. Costs compound on a 192.428M anchor, while revenue starts at 31.479M and contributes to operating profit through the model’s approximately 36.31% gross margin. Higher spending also lowers cash and investment income. This is a result conditional on the ranges and the services-only model, not a universal ranking of NuScale’s business drivers.

### Recorded partner question and response

**Supplied partner question:** What actual base costs and growth rates produce the FCFE change, and can the difference be traced through operating expenses, tax, noncash adjustments, working capital and interest income?

**Evidence response:** The model uses 192.428M of FY2025-derived recurring cash-equivalent costs, 0% versus 2% growth for 2026–2030, no loss-related tax benefit, no cost-linked payable financing, and a fixed 3% investment yield applied to recalculated liquidity. In 2030, D&A and capex are each 0.508M and offset. The partner subsequently supplied an arithmetic sign-off and found the comparison internally consistent. The full exchange and the requested cost/tax labels are recorded later.



### Sensitivity — Learn on your own

**1. What is one-at-a-time sensitivity?** It changes one independent input from its base to specified lower or higher values while holding every other independent input at base. The entire linked model recalculates, so dependent items such as profit, cash and investment income can change. Resetting to base before every run prevents multiple assumption changes from being mixed together. This method does not measure combinations of changes or interactions between simultaneously varied drivers.

**2. How does the chosen input range affect the ranking?** The output span is the maximum minus minimum output over the tested lower/base/higher cases. A wider range can create a larger span even when a driver is not inherently more influential. Narrowing ranges can shrink spans or change the ranking; nonlinear model relationships also matter. Comparisons should state “over these ranges” and justify each range. Here, the cost-growth range spans 4 percentage points and the revenue-growth range spans 20 percentage points; the dollar bases and model relationships differ as well.

**3. Why is a sensitivity table not a forecast probability?** It gives conditional answers: what the model produces *if* an input takes a specified value. It assigns no probabilities to the cases and does not show how likely an outcome is. Lower/base/higher are not automatically confidence limits, equally likely outcomes, or probability-weighted forecasts. Probabilities would require separate evidence and a justified probability model, including dependencies among assumptions.

**Student takeaway:** My takeaway does not change.

Supporting model output is visible below, so a reader need not execute code.
