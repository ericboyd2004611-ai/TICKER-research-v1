# Lab 17 — Rates as known on the decision date

## Question and decision

Was each number knowable on the day we would have traded, and may Project 2 use the series?

**Current disposition: quarantine BAA pending a complete decision-date audit.** It may be admitted as a rate/economic signal once that audit passes; using today's historical values as if they were available at their observation dates is not acceptable. A complete Project 2 trade-history audit remains outstanding because no trade schedule, exact signal rule, or intraday timing was supplied. Each trade must use its own eligible ALFRED snapshot. Same-day use also needs evidence that publication occurred before the trade.

The prework series choice was not found in the local documents, so BAA remains provisional. All four assigned series are included in the new app; a custom ID can be added. The energy ETF universe from Lab 15 is XLE, XOP, AMLP, ICLN, and NLR. Rates may condition a signal, but yield levels are not ETF total returns and cannot replace the optimizer's return inputs. Lab 15's separate 40% fund-cap issue remains relevant to mandate compliance.

## Connections to Labs 15 and 16

Lab 15 supplied the Streamlit portfolio explorer and historical ETF estimates. Its original files are preserved. Lab 16 supplied the as-of logic: remove publications after the decision date first, then select the latest eligible revision for each measured period. The measured date, publication date, and revision date have different meanings.

Lab 16's training decision was March 31, 2026. Its as-of signals were AAA +1.98%, BBB −1.02%, and CCC +0.91%; the naive signals were +5.83%, −5.15%, and +1.82%. Those were synthetic index-change signals, not demonstrated trading returns. Lab 17 applies the availability question to real FRED/ALFRED rates.

## App saved: `asof_app.py`

The sidebar starts with all four selected:

| ID | Series | Native frequency |
|---|---|---|
| BAA | Moody's Baa corporate bond yield | Monthly |
| FEDFUNDS | Federal funds rate | Monthly |
| DGS10 | 10-year Treasury yield | Daily |
| MORTGAGE30US | 30-year mortgage rate | Weekly |

It also includes a custom FRED ID box, start date defaulting to January 1, 2020, and an “As known on” date defaulting to today. October 5 was used for the acceptance checkpoint; the later month-end/today exercise restored the default to today. Each selected series has one chart of today's values from the start date and a caption giving the last measured date present in the requested historical snapshot.

The combined table links each ID to its FRED page and reports the last measured date/value then, last measured date/value today, today's nonmissing observations after the last historical date, and revised nonmissing values on shared dates. The chart start date does not truncate the table's histories. If no historical observation exists, its last-date fields and subsequent-value count are blank; the app does not invent a cutoff date.

The attribution under the title reads: data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded today; built with AI help, a learning demonstration, not investment advice. It includes the current download date.

## Data and timing rules

Two separately cached functions make one request per series to each source on a cache miss:

```text
https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES
https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=SERIES&vintage_date=YYYY-MM-DD
```

No API key or account is used. Downloads are cached for one hour and keyed by today's date; changing only the chart start does not trigger another download. A period (`.`) is missing data, not zero. No interpolation, backward fill, frequency aggregation, or automatic conversion is applied. Assigned rate series use percent units; differences are percentage points (100 basis points per point). Custom series retain their source units.

Unknown IDs and network/parse failures display a series-specific error while other series continue. Invalid or unverified historical downloads never fall back to current values. ALFRED sometimes labels a request for today with its latest earlier archive date: on October 29, the DGS10 response was labelled October 28. The app accepts an explicitly dated earlier vintage, displays that archive date, and rejects a vintage later than the requested cutoff.

A monthly label such as March 1 measures a period; it does not establish publication on March 1. Daily ALFRED snapshots do not establish intraday availability. A conservative trading rule uses the preceding calendar day's information; same-day publication requires a timestamp check. ALFRED may use first availability in FRED when source release dates cannot be established, and early archive coverage may be incomplete.

