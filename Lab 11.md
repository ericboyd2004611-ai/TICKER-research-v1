# Lab 11 — SMR Base Model Run

Date: September 29, 2026  
Company: NuScale Power (SMR)

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

## Step 1 — Completed

Ran the existing Lab 10 company model using its unchanged base inputs:

```sh
cd "Week 05"
python3 lab10_smr_proforma.py
```

The run exited successfully. Its output matches the saved September 24 Lab 10 report, ignoring trailing whitespace. All accounting checks pass for 2026–2030, including the balance sheet, cash roll-forward, and equity roll-forward. Cash stays above the model's minimum requirement in every forecast year.

The conditional services-only/wind-down value is $0.1063 per share. This is the existing model's scenario result, not a current market price target. Historical source notes and the dated market observation in the output are retained from Lab 10; they were not refreshed during this run.

## Partner exchange 1 — In progress

### Partner's company and proposed input

Company: Joby Aviation. Proposed key input: commercial-service start timing, tied in the partner's explanation to FAA type certification and the start of scaling U.S. revenue.

Partner explanation supplied by the student:

> my partners company is Joby Aviation. The input is when commercial service starts: the date Joby gets FAA type certification and US revenue begins to scale. A type certificate is the FAA's approval that an aircraft design is safe for commercial passengers.
>
> Why timing beats every other input. Joby has no core air-taxi revenue yet. Its current revenue is mostly the Blade helicopter business, which brought in $36.2 million in Q2 revenue. Nearly all of Joby's value therefore sits in cash flows years away. Timing hits that value through three channels at once.

These are partner-provided claims, not independently verified findings. The year and source for the Q2 revenue figure were not supplied. The initial explanation ended before identifying its three timing channels; the follow-up below supplies them. The claim that timing matters more than every other input has not yet been demonstrated by model sensitivities.

### Draft listener response — AI preparation, not a recorded exchange

“My understanding is that a later launch pushes expected air-taxi cash flows farther into the future, adds spending before those revenues arrive, and could create a need for additional financing. Those effects could reduce value per share.”

### Suggested question — not yet asked or answered

“What evidence supports your earliest, base-case, and latest revenue-start dates, and what approvals or operational steps must occur between type certification and commercial launch?”

### Gaps recorded from the supplied notes

- Partner's three timing channels have now been supplied and are recorded below.
- Proposed certification dates and supporting rationale are now recorded below; separate commercial-launch dates and original-source verification remain outstanding.
- The explanation links certification and revenue scaling; the time and remaining requirements between those events need clarification.
- The year and source supporting the stated $36.2 million Q2 Blade revenue figure are missing.
- The actual listener restatement, question asked, and partner answer remain unrecorded.
- The SMR explanation, teach-back, question, and answer have now been supplied and are recorded in the SMR section below.

These gaps were recorded from the student's supplied notes during AI assistance. No claim is made that the partners recorded them before consulting AI. Practice partner material in the saved Lab 10 output below remains preparation, not a completed exchange.

### Partner's three timing channels — additional notes

The following financial figures and source labels were supplied by the student from the partner's explanation. Original source links have not been supplied or independently verified.

1. **Discounting:** At an assumed 15% required return (partner judgment, not sourced), delaying an otherwise unchanged future cash-flow stream by one year multiplies its present value by 1 / 1.15 = 0.8696, a **13.04% reduction**. This applies to the shifted cash flows, not automatically to the entire company's equity value.
2. **Extra cash burn:** Partner reports $202 million of cash and short-term investment use in Q2 2026 and $385–415 million of cash-use guidance for the second half of 2026, labelled “SEC.” Doubling the half-year guidance gives **$770–830 million annually**, rather than $750–800 million. This annualization is an illustrative calculation, not verified annual guidance or a forecast that spending remains constant.
3. **Financing and dilution:** Partner reports $2.3 billion of cash and investments at Q2 2026, a stated two-to-three-year runway (source labels “SEC” and “Fool”), a September 24 share price of $6.24 (label “247wallst”), and approximately 970 million Q2 weighted-average shares (label “SEC”). At $800 million annual cash use, simple runway is **2.875 years**. Raising $800 million at $6.24 would issue **128.205 million shares**, before fees. Relative to an illustrative 970 million starting shares, share count rises **13.22%**; existing holders' percentage ownership falls **11.67%**, calculated as 128.205 / (970 + 128.205). Weighted-average shares are not necessarily the actual shares outstanding at a future financing date, so the denominator needs verification. A funding shortfall may require financing, spending changes, or other action; it does not establish that a stock sale is inevitable. Ownership dilution is not automatically the same percentage decline in value per share, because the financing also adds cash.

### Updated draft listener restatement — AI preparation

“A delay can lower present value by moving air-taxi cash flows farther into the future, use more cash before launch, and potentially require financing that changes the share count. Your 15% discount rate is a judgment; the launch-date range, spending path, and financing assumptions determine how strongly those channels affect value per share.”

### Remaining evidence question

“What supports your earliest, base-case, and latest commercial-launch dates? Can you provide the original filing links for cash use, liquidity, and shares, and explain what happens between type certification and revenue scaling?”

### Proposed certification range and supporting rationale — partner notes

The student supplied the following partner range for FAA type certification. Source names are recorded as provided; no article URLs or original filings accompanied these notes, and these claims have not been independently verified.

| Scenario | Proposed type-certificate timing | Partner's rationale | Evidence status |
|---|---|---|---|
| Bull | Late 2026 / early 2027 | Reported March 11, 2026 first FAA-conforming-aircraft flight testing (Aerotime); expected FAA “for credit” TIA testing later in 2026 (CompositesWorld); reported strongest quarterly final-stage progress (SEC); a Motley Fool report of expected certification by end of 2026 | Milestone claims require original-source verification. The end-2026 expectation is secondary reporting and needs confirmation against the Q2 shareholder letter. Milestones alone do not establish a completion date. |
| Base | Mid-to-late 2027 | Partner cites an early-2026 Flying report that SMG Consulting expected commercial launch closer to late 2027 or beyond, citing industry TIA delays | The cited forecast concerns commercial launch, not necessarily type certification. It does not directly establish a mid-to-late-2027 certificate date. Original wording, publication date, and any updated forecast need checking. |
| Bear | 2028–2029 | Possible aerospace certification slippage | Explicit partner judgment. No quantified eVTOL delay evidence was supplied to calibrate these dates. |

The partner describes TIA as Type Inspection Authorization and associates it with FAA testing against certification requirements. The exact regulatory definition and remaining program steps have not been verified here.

**Partner's market observation:** The stock reportedly fell 63% over the past year, attributed to certification impatience and heavy cash burn; the partner infers that investors already price some delay. The measurement date, price series, and source were not supplied. Neither the percentage nor the causal attribution has been verified. A stock decline alone does not quantify the certification delay embedded in the price.

### Follow-up question for the actual exchange

“Your base-case source forecasts commercial launch rather than the certificate date. What certificate date and certificate-to-launch lag are you assuming separately in each scenario, and what evidence supports those assumptions?”

### Exchange completion status

The partner's proposed input, three mechanisms, timing range, and stated rationale are now recorded. Original-source verification remains outstanding. The actual listener restatement and question asked must still be confirmed, along with the partner's answer to the certification-versus-launch distinction. The SMR explanation and response are now recorded in the later SMR section. AI-drafted statements and questions above are preparation, not evidence that the exchange occurred.

## SMR side of partner exchange — supplied explanation, teach-back, and answer

The following records the student's supplied discussion material. Current-company figures and management/contract claims have not been independently verified; no original source links were supplied with this material. The saved Lab 10 baseline below remains unchanged.

### Part 1 — Explainer

Proposed key input: annual cash operating costs, separating recurring engineers, R&D, and overhead from contingent ENTRA1 milestone payments. The supplied explanation defines cash costs as excluding noncash stock compensation and describes ENTRA1 as NuScale's commercial partner. Whether this input matters most remains a sensitivity hypothesis, not a tested ranking.

Supporting claims supplied:

- Q2 2026 revenue of $0.075M versus $8.1M a year earlier.
- Q2 cash and investments of $1.9B, no debt, a September 25, 2026 price around $8.41, and approximately 430M shares from an aggregator. These imply approximately $3.616B market capitalization and cash/investments equal to 52.5% of that amount. The share count requires checking against the filing.
- A $50M annual cost change over five years, discounted at an assumed 12%, changes present value by approximately $180M, or approximately 5% of the stated market capitalization.
- A $507.4M ENTRA1 Milestone Contribution 1 expense was the main driver of higher 2025 costs.
- A potential TVA/ENTRA1 power purchase agreement is said to trigger approximately $16M per module; 72 modules imply $1.152B, approximately 31.9% of the stated market capitalization. Contract triggers, timing, and amounts require original-source verification.
- Raising $100M at $8.41 would issue about 12M shares, described in the supplied explanation as approximately 3% dilution.
- H1 2026 operating cash burn of $372.9M alongside an approximately $268M decline in accounts payable suggests, in the student's explicitly labelled inference, that much of the burn settled previously accrued milestones. The relevant payable and cash-flow reconciliation require verification. Annualizing headline burn gives $745.8M, potentially overstating recurring expenditure.

### Part 2 — Supplied listener teach-back and question

“So NuScale has basically no revenue, and about half its market value is cash. Every dollar it spends comes straight out of that pile, times however many years until reactors ship. The catch is that 'cash costs' hides two things: steady overhead of maybe $200-something million a year, and huge one-off payments to ENTRA1 that could exceed a billion if the TVA deal firms up. If you blend them, you either overstate or understate the burn by hundreds of millions. What supports the range you'd use for each piece?”

### Part 3 — Supplied answer: evidence for the range

**Recurring costs: $170M–$280M annually; approximately $230M base.**

- Low: attributed management statement of historical quarterly operating expenses of $41–44M, equivalent to $164–176M annually. Whether those expenses exclude noncash items and match the forecast scope needs verification.
- Base: supplied Q2 R&D $18.4M + G&A $26.9M + other expenses $18.5M = $63.8M. The supplied explanation attributes other expenses to engineers reclassified from cost of sales. Subtracting estimated quarterly stock compensation of $5.875M (half of reported H1 $11.75M) yields $57.925M quarterly, or **$231.7M annually**. Using an H1 average for Q2 compensation is an assumption; other noncash charges and working-capital effects must also be reconciled before calling this cash burn.
- High: $280M is a judgment based on possible continued R&D/headcount growth, including a supplied $6.6M year-over-year R&D increase. No company guidance supporting this endpoint was supplied.
- Investment income: supplied Q2 $13.9M annualizes to $55.6M. It is separate from operating costs and depends on future invested balances and yields.

**Future ENTRA1 milestone contributions: $0 to approximately $1.152B, proposed probability weighting.**

- Zero-payment case: the supplied explanation says the next phase is contingent on signed power purchase agreements and the TVA arrangement remains nonbinding.
- High-payment case: 72 modules × $16M = $1.152B.
- Deal probability is explicitly a judgment; no numerical probability has been supplied. Payment timing, partial-module outcomes, and associated commercial revenue must be modelled consistently with the same scenario.

**Illustrative runway:** $1.9B / $230M = 8.26 years; after a $1.152B payment, ($1.9B − $1.152B) / $230M = 3.25 years. These are simple ratios, excluding other cash uses, revenues, investment income, funding, minimum cash requirements, and timing. The supplied explanation attributes one analyst's 2–3-year estimate to annualizing milestone-inflated H1 burn; that attribution is unverified because the analyst source was not supplied.

### Arithmetic and consistency checks against the saved model

- With five end-of-year payments, $50M × [1 − (1.12)^−5] / 0.12 = **$180.24M**, approximately **4.98%** of $3.616B. This is a stand-alone illustration at 12%, not a sensitivity run of the saved model, which uses **15%**.
- $100M / $8.41 = **11.89M new shares**. Against an illustrative 430M starting shares, share count increases **2.77%** and existing holders' ownership percentage falls **2.69%**, before fees. A share issuance also adds cash, so ownership dilution is not automatically the same percentage loss of per-share value.
- Saved Lab 10 recurring cash operating costs are **$192.428M annually**, not $230M. That model deliberately treats compensation as future cash-equivalent pay and does **not** subtract stock compensation from its recurring expense anchor. The new definition differs; it cannot be substituted without deciding how ongoing compensation and dilution are treated.
- Saved Lab 10 already separates the **$259.884M opening ENTRA1 payable**, paid in 2026, from recurring expenses. It assumes **zero new project-triggered milestone payments** in its services-only scenario. An accrued expense and its later payment must not both be charged as new expenses.
- Saved Lab 10 starts from December 31, 2025 balances, holds annual services revenue at **$31.479M**, and uses approximately **346.765M economic shares/awards**. The new Q2 2026 liquidity and approximately 430M shares describe a different measurement date and denominator. They are discussion inputs, not replacements already implemented in the baseline.
- “Steady and predictable” recurring costs is an assumption to test. The supplied discussion itself identifies staffing and R&D changes. Accounting operating expenses, cash operating expenditure, and total operating cash flow are different measures.

### Remaining exchange gaps

Both companies' explanations and proposed ranges are now recorded, and the SMR teach-back/question/answer text has been supplied. The actual Joby listener restatement and question asked remain to be documented; the response distinguishing certificate timing from commercial-launch timing is still outstanding. Original source links are needed to verify the newer company claims. No model inputs or baseline forecasts were changed by adding this discussion.

## Which assumptions drive my company's forecast and value, and what explains their effects?

For NuScale (SMR), the main drivers are operating costs, commercialization timing, ENTRA1 payments, and the model's terminal assumption.

| Assumption | Why it affects the forecast and value |
|---|---|
| **Recurring operating costs** | The baseline assumes **$192.428M annually**. Higher costs increase losses and reduce remaining cash, leaving less for shareholders. These costs accumulate across all five forecast years. |
| **Revenue growth and commercialization timing** | The baseline holds services revenue at **$31.479M annually**. Earlier profitable commercialization could increase cash flows, but would also require modelling related spending, milestone payments, and funding. |
| **ENTRA1 milestone payments** | The model separately pays the **$259.884M opening obligation** in 2026 and assumes no new milestones. Additional payments would reduce liquidity; their timing must match the commercial projects that trigger them. |
| **Terminal treatment** | The baseline assumes **wind-down after 2030**, with no continuing business value. This is a major reason its value is low: it excludes successful reactor commercialization beyond the forecast. |
| **Discount rate** | The assumed **15% required return** reduces the present value of future shareholder proceeds. A higher rate lowers today's value. |
| **Financing and share count** | The baseline assumes no new financing. If spending requires new equity, the additional shares change how future value is divided among shareholders. |

