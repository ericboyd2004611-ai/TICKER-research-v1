# Lab 19 — Buffett, Graham and Burry on the same SEC facts

Completed November 5, 2026. This version implements the supplied official requirements and replaces the earlier Buffett/Graham/Lynch draft. The old work is preserved separately as `Lab 19 earlier draft.md` and `lab19_draft_lynch/`; it is excluded from the current submission ZIP.

## Answer and Project 2 disposition

The investors agree that COST has favorable profitability and cash-generation evidence. They split on the required safeguards: Graham fails COST on liquidity even though its earnings tests pass, while Buffett and Burry pass all their assigned checks. Model verdicts remain separate from check scores.

**Project 2: only with the condition that SEC inputs and missing tags are reviewed, thresholds are fixed before screening, and the panel is used for research triage rather than price-based selection.**

## Requirements completed

| Requirement | Evidence |
|---|---|
| Buffett, Graham and Burry skills | `lab19/skills/`, with SKILL.md name/description, bundled runner, shared code and philosophy source links; installed in the Codex user-skills folder |
| All specified checks computed from the same SEC facts | `lab19/panel_engine.py`, preserving the Lab 18 selection engine and expanding the common packet for everyone |
| COST known-answer proof | Both five-year ratio series and all eight check outcomes match the supplied answers |
| Graham threshold probe | Actual skill configuration changed to 1.0, COST rerun and saved in `reports/probe_threshold_1/`, then configuration restored to 2.0 |
| Three separately written memos per company | COST and SUN memos plus numeric-audit JSONs in `lab19/reports/` |
| App panel, verdicts and side-by-side memos | `panel_app.py`; UI tests passed for COST and SUN |
| Flag unprinted numbers across all memos | Numeric auditing loops over every displayed memo; injected unsupported number detected |
| Fund’s largest company exercise | SUN from the dated AMLP issuer holdings snapshot; working fund assumption explained below |
| Missing values preserved | SUN’s missing required tags produce not found values and not known dependent checks |
| Explain Graham function | Source and explanation below; also available in the app’s code expander |

## Common data rules and sources

COST uses the exact Lab 18 archived SEC companyfacts bytes; no fresh COST download was substituted. The expanded shared packet adds AssetsCurrent and LiabilitiesCurrent from that same archive to calculate current ratio. All three skills read the same expanded printed report and its code-computed checks. SUN companyfacts was downloaded directly from SEC EDGAR on November 5, 2026.

The rules remain: exact 10-K form, annual flows using the original 330–380-day convention, five latest fiscal-year-end dates, latest filing wins for repeated periods, prescribed tag precedence, raw missing values printed as not found and dependent values/checks as not known. ROE uses year-end StockholdersEquity. Nonpositive equity makes ROE and liabilities/equity unknown. Current liabilities at or below zero make current ratio unknown. Current ratio uses AssetsCurrent / LiabilitiesCurrent. Owner earnings remains operating cash flow minus total capital spending. Comparisons use unrounded values; ratio display rounds to two decimals.

Revenue: RevenueFromContractWithCustomerExcludingAssessedTax then Revenues; net income: NetIncomeLoss; operating cash flow: NetCashProvidedByUsedInOperatingActivities; capital spending: PaymentsToAcquirePropertyPlantAndEquipment then PaymentsToAcquireProductiveAssets; equity: StockholdersEquity; liabilities: Liabilities. No partnership-equity or custom capital-spending tag is silently substituted. Field-level selected dates, tags and accessions are printed in each common report.

Annual every-year checks require five complete observations. Endpoint-growth checks require five fiscal-year slots and nonmissing endpoint values; an intermediate value is not an input to an endpoint comparison. Missing evidence is never automatically failed.

