# Starting-point research — AI-generated draft

Prepared October 19, 2026 by Codex. Student review and acceptance pending.
Proposed final analysis boundary: September 1, 2026 market close. This is later
than the lab's 2:34 PM timestamp; it does not reconstruct Edition A's information.

## Source ledger

Amounts: USD millions except actual shares. [June 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm).

| Observation | Value | Locator |
|---|---:|---|
| Cash | 766.460 | p. 1 |
| Short-term investments | 305.688 | p. 1 |
| Investments | 820.849 | p. 1 |
| Restricted: CFPP / Houston | 5.100 / 4.463 | Note 2 |
| Debt | 0 | MD&A liquidity |
| Liabilities | 35.536 | p. 1 |
| Commitments | 168.383 | Note 16 |
| PMA accrued | 0 | Note 9 |
| H1 CFO | -372.860 | p. 5 |
| H1 PMA settlement | 259.884 | Note 9 |
| June Class A | 410,367,790 | Note 3 |
| June LLC units | 19,333,750 | Note 3 |
| Options / RSUs | 4,496,162 / 4,940,900 | Note 3 |
| July 30 Class A | 410,389,522 | Cover |

Unaccrued future PMA obligations remain possible. Class B voting stock adds no
separate economics beyond paired LLC units. Source: Notes 3 and 9 above.

[September 1 close: $9.21](https://stockanalysis.com/stocks/smr/history/),
[cross-check](https://ca.finance.yahoo.com/quote/SMR/history/).
Volume differs across providers; price agrees.

## Calculations and modeling decisions

Run `python3 research_bridge.py` from Project 1. Exact inputs and generated
calculations are in `data/research-inputs.json` and `output/research-bridge.json`.
The script adds three nonoverlapping asset categories to obtain 1,892.997.
It excludes both restricted balances without subtracting them again.

The June economic denominator is 429,701,540. Adding all options and RSUs gives
439,138,602, a deliberately gross award allowance with no exercise proceeds.
It is not a measured fully diluted September denominator. Option exercise prices,
award terms, intervening issuance and exchanges still need reconciliation.

Multiplying June interests by the September price is an explicitly stale-share
diagnostic. The cash-adjusted output is not enterprise value: it has not resolved
lease treatment, operating cash needs, contingent claims, or post-June spending.
Do not deduct all commitments while also forecasting the same operating spending.
Do not deduct book NCI again when valuing consolidated interests on an if-converted basis.

Removing one identified settlement from historical CFO is a diagnostic only;
it does not turn the remaining cash use into normalized FCFF or establish runway.

## Remaining verification before a decision-grade bridge

- Inspect filings and announcements through the chosen September close; the
  present review does not certify completeness of intervening disclosures.
- Roll cash, investments and operating liabilities forward or explicitly retain
  the last-reported basis and assess the lag. Do not invent September balances.
- Map lease, tax-agreement and commercialization claims to forecast cash flows.
- Reconcile share/award changes through the boundary and model future financing.
- Build operating value from explicit scenarios before producing a price target.