**Central explanation:** Recurring costs steadily consume cash, while commercialization timing determines how long that spending continues before meaningful revenue arrives. ENTRA1 payments can add large cash demands along the way.

The model's **$0.1063 per-share result is a conditional services-only wind-down value**, not a complete valuation of NuScale's commercial potential. These mechanisms identify important drivers; a consistent sensitivity comparison is needed to establish which input has the largest numerical effect. This explanation does not change the saved baseline inputs or results.

## Two operating drivers already in the model

1. **Revenue growth:** Set at **0%**, keeping annual services revenue at **$31.479 million**. Higher growth increases sales and gross profit, assuming the gross margin stays constant.
2. **Operating-cost growth:** Set at **0%**, keeping annual cash operating costs at **$192.428 million**. Higher cost growth increases losses and reduces cash available to shareholders.

These are the existing baseline settings; no model inputs were changed.

## V — Check the result

Automated evidence checks were performed against the saved unrounded results. These are AI/code checks, not a claim that a partner performed them.

| Check | Actual result |
|---|---|
| Base before and after | PASS: identical inputs, all annual statement fields, and checks, with exact equality. |
| Only selected independent input changes | PASS: each scenario’s complete saved input set equals a fresh base copy except its named driver. Both driver base cases equal the initial base. Linked statement quantities are recalculated. |
| Accounting checks | PASS for every year of all eight runs (initial base, six driver cases, restored base). No invalid production runs. |
| Signed changes | PASS: every reported EBIT and FCFE change recomputes as scenario minus initial base. |
| Spans | PASS: maximum minus minimum of the three valid lower/base/higher results for each driver. |

Accounting/recomputation tolerance: **1e-7 USD million**. Displayed amounts are rounded to **0.001 USD million**; subtracting rounded cells can differ by 0.001 from the displayed change calculated from unrounded values. The restored-base match is exact, stronger than this tolerance.

### Selected evidence for partner exchange 2

Selected run: annual operating-cost growth rises from 0% to +2% in every year 2026–2030 (+2 percentage points each year). Revenue growth remains 0%. The complete saved assumption sets confirm that all other independent inputs remain at base.

| 2030 item (USD millions) | Base | Higher cost-growth run | Signed change |
|---|---:|---:|---:|
| Revenue | 31.479 | 31.479 | +0.000 |
| Cash operating costs | 192.428 | 212.456 | +20.028 |
| Operating profit / EBIT | -181.505 | -201.533 | -20.028 |
| Investment income | 7.208 | 5.676 | -1.532 |
| Taxes | 0.342 | 0.342 | +0.000 |
| Net income | -174.639 | -196.199 | -21.560 |
| D&A addback | 0.508 | 0.508 | +0.000 |
| Operating cash flow | -174.131 | -195.691 | -21.560 |
| Capex cash flow | -0.508 | -0.508 | +0.000 |
| FCFE | -174.639 | -196.199 | -21.560 |
| Closing cash | 156.545 | 93.932 | -62.613 |
| Closing equity | 289.733 | 227.120 | -62.613 |

**Recompute from unrounded evidence:**

- EBIT: -201.533060798 − (-181.505000000) = **-20.028060798 USD M**.
- FCFE: -196.199257455 − (-174.639173989) = **-21.560083466 USD M**.

**Statement trace:** The input gives 2030 cash operating costs of 192.428 × 1.02^5 = 212.456 USD M. Unchanged revenue, gross margin and D&A mean the 20.028 increase in costs lowers EBIT by 20.028. Cumulative cash spending also reduces the model’s average invested liquidity, lowering 2030 investment income by 1.532. With taxes unchanged, net income and FCFE fall by 21.560. In 2030, working-capital, material-purchase and ENTRA1 movements are zero in both cases; D&A of 0.508 and capex of 0.508 offset. Lower cumulative net income flows into lower equity and lower cash. The full annual linked statements and checks are retained in the sensitivity section.

### Recorded review and takeaway

The supplied arithmetic sign-off, statement questions, model response and reconciled prediction are recorded below. **Student takeaway: My takeaway does not change.**

### Partner exchange 2 — supplied feedback and model evidence

**Feedback supplied:** The listener recomputed −196.199 − (−174.639) = −21.560 USD M and confirmed the arithmetic. The listener explicitly could not confirm input isolation without seeing the model. They requested side-by-side revenue, capex, working-capital, tax, financing, interest, ENTRA1 and share-issuance evidence, then an income-statement, cash-flow and balance-sheet trace. They offered a clearly labelled illustrative $230M starting cost base at 5% versus 7% growth over four years and asked for the actual model settings. They questioned noncash compensation, tax benefits, working-capital offsets and lost investment income. This records the supplied feedback; it does not claim that the listener has subsequently reviewed the evidence below.

**Correction to the isolation criterion:** Only the selected independent assumption changes. Linked accounting outputs should change when the model requires it. In particular, unchanged investment-yield assumptions do not require unchanged investment income: lower cash balances reduce interest earned. A changed linked output is not evidence that a second independent input changed.

**Correction to negative-FCFE wording:** Negative FCFE represents a cash shortfall after operating cash flow, capex and net debt borrowing. It need not mean a new shareholder contribution. In these runs the shortfall uses existing liquidity; there is no new equity or debt financing.

#### Actual inputs and linked quantities side by side

The actual anchor is **$192.428M**, with **0% versus +2% annual cost growth** applied in **2026, 2027, 2028, 2029 and 2030**. Thus the higher 2030 cost is 192.428 × 1.02^5, not the listener's illustrative $230M at 5%/7% for four years.

| Item | Base | Higher-cost case | Independent input or linked output? |
|---|---|---|---|
| Annual cost growth, 2026–2030 | 0% | +2% | Only changed independent assumption |
| Annual revenue growth | 0% | 0% | Unchanged input |
| Revenue in each forecast year (USD M) | 31.479 | 31.479 | Same linked output |
| Annual capex (USD M) | 0.508 | 0.508 | Unchanged input |
| Receivables/prepaids rule | Opening balances / opening revenue ratios | Same | Unchanged rule; flat revenue means no cash movement in either run |
| Ordinary liabilities (USD M) | 39.077, held constant | 39.077, held constant | No extra payable funding from higher costs |
| Long-lead materials purchases (USD M) | 6.929 in 2026; 41.938 in 2027; zero thereafter | Same | Unchanged schedule; no inventory-days driver |
| Tax assumption | 0.342 annual foreign allowance + 25% of positive pretax income | Same | Unchanged rule; no loss refund or deferred-tax benefit |
| 2030 tax expense / cash tax (USD M) | 0.342 | 0.342 | Same output despite losses; not zero |
| Net debt issued/repaid | Zero | Zero | Unchanged assumption; no debt interest |
| Investment yield | 3% | 3% | Unchanged input applied to recalculated liquidity |
| 2030 investment income (USD M) | 7.208 | 5.676 | Linked output changes |
| ENTRA1 payment (USD M) | 259.884 in 2026; zero thereafter | Same | Separate opening-payable settlement; not grown with recurring costs |
| New equity issuance/distributions | Zero | Zero | Unchanged assumption |
| Share denominator (millions) | 346.764728 | 346.764728 | Unchanged model denominator |

#### Trace answering the listener's questions

**Income statement:** The model uses one aggregate cash-operating-expense line, not separate forecast R&D/G&A/other lines. By 2030 it rises from 192.428 to 212.456 USD M, an increase of **20.028M**. With unchanged revenue, gross margin and D&A, EBIT falls by exactly that unrounded cost difference, from −181.505 to −201.533M. Investment income also falls by **1.532M** because prior spending reduces available liquidity. Tax remains 0.342M in both cases; no tax benefit is generated by losses. Net income therefore falls by **21.560M**.

**Cash flow statement:** 2030 D&A addback remains 0.508M. The model treats recurring compensation as cash-equivalent future pay and has no future SBC addback; it does not forecast actual stock-award vesting and issuance. Receivables/prepaids, long-lead-material purchases and ENTRA1 cash movements are zero in 2030 in both runs, and ordinary liabilities do not scale with cost. Operating cash flow falls from −174.131 to −195.691M. Subtracting unchanged capex of 0.508M gives FCFE of −174.639 versus −196.199M. Thus **−20.028M additional costs − 1.532M lost investment income = −21.560M FCFE change**, using unrounded values for the calculation.

**Balance sheet:** Cumulative differences across all five years reduce 2030 cash from **156.545 to 93.932M**, a **62.613M** reduction, rather than just the final-year 21.560M change. Consolidated equity falls from **289.733 to 227.120M**, also 62.613M, because net income rolls into equity. The model does not show a separate retained-earnings account. Other ending assets and liabilities are unchanged in this comparison, so cash and equity move together and both balance sheets reconcile within 1e-7 USD M. Higher-case cash remains **68.932M above the $25M minimum**.


#### Follow-up listener sign-off and requested labels

**Supplied listener sign-off:** The listener reports recomputing all table values and finding them internally consistent. They confirm the 21.560M FCFE decline is explained by 20.028M higher operating costs plus 1.532M lower investment income. They find the selected 2030 bridge consistent with cost-only input changes and request clear labels for the base-cost derivation, tax allowance, and capex/working-capital treatment. This records the supplied feedback; the complete independent-input comparison is separately supported by the automated checks.

**FY2025-derived recurring cost anchor, not a reported cash-cost line:** The saved model cites NuScale's [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm), particularly the statement of operations, cash-flow statement and Note 9 ENTRA1. The saved model's derivation in USD millions is:

| Derivation | USD millions |
|---|---:|
| FY2025 R&D | 45.532 |
| FY2025 G&A | 609.825 |
| Less identified ENTRA1 charge | −507.393 |
| FY2025 other operating expenses | 45.645 |
| Normalized operating-expense anchor | 193.609 |
| Less separately modelled depreciation | −1.004 |
| Less separately modelled amortization | −0.177 |
| Model recurring cash-equivalent expense anchor | **192.428** |

These amounts and the filing reference are taken from the saved Lab 10 source and notes; this addition does not represent a new filing verification. The anchor is based on FY2025 reported expenses with modelling adjustments. The first forecast increase occurs in 2026, so the 2030 higher-cost result uses five growth steps. The anchor excludes the identified ENTRA1 expense, while the unpaid opening ENTRA1 balance of 259.884M is settled separately in 2026. **Stock compensation is not subtracted:** the model treats future compensation as cash-equivalent pay and adds back no future SBC. Therefore the anchor differs in date, components and compensation treatment from the partner's approximately 230M estimate based on Q2 2026 expenses less estimated SBC. The two estimates need a common-basis reconciliation before substitution.

**Tax label:** The code explicitly uses a **0.342M annual foreign-tax allowance**, plus 25% of positive pretax income. The 0.342M amount is anchored to the saved FY2025 income-tax expense; repeating it as a future foreign cash-tax allowance is a **model judgment**. No tax refund or deferred-tax asset is created for forecast losses. This identifies the model's treatment, not independent confirmation that all historical 0.342M was legally classified as foreign tax. That historical composition would require checking the tax note.

**2030 cash-flow bridge:** Capex is **not zero**: it is a 0.508M cash outflow in both runs. D&A is a 0.508M noncash addback, so the two offset exactly in 2030 under the saved depreciation/run-off and maintenance-capex assumptions. Receivables and prepaids are linked to flat revenue and do not change; ordinary liabilities are deliberately held constant, so rising costs do not generate extra payable financing. Scheduled long-lead-material purchases and the opening ENTRA1 payment have finished before 2030. Those 2030 cash movements are zero by assumption and schedule, not missing links. Therefore FCFE equals EBIT + investment income − tax in that year. The same simplified bridge should not be assumed for earlier forecast years.

**Funding scope:** Under the existing inputs, the higher-cost run ends 2030 with 93.932M cash, 68.932M above the model's 25M floor, and all annual minimum-cash checks pass. This supports no new funding within this scenario only. Replacing the cost anchor or adding new project-linked payments would be a different scenario requiring a full rerun; no such change was made here.


#### Prediction comparison — student-supplied answer to item 2

**Original prediction, as supplied:**

- With no tax, the FCFE gap should roughly equal the 2030 cash-cost gap.
- Interest income on lower cash would make the FCFE gap larger than the cost gap.
- Payables scaling with costs would make it smaller.
- Illustration, explicitly not the actual model: a $230M base growing at 5% versus 7% over four years gives approximately a $21.9M cost gap.

**Actual result:** A **20.028M cost increase**, **1.532M reduction in investment income**, and **21.560M decline in FCFE**, all USD millions.

**What matched — supplied reflection:** Costs dominate the selected change, explaining approximately 92.9% of the FCFE decline. The direction of the interest effect was correct: FCFE fell more than costs rose.

**What surprised me — supplied reflection:**

1. **The illustration was close for the wrong reasons.** Its approximately $21.9M figure was within $0.3M of the FCFE decline, but the inputs and output measure differed. The overstatements and understatements roughly cancelled; the closeness does not establish a calibrated or validated numerical prediction.

| Item | Original illustration | Actual model | Effect on comparison |
|---|---|---|---|
| Base cost | $230M | $192.428M | Illustration used a higher anchor, increasing its cost gap |
| Annual growth rates | 5% versus 7% | 0% versus 2% | Same two-percentage-point separation, but higher compounding rates in the illustration increase its cost gap |
| Growth periods | Four | Five, 2026–2030 | Fewer periods reduce the illustration's gap |
| Output measured | Cost gap only | FCFE gap including investment-income effect | Illustration omitted the interest linkage |

Recomputed illustration: 230 × (1.07^4 − 1.05^4) = **21.917M**. It exceeds the actual **cost gap** by **1.889M** and exceeds the actual **FCFE decline magnitude** by **0.357M**. These are different comparisons; the cost-gap comparison is the matching-output comparison.

2. **The interest effect was larger than expected.** The supplied reflection describes interest as initially a footnote; it accounts for approximately 7.1% of the final-year FCFE decline. The student identifies remaining liquidity as a follow-up research question rather than treating the interest linkage as negligible. The computed higher-cost case still passes the $25M cash floor; this concern does not establish a funding shortfall in the current run.

3. **The working-capital offset did not occur.** The prediction identified cost-linked payables as a possible dampener, but the actual model holds ordinary liabilities constant. That mechanism is absent by assumption; its absence is not a failed accounting reconciliation.

**Tax clarification preserving the original prediction:** The original wording assumed “no tax.” The actual model has a $0.342M foreign-tax allowance in both cases. Its *change* is zero, so tax does not alter the difference between the cases despite the nonzero level.

**Student takeaway:** My takeaway does not change.

## E — Find the driver