Only the reference text of [Graham’s page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/ben_graham.md) and [Burry’s page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md) was used for philosophy. No FAskills installation, orchestration or paid financial service supplied this work. SEC sources: [ticker mapping](https://www.sec.gov/files/company_tickers.json), [COST facts](https://data.sec.gov/api/xbrl/companyfacts/CIK0000909832.json), [SUN facts](https://data.sec.gov/api/xbrl/companyfacts/CIK0001552275.json). [Streamlit columns documentation](https://docs.streamlit.io/develop/api-reference/layout/st.columns) supports the side-by-side presentation. The issuer holdings sheet is used only to select the fund company, not to supply financial-statement inputs.

## COST: known-answer verification

| Fiscal-year-end | Current ratio | Liabilities / equity |
|---|---:|---:|
| 2022-08-28 | 1.02 | 2.11 |
| 2023-09-03 | 1.07 | 1.75 |
| 2024-09-01 | 0.97 | 1.96 |
| 2025-08-31 | 1.03 | 1.64 |
| 2026-08-30 | 1.06 | 1.49 |

Every displayed value above matches the supplied known answer. The expected arrays exist only in the acceptance test, not in production calculations.

| Investor | Check | COST |
|---|---|---|
| Buffett | ROE >= 15% every year | pass |
| Buffett | Owner earnings positive every year | pass |
| Buffett | Owner earnings grew, first year to last | pass |
| Graham | Current ratio >= 2.0, latest year | fail (1.06) |
| Graham | Net income positive every year | pass |
| Graham | Net income grew, first year to last | pass |
| Burry | Operating cash flow >= net income every year | pass |
| Burry | Liabilities <= twice equity, latest year | pass (1.49) |

**Buffett 3 of 3; Graham 2 of 3; Burry 2 of 2.** Scores have different denominators and are not interchangeable votes. Burry’s liabilities check is latest-year only; the earliest ratio of 2.11 does not make that latest-year check fail.

## Threshold probe

Graham’s executable configuration is `lab19/skills/graham-panel/config.json`. I actually set its current_ratio_threshold to 1.0, reran COST, saved the full output separately, and restored 2.0. Latest COST current ratio is 1.06, so the lower threshold makes Graham pass all his checks (3 of 3). A failed automated test initially referenced an unrendered report field; that test harness issue was fixed, and all acceptance tests then passed. No financial value was altered.

**Threshold kept: 2.0 — preserves the assigned defensive liquidity buffer rather than tuning the rule to make COST pass.**

This same line appears under Graham’s saved memo and in the app. The app’s probe checkbox also shows the lower-threshold check results, clearly warns that saved memos refer to the retained rule, and does not pretend to regenerate a model judgment automatically. Passing a changed screen does not by itself require an Own verdict.

## My fund’s largest company

Lab 15 lists five energy funds rather than one confirmed fund. **Working assumption: AMLP**, the largest portfolio allocation, is used here; the user was asked to confirm the fund and has not supplied a different choice. This assumption remains visible rather than being represented as a confirmed personal choice.

ALPS’s [AMLP issuer fact sheet](https://www.alpsfunds.com/hubfs/alps-docs/lit/fs/alerian-mlp-etf-amlp-fs.pdf), as of September 30, 2026, ranks Sunoco LP first at 12.46%, followed by MPLX at 12.33%. This is a dated issuer snapshot, not a claim about today’s exact daily rank. The archived PDF and `company_selection.json` preserve the evidence. If another fund or a different holdings date is required, that company choice needs to be rerun.

SUN files an [EDGAR 10-K for the year ended December 31, 2025](https://www.sec.gov/Archives/edgar/data/1552275/000155227526000021/sun-20251231.htm), filed February 19, 2026. No next-largest-company fallback was used. Its five annual periods are FY2021–FY2025; its FY2026 annual filing is not yet available in the retrieved facts.

| Investor | Check | SUN |
|---|---|---|
| Buffett | ROE >= 15% every year | not known |
| Buffett | Owner earnings positive every year | not known |
| Buffett | Owner earnings grew, first year to last | not known |
| Graham | Current ratio >= 2.0, latest year | fail (1.38) |
| Graham | Net income positive every year | pass |
| Graham | Net income grew, first year to last | pass |
| Burry | Operating cash flow >= net income every year | fail |
| Burry | Liabilities <= twice equity, latest year | not known |

SUN’s prescribed StockholdersEquity tag is not found. Some later capital-spending facts are not found under either allowed tag. Those gaps are not estimates, zeroes or automatic failures. Burry’s cash test fails because FY2024 operating cash flow of 549.00 is below net income of 866.00 (USD millions), despite stronger latest-year cash coverage.

## Check scores and model verdicts

| Company | Investor | Checks passed | Not known | Model verdict |
|---|---|---|---:|---|
| COST | Buffett | 3 of 3 | 0 | Own the business |
| COST | Graham | 2 of 3 | 0 | Watch it |
| COST | Burry | 2 of 2 | 0 | Watch it |
| SUN | Buffett | 0 of 3 | 3 | Watch it |
| SUN | Graham | 2 of 3 | 0 | Watch it |
| SUN | Burry | 0 of 2 | 1 | Pass |

On COST, Buffett gives provisional business-quality approval to the demonstrated cash record; Graham wants the specified liquidity buffer; Burry’s alarms do not fire but he wants fuller accounting diligence. Thus Buffett and Burry agree numerically while their model judgments differ. On SUN, unknown tags limit Buffett; Graham fails the liquidity rule; Burry identifies a specific cash-versus-income exception. None of these judgments is based on market price.

## Explain the code: Graham checks

The function is `graham_checks` in [panel_engine.py](lab19/panel_engine.py). It was opened for inspection and is also shown in the running app.

```python
def graham_checks(records, threshold):
    """Graham's assignment checks: missing required input -> not known."""
    latest = records[-1]['metrics']
    return {
        f'Current ratio >= {threshold:.1f}, latest year': status(
            [latest['current_ratio']['value']], lambda ratio: ratio >= threshold),
        'Net income positive every year': all_years(records, ['net_income'], lambda ni: ni > 0),
        'Net income grew, first year to last': grew(records, 'net_income'),
    }
```

- `latest = records[-1]["metrics"]` selects the latest fiscal year from the oldest-to-newest records.
- `status([ratio], predicate)` first looks for a missing required value. Missing gives not known. Otherwise the unrounded ratio is compared with the threshold: true gives pass; false gives fail.
- `all_years` requires five annual net-income observations. A missing one gives not known; otherwise every net income must be strictly positive.
- `grew` compares the first and last fiscal years. Missing endpoints give not known; the last must be strictly greater than the first to pass.
- The function returns check outcomes, not the investor’s memo or verdict. Model judgment is written after reading the printed results.

## App and verification

The app `Week 10/panel_app.py` shows the investor/check table, check counts and verdicts, then three simultaneous columns with Buffett, Graham and Burry memos. It also shows both ratio histories, raw figures and XBRL tags. Every displayed memo is scanned for unsupported numeric tokens, highlighted in red and aggregated across the panel. Saved memo/report hashes expose edits and threshold mismatches. No unsupported numbers remain in the six submitted memos. Token membership alone cannot prove the correct unit, year or interpretation, so semantic review still matters.

Five accounting test methods passed, covering all supplied COST dates/ratios/checks, threshold sensitivity, inclusive and unrounded boundaries, missing inputs/nonpositive equity, Burry’s every-year versus latest-year logic, SUN unknowns, and numeric auditing. Streamlit AppTest passed: eight check rows; three verdicts; three memo columns; COST 3/3, 2/3, 2/2; probe 3/3, 3/3, 2/2; injected unsupported number detected; SUN unknowns displayed. The source companyfacts bytes for COST were confirmed unchanged from Lab 18.

Run from the repository root:

```sh
.venv-rates/bin/streamlit run 'Week 10/panel_app.py' --server.headless true --server.port 8505 --server.address 127.0.0.1
```

App: http://127.0.0.1:8505. Saved cases are COST and SUN; another ticker needs its SEC input and model-written memos before it can be displayed. The app does not silently invent missing memos or facts.

Reproduce offline and audit:

```sh
python 'Week 10/lab19/panel_engine.py' COST --audit
python 'Week 10/lab19/panel_engine.py' SUN --audit
.venv-rates/bin/python -m unittest discover -s 'Week 10/lab19' -p 'test_official_panel.py' -v
.venv-rates/bin/python 'Week 10/lab19/verify_app.py'
```

Each installed skill (`$buffett-panel`, `$graham-panel`, `$burry-panel`) contains a runner that uses the same shared engine. Supply the `lab19` directory and ticker. Their Python runners compute and audit; the AI supplies the memo after reading output. `requirements-lab19.txt` contains the app dependencies.

## Full submitted model memos

### COST — Buffett-inspired model memo

Decision: **Own the business**

This is a provisional business-quality judgment, not Warren Buffett's actual opinion. All monetary figures are USD millions.

I would provisionally want to own this business on the cash-generation evidence. Owner earnings increased from 3,501.00 to 9,382.00 across the supplied endpoints. The ROE, positive owner-earnings and endpoint-growth checks all pass. This is an attractive financial record for an owner-oriented business.

I would not confuse the passing screen with a proven moat. Owner earnings fell from 6,745.00 to 6,629.00 within the window, so growth was not uninterrupted. The latest current ratio is 1.06, which deserves attention even though liquidity is not in my assigned checks. The lab deducts total capital spending, and year-end equity can make ROE sensitive to financing and distributions.

I would move to watch it if cash generation weakened persistently or further filing evidence undermined its durability. Competitive advantage and management quality still need examination. This judgment says nothing about the price of the shares.

### COST — Graham-inspired model memo

Decision: **Watch it**

This is a business-quality simulation, not Benjamin Graham's actual opinion. All monetary figures are USD millions.

I see favorable earnings but an incomplete defensive case. Net income was positive in every supplied year and grew from 5,844.00 to 9,226.00 between the endpoints. Those checks pass.

The latest current ratio is 1.06, below the retained 2.0 threshold, so the assigned liquidity check fails. Passing earnings tests does not erase that failure, and the failure alone is not proof of imminent insolvency. The ratio describes balance-sheet coverage, not the timing or reliability of each inflow and obligation.

I would keep the business on watch while examining whether operating cash generation and the structure of its obligations justify a different business-quality judgment. I would change my view on convincing evidence of resilience, not simply by lowering a rule to obtain a pass. No valuation or price conclusion is made.

Threshold kept: **2.0** — preserves the assigned defensive liquidity buffer rather than tuning the rule to make COST pass.

### COST — Burry-inspired model memo

Decision: **Watch it**

This is an earnings-quality simulation, not Michael Burry's actual opinion. All monetary figures are USD millions.

The assigned accounting alarms do not fire. Operating cash flow is at least net income in every supplied year; in the latest year the figures are 15,817.00 and 9,226.00. Latest liabilities/equity is 1.49, so the latest-year liabilities check passes as well.

I would not call those passes proof that the accounting is clean or that the business is safe. The ratio was 2.11 at the earliest endpoint, but the assigned liabilities test deliberately evaluates only the latest year. Total liabilities also include more than interest-bearing borrowing. Cash flow can be affected by working-capital timing, which these summary tests do not investigate.

I would watch the business until the notes and cash-flow reconciliation explained the quality and persistence of the cash generation. Evidence of sustained cash backing with no concerning disclosures could strengthen the case; unexplained cash deterioration or obligations could weaken it. This is not a short thesis or a price judgment.

### SUN — Buffett-inspired model memo

Decision: **Watch it**

This is a business-quality simulation, not Warren Buffett's actual opinion. All monetary figures are USD millions.

I cannot give a complete owner-quality assessment from the prescribed tags. Equity is not found, so ROE is not known. Capital spending is not found for the later supplied years, so the full owner-earnings record and its assigned checks are not known. I will not replace partnership-equity or capital-spending tags with estimates to create a passing screen.

The latest operating cash flow is 1,192.00 against net income of 527.00, but that favorable observation does not establish the missing owner-earnings history. I would watch the business until reviewed filing evidence resolved the missing inputs under an explicitly approved mapping. If the rules remain unchanged, the unknown results remain unknown. No price conclusion is offered.

### SUN — Graham-inspired model memo

Decision: **Watch it**

This is a business-quality simulation, not Benjamin Graham's actual opinion. All monetary figures are USD millions.

Net income is positive in every supplied year and grew from 524.00 to 527.00 between the endpoints, so those assigned checks pass. The latest current ratio is 1.38, below the retained 2.0 threshold; that liquidity check fails.

I would not call the business insolvent from that ratio alone, nor would I infer complete financial strength from the earnings checks. The prescribed equity tag is not found, and the business's ability to meet obligations needs fuller filing review. I would remain on watch until the financing and cash-timing evidence justified a stronger conclusion. No share-price or valuation claim is made.

Threshold kept: **2.0** — preserves the assigned defensive liquidity buffer rather than tuning the rule to make a company pass.

### SUN — Burry-inspired model memo

Decision: **Pass**

This is an earnings-quality simulation, not Michael Burry's actual opinion. All monetary figures are USD millions.

I would pass on advancing this business through the limited screen until the cash mismatch was explained. Operating cash flow of 549.00 was below net income of 866.00 in a supplied year, so the every-year cash-coverage check fails. Latest operating cash flow of 1,192.00 exceeds latest net income of 527.00, but that does not reverse an every-year test.

The prescribed equity tag is not found, so the latest liabilities test is not known rather than failed. The cash shortfall does not establish accounting manipulation: working-capital timing or other legitimate effects may explain it. A credible filing-based reconciliation could change my view; an estimate for missing equity would not. This is a cautious business-screening judgment, not a short or price recommendation.

## Trust and AI disclosure

I would trust this as a reproducible screening and research tool only with the condition stated at the start. The threshold probe shows that disagreement can come from a chosen rule rather than new information. A missing tag is a coverage limitation, not proof of an economic absence. Cash coverage is not proof against manipulation, high ROE is not proof of a moat, and a low current ratio is not a standalone insolvency diagnosis.

All memos are model simulations written sequentially in one Codex conversation. They are not independent historical investors or blinded experts. The model, shared SEC facts and selection engine can produce correlated errors. No price data, target, valuation or security recommendation is offered.

Codex read the reference philosophy pages, implemented and installed the skills, ran SEC calculations and the threshold probe, downloaded SUN and the issuer selection evidence, wrote the six memos, tested the app, and drafted this report. No independent student reconciliation of the original filing rows or model judgments is recorded.
