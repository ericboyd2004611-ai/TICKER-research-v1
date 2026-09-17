# Lab 08 — NuScale peer comparison

Status: the student accepted the AI-assisted peer decisions, the main DCF criticism, and the final watch-defer call. Personal source review remains to be confirmed. Price rows have been verified by Codex, with the BWXT adjustment convention noted below. Policy was AI-assisted, not independently student-written; process limitations are disclosed rather than backdated.

## Reopen and explain

The saved Lab 07 calculator was rerun with `python3 'Week 04/peer_pe_valuation.py'`. It reproduces the Asbury exercise range of $215.81–$246.18. These are validation numbers only, not NuScale valuation inputs.

Method to explain in your own words: divide an admitted peer's same-date share price by its annual reported diluted EPS, then multiply that multiple by the target's compatible annual reported diluted EPS. Positive, comparable earnings are necessary for a meaningful conventional P/E valuation. No cash/debt bridge applies to this equity route.

## Target and dates

- Target carried forward from Week 3: NuScale Power, NYSE: SMR, Class A common stock.
- Saved Week 3 valuation review date: September 10, 2026.
- Saved price observation date: September 9, 2026; saved price $10.81. Codex verified the September 9 Close and Adj. Close columns, both $10.81, in the Stock Analysis history table.
- Currency and earnings basis: USD per Class A share; annual reported GAAP basic and diluted loss per share, not adjusted EPS or quarterly EPS.

## Initial student policy — required before candidate suggestions


> I will compare NuScale with listed operating companies that develop or supply nuclear reactor technology, engineering, or related services. I will prioritize similar commercialization risks, long project timelines, regulatory requirements, and dependence on customer contracts. A shared nuclear-industry label alone is insufficient.
>
> I will qualify differences in company size, reactor technology, revenue mix, and commercialization stage when the underlying economics remain informative. I will exclude businesses primarily earning money from electricity sales, uranium mining, or unrelated activities.
>
> For P/E calculations, I will use positive annual reported diluted EPS available by September 10, 2026, and prices from September 9, 2026, on compatible currency and share bases. Loss-making candidates may inform business comparisons but cannot supply usable P/E multiples. I will not change peer decisions merely to obtain a preferred valuation.

No separate pre-research rejection prediction was recorded. The policy's stated exclusions are preserved above; a prediction is not being backdated.

## Target evidence checked by Codex

NuScale's 2025 revenue came from technology licensing and engineering services tied to nuclear-project development. The annual release attributes the revenue change to RoPower licensing and Fluor FEED engineering work. This raises a focused research question: which listed operating companies have sufficiently comparable nuclear technology commercialization economics, customer/project risks, and maturity to inform NuScale's valuation?