| Output span over stated ranges (USD millions) | Revenue growth: −10% / 0% / +10% | Cost growth: −2% / 0% / +2% | Larger span |
|---|---:|---:|---|
| 2030 operating profit / EBIT | 11.660 | 38.516 | Operating-cost growth |
| 2030 FCFE | 9.362 | 41.510 | Operating-cost growth |
| Value per share | Unavailable | Unavailable | Cannot rank |

**Over these ranges**, operating-cost growth has the larger span for both final-year operating profit and FCFE. A span depends on the chosen range and the model’s scale and relationships; this does not establish an inherently more important driver for every possible scenario. No value-per-share ranking is available.

Verification command: `python3 "Week 06/lab11_verify.py"`. Visible model evidence and recorded SMR review are retained above.

## Lab 11 — Reproducible operating-driver sensitivities

Run command: `python3 "Week 06/lab11_sensitivity.py"` from the course folder.

Each run loads a fresh copy of the working Lab 10 module and deep-copies the separately saved base inputs. Only the named growth assumption changes; opening balances, other independent assumptions and constants reset to base. The entire linked model recalculates. The original model is not edited.

Working Lab 10 source SHA-256: `c46d64fef740475d0380fbe8826c794a42ba8d748b4730929a065285a1883815`. Source matches the saved base-run source.

### Existing ranges (unchanged)

| Driver | Lower | Base | Higher | Affected years and units | Previously recorded reason |
|---|---:|---:|---:|---|---|
| Revenue growth | −10% | 0% | +10% | Annual growth in each year 2026–2030; −10/0/+10 percentage-point shifts from base | Labelled judgment: existing Lab 10 services-revenue sensitivity range; historical growth was +93.24%, +62.41%, and −15.02% in 2023–2025. This range is not company guidance or the full historical range. |
| Operating-cost growth | −2% | 0% | +2% | Annual growth in each year 2026–2030; −2/0/+2 percentage-point shifts from base | Labelled judgment: previously selected annual cost reduction/escalation around flat costs; the +2% case already appears in Lab 10. No new range is selected here. |

Revenue in year y = 31.479 × (1 + revenue growth)^(y − 2025). Cash operating costs = 192.428 × (1 + operating-cost growth)^(y − 2025). Amounts are USD millions. The 2026 rate applies first; subsequent years compound. Percentage-point changes describe changes in rates, not relative percent changes in those rates.

### Output definitions and valuation limitation

Final year is 2030. Operating profit is EBIT. **FCFE = operating cash flow − capital expenditures + net debt borrowing**, with zero net debt borrowing in this model. Investment liquidation is excluded; operating cash flow includes the model’s investment income and operating working-capital and ENTRA1 payments. All annual signed cash flows are retained.

**Value per share is unavailable for this exercise:** forecast FCFE is negative and a defensible going-concern valuation remains unresolved. The earlier conditional wind-down illustration is preserved in Lab 10 but is not treated as a valid company valuation for this sensitivity task. No terminal value is added. Value/share changes and spans are also unavailable.

### Lower/base/higher results and signed changes

Amounts and changes are USD millions. Changes = scenario minus first base run. Invalid runs are flagged and excluded from spans, never ranked.

| Run | Revenue growth, each year (%) | Cost growth, each year (%) | 2030 EBIT | Δ EBIT | 2030 FCFE | Δ FCFE | Value/share (USD) | Status |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Initial base | +0.0 | +0.0 | -181.505 | +0.000 | -174.639 | +0.000 | Unavailable | VALID |
| Revenue growth — Lower | -10.0 | +0.0 | -186.186 | -4.681 | -178.687 | -4.048 | Unavailable | VALID |
| Revenue growth — Base | +0.0 | +0.0 | -181.505 | +0.000 | -174.639 | +0.000 | Unavailable | VALID |
| Revenue growth — Higher | +10.0 | +0.0 | -174.526 | +6.979 | -169.325 | +5.314 | Unavailable | VALID |
| Operating-cost growth — Lower | +0.0 | -2.0 | -163.017 | +18.488 | -154.690 | +19.950 | Unavailable | VALID |
| Operating-cost growth — Base | +0.0 | +0.0 | -181.505 | +0.000 | -174.639 | +0.000 | Unavailable | VALID |
| Operating-cost growth — Higher | +0.0 | +2.0 | -201.533 | -20.028 | -196.199 | -21.560 | Unavailable | VALID |
| Restored base | +0.0 | +0.0 | -181.505 | +0.000 | -174.639 | +0.000 | Unavailable | VALID |

### Output spans: maximum minus minimum

| Driver | Valid lower/base/higher runs | 2030 EBIT span (USD M) | 2030 FCFE span (USD M) | Value/share span |
|---|---:|---:|---:|---|
| Revenue growth | 3/3 | 11.660 | 9.362 | Unavailable |
| Operating-cost growth | 3/3 | 38.516 | 41.510 | Unavailable |

### Restored base

Restored base rerun matches the first base run exactly across inputs, every annual statement field and accounting checks: **PASS**.

### Traceable annual statements and visible checks

All amounts below are USD millions. Raw check gaps are shown in scientific notation; tolerance is 1e-7 million. The original model also checks minimum cash and nonnegative PP&E, intangibles, long-lead materials and ENTRA1 liability. All independent inputs and unrounded statement fields are retained for every run in `Lab11_Sensitivity_Results.json`.

#### Initial base

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -182.178 | -182.178 | -182.102 | -181.505 | -181.505 |
| Investment income | 27.987 | 22.638 | 17.233 | 12.294 | 7.208 |
| Pretax income | -154.191 | -159.540 | -164.869 | -169.211 | -174.297 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 959.018 | 799.136 | 633.925 | 464.372 | 289.733 |
| Liabilities plus equity | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -0.000 | -0.000 | -0.000 | -0.000 | -0.000 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -420.165 | -200.639 | -164.106 | -169.045 | -174.131 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 30.081 | -201.147 | -164.614 | -169.553 | -174.639 |
| Opening cash | 836.417 | 866.498 | 665.351 | 500.737 | 331.184 |
| Closing cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| FCFE before equity issuance/distributions | -420.673 | -201.147 | -164.614 | -169.553 | -174.639 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +0.000e+00 | -5.684e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 841.498 | PASS |
| 2027 | +0.000e+00 | -2.842e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 640.351 | PASS |
| 2028 | +0.000e+00 | +2.842e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 475.737 | PASS |
| 2029 | +5.684e-14 | +2.842e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 306.184 | PASS |
| 2030 | +5.684e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 131.545 | PASS |

#### Revenue growth — Lower

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 28.331 | 25.498 | 22.948 | 20.653 | 18.588 |
| Cost of sales | 18.043 | 16.239 | 14.615 | 13.153 | 11.838 |
| Gross profit | 10.288 | 9.259 | 8.333 | 7.500 | 6.750 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -183.321 | -184.350 | -185.200 | -185.436 | -186.186 |
| Investment income | 27.990 | 22.629 | 17.178 | 12.163 | 6.971 |
| Pretax income | -155.331 | -161.721 | -168.021 | -173.273 | -179.215 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -155.673 | -162.063 | -168.363 | -173.615 | -179.557 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.683 | 664.548 | 497.855 | 325.207 | 146.520 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 7.540 | 6.786 | 6.108 | 5.497 | 4.947 |
| Prepaid expenses | 4.389 | 3.950 | 3.555 | 3.200 | 2.880 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 996.955 | 834.892 | 666.528 | 492.914 | 313.357 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 957.878 | 795.815 | 627.451 | 453.837 | 274.280 |
| Liabilities plus equity | 996.955 | 834.892 | 666.528 | 492.914 | 313.357 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -155.673 | -162.063 | -168.363 | -173.615 | -179.557 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | 1.326 | 1.193 | 1.074 | 0.966 | 0.870 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -419.980 | -201.627 | -166.185 | -172.140 | -178.179 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 30.266 | -202.135 | -166.693 | -172.648 | -178.687 |
| Opening cash | 836.417 | 866.683 | 664.548 | 497.855 | 325.207 |
| Closing cash | 866.683 | 664.548 | 497.855 | 325.207 | 146.520 |
| FCFE before equity issuance/distributions | -420.488 | -202.135 | -166.693 | -172.648 | -178.687 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +1.137e-13 | +0.000e+00 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 841.683 | PASS |
| 2027 | +2.274e-13 | -2.842e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 639.548 | PASS |
| 2028 | +2.274e-13 | +5.684e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 472.855 | PASS |
| 2029 | +2.842e-13 | +5.684e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 300.207 | PASS |
| 2030 | +2.842e-13 | +0.000e+00 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 121.520 | PASS |

#### Revenue growth — Base

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -182.178 | -182.178 | -182.102 | -181.505 | -181.505 |
| Investment income | 27.987 | 22.638 | 17.233 | 12.294 | 7.208 |
| Pretax income | -154.191 | -159.540 | -164.869 | -169.211 | -174.297 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 959.018 | 799.136 | 633.925 | 464.372 | 289.733 |
| Liabilities plus equity | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -0.000 | -0.000 | -0.000 | -0.000 | -0.000 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -420.165 | -200.639 | -164.106 | -169.045 | -174.131 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 30.081 | -201.147 | -164.614 | -169.553 | -174.639 |
| Opening cash | 836.417 | 866.498 | 665.351 | 500.737 | 331.184 |
| Closing cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| FCFE before equity issuance/distributions | -420.673 | -201.147 | -164.614 | -169.553 | -174.639 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +0.000e+00 | -5.684e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 841.498 | PASS |
| 2027 | +0.000e+00 | -2.842e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 640.351 | PASS |
| 2028 | +0.000e+00 | +2.842e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 475.737 | PASS |
| 2029 | +5.684e-14 | +2.842e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 306.184 | PASS |
| 2030 | +5.684e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 131.545 | PASS |

#### Revenue growth — Higher

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 34.627 | 38.090 | 41.899 | 46.088 | 50.697 |
| Cost of sales | 22.053 | 24.258 | 26.684 | 29.352 | 32.288 |
| Gross profit | 12.574 | 13.832 | 15.215 | 16.736 | 18.410 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -181.035 | -179.777 | -178.318 | -176.200 | -174.526 |
| Investment income | 27.984 | 22.647 | 17.289 | 12.438 | 7.484 |
| Pretax income | -153.051 | -157.131 | -161.030 | -163.762 | -167.042 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -153.393 | -157.473 | -161.372 | -164.104 | -167.384 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.313 | 666.117 | 503.738 | 337.870 | 168.545 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 9.216 | 10.137 | 11.151 | 12.266 | 13.493 |
| Prepaid expenses | 5.365 | 5.901 | 6.491 | 7.140 | 7.854 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 999.235 | 841.763 | 680.391 | 516.286 | 348.902 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 960.158 | 802.686 | 641.314 | 477.209 | 309.825 |
| Liabilities plus equity | 999.235 | 841.763 | 680.391 | 516.286 | 348.902 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -153.393 | -157.473 | -161.372 | -164.104 | -167.384 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -1.325 | -1.458 | -1.604 | -1.764 | -1.941 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -420.350 | -199.688 | -161.871 | -165.361 | -168.817 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 29.896 | -200.196 | -162.379 | -165.869 | -169.325 |
| Opening cash | 836.417 | 866.313 | 666.117 | 503.738 | 337.870 |
| Closing cash | 866.313 | 666.117 | 503.738 | 337.870 | 168.545 |
| FCFE before equity issuance/distributions | -420.858 | -200.196 | -162.379 | -165.869 | -169.325 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +1.137e-13 | -5.684e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 841.313 | PASS |
| 2027 | +0.000e+00 | -2.842e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 641.117 | PASS |
| 2028 | +0.000e+00 | +2.842e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 478.738 | PASS |
| 2029 | +5.684e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 312.870 | PASS |
| 2030 | +5.684e-14 | +0.000e+00 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 143.545 | PASS |

#### Operating-cost growth — Lower

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 188.579 | 184.808 | 181.112 | 177.489 | 173.940 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -178.329 | -174.558 | -170.786 | -166.566 | -163.017 |
| Investment income | 28.045 | 22.870 | 17.755 | 13.226 | 8.669 |
| Pretax income | -150.285 | -151.688 | -153.030 | -153.340 | -154.348 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -150.627 | -152.030 | -153.372 | -153.682 | -154.690 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 870.404 | 677.109 | 524.334 | 370.652 | 215.962 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 1002.001 | 849.971 | 696.599 | 542.917 | 388.227 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 962.924 | 810.894 | 657.522 | 503.840 | 349.150 |
| Liabilities plus equity | 1002.001 | 849.971 | 696.599 | 542.917 | 388.227 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -150.627 | -152.030 | -153.372 | -153.682 | -154.690 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -0.000 | -0.000 | -0.000 | -0.000 | -0.000 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -416.259 | -192.787 | -152.267 | -153.174 | -154.182 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 33.987 | -193.295 | -152.775 | -153.682 | -154.690 |
| Opening cash | 836.417 | 870.404 | 677.109 | 524.334 | 370.652 |
| Closing cash | 870.404 | 677.109 | 524.334 | 370.652 | 215.962 |
| FCFE before equity issuance/distributions | -416.767 | -193.295 | -152.775 | -153.682 | -154.690 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +1.137e-13 | -5.684e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 845.404 | PASS |
| 2027 | +1.137e-13 | -2.842e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 652.109 | PASS |
| 2028 | +0.000e+00 | -5.684e-14 | +5.684e-14 | +0.000e+00 | +0.000e+00 | 499.334 | PASS |
| 2029 | +1.137e-13 | +2.842e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 345.652 | PASS |
| 2030 | +5.684e-14 | +0.000e+00 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 190.962 | PASS |

#### Operating-cost growth — Base

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -182.178 | -182.178 | -182.102 | -181.505 | -181.505 |
| Investment income | 27.987 | 22.638 | 17.233 | 12.294 | 7.208 |
| Pretax income | -154.191 | -159.540 | -164.869 | -169.211 | -174.297 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 959.018 | 799.136 | 633.925 | 464.372 | 289.733 |
| Liabilities plus equity | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -0.000 | -0.000 | -0.000 | -0.000 | -0.000 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -420.165 | -200.639 | -164.106 | -169.045 | -174.131 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 30.081 | -201.147 | -164.614 | -169.553 | -174.639 |
| Opening cash | 836.417 | 866.498 | 665.351 | 500.737 | 331.184 |
| Closing cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| FCFE before equity issuance/distributions | -420.673 | -201.147 | -164.614 | -169.553 | -174.639 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +0.000e+00 | -5.684e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 841.498 | PASS |
| 2027 | +0.000e+00 | -2.842e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 640.351 | PASS |
| 2028 | +0.000e+00 | +2.842e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 475.737 | PASS |
| 2029 | +5.684e-14 | +2.842e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 306.184 | PASS |
| 2030 | +5.684e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 131.545 | PASS |