Official explanations: [ALFRED help](https://alfred.stlouisfed.org/help), [real-time periods](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html), and [FRED versus ALFRED](https://fred.stlouisfed.org/docs/api/fred/fred_vs_alfred.html).

## Live evidence from the initial rates app

Downloaded October 29, 2026, with an observation window of January 1, 2025–March 31, 2026 and a March 31, 2026 snapshot:

| Series | Latest measured date present then | Value (%) | Current observations unavailable then |
|---|---|---:|---:|
| BAA | 2026-02-01 | 5.81 | 1 |
| FEDFUNDS | 2026-02-01 | 3.64 | 1 |
| DGS10 | 2026-03-30 | 4.35 | 1 |
| MORTGAGE30US | 2026-03-26 | 6.38 | 0 |

All nonmissing values on shared dates were unchanged in this particular comparison. That does not prove these series are never revised. BAA's March observation in current history was unavailable on March 31: selecting by measured date alone would introduce look-ahead bias. Comparisons, request URLs, and retrieval timestamps are saved in `rates_evidence/`.

The earlier `rates_app.py` remains available with a conservative previous-day default, comparison charts, CSV/source exports, and an eligibility explanation. `Rates README.md` documents it. The requested `asof_app.py` is the new FRED-style multi-series page and defaults to today's as-known date.

## Run commands

From `/Users/ericboyd/Fin 439`:

```sh
.venv-rates/bin/streamlit run 'Lab 15/asof_app.py' --server.headless true --server.port 8503
```

This command was executed successfully; the local app is at http://localhost:8503.

On a new setup, create a virtual environment and install `Lab 15/requirements-rates.txt`. To reproduce the checks:

```sh
cd 'Lab 15'
../.venv-rates/bin/python -m unittest test_rates -v
../.venv-rates/bin/python verify_rates_live.py
../.venv-rates/bin/python verify_asof_app.py
```

## Verification and AI disclosure

The initial engine passed three safety tests covering missing/future observations, vintage-label validation, and revision versus unavailability classification. Its four live series comparisons and default/same-day Streamlit AppTest checks passed. The new app was compiled and its Streamlit server started successfully. `verify_asof_app.py` checks all four default live series, a March 31 historical date, and isolation of a simulated unknown-ID request failure. New-app live verification results are recorded below after completion.

The new-app live checks **passed**: all four default series loaded, the historical-date view loaded, and the simulated unknown-ID failure left all four valid rows available. Today's latest observations were BAA September 1 at 6.47%, FEDFUNDS September 1 at 3.75%, DGS10 October 27 at 4.99%, and MORTGAGE30US October 29 at 7.24%.

With the new app's full histories and a March 31 cutoff, current values after the last known historical date numbered **7 BAA, 7 FEDFUNDS, 146 DGS10, and 31 MORTGAGE30US**. Shared-date revisions were zero for these downloads. These counts differ from the initial evidence table because the new app compares current history through today, rather than ending the observation window at March 31.

Codex wrote the apps, downloaded the evidence, ran automated verification, and drafted this file. Independent student verification and the final Project 2 series choice have not been recorded.

## October 5 acceptance check and PAYEMS revision probe

Ran `probe_lab17.py` against the actual Streamlit app and live public CSV downloads on October 29, 2026. All supplied expectations passed without a data-download correction:

| Series | Latest measured period/date as known October 5 | Value |
|---|---|---:|
| BAA | September 2026 | 6.47 |
| FEDFUNDS | September 2026 | 3.75 |
| DGS10 | October 2, 2026 | 5.28 |
| MORTGAGE30US | October 1, 2026 | 7.28 |

Added PAYEMS via the custom-ID input and changed the as-known date to January 15, 2025. The latest known observation was **December 2024, 159,536 thousand jobs**. Today's value for that same December was **158,316 thousand**, lower by **1,220 thousand jobs**. The app counted **381 revised shared-date values**, well above zero, confirming that the historical download differs from today's history. The revision count covers the full common downloaded history, not just dates after the chart start. Today's latest PAYEMS observation was September 2026 at 159,044 thousand; that is a different measured month and must not be used as the December revision comparison.

Added “Today's value for that same date” to the summary table so the historical latest observation can be compared directly with its current revision. The October 5 checkpoint and PAYEMS probe remain reproducible test settings. The latest exercise leaves the saved app default at today.

Reproduce from the repository root:

```sh
.venv-rates/bin/python 'Lab 15/probe_lab17.py'
```

Machine-readable results are saved in `rates_evidence/lab17_acceptance.json`. Values in that evidence reflect the retrieval date and current FRED history may change. The tests assert historical dates/values, a lower current December PAYEMS value, and more than 100 shared-date revisions. No expected observations are hard-coded into the app's downloads or display.

## Last month-end versus today

Tested September 30, 2026 (the last day of last month), then October 29, 2026 (today). BAA is already selected by its ID; it remains the provisional personal series pending confirmation of the student's prework choice.

| Series | Latest known at September 30 | Value then (%) | Latest known today | Value today (%) | Current values after the earlier last date | Shared-date revisions |
|---|---|---:|---|---:|---:|---:|
| BAA | August 2026 | 6.32 | September 2026 | 6.47 | 1 | 0 |
| FEDFUNDS | August 2026 | 3.63 | September 2026 | 3.75 | 1 | 0 |
| DGS10 | September 29 | 5.26 | October 27 | 4.99 | 19 | 0 |
| MORTGAGE30US | September 24 | 7.03 | October 29 | 7.24 | 5 | 0 |

The later observations disappear from the September 30 snapshot because they were not yet published/available then. Some measure periods after September 30 as well. BAA's September average is the clear publication-lag example: the measured month had ended, but its value was not in the snapshot. Revisions are a different question: all four had zero changed nonmissing values on shared dates in this comparison.

**DGS10 is a daily market rate with almost no publication lag (about one day here) and no observed revisions in this test.** At September 30 its latest observation was September 29. At today's retrieval, its latest measured date was October 27, with the FRED page reporting an October 28 update. The count of 19 subsequent observations is newly available daily data, not a 19-day publication lag. Zero revisions in this test is not a guarantee against future corrections.

## Data card — BAA (provisional personal choice)

| Field | Description |
|---|---|
| Series ID | BAA |
| Source and link | Moody's; distributed by FRED, Federal Reserve Bank of St. Louis: [FRED BAA](https://fred.stlouisfed.org/series/BAA). Historical versions: [ALFRED BAA](https://alfred.stlouisfed.org/series?seid=BAA). |
| What it measures | Monthly Moody's seasoned Baa corporate bond yield. FRED's notes describe bonds with maturities of 20 years and above. It is a corporate borrowing-yield indicator, not a bond total return. |
| Units / frequency | Percent; not seasonally adjusted; monthly. |
| Publication lag | September 2026 was absent September 30 and present October 5. FRED reports the September value updated October 1, 2026 at 10:31 AM CDT: approximately one calendar day after month-end for this release. This is an observed release example, not a universal fixed release rule. The September 1 label is the measured-month label, not the release date. |
| Revisions | Zero shared-date revisions between September 30's vintage and today's full history; none in the earlier March 31 and October 5 comparisons either. Treat as no revisions observed in these tests, not an immutable series. FRED states that data are subject to revision. |
| Download / page-check date | October 29, 2026. |
| Project 2 disposition | Quarantine pending verification of an eligible vintage for every trade. Admit only as a documented rate signal after that audit passes. Do not substitute it for ETF returns. Final personal-series choice is still unconfirmed. |

### Final admission statement

**Quarantine BAA:** September 2026's 6.47% was unavailable on September 30 and appeared October 1. No revisions were observed in our comparisons, but observation dates still precede availability. Admit only after every Project 2 decision uses an eligible ALFRED vintage, with publication-time evidence for same-day trades; today's history with a fixed lag is insufficient. This disposition concerns the data's eligibility for the proposed historical strategy, not a rejection of BAA as an economic indicator. BAA remains the provisional personal-series choice.

### Three values read directly against FRED

Read the observation list on the actual [BAA FRED series page](https://fred.stlouisfed.org/series/BAA), independently of the CSV parser, then checked those dates in the downloaded data:

| Measured month | FRED page (%) | App download (%) | Result |
|---|---:|---:|---|
| July 2026 | 6.19 | 6.19 | Match |
| August 2026 | 6.32 | 6.32 | Match |
| September 2026 | 6.47 | 6.47 | Match |

Also read three observations directly from the [DGS10 FRED page](https://fred.stlouisfed.org/series/DGS10): October 23 at 5.00%, October 26 at 5.00%, and October 27 at 4.99%. All three matched the download. DGS10's source is the Board of Governors of the Federal Reserve System, H.15 Selected Interest Rates; it measures a 10-year constant-maturity Treasury market yield, in percent, daily, not seasonally adjusted.

Codex performed these page readings and checks; this does not claim the student independently checked them. `probe_month_end.py` exercised both dates in Streamlit and asserted all six page-read values against the CSVs. Results are saved in `rates_evidence/month_end_probe.json`. Reproduce with `.venv-rates/bin/python 'Lab 15/probe_month_end.py'` from the repository root. The app now opens with today's as-known date, completing the requested sequence.