| Input | Evidence | Fiscal period / publication | Source locator |
|---|---|---|---|
| Reported annual diluted EPS | **−$2.17** | Year ended December 31, 2025; annual results released February 26, 2026, before the comparison date | [2025 10-K](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm), Consolidated Statements of Operations and Note 3, Equity and Loss Per Share |
| Business revenue explanation | Licensing and engineering services | FY2025; February 26, 2026 release | [Annual earnings release](https://www.nuscalepower.com/press-releases/2026/nuscale-power-reports-fourth-quarter-and-full-year-2025-results), Financial Update, revenue paragraph |

The target EPS is negative. Multiplying positive peer P/E multiples by this loss would not produce an economically meaningful share valuation. Taking the absolute value, substituting adjusted profits, or annualizing a quarter would not resolve this lab's limitation. Positive comparable annual reported diluted earnings would be necessary to revisit P/E; those earnings must also have been public by the comparison date. Future profitability cannot repair the historical input retroactively.

## Candidate decisions

Claude suggested BWXT and OKLO. Codex subsequently checked their primary sources; this is a review of Claude's candidates, not an independent pre-response candidate search.

| Candidate | Verified business evidence and difference | Annual reported diluted EPS (USD/share) | Publication date | Disposition accepted by student |
|---|---|---|---|---|
| BWX Technologies (BWXT) | Nuclear components, fuel and reactor engineering; mature government-contract manufacturing differs from NuScale commercialization. [2025 10-K](https://www.sec.gov/Archives/edgar/data/1486957/000148695726000007/bwxt-20251231.htm), Item 1, Government Operations; Item 7, segment discussion | **$3.58**, year ended December 31, 2025; 10-K Note 17, Earnings Per Share | **February 23, 2026**, [annual release](https://investors.bwxt.com/news-releases/news-release-details/bwx-technologies-reports-fourth-quarter-and-full-year-2025) | **Qualify** under the original policy's allowance for stage/revenue-mix differences; exclude instead if the student requires early commercialization as a hard condition. Positive EPS alone does not establish fit. |
| Oklo (OKLO) | Reactor development shares deployment risk, but intended primary business is owning plants and selling power through PPAs. [2025 10-K](https://www.sec.gov/Archives/edgar/data/1849056/000162828026018698/oklo-20251231.htm), Item 1, Our Business Model, pp. 6–7 | **−$0.72**, year ended December 31, 2025; Consolidated Statements of Operations, Class A basic and diluted loss per share | **March 17, 2026**, [annual release](https://oklo.com/newsroom/oklo-publishes-full-year-2025-financial-results-and-business-update) | **Exclude** from valuation peers under a substantive reading of the electricity-sales exclusion; retain as qualitative context. Negative EPS also prevents a usable P/E. |

### Audit of Claude's response

- **EPS verified:** BWXT $3.58 and OKLO −$0.72 agree with their annual 10-Ks; secondary reporting is unnecessary for these figures.
- **Policy drift:** Claude's optimized scope emphasizes pre-/early-commercial stage and excludes diversified industrials with minor nuclear segments. The original allows qualification for commercialization-stage differences. Do not silently adopt a stricter policy after seeing candidates. Claude also says unsourced figures become estimates; this lab instead requires unresolved evidence to stay unresolved.
- **Initial price evidence gap (subsequently addressed below):** Claude reports September 9 closes of BWXT $156.71 and OKLO $42.57, but the pasted response does not retain actual price-source URLs. Its alternate prices differ. Codex opened [Nasdaq BWXT historical data](https://www.nasdaq.com/market-activity/stocks/bwxt/historical), but the retrieved page did not establish the dated close. No verified price has been entered into the calculator. The suggested adjusted/unadjusted explanation is unverified.
- **Arithmetic check:** 156.71 / 3.58 = 43.773743x, or 43.77x. The price row was subsequently verified below; its adjustment convention remains relevant. This is BWXT's multiple, not a NuScale valuation.
- **Oklo policy interpretation:** Lack of current power revenue does not remove the economic difference in its disclosed intended business model. Proposed exclusion rests on that model, not on disliking the valuation result.
- **NuScale earnings attribution:** Claude pairs −$2.17 EPS with total consolidated net loss of $664.5M. The EPS numerator is instead the $355.794M loss attributable to Class A stockholders, per NuScale's 10-K Statements of Operations. Do not divide total consolidated loss by Class A weighted-average shares.

### Accepted decision explanations

The student approved the following AI-assisted explanations in chat:

- **BWXT — qualify:** I qualify BWXT because its nuclear components and reactor-engineering work shares technical, regulatory, and long-contract characteristics with NuScale. However, BWXT's established government business differs from NuScale's early commercialization stage, so its P/E offers limited comparability.
- **Oklo — exclude:** I exclude Oklo because its planned primary business is owning plants and selling electricity, while NuScale earns revenue from technology licensing and engineering services. That conflicts with my policy's electricity-sales exclusion, despite similar reactor-development risks.

The student still needs to open the linked Business and EPS sections personally; this document records Codex's source verification without claiming the student has already performed it.

BWXT is admitted with qualification; its dated source price is verified with the adjustment caveat below. OKLO is retained in the evidence table as excluded.

## Validation

### Same-date price evidence verified September 17, 2026

All prices below are USD per listed common share, dated September 9, 2026. Stock Analysis is a secondary market-data provider, not the issuer.

| Company | Source price | Source and exact locator | Basis / limitation |
|---|---:|---|---|
| SMR | $10.81 | [Stock Analysis history](https://stockanalysis.com/stocks/smr/history/), September 9, 2026 row, Close | Close and Adj. Close both $10.81; Class A common shares |
| BWXT | $156.71 | [BWXT IR Historic Prices](https://investors.bwxt.com/stock-information/historic-prices), Week of September 8, 2026, September 9 row, Closing Price | Source: LSEG; split factor 1:1. Page says historical prices reflect splits and/or dividends since the date shown. This is the source-displayed adjusted historical closing price, not independently confirmed as the original unadjusted close. |
| OKLO | $42.57 | [Stock Analysis history](https://stockanalysis.com/stocks/oklo/history/), September 9, 2026 row, Close | Close and Adj. Close both $42.57; excluded candidate, retained for documentation |

The MarketBeat differences provided in chat were not independently reconciled. Do not assert that adjustments explain them. The BWXT price is used transparently under its source convention; an original unadjusted closing-price record would resolve the remaining price-basis caveat. It cannot alter the negative-target-EPS limitation.

### Calculator and removal check

Executed `python3 'Week 04/lab08_smr.py'` with SMR price $10.81, EPS −$2.17, and only qualified BWXT price $156.71, EPS $3.58. OKLO stays excluded.

Hand-check arithmetic: $156.71 / $3.58 = **43.773743x**, matching the calculator. This check was performed by Codex; the student should be able to reproduce it.

Codex prediction before the removal run: removing the sole admitted peer leaves no peer multiple and no estimate. A meaningful NuScale estimate is already unavailable because of negative target EPS.

Observed output:

```text
Target EPS is missing or nonpositive; implied prices are not meaningful.
BWXT: P/E 43.773743x
Peer P/E statistics are available, but target implied prices and sensitivity are not meaningful.

Remove sole qualified peer BWXT:
Target EPS is missing or nonpositive; implied prices are not meaningful.
No usable peers; no estimate.
```

Interpretation: BWXT supplies a positive multiple under the documented price convention, but cannot produce a valid NuScale price from negative annual EPS. Removing BWXT eliminates that reference multiple; it does not fix the target's earnings. No alternative valuation method or substitute company is used.

## Comparison with the saved DCF

| Method | NuScale result and date | Main assumption or limitation |
|---|---|---|
| Week 3 DCF | Saved mechanical sensitivity range **−$56.75 to −$31.51/share**, base **−$40.55**, September 10, 2026 review | Negative starting FCFF persists under positive growth; growth and WACC are training placeholders. This is not a defensible equity price range. |
| Peer P/E | **Unusable:** FY2025 reported diluted EPS **−$2.17** was public before September 10, 2026 | Negative target EPS prevents a meaningful conventional P/E estimate. BWXT qualified; OKLO excluded. BWXT uses its IR historical-price adjustment convention. |

DCF provenance: `../Week 03/Lab 6 Complete.md` and `../Week 03/SMR_DCF_inputs.md`. No range has been invented and the methods have not been averaged.

## Codex skeptical review — student accepts the main criticism

Weakest supported assumption: treating an unusually negative historical FCFF base as a perpetual-growth starting point while retaining training growth and discount-rate assumptions. The saved DCF already acknowledges this problem.

Valuation-object concern: the saved model uses consolidated cash flow and cash with weighted-average Class A EPS shares. The ownership/noncontrolling-interest allocation and valuation-date share count require reconciliation before defending a Class A per-share DCF. EPS weighted-average shares are not automatically the appropriate current ownership denominator.

One question that could change the call: **What sourced evidence supports a sustainable path from NuScale's cash losses to positive cash flow attributable to Class A shareholders, after funding needs and dilution?**

**Student judgment — accept:** My saved DCF range is unreliable because it extends negative cash flow using placeholder growth and discount-rate assumptions. The peer comparison cannot validate that range because NuScale's negative reported EPS makes P/E unusable. Neither result establishes that the stock is overpriced.

Evidence supporting this judgment: `../Week 03/Lab 6 Complete.md`, sections 2–3, explicitly identifies placeholder growth and WACC and reports the negative-FCFF sensitivity results. NuScale's linked 2025 10-K, Note 3, reports diluted loss per share of $2.17.

The separate ownership/share-count concern remains unresolved; no reconciled Class A valuation has been supplied. No pre-response statement of what would change the student's mind was recorded. The final call below states the evidence that would change the decision.

## Conditional conclusion — accepted by student

**My call is watch-defer.** I withhold a price range because my DCF uses unsupported assumptions and NuScale's negative annual earnings make P/E unusable. I would reconsider if evidence supports sustainable positive cash flow after funding needs and dilution, and a revised, company-specific DCF supports value above the market price.

The peer comparison adds a check on business economics: BWXT offers a qualified nuclear-engineering reference, while Oklo's intended electricity-sales model conflicts with the policy. Neither provides a valid price for NuScale using its negative annual EPS. The DCF's negative mechanical output and the unusable P/E therefore cannot be compared as two defensible price ranges or averaged.

**Answer to the skeptical question:** This analysis has not established a sourced, sustainable path to positive cash flow attributable to Class A shareholders after funding needs and dilution. That missing evidence is why I defer. Evidence supporting that path, together with a revised company-specific DCF, would change my decision.

This final rule uses sustainable cash flow plus valuation support. It clarifies the differing Week 3 rules: two positive operating-cash-flow quarters may be evidence of progress, but alone do not establish valuation upside.