#### Operating-cost growth — Higher

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 196.277 | 200.202 | 204.206 | 208.290 | 212.456 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -186.027 | -189.952 | -193.880 | -197.367 | -201.533 |
| Investment income | 27.929 | 22.404 | 16.699 | 11.330 | 5.676 |
| Pretax income | -158.097 | -167.548 | -177.181 | -186.038 | -195.857 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -158.439 | -167.890 | -177.523 | -186.380 | -196.199 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 862.592 | 653.437 | 476.511 | 290.131 | 93.932 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 994.189 | 826.299 | 648.776 | 462.396 | 266.197 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 955.112 | 787.222 | 609.699 | 423.319 | 227.120 |
| Liabilities plus equity | 994.189 | 826.299 | 648.776 | 462.396 | 266.197 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -158.439 | -167.890 | -177.523 | -186.380 | -196.199 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -0.000 | -0.000 | -0.000 | -0.000 | -0.000 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -424.071 | -208.647 | -176.418 | -185.872 | -195.691 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 26.175 | -209.155 | -176.926 | -186.380 | -196.199 |
| Opening cash | 836.417 | 862.592 | 653.437 | 476.511 | 290.131 |
| Closing cash | 862.592 | 653.437 | 476.511 | 290.131 | 93.932 |
| FCFE before equity issuance/distributions | -424.579 | -209.155 | -176.926 | -186.380 | -196.199 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +1.137e-13 | -5.684e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 837.592 | PASS |
| 2027 | +1.137e-13 | -2.842e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 628.437 | PASS |
| 2028 | +2.274e-13 | +5.684e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 451.511 | PASS |
| 2029 | +1.705e-13 | +2.842e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 265.131 | PASS |
| 2030 | +1.990e-13 | +2.842e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 68.932 | PASS |

#### Restored base

**Income statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -182.178 | -182.178 | -182.102 | -181.505 | -181.505 |
| Investment income | 27.987 | 22.638 | 17.233 | 12.294 | 7.208 |
| Pretax income | -154.191 | -159.540 | -164.869 | -169.211 | -174.297 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |

