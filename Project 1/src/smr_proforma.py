"""SMR Lab 09: annual-report-based, conditional services-only/wind-down case.

USD millions, shares in millions. Standard library only. Read SMR_Assumptions.md.
This is NOT a current price target or a forecast of management's intentions.
"""

from dataclasses import dataclass, replace
from pathlib import Path
import argparse


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
        raise ValueError(f"{label}: {actual:.9f} != {expected:.9f}")


def check_balance(row):
    check_close("Balance sheet", total_assets(row), total_liabilities(row) + row["equity"])


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
                   change_cash=cfo+cfi+cff, shares=SHARES)
        row["assets"] = total_assets(row)
        row["liabilities"] = total_liabilities(row)
        row["liabilities_equity"] = row["liabilities"] + row["equity"]
        row["balance_gap"] = row["assets"] - row["liabilities_equity"]
        check_balance(row)
        check_close("Cash roll-forward", row["cash"] - prior["cash"], cfo+cfi+cff)
        check_close("Equity roll-forward", row["equity"] - prior["equity"], net_income)
        check_close("PMA settlement", pma_payment + row["pma_liability"], prior["pma_liability"])
        if row["cash"] < a.minimum_cash - TOL:
            raise FundingRequired(f"{year}: cash {row['cash']:.3f} below minimum "
                                  f"{a.minimum_cash:.3f}; revise funding/share assumptions")
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
     ("Closing cash", "cash")]),
]


def render():
    a = Assumptions()
    rows = project(a)
    v = value(rows, a)
    lines = ["# SMR — Lab 09 five-year statements and conditional valuation", "",
             "**Case: services-only through 2030, followed by wind-down.** "
             "This is a downside scenario, not a probability-weighted fair value or current price target.", "",
             "Measurement date: December 31, 2025; information basis: 2025 annual report "
             "published February 26, 2026. Retrospective classroom exercise; no 2026 interim update.", "",
             "USD millions except per-share values; shares in millions. "
             "Sources, assumptions, and limitations: [SMR_Assumptions.md](SMR_Assumptions.md).", "",
             f"**Conditional value per share: ${v['per_share']:.4f} "
             f"(${v['per_share']:.2f} rounded).** Present equity value: ${v['equity_value']:.3f} million.", ""]
    for title, fields in TABLES:
        lines += [f"## {title}", "", "| USD millions | " + " | ".join(str(r['year']) for r in rows) + " |",
                  "|---|" + "---:|" * len(rows)]
        for label, key in fields:
            lines.append(f"| {label} | " + " | ".join(f"{0.0 if abs(r[key]) < TOL else r[key]:,.3f}" for r in rows) + " |")
        lines.append("")
    lines += ["## Valuation bridge", "",
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = render()
    print(report)
    if args.write_report:
        Path(__file__).with_name("SMR_Five_Year_Results.md").write_text(report)


if __name__ == "__main__":
    main()
