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