**Balance sheet (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 959.018 | 799.136 | 633.925 | 464.372 | 289.733 |
| Liabilities plus equity | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

**Cash flow statement (USD millions)**

| Item | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | -0.000 | -0.000 | -0.000 | -0.000 | -0.000 |
| Long-lead material purchases | -6.929 | -41.938 | -0.000 | -0.000 | -0.000 |
| ENTRA1 payable settlement | -259.884 | -0.000 | -0.000 | -0.000 | -0.000 |
| Operating cash flow | -420.165 | -200.639 | -164.106 | -169.045 | -174.131 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 30.081 | -201.147 | -164.614 | -169.553 | -174.639 |
| Opening cash | 836.417 | 866.498 | 665.351 | 500.737 | 331.184 |
| Closing cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| FCFE before equity issuance/distributions | -420.673 | -201.147 | -164.614 | -169.553 | -174.639 |

Opening balance gap: +0.000e+00 USD M.

| Year | Balance gap | Cash gap | Equity gap | ENTRA1 gap | FCFE gap | Cash above minimum | Check |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026 | +0.000e+00 | -5.684e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 841.498 | PASS |
| 2027 | +0.000e+00 | -2.842e-14 | -5.684e-14 | +0.000e+00 | +0.000e+00 | 640.351 | PASS |
| 2028 | +0.000e+00 | +2.842e-14 | +2.842e-14 | +0.000e+00 | +0.000e+00 | 475.737 | PASS |
| 2029 | +5.684e-14 | +2.842e-14 | -2.842e-14 | +0.000e+00 | +0.000e+00 | 306.184 | PASS |
| 2030 | +5.684e-14 | +0.000e+00 | +0.000e+00 | +0.000e+00 | +0.000e+00 | 131.545 | PASS |

### Student interpretation

Reserved for the student’s predicted input → statement → output link and partner discussion.

## Saved base inputs

```json
{
  "assumptions": {
    "revenue_growth": 0.0,
    "opex_growth": 0.0,
    "cash_yield": 0.03,
    "discount_rate": 0.15,
    "capex": 0.508,
    "minimum_cash": 25.0,
    "closure_cost": 50.0,
    "receivable_recovery": 0.8,
    "llm_recovery": 0.0,
    "restricted_cash_recovery": 0.0,
    "extra_terminal_claims": 0.0
  },
  "opening_balance_sheet": {
    "cash": 836.417,
    "investments": 450.754,
    "receivables": 8.378,
    "prepaid": 4.877,
    "ppe": 1.924,
    "intangibles": 0.527,
    "llm": 63.767,
    "other_assets": 45.868,
    "ordinary_liabilities": 39.077,
    "pma_liability": 259.884,
    "equity": 1113.551
  },
  "constants": {
    "BASE_REVENUE": 31.479,
    "BASE_MARGIN": 0.36313097620635976,
    "NORMALIZED_OPEX": 193.60900000000007,
    "CASH_OPEX": 192.42800000000008,
    "CLASS_A": 318.480601,
    "EXCHANGEABLE_UNITS": 19.413185,
    "RSUS": 4.184488,
    "OPTIONS": 4.686454,
    "SHARES": 346.764728,
    "LLM_PURCHASES": [
      6.929,
      41.938,
      0.0,
      0.0,
      0.0
    ],
    "TOL": 1e-07
  },
  "historical_inputs": {
    "2023": {
      "revenue": 22.81,
      "prior_revenue": 11.804,
      "cogs": 18.961,
      "gross_profit": 3.849,
      "ga": 65.404,
      "net_income": -180.115,
      "llm": 36.361,
      "ppe": 4.116,
      "equity": 129.338,
      "parent_equity": 93.457,
      "depreciation": 2.38,
      "capex": 1.725,
      "provider_capex": -1.73,
      "pretax": -180.115,
      "tax": 0.0,
      "cfo": -183.254,
      "net_borrowing": 0.0
    },
    "2024": {
      "revenue": 37.045,
      "prior_revenue": 22.81,
      "cogs": 4.937,
      "gross_profit": 32.108,
      "ga": 75.901,
      "net_income": -348.387,
      "llm": 43.388,
      "ppe": 2.421,
      "equity": 453.12,
      "parent_equity": 618.695,
      "depreciation": 1.665,
      "capex": 0.044,
      "provider_capex": -0.04,
      "pretax": -346.452,
      "tax": 1.935,
      "cfo": -108.666,
      "net_borrowing": 0.0
    },
    "2025": {
      "revenue": 31.479,
      "prior_revenue": 37.045,
      "cogs": 20.048,
      "gross_profit": 11.431,
      "ga": 609.825,
      "net_income": -664.462,
      "llm": 63.767,
      "ppe": 1.924,
      "equity": 1113.551,
      "parent_equity": 1168.841,
      "depreciation": 1.004,
      "capex": 0.508,
      "provider_capex": -0.51,
      "pretax": -664.12,
      "tax": 0.342,
      "cfo": -459.61,
      "net_borrowing": 0.0
    }
  }
}
```

## Full saved model output

# Lab 10 — Part 1: SMR history and ratios

Fiscal years ended December 31; USD millions unless indicated. Every historical cell identifies its source filing and statement. Retrieval/check date: September 24, 2026.

## Three-year history grid

| Item | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Revenue | 22.810 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 37.045 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 31.479 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Gross profit (filing calls dollar amount gross margin) | 3.849 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 32.108 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 11.431 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| SG&A proxy: reported G&A | 65.404 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 75.901 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 609.825 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Net income / (loss), consolidated | -180.115 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | -348.387 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | -664.462 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Inventory proxy: long-lead material WIP | 36.361 ([2023 10-K: balance sheet](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 43.388 ([2024 10-K: balance sheet](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 63.767 ([2025 10-K: balance sheet](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| PP&E, net at year-end | 4.116 ([2023 10-K: balance sheet](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 2.421 ([2024 10-K: balance sheet](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 1.924 ([2025 10-K: balance sheet](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Shareholders' equity, including NCI | 129.338 ([2023 10-K: balance sheet](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 453.120 ([2024 10-K: balance sheet](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 1,113.551 ([2025 10-K: balance sheet](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Shareholders' equity, excluding NCI | 93.457 ([2023 10-K: balance sheet](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 618.695 ([2024 10-K: balance sheet](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 1,168.841 ([2025 10-K: balance sheet](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |

G&A is a verified reported line used as the SG&A proxy; an exact separate standardized SG&A total is **unresolved/not separately reported**. Do not add all R&D and other costs to G&A and call that reported SG&A. The inventory proxy is long-lead materials, not ordinary merchandise inventory. A separate conventional inventory total is **unresolved/not separately reported**. Consolidated net loss and equity are used consistently with the consolidated forecast; parent equity is shown separately to avoid confusing the ownership bases.

## Two direct filing checks — performed by Codex

1. Opened the 2025 10-K, statement of operations F-5: 31,479 revenue - 20,048 cost of sales = 11,431 gross profit, in thousands; conversion gives **11.431 million**, matching the grid. [Filing](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm).
2. Opened the 2023 10-K, Note 8 PP&E: 24,861 gross cost - 20,745 accumulated depreciation + zero assets under development = 4,116, in thousands; **4.116 million** also matches the balance sheet F-3. [Filing](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html).

These are AI-performed source checks, not an assertion that the student personally opened the filings. If personal verification is required, the student should repeat them.

## Ratio inputs

| Input | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Cost of sales | 18.961 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 4.937 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 20.048 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Prior-year revenue for growth | 11.804 ([2023 10-K: operations, prior-year column](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 22.810 ([2024 10-K: operations, prior-year column](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 37.045 ([2025 10-K: operations, prior-year column](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Depreciation only | 2.380 ([2023 10-K: cash flows](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 1.665 ([2024 10-K: cash flows](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 1.004 ([2025 10-K: cash flows](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Pretax income / (loss) | -180.115 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | -346.452 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | -664.120 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Income-tax expense | 0.000 ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 1.935 ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 0.342 ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Operating cash flow | -183.254 ([2023 10-K: cash flows](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | -108.666 ([2024 10-K: cash flows](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | -459.610 ([2025 10-K: cash flows](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Net debt borrowing | 0.000 ([2023 10-K: cash flows; liquidity](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 0.000 ([2024 10-K: cash flows; liquidity](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 0.000 ([2025 10-K: cash flows; liquidity](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |

## Three-year ratio table

All ratios below are calculations from the cited inputs, not quoted management metrics. Year-end balances are used for inventory and net PP&E, matching the saved ABG exercise convention. The video itself was not supplied; its exact conventions remain unresolved.

| Ratio / formula | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Gross margin = gross profit / revenue | 16.87% ([2023 10-K: derived from inputs above](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 86.67% ([2024 10-K: derived from inputs above](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 36.31% ([2025 10-K: derived from inputs above](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| SG&A / gross profit, using reported G&A proxy | 1699.25% ([2023 10-K: derived from inputs above](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 236.39% ([2024 10-K: derived from inputs above](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 5334.84% ([2025 10-K: derived from inputs above](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Inventory days proxy = year-end LLM / cost of sales × 365 | 699.95 ([2023 10-K: derived from inputs above](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 3207.74 ([2024 10-K: derived from inputs above](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 1160.96 ([2025 10-K: derived from inputs above](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Depreciation / year-end net PP&E | 57.82% ([2023 10-K: derived from inputs above](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 68.77% ([2024 10-K: derived from inputs above](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | 52.18% ([2025 10-K: derived from inputs above](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Effective tax arithmetic = expense / pretax result | 0.0000% ([2023 10-K: derived from inputs above](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | -0.5585% ([2024 10-K: derived from inputs above](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | -0.0515% ([2025 10-K: derived from inputs above](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |
| Reported revenue growth = revenue / prior revenue - 1 | 93.24% ([2023 10-K: derived from inputs above](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | 62.41% ([2024 10-K: derived from inputs above](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | -15.02% ([2025 10-K: derived from inputs above](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |

The LLM-days calculation combines manufacturing materials with service/licensing cost of sales: it is a mechanical proxy, **not a defensible inventory-turnover forecast driver**. High depreciation/net-PP&E ratios reflect a small depreciated asset base, not a useful-life estimate. Negative effective-tax arithmetic reflects tax expense despite pretax losses; normalized profitable tax rates remain unresolved. The forecast's 25% is judgment, not this historical ratio.

## Capital spending: filing beside provider

Provider chosen because none was specified: Stock Analysis annual Capital Expenditures field (page credits S&P Global Market Intelligence). Use FY columns, not TTM.

| Year | Filing PP&E purchases, positive spending | Provider field, cash-flow sign | Reconciliation |
|---|---:|---:|---|
| 2023 | 1.725 ([2023 10-K: cash flows: PP&E purchases](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | [-1.73](https://stockanalysis.com/stocks/smr/financials/cash-flow-statement/) | Matches negative filing outflow rounded to 2 decimals |
| 2024 | 0.044 ([2024 10-K: cash flows: PP&E purchases](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | [-0.04](https://stockanalysis.com/stocks/smr/financials/cash-flow-statement/) | Matches negative filing outflow rounded to 2 decimals |
| 2025 | 0.508 ([2025 10-K: cash flows: PP&E purchases](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) | [-0.51](https://stockanalysis.com/stocks/smr/financials/cash-flow-statement/) | Matches negative filing outflow rounded to 2 decimals |

This is PP&E capex only. Long-lead material cash purchases are tracked separately in operating cash flow; purchases of financial investments are not capex. Do not substitute the provider's differently defined Levered Free Cash Flow field.

## Reported growth beside MD&A organic / same-store disclosure

| Year | Reported growth | Organic / same-store growth | MD&A explanation |
|---|---:|---|---|
| 2023 | 93.24% ([2023 10-K: operations](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | Not disclosed; same-store not applicable ([2023 10-K: Item 7 MD&A](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | CFPP engineering/development work and consulting increased revenue. ([2023 10-K: Item 7 revenue discussion](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) |
| 2024 | 62.41% ([2024 10-K: operations](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | Not disclosed; same-store not applicable ([2024 10-K: Item 7 MD&A](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | Romanian project engineering and licensing increased revenue. ([2024 10-K: Item 7 revenue discussion](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) |
| 2025 | -15.02% ([2025 10-K: operations](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) | Not disclosed; same-store not applicable ([2025 10-K: Item 7 MD&A](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) | Lower license revenue outweighed increased FEED engineering services. ([2025 10-K: Item 7 revenue discussion](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) |

No separately quantified organic rate was found in the three MD&A revenue discussions or searches for organic/same-store. Organic rate: **unresolved/not disclosed**, not zero and not automatically equal to total growth. NuScale is not a chain of stores.

## Historical FCFE

FCFE = operating cash flow - PP&E purchases + net debt borrowing. This is consolidated pre-distribution FCFE, not a Class A ownership allocation; stock issuance and sales of investment securities are excluded.

| Year | FCFE, USD millions | Status |
|---|---:|---|
| 2023 | -184.979 ([2023 10-K: cash flows, derived](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html)) | negative FCFE |
| 2024 | -108.710 ([2024 10-K: cash flows, derived](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html)) | negative FCFE |
| 2025 | -460.118 ([2025 10-K: cash flows, derived](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)) | negative FCFE |

## Unresolved items

Separate standardized SG&A and conventional inventory totals; a quantified organic growth rate; the video's precise ratio conventions; project economics sufficient for a going-concern terminal value; and unquantified terminal legal/contract/tax claims. Disclosed proxies and analyst judgments are explicitly identified rather than presented as confirmed answers.


# SMR — labelled assumptions for Lab 10

**Question:** What are five years of your company's statements worth, built from assumptions you can defend, and how do you know the statements are right?

**Company-specific line:** NuScale's valuation depends on whether commercialization produces profitable reactor projects before spending and dilution consume the value available to each share.

This application produces five linked annual statements and one **conditional downside value**. It is a services-only scenario followed by wind-down at December 31, 2030. Wind-down is an analyst modelling choice, not an announced company plan. It is neither a market price target nor a lower bound on value. Successful commercialization could be worth much more; higher spending, claims, or worse recoveries could leave less.

The balance-sheet measurement date is December 31, 2025, with information from the report published February 26, 2026. This is a retrospective annual-report exercise, not an estimate using only information public on December 31, and not a September 2026 valuation. Later quarterly reports are outside this case.

## Filing anchors

- [2025 Form 10-K — SEC](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm): F-4 opening balance sheet; F-5 operating costs; F-8 depreciation and cash flow; Note 9 ENTRA1; Note 14 awards; Note 15 tax agreement; Note 17 commitments.
- [2024 Form 10-K — company annual-report archive](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html): statements of operations and cash flows.
- [2023 Form 10-K — company annual-report archive](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html): statements of operations and cash flows.

The sourced Part 1 grid above supplies the historical inputs. Revenue and margins are volatile; repeating them in a forecast requires judgment.

## Forecast assumptions

Each row has an explicit **history**, **guidance**, or **judgment** label. Ratios repeated in future years are judgments even when their starting values come from history. Figures and formulas are editable in `lab10_smr_proforma.py`; numerical settings are centralized in `Assumptions` or named constants.

| Value | Label (history, guidance, judgment) | Reason |
|---|---|---|
| Opening 2025 balance-sheet amounts in OPENING; USD millions | history | Transcribed from the [2025 10-K balance sheet](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm); grouped consistently for the consolidated model. |
| Services revenue: 31.479 each year; 0% growth | judgment | Hold the latest annual scale without presuming new module sales. This still assumes replacement service work is won; it is not contracted backlog. Sensitivity: -10% / +10% annual growth. |
| Gross margin: 11.431 / 31.479 = 36.31% | judgment | History-derived ratio, forecast judgment to repeat it. Does not extrapolate the unusually high 2024 margin. |
| Recurring operating expense anchor: 45.532 + (609.825 - 507.393) + 45.645 = 193.609 | history | Arithmetic using reported expense lines and the disclosed ENTRA1 charge. Treating the remaining amount as a recurring forecast base is a separate judgment in the cash-cost row. |
| Cash operating costs: 193.609 - 1.004 - 0.177 = 192.428 annually | judgment | Subtract historical D&A and model it separately. Hold costs flat, implying active cost control despite inflation; test 2% inflation. |
| Compensation: Cash equivalent for future compensation; no future SBC addback | judgment | Historical stock compensation remains in the expense anchor and is treated as future cash pay. This avoids treating employee awards as free funding. Existing awards are included separately in the share allowance. Simplified economic statements, not a GAAP SBC vesting forecast. |
| ENTRA1 cash settlement: 259.884 in 2026 | history | The 2025 10-K, Note 9, confirms the opening payable was paid in January 2026; settle it without expensing the same charge twice. |
| New ENTRA1 milestones: Zero | judgment | Conditional on no additional triggering projects. Must be replaced alongside any commercialization revenue scenario; not an assumption that successful module sales incur no milestone cost. |
| Long-lead materials: Add 6.929 in 2026 and 41.938 in 2027 | judgment | The purchase schedule is reported history; I assume no discretionary additions beyond those commitments and no materials sales in this case. |
| Other purchase/service/marketing commitments: Included within recurring cash operating costs | judgment | Avoid adding ordinary contract spending twice. Assumes the retained expense budget covers those obligations; amounts capitalized to materials and opening ENTRA1 settlement are separate. |
| Receivables/prepaids: Opening balance / opening revenue ratios | judgment | Constant balances in the flat-revenue case; changes consume/release operating cash in sensitivities. All receivables treated as an operating proxy, including the small investment-related portion. |
| Ordinary liabilities: Hold 39.077 constant | judgment | Model ongoing replacement of paid obligations, with no incremental supplier financing. Includes all opening liabilities other than the separately settled ENTRA1 payable. Settle this balance at wind-down. |
| Capex: 0.508 annually | judgment | History-informed maintenance assumption; a module production case would need different reinvestment. |
| Depreciation / amortization: 1.004 / 0.177, each capped at the opening asset balance | judgment | Simple run-off convention; new capex starts depreciation in the following year. Prevents negative assets. |
| Other assets: Hold at 45.868 | judgment | Includes restricted cash, IPR&D, goodwill and other assets; no optimistic fair-value uplift. Terminal recoveries are specified separately. |
| Investments: Sell 450.754 at carrying value in 2026 | judgment | Assumed liquidity at par, not a forecast of realized market prices. Separate investing cash flow; not revenue or an operating cash inflow. |
| Investment return: 3% on estimated average available liquidity | judgment | Judgment, not a sourced September 2026 yield. Known January ENTRA1 payment reduces the interest base before accrual. |
| Cash tax: 0.342 foreign allowance plus 25% of positive pretax income | judgment | Losses generate no refund or deferred-tax asset. All default forecast years lose money. No claimed value for NOLs. |
| Financing/distributions: Zero debt, new capital, buybacks and dividends | judgment | Feasibility condition, not guaranteed funding availability. Minimum cash is 25; script refuses a scenario that breaches it instead of silently inserting financing. |
| Discount rate: 15%; test 10% / 20% | judgment | Required equity return chosen for a risky conditional outcome; not a measured CAPM/WACC estimate. No claim that discounting alone prices commercialization probabilities. |
| Terminal treatment: Wind-down after 2030; zero going-concern value | judgment | Avoid capitalizing negative cash flows forever. This assumption defines the case and is its largest limitation. |
| Recoveries: Cash 100%; receivables 80%; everything else 0% | judgment | No assumed proceeds from materials, IP, prepaid costs, PP&E or restricted cash. Recovery percentages are judgments, not appraisals. |
| Closure costs: Additional 50 | judgment | Covers incremental closure burden beyond recorded liabilities; unverified planning allowance. Test 100. |
| Additional terminal claims: Zero by default; test 100 | judgment | Contingent legal, contract and tax-agreement termination claims are not fully quantified. A zero setting is a scenario condition, not a finding that no claims exist. |
| Dealer floor-plan borrowing: none; SMR replacement line is the ENTRA1 payable (259.884 at opening, paid in 2026) | history | The filings do not identify dealer floor-plan financing. I track the commercialization payment separately because it is the company-specific cash obligation. |

No forecast input is labelled guidance: no management five-year guidance has been verified. A contractual commitment is a historical disclosure, not an earnings forecast. Forecast reasons above are AI-authored analytical explanations, not a claim of student-authored judgment.

## Partner challenge and response

**Status: AI-assisted preparation only; the actual partner exchange has not been supplied.**

**Practice attack on my judgment — flat cash operating costs of 192.428 million:** “Why hold annual cash operating costs at 192.428 million for five years when inflation and commercialization work could increase them, and what evidence would make you change that number?”

**My proposed answer (two sentences):** I use 192.428 million because it starts with 2025 reported operating expenses, removes the identified ENTRA1 charge and separately modelled depreciation/amortization, and holds the remaining spending flat as an explicit cost-control assumption rather than management guidance. I would replace that flat path if comparable recurring expenses in later filings or a disclosed staffing/commercialization budget show a different run rate; allowing 2% annual cost growth already reduces this scenario's value from about $0.1063 to $0.0166 per share.

**Additional specific criticism you can use — 2030 wind-down judgment:** “Why does the end of your five-year forecast also become the end of NuScale's business, and what evidence supports assigning zero value to its technology after 2030 rather than extending the forecast until commercialization or a supported shutdown date?”

**Proposed two-sentence response:** I chose a 2030 wind-down to define a limited downside scenario, not because the filings say NuScale will close then, so the $0.11 result cannot stand alone as the company's fair value. I would replace that endpoint with a longer operating forecast if binding contracts and credible project economics support continued operation, including the associated milestone payments, funding needs and dilution.

**Actual partner attack:** [Unresolved — paste the partner's exact question and identify the judgment/value challenged.]

**Answer delivered to the partner:** [Unresolved — confirm the two-sentence answer above was used, or record the actual two-sentence response.]

**My attack on their model:** [Unresolved — identify their company, judgment-labelled assumption and value before recording the actual question.]

**Draft attack to adapt, not a recorded exchange:** “What filing evidence supports your [assumption/value] rather than [specific historical benchmark], and if it moves to that benchmark, does your model still meet its cash floor without extra borrowing or share issuance?”

**Their actual answer:** [Unresolved — record their explanation and the evidence that would change their number.]

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
python lab10_smr_proforma.py --write-report
python lab10_smr_proforma.py
python proforma.py
```

`Lab10_SMR_Proforma_Results.md` is generated from the same calculations as terminal output. It includes the income statement, balance sheet, cash flow statement, valuation bridge and sensitivities. `proforma.py` remains the ABG reference.

Suggested checkout wording: “I valued a services-only SMR downside case using five linked statements and discounted residual shareholder proceeds. My assumptions are labelled, all statements reconcile, and I explicitly settle the opening ENTRA1 payable. My result excludes successful reactor commercialization, so it is a conditional scenario value rather than my final fair-value estimate for SMR.”

## SMR opening balance sheet — December 31, 2025

Replacement instruction: "Replace the ABG opening balance sheet and assumptions with these."
The three-column assumption table above and this opening balance sheet are the inputs to this new SMR file. Amounts are USD millions.

| Opening line | Value |
|---|---:|
| Cash | 836.417 |
| Investments, short and long term | 450.754 |
| Receivables | 8.378 |
| Prepaid expenses | 4.877 |
| PP&E, net | 1.924 |
| Intangibles | 0.527 |
| Long-lead material WIP | 63.767 |
| Other assets including restricted cash | 45.868 |
| Ordinary liabilities | 39.077 |
| ENTRA1 payable | 259.884 |
| Consolidated shareholders' equity including NCI | 1,113.551 |
| Total assets | 1,412.512 |
| Total liabilities | 298.961 |
| Total liabilities plus equity | 1,412.512 |

Source: [2025 10-K, balance sheet F-4](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm). Investments = 417.800 + 32.954; other assets = 5.100 restricted cash + 16.900 IPR&D + 8.255 goodwill + 15.613 other assets; ordinary liabilities = 298.961 total liabilities - 259.884 ENTRA1 payable. No dealer floor-plan debt.

# SMR — Lab 10 five-year statements and conditional valuation

**Case: services-only through 2030, followed by wind-down.** This is a downside scenario, not a probability-weighted fair value or current price target.

Measurement date: December 31, 2025; information basis: 2025 annual report published February 26, 2026. Retrospective classroom exercise; no 2026 interim update.

USD millions except per-share values; shares in millions. Full assumptions, filing sources, and limitations are included below.

**Conditional value per share: $0.1063 ($0.11 rounded).** Present equity value: $36.876 million.

## Income statement

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 31.479 | 31.479 | 31.479 | 31.479 | 31.479 |
| Cost of sales | 20.048 | 20.048 | 20.048 | 20.048 | 20.048 |
| Gross profit | 11.431 | 11.431 | 11.431 | 11.431 | 11.431 |
| Cash operating expenses | 192.428 | 192.428 | 192.428 | 192.428 | 192.428 |
| Depreciation | 1.004 | 1.004 | 0.932 | 0.508 | 0.508 |
| Amortization | 0.177 | 0.177 | 0.173 | 0.000 | 0.000 |
| Operating income | -182.178 | -182.178 | -182.102 | -181.505 | -181.505 |
| Investment income | 27.987 | 22.638 | 17.233 | 12.294 | 7.208 |
| Pretax income | -154.191 | -159.540 | -164.869 | -169.211 | -174.297 |
| Tax | 0.342 | 0.342 | 0.342 | 0.342 | 0.342 |
| Consolidated net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |

## Balance sheet

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| Investments | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Receivables | 8.378 | 8.378 | 8.378 | 8.378 | 8.378 |
| Prepaid expenses | 4.877 | 4.877 | 4.877 | 4.877 | 4.877 |
| PP&E | 1.428 | 0.932 | 0.508 | 0.508 | 0.508 |
| Intangibles | 0.350 | 0.173 | 0.000 | 0.000 | 0.000 |
| Long-lead materials | 70.696 | 112.634 | 112.634 | 112.634 | 112.634 |
| Other assets incl. restricted cash | 45.868 | 45.868 | 45.868 | 45.868 | 45.868 |
| Total assets | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Ordinary liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| ENTRA1 payable | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Total liabilities | 39.077 | 39.077 | 39.077 | 39.077 | 39.077 |
| Consolidated equity incl. NCI | 959.018 | 799.136 | 633.925 | 464.372 | 289.733 |
| Liabilities plus equity | 998.095 | 838.213 | 673.002 | 503.449 | 328.810 |
| Balance gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Cash flow statement

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Net income | -154.533 | -159.882 | -165.211 | -169.553 | -174.639 |
| Add D&A | 1.181 | 1.181 | 1.105 | 0.508 | 0.508 |
| Receivables/prepaids movement | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Long-lead material purchases | -6.929 | -41.938 | 0.000 | 0.000 | 0.000 |
| ENTRA1 payable settlement | -259.884 | 0.000 | 0.000 | 0.000 | 0.000 |
| Operating cash flow | -420.165 | -200.639 | -164.106 | -169.045 | -174.131 |
| Capital expenditure | -0.508 | -0.508 | -0.508 | -0.508 | -0.508 |
| Investment liquidation | 450.754 | 0.000 | 0.000 | 0.000 | 0.000 |
| Investing cash flow | 450.246 | -0.508 | -0.508 | -0.508 | -0.508 |
| Financing cash flow | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Net change in cash | 30.081 | -201.147 | -164.614 | -169.553 | -174.639 |
| Opening cash | 836.417 | 866.498 | 665.351 | 500.737 | 331.184 |
| Closing cash | 866.498 | 665.351 | 500.737 | 331.184 | 156.545 |
| FCFE before equity issuance/distributions | -420.673 | -201.147 | -164.614 | -169.553 | -174.639 |

## Forecast FCFE and positive value

FCFE = operating cash flow - capital spending + net debt borrowing (zero here). Investment liquidation is excluded from FCFE; it converts existing assets into cash.

| Year | FCFE, USD millions | Status |
|---|---:|---|
| 2026 | -420.673 | negative FCFE |
| 2027 | -201.147 | negative FCFE |
| 2028 | -164.614 | negative FCFE |
| 2029 | -169.553 | negative FCFE |
| 2030 | -174.639 | negative FCFE |

PV of positive forecast FCFE only: 0.000 million (a diagnostic, not an additional distribution in this retained-cash case). Negative FCFE remains in every cash forecast and consumes liquidity; it is not deleted to inflate equity value. Only the positive residual shareholder distribution is valued here.

A terminal perpetuity on negative cash flow can produce arithmetic, but not a meaningful going-concern equity valuation, because it assumes losses persist forever instead of establishing a sustainable distributable cash flow.

## Valuation bridge

- 2030 cash: 156.545.
- Recoverable noncash assets: 6.702.
- Settle remaining liabilities: (39.077).
- Additional wind-down cost: (50.000).
- Terminal shareholder distribution: 74.171.
- Discount five years at 15%: present equity value 36.876.
- Divide by 346.764728 million economic shares/awards: $0.1063.

All shareholder proceeds occur at the end of 2030. Operating losses already reduce terminal cash: do not subtract their PV again or add opening cash again. The forecast statements are before liquidation; the bridge settles assets and claims separately.

## Checks

PASS: opening and all five forecast balance sheets; cash and equity roll-forwards; ENTRA1 payable settlement; nonnegative depreciable assets; minimum cash. Equity rolls forward from net income, never as a balancing plug.

## Sensitivity — same services-only/wind-down framework

| Change | Value/share |
|---|---:|
| Default | $0.1063 |
| 10% discount rate | $0.1328 |
| 20% discount rate | $0.0860 |
| Revenue declines 10% annually | $0.0880 |
| Revenue grows 10% annually | $0.1294 |
| Cash operating expenses grow 2% annually | $0.0166 |
| Wind-down cost 100 million | $0.0347 |
| Additional terminal claims 100 million | $0.0000 |

A low number here does not establish that SMR is overpriced. The case deliberately assigns no value to successful module commercialization. A going-concern case needs project timing, net contract economics, milestone payments, financing, dilution, and tax-receivable-agreement treatment.

## CHECK BLOCK — unrounded calculations, USD millions

Tolerance: 1e-07 million. A failure stops execution and names its year and gap.

| Year | Assets - liabilities - equity | Cash roll-forward gap | Equity roll-forward gap | Cash above minimum | Result |
|---|---:|---:|---:|---:|---|
| 2026 | 0.000000000 | 0.000000000 | 0.000000000 | 841.498 | PASS |
| 2027 | 0.000000000 | 0.000000000 | 0.000000000 | 640.351 | PASS |
| 2028 | 0.000000000 | 0.000000000 | 0.000000000 | 475.737 | PASS |
| 2029 | 0.000000000 | 0.000000000 | 0.000000000 | 306.184 | PASS |
| 2030 | 0.000000000 | 0.000000000 | 0.000000000 | 131.545 | PASS |

Conditional services-only/wind-down value per share: **$0.1063**.

## Market comparison — saved dated observation

No revolver is drawn in any year: opening cash and investment liquidation cover the forecast losses and commitments while keeping cash above the 25 million floor; this case assumes no revolving facility.

Market observation: **$8.54 per Class A share**, September 24, 2026, 1:56 p.m. EDT, market open (intraday, not closing price). [Source](https://stockanalysis.com/stocks/smr/).

Common comparison denominator: 346.764728 million economic shares/awards, the model's frozen year-end-2025 if-converted, gross-award assumption. Model equity = 36.876 million; applying the observed quote to the same denominator gives a market-price benchmark of 2961.371 million. That benchmark is not today's actual market capitalization. The quote page reports 429.72 million shares outstanding, a different date and share definition. The annual-report model has not been rolled forward for subsequent cash flows or issuance.

Using the same frozen 346.764728-million-share basis, the services-only wind-down model says $0.1063 per share and the market quote says $8.54 at September 24, 2026, 1:56 p.m. EDT; what commercialization outcomes and changes since the model's 2025 starting date could explain the gap?



## Model source snapshot

The exact source used for this run is included for reproducibility.

```python
"""SMR Lab 10: annual-report-based, conditional services-only/wind-down case.

USD millions, shares in millions. Standard library only. All assumptions and filing sources are embedded below.
This is NOT a current price target or a forecast of management's intentions.
"""

from dataclasses import dataclass, replace
from pathlib import Path
import argparse


FILINGS = {
    2023: "https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html",
    2024: "https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html",
    2025: "https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm",
}
PROVIDER = "https://stockanalysis.com/stocks/smr/financials/cash-flow-statement/"
# HISTORY: each year is transcribed from that year's own 10-K; USD millions.
# Net income and total equity include NCI. Parent-only equity is separate.
HISTORY = {
    2023: dict(revenue=22.810, prior_revenue=11.804, cogs=18.961, gross_profit=3.849,
               ga=65.404, net_income=-180.115, llm=36.361, ppe=4.116,
               equity=129.338, parent_equity=93.457, depreciation=2.380,
               capex=1.725, provider_capex=-1.73, pretax=-180.115, tax=0.0,
               cfo=-183.254, net_borrowing=0.0),
    2024: dict(revenue=37.045, prior_revenue=22.810, cogs=4.937, gross_profit=32.108,
               ga=75.901, net_income=-348.387, llm=43.388, ppe=2.421,
               equity=453.120, parent_equity=618.695, depreciation=1.665,
               capex=.044, provider_capex=-.04, pretax=-346.452, tax=1.935,
               cfo=-108.666, net_borrowing=0.0),
    2025: dict(revenue=31.479, prior_revenue=37.045, cogs=20.048, gross_profit=11.431,
               ga=609.825, net_income=-664.462, llm=63.767, ppe=1.924,
               equity=1113.551, parent_equity=1168.841, depreciation=1.004,
               capex=.508, provider_capex=-.51, pretax=-664.120, tax=.342,
               cfo=-459.610, net_borrowing=0.0),
}


def historical_ratios(row):
    return dict(gross_margin=row["gross_profit"] / row["revenue"],
                ga_gp=row["ga"] / row["gross_profit"],
                inventory_days=row["llm"] / row["cogs"] * 365,
                depreciation_ppe=row["depreciation"] / row["ppe"],
                tax_rate=0.0 if row["tax"] == 0 else row["tax"] / row["pretax"],
                growth=row["revenue"] / row["prior_revenue"] - 1,
                fcfe=row["cfo"] - row["capex"] + row["net_borrowing"])


def filing_cell(year, text, locator):
    return f"{text} ([{year} 10-K: {locator}]({FILINGS[year]}))"


def render_history():
    years = tuple(HISTORY)
    lines = ["# Lab 10 — Part 1: SMR history and ratios", "",
             "Fiscal years ended December 31; USD millions unless indicated. "
             "Every historical cell identifies its source filing and statement. "
             "Retrieval/check date: September 24, 2026.", "",
             "## Three-year history grid", "",
             "| Item | 2023 | 2024 | 2025 |", "|---|---:|---:|---:|"]
    fields = [("Revenue", "revenue", "operations"),
              ("Gross profit (filing calls dollar amount gross margin)", "gross_profit", "operations"),
              ("SG&A proxy: reported G&A", "ga", "operations"),
              ("Net income / (loss), consolidated", "net_income", "operations"),
              ("Inventory proxy: long-lead material WIP", "llm", "balance sheet"),
              ("PP&E, net at year-end", "ppe", "balance sheet"),
              ("Shareholders' equity, including NCI", "equity", "balance sheet"),
              ("Shareholders' equity, excluding NCI", "parent_equity", "balance sheet")]
    for label, key, locator in fields:
        lines.append(f"| {label} | " + " | ".join(
            filing_cell(y, f"{HISTORY[y][key]:,.3f}", locator) for y in years) + " |")
    lines += ["", "G&A is a verified reported line used as the SG&A proxy; an exact "
              "separate standardized SG&A total is **unresolved/not separately reported**. "
              "Do not add all R&D and other costs to G&A and call that reported SG&A. "
              "The inventory proxy is long-lead materials, not ordinary merchandise inventory. "
              "A separate conventional inventory total is **unresolved/not separately reported**. "
              "Consolidated net loss and equity are used consistently with the consolidated forecast; "
              "parent equity is shown separately to avoid confusing the ownership bases.", "",
              "## Two direct filing checks — performed by Codex", "",
              "1. Opened the 2025 10-K, statement of operations F-5: "
              "31,479 revenue - 20,048 cost of sales = 11,431 gross profit, in thousands; "
              "conversion gives **11.431 million**, matching the grid. "
              f"[Filing]({FILINGS[2025]}).",
              "2. Opened the 2023 10-K, Note 8 PP&E: 24,861 gross cost - 20,745 accumulated "
              "depreciation + zero assets under development = 4,116, in thousands; "
              "**4.116 million** also matches the balance sheet F-3. "
              f"[Filing]({FILINGS[2023]}).", "",
              "These are AI-performed source checks, not an assertion that the student personally "
              "opened the filings. If personal verification is required, the student should repeat them.", "",
              "## Ratio inputs", "",
              "| Input | 2023 | 2024 | 2025 |", "|---|---:|---:|---:|"]
    for label, key, loc in [("Cost of sales", "cogs", "operations"),
                             ("Prior-year revenue for growth", "prior_revenue", "operations, prior-year column"),
                             ("Depreciation only", "depreciation", "cash flows"),
                             ("Pretax income / (loss)", "pretax", "operations"),
                             ("Income-tax expense", "tax", "operations"),
                             ("Operating cash flow", "cfo", "cash flows"),
                             ("Net debt borrowing", "net_borrowing", "cash flows; liquidity")]:
        lines.append(f"| {label} | " + " | ".join(
            filing_cell(y, f"{HISTORY[y][key]:,.3f}", loc) for y in years) + " |")
    lines += ["", "## Three-year ratio table", "",
              "All ratios below are calculations from the cited inputs, not quoted management metrics. "
              "Year-end balances are used for inventory and net PP&E, matching the saved ABG "
              "exercise convention. The video itself was not supplied; its exact conventions remain unresolved.", "",
              "| Ratio / formula | 2023 | 2024 | 2025 |", "|---|---:|---:|---:|"]
    ratios = {y: historical_ratios(HISTORY[y]) for y in years}
    for label, key, fmt in [
        ("Gross margin = gross profit / revenue", "gross_margin", ".2%"),
        ("SG&A / gross profit, using reported G&A proxy", "ga_gp", ".2%"),
        ("Inventory days proxy = year-end LLM / cost of sales × 365", "inventory_days", ".2f"),
        ("Depreciation / year-end net PP&E", "depreciation_ppe", ".2%"),
        ("Effective tax arithmetic = expense / pretax result", "tax_rate", ".4%"),
        ("Reported revenue growth = revenue / prior revenue - 1", "growth", ".2%"),
    ]:
        lines.append(f"| {label} | " + " | ".join(
            filing_cell(y, format(ratios[y][key], fmt), "derived from inputs above")
            for y in years) + " |")
    lines += ["", "The LLM-days calculation combines manufacturing materials with service/licensing "
              "cost of sales: it is a mechanical proxy, **not a defensible inventory-turnover forecast driver**. "
              "High depreciation/net-PP&E ratios reflect a small depreciated asset base, not a useful-life estimate. "
              "Negative effective-tax arithmetic reflects tax expense despite pretax losses; normalized "
              "profitable tax rates remain unresolved. The forecast's 25% is judgment, not this historical ratio.", "",
              "## Capital spending: filing beside provider", "",
              "Provider chosen because none was specified: Stock Analysis annual Capital Expenditures field "
              "(page credits S&P Global Market Intelligence). Use FY columns, not TTM.", "",
              "| Year | Filing PP&E purchases, positive spending | Provider field, cash-flow sign | Reconciliation |",
              "|---|---:|---:|---|"]
    for y in years:
        r = HISTORY[y]
        lines.append(f"| {y} | {filing_cell(y, format(r['capex'], '.3f'), 'cash flows: PP&E purchases')} "
                     f"| [{r['provider_capex']:.2f}]({PROVIDER}) | Matches negative filing outflow rounded to 2 decimals |")
    lines += ["", "This is PP&E capex only. Long-lead material cash purchases are tracked separately "
              "in operating cash flow; purchases of financial investments are not capex. "
              "Do not substitute the provider's differently defined Levered Free Cash Flow field.", "",
              "## Reported growth beside MD&A organic / same-store disclosure", "",
              "| Year | Reported growth | Organic / same-store growth | MD&A explanation |", "|---|---:|---|---|"]
    explanations = {2023: "CFPP engineering/development work and consulting increased revenue.",
                    2024: "Romanian project engineering and licensing increased revenue.",
                    2025: "Lower license revenue outweighed increased FEED engineering services."}
    for y in years:
        lines.append(f"| {y} | {filing_cell(y, format(ratios[y]['growth'], '.2%'), 'operations')} "
                     f"| {filing_cell(y, 'Not disclosed; same-store not applicable', 'Item 7 MD&A')} "
                     f"| {filing_cell(y, explanations[y], 'Item 7 revenue discussion')} |")
    lines += ["", "No separately quantified organic rate was found in the three MD&A revenue discussions "
              "or searches for organic/same-store. Organic rate: **unresolved/not disclosed**, not zero "
              "and not automatically equal to total growth. NuScale is not a chain of stores.", "",
              "## Historical FCFE", "",
              "FCFE = operating cash flow - PP&E purchases + net debt borrowing. "
              "This is consolidated pre-distribution FCFE, not a Class A ownership allocation; "
              "stock issuance and sales of investment securities are excluded.", "",
              "| Year | FCFE, USD millions | Status |", "|---|---:|---|"]
    for y in years:
        lines.append(f"| {y} | {filing_cell(y, format(ratios[y]['fcfe'], '.3f'), 'cash flows, derived')} "
                     f"| {'negative FCFE' if ratios[y]['fcfe'] < 0 else 'positive FCFE'} |")
    lines += ["", "## Unresolved items", "",
              "Separate standardized SG&A and conventional inventory totals; a quantified organic growth rate; "
              "the video's precise ratio conventions; project economics sufficient for a going-concern terminal "
              "value; and unquantified terminal legal/contract/tax claims. Disclosed proxies and analyst "
              "judgments are explicitly identified rather than presented as confirmed answers.", ""]
    return "\n".join(lines)


# Embedded notes keep this file self-contained.
ASSUMPTION_NOTES = """
# SMR — labelled assumptions for Lab 10

**Question:** What are five years of your company's statements worth, built from assumptions you can defend, and how do you know the statements are right?

**Company-specific line:** NuScale's valuation depends on whether commercialization produces profitable reactor projects before spending and dilution consume the value available to each share.

This application produces five linked annual statements and one **conditional downside value**. It is a services-only scenario followed by wind-down at December 31, 2030. Wind-down is an analyst modelling choice, not an announced company plan. It is neither a market price target nor a lower bound on value. Successful commercialization could be worth much more; higher spending, claims, or worse recoveries could leave less.

The balance-sheet measurement date is December 31, 2025, with information from the report published February 26, 2026. This is a retrospective annual-report exercise, not an estimate using only information public on December 31, and not a September 2026 valuation. Later quarterly reports are outside this case.

## Filing anchors

- [2025 Form 10-K — SEC](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm): F-4 opening balance sheet; F-5 operating costs; F-8 depreciation and cash flow; Note 9 ENTRA1; Note 14 awards; Note 15 tax agreement; Note 17 commitments.
- [2024 Form 10-K — company annual-report archive](https://cdn.kscope.io/62a073e6c1813708a9ebad7871d8b84c.html): statements of operations and cash flows.
- [2023 Form 10-K — company annual-report archive](https://cdn.kscope.io/f1f735ff169c43eb7a291e11a5c9f9a6.html): statements of operations and cash flows.

The sourced Part 1 grid above supplies the historical inputs. Revenue and margins are volatile; repeating them in a forecast requires judgment.

## Forecast assumptions

Each row has an explicit **history**, **guidance**, or **judgment** label. Ratios repeated in future years are judgments even when their starting values come from history. Figures and formulas are editable in `lab10_smr_proforma.py`; numerical settings are centralized in `Assumptions` or named constants.

| Value | Label (history, guidance, judgment) | Reason |
|---|---|---|
| Opening 2025 balance-sheet amounts in OPENING; USD millions | history | Transcribed from the [2025 10-K balance sheet](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm); grouped consistently for the consolidated model. |
| Services revenue: 31.479 each year; 0% growth | judgment | Hold the latest annual scale without presuming new module sales. This still assumes replacement service work is won; it is not contracted backlog. Sensitivity: -10% / +10% annual growth. |
| Gross margin: 11.431 / 31.479 = 36.31% | judgment | History-derived ratio, forecast judgment to repeat it. Does not extrapolate the unusually high 2024 margin. |
| Recurring operating expense anchor: 45.532 + (609.825 - 507.393) + 45.645 = 193.609 | history | Arithmetic using reported expense lines and the disclosed ENTRA1 charge. Treating the remaining amount as a recurring forecast base is a separate judgment in the cash-cost row. |
| Cash operating costs: 193.609 - 1.004 - 0.177 = 192.428 annually | judgment | Subtract historical D&A and model it separately. Hold costs flat, implying active cost control despite inflation; test 2% inflation. |
| Compensation: Cash equivalent for future compensation; no future SBC addback | judgment | Historical stock compensation remains in the expense anchor and is treated as future cash pay. This avoids treating employee awards as free funding. Existing awards are included separately in the share allowance. Simplified economic statements, not a GAAP SBC vesting forecast. |
| ENTRA1 cash settlement: 259.884 in 2026 | history | The 2025 10-K, Note 9, confirms the opening payable was paid in January 2026; settle it without expensing the same charge twice. |
| New ENTRA1 milestones: Zero | judgment | Conditional on no additional triggering projects. Must be replaced alongside any commercialization revenue scenario; not an assumption that successful module sales incur no milestone cost. |
| Long-lead materials: Add 6.929 in 2026 and 41.938 in 2027 | judgment | The purchase schedule is reported history; I assume no discretionary additions beyond those commitments and no materials sales in this case. |
| Other purchase/service/marketing commitments: Included within recurring cash operating costs | judgment | Avoid adding ordinary contract spending twice. Assumes the retained expense budget covers those obligations; amounts capitalized to materials and opening ENTRA1 settlement are separate. |
| Receivables/prepaids: Opening balance / opening revenue ratios | judgment | Constant balances in the flat-revenue case; changes consume/release operating cash in sensitivities. All receivables treated as an operating proxy, including the small investment-related portion. |
| Ordinary liabilities: Hold 39.077 constant | judgment | Model ongoing replacement of paid obligations, with no incremental supplier financing. Includes all opening liabilities other than the separately settled ENTRA1 payable. Settle this balance at wind-down. |
| Capex: 0.508 annually | judgment | History-informed maintenance assumption; a module production case would need different reinvestment. |
| Depreciation / amortization: 1.004 / 0.177, each capped at the opening asset balance | judgment | Simple run-off convention; new capex starts depreciation in the following year. Prevents negative assets. |
| Other assets: Hold at 45.868 | judgment | Includes restricted cash, IPR&D, goodwill and other assets; no optimistic fair-value uplift. Terminal recoveries are specified separately. |
| Investments: Sell 450.754 at carrying value in 2026 | judgment | Assumed liquidity at par, not a forecast of realized market prices. Separate investing cash flow; not revenue or an operating cash inflow. |
| Investment return: 3% on estimated average available liquidity | judgment | Judgment, not a sourced September 2026 yield. Known January ENTRA1 payment reduces the interest base before accrual. |
| Cash tax: 0.342 foreign allowance plus 25% of positive pretax income | judgment | Losses generate no refund or deferred-tax asset. All default forecast years lose money. No claimed value for NOLs. |
| Financing/distributions: Zero debt, new capital, buybacks and dividends | judgment | Feasibility condition, not guaranteed funding availability. Minimum cash is 25; script refuses a scenario that breaches it instead of silently inserting financing. |
| Discount rate: 15%; test 10% / 20% | judgment | Required equity return chosen for a risky conditional outcome; not a measured CAPM/WACC estimate. No claim that discounting alone prices commercialization probabilities. |
| Terminal treatment: Wind-down after 2030; zero going-concern value | judgment | Avoid capitalizing negative cash flows forever. This assumption defines the case and is its largest limitation. |
| Recoveries: Cash 100%; receivables 80%; everything else 0% | judgment | No assumed proceeds from materials, IP, prepaid costs, PP&E or restricted cash. Recovery percentages are judgments, not appraisals. |
| Closure costs: Additional 50 | judgment | Covers incremental closure burden beyond recorded liabilities; unverified planning allowance. Test 100. |
| Additional terminal claims: Zero by default; test 100 | judgment | Contingent legal, contract and tax-agreement termination claims are not fully quantified. A zero setting is a scenario condition, not a finding that no claims exist. |
| Dealer floor-plan borrowing: none; SMR replacement line is the ENTRA1 payable (259.884 at opening, paid in 2026) | history | The filings do not identify dealer floor-plan financing. I track the commercialization payment separately because it is the company-specific cash obligation. |

No forecast input is labelled guidance: no management five-year guidance has been verified. A contractual commitment is a historical disclosure, not an earnings forecast. Forecast reasons above are AI-authored analytical explanations, not a claim of student-authored judgment.

## Partner challenge and response

**Status: AI-assisted preparation only; the actual partner exchange has not been supplied.**

**Practice attack on my judgment — flat cash operating costs of 192.428 million:** “Why hold annual cash operating costs at 192.428 million for five years when inflation and commercialization work could increase them, and what evidence would make you change that number?”

**My proposed answer (two sentences):** I use 192.428 million because it starts with 2025 reported operating expenses, removes the identified ENTRA1 charge and separately modelled depreciation/amortization, and holds the remaining spending flat as an explicit cost-control assumption rather than management guidance. I would replace that flat path if comparable recurring expenses in later filings or a disclosed staffing/commercialization budget show a different run rate; allowing 2% annual cost growth already reduces this scenario's value from about $0.1063 to $0.0166 per share.

**Additional specific criticism you can use — 2030 wind-down judgment:** “Why does the end of your five-year forecast also become the end of NuScale's business, and what evidence supports assigning zero value to its technology after 2030 rather than extending the forecast until commercialization or a supported shutdown date?”

**Proposed two-sentence response:** I chose a 2030 wind-down to define a limited downside scenario, not because the filings say NuScale will close then, so the $0.11 result cannot stand alone as the company's fair value. I would replace that endpoint with a longer operating forecast if binding contracts and credible project economics support continued operation, including the associated milestone payments, funding needs and dilution.

**Actual partner attack:** [Unresolved — paste the partner's exact question and identify the judgment/value challenged.]

**Answer delivered to the partner:** [Unresolved — confirm the two-sentence answer above was used, or record the actual two-sentence response.]

**My attack on their model:** [Unresolved — identify their company, judgment-labelled assumption and value before recording the actual question.]

**Draft attack to adapt, not a recorded exchange:** “What filing evidence supports your [assumption/value] rather than [specific historical benchmark], and if it moves to that benchmark, does your model still meet its cash floor without extra borrowing or share issuance?”

**Their actual answer:** [Unresolved — record their explanation and the evidence that would change their number.]

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
python lab10_smr_proforma.py --write-report
python lab10_smr_proforma.py
python proforma.py
```

`Lab10_SMR_Proforma_Results.md` is generated from the same calculations as terminal output. It includes the income statement, balance sheet, cash flow statement, valuation bridge and sensitivities. `proforma.py` remains the ABG reference.

Suggested checkout wording: “I valued a services-only SMR downside case using five linked statements and discounted residual shareholder proceeds. My assumptions are labelled, all statements reconcile, and I explicitly settle the opening ENTRA1 payable. My result excludes successful reactor commercialization, so it is a conditional scenario value rather than my final fair-value estimate for SMR.”
"""


# HISTORY: 2025 10-K, F-4, F-5, F-8, Notes 9, 14 and 17.
OPENING = dict(cash=836.417, investments=450.754, receivables=8.378,
               prepaid=4.877, ppe=1.924, intangibles=0.527, llm=63.767,
               other_assets=45.868, ordinary_liabilities=39.077,
               pma_liability=259.884, equity=1113.551)
BASE_REVENUE = 31.479
BASE_MARGIN = 11.431 / BASE_REVENUE
NORMALIZED_OPEX = 45.532 + (609.825 - 507.393) + 45.645
CASH_OPEX = NORMALIZED_OPEX - 1.004 - 0.177
CLASS_A = 318.480601
EXCHANGEABLE_UNITS = 19.413185
RSUS = 4.184488
OPTIONS = 4.686454
# JUDGMENT: gross award dilution with no option proceeds, conservative proxy.
# Class B stock alone has no economics; denominator includes paired LLC units.
SHARES = CLASS_A + EXCHANGEABLE_UNITS + RSUS + OPTIONS
LLM_PURCHASES = (6.929, 41.938, 0.0, 0.0, 0.0)
TOL = 1e-7


@dataclass(frozen=True)
class Assumptions:
    # All forecast settings are analyst judgments, not management guidance.
    revenue_growth: float = 0.0
    opex_growth: float = 0.0
    cash_yield: float = 0.03
    discount_rate: float = 0.15
    capex: float = 0.508
    minimum_cash: float = 25.0
    closure_cost: float = 50.0
    receivable_recovery: float = 0.8
    llm_recovery: float = 0.0
    restricted_cash_recovery: float = 0.0
    extra_terminal_claims: float = 0.0


class FundingRequired(ValueError):
    pass


def total_assets(row):
    return sum(row[k] for k in ("cash", "investments", "receivables", "prepaid",
                                "ppe", "intangibles", "llm", "other_assets"))


def total_liabilities(row):
    return row["ordinary_liabilities"] + row["pma_liability"]


def check_close(label, actual, expected):
    if abs(actual - expected) > TOL:
        raise ValueError(f"{label}: gap = {actual - expected:+.9f} million "
                         f"({actual:.9f} versus {expected:.9f})")


def check_balance(row):
    check_close(f"{row.get('year', 2025)} balance sheet", total_assets(row),
                total_liabilities(row) + row["equity"])


def project(a=Assumptions()):
    if a.revenue_growth <= -1 or a.opex_growth <= -1 or a.discount_rate <= -1:
        raise ValueError("Growth and discount rates must exceed -100%")
    if min(a.capex, a.minimum_cash, a.closure_cost, a.extra_terminal_claims) < 0:
        raise ValueError("Cash requirements cannot be negative")
    if not all(0 <= x <= 1 for x in (a.receivable_recovery, a.llm_recovery,
                                     a.restricted_cash_recovery)):
        raise ValueError("Recovery fractions must be between zero and one")
    prior = OPENING.copy()
    check_balance(prior)
    rows = []
    for t, year in enumerate(range(2026, 2031), 1):
        revenue = BASE_REVENUE * (1 + a.revenue_growth) ** t
        cost_of_sales = revenue * (1 - BASE_MARGIN)
        gross_profit = revenue - cost_of_sales
        cash_opex = CASH_OPEX * (1 + a.opex_growth) ** t
        depreciation = min(1.004, prior["ppe"])
        amortization = min(0.177, prior["intangibles"])
        da = depreciation + amortization
        ebit = gross_profit - cash_opex - da
        receivables = revenue * OPENING["receivables"] / BASE_REVENUE
        prepaid = revenue * OPENING["prepaid"] / BASE_REVENUE
        wc_use = receivables - prior["receivables"] + prepaid - prior["prepaid"]
        llm_purchase = LLM_PURCHASES[t - 1]
        pma_payment = prior["pma_liability"]
        # Known January payment precedes interest accrual. Other flows midyear.
        # Fixed foreign-tax planning allowance; no NOL asset or tax benefit.
        foreign_tax = 0.342
        noninterest_cash = (ebit + da - foreign_tax - wc_use - llm_purchase - a.capex)
        interest_base = (prior["cash"] + prior["investments"] - pma_payment
                         + 0.5 * noninterest_cash)
        interest = max(0.0, interest_base) * a.cash_yield
        pretax = ebit + interest
        tax = foreign_tax + max(0.0, pretax) * 0.25
        net_income = pretax - tax
        cfo = net_income + da - wc_use - llm_purchase - pma_payment
        investment_sales = prior["investments"]
        cfi = investment_sales - a.capex
        cff = 0.0  # No debt, equity raises, dividends, or buybacks in this case.
        row = dict(year=year, revenue=revenue, cost_of_sales=cost_of_sales,
                   gross_profit=gross_profit, cash_opex=cash_opex,
                   depreciation=depreciation, amortization=amortization, da=da,
                   ebit=ebit, interest=interest, pretax=pretax, tax=tax,
                   net_income=net_income, opening_cash=prior["cash"],
                   cash=prior["cash"] + cfo + cfi + cff, investments=0.0,
                   receivables=receivables, prepaid=prepaid,
                   ppe=prior["ppe"] + a.capex - depreciation,
                   intangibles=prior["intangibles"] - amortization,
                   llm=prior["llm"] + llm_purchase,
                   other_assets=prior["other_assets"],
                   ordinary_liabilities=prior["ordinary_liabilities"],
                   pma_liability=prior["pma_liability"] - pma_payment,
                   equity=prior["equity"] + net_income,
                   wc_cash=-wc_use, llm_cash=-llm_purchase,
                   pma_cash=-pma_payment, cfo=cfo, capex_cash=-a.capex,
                   investment_sales=investment_sales, cfi=cfi, cff=cff,
                   change_cash=cfo+cfi+cff, shares=SHARES,
                   fcfe=cfo-a.capex)
        row["assets"] = total_assets(row)
        row["liabilities"] = total_liabilities(row)
        row["liabilities_equity"] = row["liabilities"] + row["equity"]
        row["balance_gap"] = row["assets"] - row["liabilities_equity"]
        check_balance(row)
        check_close(f"{year} Cash roll-forward", row["cash"] - prior["cash"], cfo+cfi+cff)
        check_close(f"{year} Equity roll-forward", row["equity"] - prior["equity"], net_income)
        check_close(f"{year} PMA settlement", pma_payment + row["pma_liability"], prior["pma_liability"])
        if row["cash"] < a.minimum_cash - TOL:
            raise FundingRequired(f"{year}: cash {row['cash']:.3f} below minimum "
                                  f"{a.minimum_cash:.3f}; gap = {row['cash'] - a.minimum_cash:+.9f} million; "
                                  "revise funding/share assumptions")
        if min(row[k] for k in ("ppe", "intangibles", "llm", "pma_liability")) < -TOL:
            raise ValueError(f"{year}: negative asset or PMA liability")
        rows.append(row)
        prior = row
    return rows


def value(rows, a=Assumptions()):
    last = rows[-1]
    recoveries = (last["receivables"] * a.receivable_recovery
                  + last["llm"] * a.llm_recovery
                  + 5.1 * a.restricted_cash_recovery)
    residual = (last["cash"] + last["investments"] + recoveries
                - last["liabilities"] - a.closure_cost - a.extra_terminal_claims)
    distribution = max(0.0, residual)
    pv = distribution / (1 + a.discount_rate) ** len(rows)
    return dict(recoveries=recoveries, residual=residual, distribution=distribution,
                equity_value=pv, per_share=pv/SHARES)


TABLES = [
    ("Income statement", [("Revenue", "revenue"), ("Cost of sales", "cost_of_sales"),
     ("Gross profit", "gross_profit"), ("Cash operating expenses", "cash_opex"),
     ("Depreciation", "depreciation"), ("Amortization", "amortization"),
     ("Operating income", "ebit"), ("Investment income", "interest"),
     ("Pretax income", "pretax"), ("Tax", "tax"), ("Consolidated net income", "net_income")]),
    ("Balance sheet", [("Cash", "cash"), ("Investments", "investments"),
     ("Receivables", "receivables"), ("Prepaid expenses", "prepaid"),
     ("PP&E", "ppe"), ("Intangibles", "intangibles"), ("Long-lead materials", "llm"),
     ("Other assets incl. restricted cash", "other_assets"), ("Total assets", "assets"),
     ("Ordinary liabilities", "ordinary_liabilities"), ("ENTRA1 payable", "pma_liability"),
     ("Total liabilities", "liabilities"), ("Consolidated equity incl. NCI", "equity"),
     ("Liabilities plus equity", "liabilities_equity"), ("Balance gap", "balance_gap")]),
    ("Cash flow statement", [("Net income", "net_income"), ("Add D&A", "da"),
     ("Receivables/prepaids movement", "wc_cash"), ("Long-lead material purchases", "llm_cash"),
     ("ENTRA1 payable settlement", "pma_cash"), ("Operating cash flow", "cfo"),
     ("Capital expenditure", "capex_cash"), ("Investment liquidation", "investment_sales"),
     ("Investing cash flow", "cfi"), ("Financing cash flow", "cff"),
     ("Net change in cash", "change_cash"), ("Opening cash", "opening_cash"),
     ("Closing cash", "cash"), ("FCFE before equity issuance/distributions", "fcfe")]),
]


def render():
    a = Assumptions()
    rows = project(a)
    v = value(rows, a)
    lines = ["# SMR — Lab 10 five-year statements and conditional valuation", "",
             "**Case: services-only through 2030, followed by wind-down.** "
             "This is a downside scenario, not a probability-weighted fair value or current price target.", "",
             "Measurement date: December 31, 2025; information basis: 2025 annual report "
             "published February 26, 2026. Retrospective classroom exercise; no 2026 interim update.", "",
             "USD millions except per-share values; shares in millions. "
             "Full assumptions, filing sources, and limitations are included below.", "",
             f"**Conditional value per share: ${v['per_share']:.4f} "
             f"(${v['per_share']:.2f} rounded).** Present equity value: ${v['equity_value']:.3f} million.", ""]
    for title, fields in TABLES:
        lines += [f"## {title}", "", "| USD millions | " + " | ".join(str(r['year']) for r in rows) + " |",
                  "|---|" + "---:|" * len(rows)]
        for label, key in fields:
            lines.append(f"| {label} | " + " | ".join(f"{0.0 if abs(r[key]) < TOL else r[key]:,.3f}" for r in rows) + " |")
        lines.append("")
    lines += ["## Forecast FCFE and positive value", "",
              "FCFE = operating cash flow - capital spending + net debt borrowing (zero here). "
              "Investment liquidation is excluded from FCFE; it converts existing assets into cash.", "",
              "| Year | FCFE, USD millions | Status |", "|---|---:|---|"]
    for row in rows:
        lines.append(f"| {row['year']} | {row['fcfe']:.3f} | "
                     f"{'negative FCFE' if row['fcfe'] < 0 else 'positive FCFE'} |")
    positive_fcfe_pv = sum(max(0.0, r["fcfe"]) / (1+a.discount_rate)**t
                           for t, r in enumerate(rows, 1))
    lines += ["", f"PV of positive forecast FCFE only: {positive_fcfe_pv:.3f} million "
              "(a diagnostic, not an additional distribution in this retained-cash case). "
              "Negative FCFE remains in every cash forecast and consumes liquidity; it is not deleted "
              "to inflate equity value. Only the positive residual shareholder distribution is valued here.", "",
              "A terminal perpetuity on negative cash flow can produce arithmetic, but not a meaningful "
              "going-concern equity valuation, because it assumes losses persist forever instead of "
              "establishing a sustainable distributable cash flow.", "",
              "## Valuation bridge", "",
              f"- 2030 cash: {rows[-1]['cash']:.3f}.",
              f"- Recoverable noncash assets: {v['recoveries']:.3f}.",
              f"- Settle remaining liabilities: ({rows[-1]['liabilities']:.3f}).",
              f"- Additional wind-down cost: ({a.closure_cost:.3f}).",
              f"- Terminal shareholder distribution: {v['distribution']:.3f}.",
              f"- Discount five years at {a.discount_rate:.0%}: present equity value {v['equity_value']:.3f}.",
              f"- Divide by {SHARES:.6f} million economic shares/awards: ${v['per_share']:.4f}.", "",
              "All shareholder proceeds occur at the end of 2030. Operating losses already reduce "
              "terminal cash: do not subtract their PV again or add opening cash again. "
              "The forecast statements are before liquidation; the bridge settles assets and claims separately.", "",
              "## Checks", "",
              "PASS: opening and all five forecast balance sheets; cash and equity roll-forwards; "
              "ENTRA1 payable settlement; nonnegative depreciable assets; minimum cash. "
              "Equity rolls forward from net income, never as a balancing plug.", "",
              "## Sensitivity — same services-only/wind-down framework", "",
              "| Change | Value/share |", "|---|---:|"]
    cases = [("Default", a), ("10% discount rate", replace(a, discount_rate=.10)),
             ("20% discount rate", replace(a, discount_rate=.20)),
             ("Revenue declines 10% annually", replace(a, revenue_growth=-.10)),
             ("Revenue grows 10% annually", replace(a, revenue_growth=.10)),
             ("Cash operating expenses grow 2% annually", replace(a, opex_growth=.02)),
             ("Wind-down cost 100 million", replace(a, closure_cost=100)),
             ("Additional terminal claims 100 million", replace(a, extra_terminal_claims=100))]
    for label, scenario in cases:
        try:
            result = value(project(scenario), scenario)
            lines.append(f"| {label} | ${result['per_share']:.4f} |")
        except FundingRequired as exc:
            lines.append(f"| {label} | Funding required: {exc} |")
    lines += ["", "A low number here does not establish that SMR is overpriced. "
              "The case deliberately assigns no value to successful module commercialization. "
              "A going-concern case needs project timing, net contract economics, milestone payments, "
              "financing, dilution, and tax-receivable-agreement treatment.", ""]
    return "\n".join(lines)


def render_opening():
    check_balance(OPENING)
    fields = [("Cash", "cash"), ("Investments, short and long term", "investments"),
              ("Receivables", "receivables"), ("Prepaid expenses", "prepaid"),
              ("PP&E, net", "ppe"), ("Intangibles", "intangibles"),
              ("Long-lead material WIP", "llm"),
              ("Other assets including restricted cash", "other_assets"),
              ("Ordinary liabilities", "ordinary_liabilities"),
              ("ENTRA1 payable", "pma_liability"),
              ("Consolidated shareholders' equity including NCI", "equity")]
    lines = ["## SMR opening balance sheet — December 31, 2025", "",
             'Replacement instruction: "Replace the ABG opening balance sheet and assumptions with these."',
             "The three-column assumption table above and this opening balance sheet are the inputs "
             "to this new SMR file. Amounts are USD millions.", "",
             "| Opening line | Value |", "|---|---:|"]
    lines += [f"| {label} | {OPENING[key]:,.3f} |" for label, key in fields]
    lines += [f"| Total assets | {total_assets(OPENING):,.3f} |",
              f"| Total liabilities | {total_liabilities(OPENING):,.3f} |",
              f"| Total liabilities plus equity | {total_liabilities(OPENING) + OPENING['equity']:,.3f} |",
              "", f"Source: [2025 10-K, balance sheet F-4]({FILINGS[2025]}). "
              "Investments = 417.800 + 32.954; other assets = 5.100 restricted cash + "
              "16.900 IPR&D + 8.255 goodwill + 15.613 other assets; ordinary liabilities = "
              "298.961 total liabilities - 259.884 ENTRA1 payable. No dealer floor-plan debt.", ""]
    return "\n".join(lines)


def render_checks():
    a = Assumptions()
    rows = project(a)  # Executes the same mandatory checks again; failures propagate.
    prior = OPENING
    lines = ["## CHECK BLOCK — unrounded calculations, USD millions", "",
             f"Tolerance: {TOL:g} million. A failure stops execution and names its year and gap.", "",
             "| Year | Assets - liabilities - equity | Cash roll-forward gap | Equity roll-forward gap | Cash above minimum | Result |",
             "|---|---:|---:|---:|---:|---|"]
    for row in rows:
        balance_gap = total_assets(row) - total_liabilities(row) - row["equity"]
        cash_gap = row["cash"] - prior["cash"] - row["change_cash"]
        equity_gap = row["equity"] - prior["equity"] - row["net_income"]
        for name, gap in (("balance sheet", balance_gap), ("cash roll-forward", cash_gap),
                          ("equity roll-forward", equity_gap)):
            check_close(f"{row['year']} {name}", gap, 0.0)
        # Display numerical round-off as zero only after checks pass.
        display = [0.0 if abs(gap) <= TOL else gap for gap in (balance_gap, cash_gap, equity_gap)]
        lines.append(f"| {row['year']} | {display[0]:.9f} | {display[1]:.9f} | "
                     f"{display[2]:.9f} | {row['cash'] - a.minimum_cash:.3f} | PASS |")
        prior = row
    lines += ["", f"Conditional services-only/wind-down value per share: **${value(rows, a)['per_share']:.4f}**.", ""]
    return "\n".join(lines)


def render_market_checkout():
    # Saved observation, not a live quote fetched each time this file runs.
    market_price = 8.54
    quote_time = "September 24, 2026, 1:56 p.m. EDT"
    quote_source = "https://stockanalysis.com/stocks/smr/"
    rows = project()
    model = value(rows)
    benchmark_equity = market_price * SHARES
    return "\n".join([
        "## Market comparison — saved dated observation", "",
        "No revolver is drawn in any year: opening cash and investment liquidation cover "
        "the forecast losses and commitments while keeping cash above the 25 million floor; "
        "this case assumes no revolving facility.", "",
        f"Market observation: **${market_price:.2f} per Class A share**, {quote_time}, "
        f"market open (intraday, not closing price). [Source]({quote_source}).", "",
        f"Common comparison denominator: {SHARES:.6f} million economic shares/awards, "
        "the model's frozen year-end-2025 if-converted, gross-award assumption. "
        f"Model equity = {model['equity_value']:.3f} million; applying the observed quote "
        f"to the same denominator gives a market-price benchmark of {benchmark_equity:.3f} million. "
        "That benchmark is not today's actual market capitalization. The quote page reports "
        "429.72 million shares outstanding, a different date and share definition. "
        "The annual-report model has not been rolled forward for subsequent cash flows or issuance.", "",
        f"Using the same frozen {SHARES:.6f}-million-share basis, the services-only wind-down "
        f"model says ${model['per_share']:.4f} per share and the market quote says "
        f"${market_price:.2f} at {quote_time}; what commercialization outcomes and changes "
        "since the model's 2025 starting date could explain the gap?", "",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = (render_history() + "\n" + ASSUMPTION_NOTES + "\n"
              + render_opening() + "\n" + render() + "\n" + render_checks()
              + "\n" + render_market_checkout())
    print(report)
    if args.write_report:
        Path(__file__).with_name("Lab10_SMR_Proforma_Results.md").write_text(report)


if __name__ == "__main__":
    main()

```
