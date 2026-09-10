# NuScale Power (NYSE: SMR) — DCF Inputs

**Filing used:** NuScale Power Corporation 2025 Form 10-K, filed February 26, 2026. Dollar figures are in millions unless stated otherwise.

**Market price:** **$10.81 per share**, September 9, 2026 closing price (the latest completed trading day available when checked on September 10, 2026).

## Value-to-price check

**DCF value per share: -$40.5535 | Latest available market price: $10.81**

The DCF value is **outside 0.5x to 2x** today's latest available price. No inputs were adjusted. The one input I distrust most is **starting FCFF (-$460.118 million)** because 2025 operating cash flow includes unusually large commercialization payments, including a $247.5 million milestone contribution. That makes one year's negative cash flow a weak normalized base for a perpetual-growth DCF.

## Sensitivity and reverse DCF

The training case was tested first using its original inputs and a $30.00 target. Its nine sensitivity values matched the provided table cell for cell, and the reverse DCF solved to a **+1.7779 percentage-point uniform shift** across all five explicit growth rates.

For SMR, the growth path and WACC are unresolved, so the script retains **8%, 6%, 5%, 4%, 3% growth and 10% WACC as training placeholders**. With the $10.81 target price, the reverse DCF finds **no solution within the permitted -5 to +10 percentage-point shift bracket**. It holds starting FCFF, WACC, terminal growth, non-operating cash, debt, and diluted shares fixed. This reverse DCF is only a search for one assumption set consistent with the price; it is not proof that SMR is mispriced.

## Conditional call

**Watch-defer. Initiate if SMR establishes a sustainable positive normalized FCFF base and a sourced scenario DCF then supports value above the market price; otherwise remain on the watchlist. Monitor: quarterly operating cash burn.**

| Input | SMR value | Where SMR's value comes from |
|---|---:|---|
| Starting FCFF | **-$460.118 million** | 2025 Consolidated Statement of Cash Flows: operating cash flow **-$459.610M** + after-tax interest paid **$0** - capital expenditures **$0.508M**. |
| Growth, Years 1-5 | **Unresolved; placeholders: 8%, 6%, 5%, 4%, 3%** | Item 7 shows unstable performance: revenue grew 62.4% in 2024 and declined 15.0% in 2025. SMR has negative FCFF and gives no dependable five-year FCFF forecast, so the training values remain in `dcf.py` and are marked as placeholders. |
| WACC | **Unresolved; placeholder: 10%** | SMR reports no debt, so WACC is approximately its cost of equity. Beta and the valuation-date risk-free rate are external market inputs not supplied by the 10-K; the training value remains in `dcf.py` and is marked as a placeholder. |
| Terminal growth | **3.0% forecast assumption** | Long-run nominal economic growth rather than SMR's historical growth. This assumption is only economically meaningful after SMR reaches stable, positive FCFF. |
| Cash / debt / diluted shares | **$836.417M / $0 / 163.731673M** | Balance-sheet cash and cash equivalents; management reports no debt; the EPS note reports 163,731,673 weighted-average basic and diluted Class A shares for 2025. |

## Sources and cautions

- [NuScale Power 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)
- [SMR historical price data](https://stockanalysis.com/stocks/smr/history/)
- SMR also reported $450.8 million of liquid investments, but the input above follows the requested cash figure and does not add those investments.
- Because starting FCFF is negative and the growth rates and WACC are placeholders, the script's output is a mechanical course result, not a defensible price target.
