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
