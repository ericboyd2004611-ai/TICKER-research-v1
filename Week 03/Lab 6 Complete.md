# NuScale Power (NYSE: SMR) — DCF and Reverse DCF Report

**Valuation review date:** September 10, 2026  
**Financial-statement date:** December 31, 2025  
**Filing:** NuScale Power Corporation 2025 Form 10-K, filed February 26, 2026  
**Latest completed-day price used:** **$10.81 per share at the September 9, 2026 close**

Dollar amounts are in millions except per-share values. Reported facts, estimates, placeholders, and decision rules are labelled separately below.

## 1. Training-case validation

The training case uses its original inputs and a **$30.00 target price**.

| WACC \ terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| 9% | $28.60 | $32.94 | $39.02 |
| 10% | $24.36 | **$27.50** | $31.69 |
| 11% | $21.06 | $23.41 | $26.44 |

The grid matches the supplied training table cell for cell. Its base case is the center cell, **$27.50**. Value falls moving down as WACC rises and increases moving right as terminal growth rises. The corner-derived sensitivity range is **$21.06 to $39.02 per diluted share**.

The training reverse DCF solves for one variable: a uniform shift added to all five explicit growth rates. The solved shift is **+1.7779 percentage points**, approximately **+1.78 points**, to reach $30.00. Starting FCFF, WACC, terminal growth, non-operating cash, debt, and diluted shares are held fixed.

## 2. SMR inputs and sources

| Input | Value used | Classification | Exact locator and as-of date |
|---|---:|---|---|
| Starting FCFF | **-$460.118** | Reported inputs; calculated result | For the year ended **December 31, 2025**: operating cash flow of -$459.610 and purchases of property, plant and equipment of $0.508, from the 10-K **Consolidated Statements of Cash Flows, pages F-7 to F-8**. Management reports no debt, so the after-tax interest add-back is $0. Calculation: `-$459.610 + $0 - $0.508 = -$460.118`. |
| Growth, Years 1-5 | **8%, 6%, 5%, 4%, 3%** | **Unresolved; training placeholders retained** | Reviewed as of **September 10, 2026**. The 10-K **Item 7, MD&A, Results of Operations, pages 35-36** reports revenue of $22.810 in 2023, $37.045 in 2024, and $31.479 in 2025. That is +62.4% and then -15.0%, and the filing supplies no dependable five-year FCFF path. |
| WACC | **10%** | **Unresolved; training placeholder retained** | Reviewed as of **September 10, 2026**. The 10-K **Item 7, Liquidity and Capital Resources, page 38** says SMR had no debt at December 31, 2025. Beta and a valuation-date risk-free rate are not supplied in the filing, so a company-specific WACC was not fabricated. |
| Terminal growth | **3.0%** | **Forecast assumption, not a reported company fact** | Assumption as of **September 10, 2026**, representing long-run nominal economic growth rather than SMR's historical growth. It would be economically appropriate only after positive, stable FCFF is reached. |
| Non-operating cash | **$836.417** | Reported fact | As of **December 31, 2025**, from the 10-K **Consolidated Balance Sheets, page F-4**, “Cash and cash equivalents.” The model does not add the separately reported investments. |
| Debt | **$0** | Reported fact | As of **December 31, 2025**, from the 10-K **Item 7, Liquidity and Capital Resources, page 38**, which states the company had no debt. |
| Diluted shares | **163.731673** | Reported fact; loss-year EPS convention | For the year ended **December 31, 2025**, from **Note 3, Equity and Loss Per Share, page F-16**: weighted-average shares for basic and diluted loss per share. Potential shares were anti-dilutive because SMR reported a loss. |
| Market price | **$10.81** | Market fact | **September 9, 2026 closing price**, retrieved September 10, 2026 from the linked historical-price source below. |

## 3. SMR sensitivity grid and direction

| WACC \ terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| 9% | -$42.10 | -$48.20 | -$56.75 |
| 10% | -$36.14 | **-$40.55** | -$46.44 |
| 11% | -$31.51 | -$34.82 | -$39.07 |

The base case is the center cell, **-$40.55 per diluted share**. The corner-derived range is **-$56.75 to -$31.51**. Because the starting FCFF is negative, the usual direction does not hold: the calculated value becomes more negative moving right as terminal growth rises, and less negative moving down as WACC rises. This reversal is a model warning, not an economic claim that higher WACC creates value.

## 4. SMR reverse DCF

The target is the **$10.81** market price. The solved variable is a uniform shift added to all five explicit growth rates. The search correctly reports **no solution inside the permitted -5 to +10 percentage-point bracket**; it does not report a boundary as though it were an answer.

Held fixed: **starting FCFF of -$460.118, WACC of 10% (training placeholder), terminal growth of 3%, non-operating cash of $836.417, debt of $0, and diluted shares of 163.731673**.

A reverse DCF identifies, when a solution exists, one set of assumptions consistent with the target price. It is **not proof of mispricing**. Here, the absence of a solution in the specified bracket shows that this particular negative-FCFF model and restricted growth-shift test cannot reproduce the market price.

## 5. Reasonableness check

**DCF value per share: -$40.5535 | Market price: $10.81**

The DCF result is outside the stated **0.5x to 2x price band**. No input was changed to force agreement. The input I distrust most is **starting FCFF**: 2025 operating cash flow includes unusual commercialization cash uses, including a $247.5 milestone contribution described in **Item 7, Liquidity and Capital Resources, page 38**. Therefore, one year's negative reported FCFF is not a credible normalized base for a perpetual-growth DCF.

## 6. Conditional call

**Watch-defer. Initiate if SMR reports positive net cash provided by operating activities for two consecutive fiscal quarters; otherwise remain on the watchlist. Monitor: quarterly operating cash flow.**

This is a forward-looking decision rule, not a claim that SMR has already achieved positive operating cash flow.

## Sources

- [NuScale Power 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm)
- [SMR historical price data](https://stockanalysis.com/stocks/smr/history/)
- Model output: `python dcf.py` in the Week 03 folder.
