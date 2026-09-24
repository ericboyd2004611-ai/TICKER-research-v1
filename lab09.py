"""FIN 439 — Week 5, Lab 09: Defensible valuation and statement checks."""


def print_lab09_notes():
    print("Week 5 — Lab 09: Valuation and Financial Statement Verification")
    print(
        """
What are five years of a company's statements worth, built from assumptions
you can defend, and how do you know the statements are right?

Five years of historical statements provide the foundation for a valuation.
A company's value comes from its future cash flows, discounted for risk.

1. Verify the historical statements.
   Trace figures to audited filings and footnotes. Check that assets equal
   liabilities plus equity, ending cash reconciles to the balance sheet,
   and net income reconciles to operating cash flow. Keep reporting periods,
   units, and accounting definitions consistent. These checks support
   reliability, but do not guarantee that every reported figure is correct.

2. Defend the forecast assumptions.
   Support revenue growth, margins, taxes, capital spending, and working
   capital with historical performance and business evidence. Separate
   reported facts from forecasts and identify unresolved assumptions.

3. Forecast five years of free cash flow to the firm.
   FCFF = EBIT * (1 - tax rate) + depreciation and amortization
          - capital expenditures - increase in operating working capital.

4. Calculate enterprise and equity value.
   Enterprise value = present value of forecast FCFF
                      + present value of terminal value.
   For a stable-growth terminal model:
   Terminal value at year 5 = FCFF year 6 / (WACC - terminal growth).
   Terminal growth must be below WACC, and the terminal business must be
   in a defensible steady state.
   Equity value = enterprise value + nonoperating cash
                  - debt - other relevant claims.
   Value per share = equity value / appropriate diluted share count.

5. Challenge the result.
   Test scenarios and sensitivity to WACC, growth, and operating assumptions.
   Examine how much enterprise value depends on the terminal value.

Connection to the current Week 3 model:
The observed value per share was -$40.5535. Growth rates and WACC were still
marked as placeholders. Positive growth applied to negative starting FCFF
makes cash flow more negative, and the terminal model perpetuates losses.
This is a mechanical result, not yet a defensible valuation. A supported
operating forecast must explain whether and how positive cash flow is reached.
Running successfully confirms execution; it does not validate the inputs
or prove that the financial statements are correct.

Three judgments: asset productivity, replacement cost, and reinvestment rate.

Asset Productivity (Earning Power):
You must judge how efficiently the company's existing assets generate revenue
and operating cash flows. This determines whether the assets are worth more
than their book value.

Replacement Cost:
You must estimate what it would actually cost to replicate the asset base
in the current market. This adjusts for inflation, technological obsolescence,
and depreciation.

Reinvestment Rate (Growth Potential):
You must judge the company's ability to deploy future capital into high-return
assets. Growth only adds value if the return on these new assets exceeds
the cost of capital.
""".strip()
    )


# ============================================================================
# ABG PRO FORMA — assumptions, projections, checks, and valuation
# ============================================================================

"""ABG five-year pro forma. Standard library only; USD millions except per share.

Inputs transcribed from the supplied lab assumption table. Historical ratios
retain their exact arithmetic; source labels are those supplied in the table.
"""

YEARS = range(2026, 2031)
GROWTH = 0.018  # judgment
GROSS_MARGIN = 0.1705  # judgment
SGA_RATIOS = (0.665, 0.655, 0.645, 0.645, 0.645)  # judgment
DEPRECIATION_RATIO = 82.4 / 3070.4  # history
IMPAIRMENT = 120.0  # judgment, noncash
CAPEX = 250.0  # guidance
TAX_RATE = 0.255  # judgment
INVENTORY_DAYS = 2135.8 / (17999.0 - 3071.7) * 365  # history
FLOOR_PLAN_RATIO = 2027.0 / 2135.8  # history
OTHER_WC_RATE = 0.008  # judgment: fraction of change in revenue
MIN_CASH = 25.0  # history
REVOLVER_LIMIT = 850.0  # judgment
REVOLVER_RATE = 0.06  # judgment
DEBT_REPAYMENT = 150.0  # judgment
BUYBACK = 150.0  # judgment
FLOOR_PLAN_RATE = 0.0467  # history
DEBT_RATE = 0.0544  # history
COST_OF_EQUITY = 0.10  # judgment
TERMINAL_GROWTH = 0.025  # judgment
SHARES = 17.951349  # million; supplied label: 10-Q, June 30, 2026
OPENING = {
    "revenue": 17999.0,
    "inventory": 2135.8,
    "ppe": 3070.4,
    "other_assets": 6371.6,
    "cash": 40.4,
    "floor_plan": 2027.0,
    "debt": 3572.0,
    "other_liabilities": 2127.5,
    "equity": 3891.7,
    "revolver": 0.0,
}
TOLERANCE = 1e-7


def balance_gap(statement):
    return (
        statement["cash"] + statement["inventory"] + statement["ppe"]
        + statement["other_assets"] - statement["floor_plan"]
        - statement["debt"] - statement["revolver"]
        - statement["other_liabilities"] - statement["equity"]
    )


def assert_balanced(year, statement):
    """Reject an unbalanced statement or infeasible cash/revolver balance."""
    gap = balance_gap(statement)
    if abs(gap) > TOLERANCE:
        raise ValueError(f"{year}: balance sheet gap = {gap:.8f} million")
    shortfall = MIN_CASH - statement["cash"]
    if shortfall > TOLERANCE:
        raise ValueError(f"{year}: minimum cash gap = {shortfall:.8f} million")
    excess = statement["revolver"] - REVOLVER_LIMIT
    if excess > TOLERANCE:
        raise ValueError(f"{year}: revolver limit gap = {excess:.8f} million")


def project():
    prior = OPENING.copy()
    assert_balanced(2025, prior)
    results = []
    for year, sga_ratio in zip(YEARS, SGA_RATIOS):
        revenue = prior["revenue"] * (1 + GROWTH)
        gross_profit = revenue * GROSS_MARGIN
        sga = gross_profit * sga_ratio
        depreciation = prior["ppe"] * DEPRECIATION_RATIO
        operating_income = gross_profit - sga - depreciation - IMPAIRMENT
        interest = (prior["floor_plan"] * FLOOR_PLAN_RATE
                    + prior["debt"] * DEBT_RATE
                    + prior["revolver"] * REVOLVER_RATE)
        pretax = operating_income - interest
        tax = max(0.0, pretax) * TAX_RATE
        net_income = pretax - tax

        inventory = (revenue - gross_profit) * INVENTORY_DAYS / 365
        floor_plan = inventory * FLOOR_PLAN_RATIO
        ppe = prior["ppe"] + CAPEX - depreciation
        change_other_wc = OTHER_WC_RATE * (revenue - prior["revenue"])
        other_assets = prior["other_assets"] + change_other_wc - IMPAIRMENT
        debt = prior["debt"] - DEBT_REPAYMENT
        equity = prior["equity"] + net_income - BUYBACK
        change_inventory = inventory - prior["inventory"]
        change_floor_plan = floor_plan - prior["floor_plan"]
        fcfe = (net_income + depreciation + IMPAIRMENT - CAPEX
                - change_inventory - change_other_wc + change_floor_plan
                - DEBT_REPAYMENT)

        cash_before_revolver = prior["cash"] + fcfe - BUYBACK
        if cash_before_revolver < MIN_CASH:
            revolver_change = min(
                MIN_CASH - cash_before_revolver,
                REVOLVER_LIMIT - prior["revolver"],
            )
        else:
            revolver_change = -min(
                cash_before_revolver - MIN_CASH, prior["revolver"]
            )
        cash = cash_before_revolver + revolver_change
        revolver = prior["revolver"] + revolver_change
        operating_cash = (net_income + depreciation + IMPAIRMENT
                          - change_inventory - change_other_wc)
        financing_cash = (change_floor_plan - DEBT_REPAYMENT - BUYBACK
                          + revolver_change)
        row = {
            "year": year, "revenue": revenue,
            "cost_of_sales": revenue - gross_profit,
            "gross_profit": gross_profit, "sga": sga,
            "depreciation": depreciation, "impairment": IMPAIRMENT,
            "operating_income": operating_income, "interest": interest,
            "pretax": pretax, "tax": tax, "net_income": net_income,
            "inventory": inventory, "floor_plan": floor_plan,
            "ppe": ppe, "other_assets": other_assets, "debt": debt,
            "other_liabilities": prior["other_liabilities"], "equity": equity,
            "cash": cash, "revolver": revolver,
            "total_assets": cash + inventory + ppe + other_assets,
            "total_liabilities": floor_plan + debt + revolver
                                 + prior["other_liabilities"],
            "total_le": floor_plan + debt + revolver
                        + prior["other_liabilities"] + equity,
            "inventory_cash": -change_inventory,
            "other_wc_cash": -change_other_wc,
            "operating_cash": operating_cash, "capex_cash": -CAPEX,
            "floor_plan_cash": change_floor_plan,
            "repayment_cash": -DEBT_REPAYMENT, "repayment": DEBT_REPAYMENT,
            "buyback_cash": -BUYBACK, "revolver_cash": revolver_change,
            "financing_cash": financing_cash,
            "change_cash": operating_cash - CAPEX + financing_cash,
            "opening_cash": prior["cash"], "fcfe": fcfe,
        }
        row["balance_gap"] = balance_gap(row)
        results.append(row)
        prior = row
    return results


def print_table(title, fields, results):
    print(f"\n{title} (USD millions)")
    print(f"{'':36}" + "".join(f"{r['year']:>13}" for r in results))
    for label, key in fields:
        print(f"{label:36}" + "".join(f"{r[key]:13,.1f}" for r in results))


def print_proforma():
    results = project()
    print_table("INCOME STATEMENT", [
        ("Revenue", "revenue"), ("Cost of sales", "cost_of_sales"),
        ("Gross profit", "gross_profit"), ("SG&A", "sga"),
        ("Depreciation", "depreciation"), ("Impairment", "impairment"),
        ("Operating income", "operating_income"), ("Interest expense", "interest"),
        ("Pretax income", "pretax"), ("Tax", "tax"), ("Net income", "net_income"),
    ], results)
    print_table("BALANCE SHEET", [
        ("Cash", "cash"), ("Inventory", "inventory"), ("PP&E", "ppe"),
        ("Other assets", "other_assets"), ("Total assets", "total_assets"),
        ("Floor plan", "floor_plan"), ("Term debt", "debt"),
        ("Revolver", "revolver"), ("Other liabilities", "other_liabilities"),
        ("Total liabilities", "total_liabilities"), ("Equity", "equity"),
        ("Total liabilities and equity", "total_le"),
    ], results)
    print_table("CASH FLOW STATEMENT", [
        ("Net income", "net_income"), ("Add depreciation", "depreciation"),
        ("Add impairment", "impairment"), ("Inventory cash movement", "inventory_cash"),
        ("Other working capital movement", "other_wc_cash"),
        ("Operating cash flow", "operating_cash"), ("Investing: capex", "capex_cash"),
        ("Floor plan movement", "floor_plan_cash"),
        ("Term debt repayment", "repayment_cash"), ("Share buyback", "buyback_cash"),
        ("Revolver draw / (repayment)", "revolver_cash"),
        ("Financing cash flow", "financing_cash"), ("Net change in cash", "change_cash"),
        ("Opening cash", "opening_cash"), ("Closing cash", "cash"),
        ("FCFE before buyback / revolver", "fcfe"),
    ], results)

    print("\nCHECKS (USD millions; computed with unrounded values)")
    for row in results:
        gap = row["balance_gap"]
        displayed_gap = 0.0 if abs(gap) <= TOLERANCE else gap
        cash_ok = row["cash"] >= MIN_CASH - TOLERANCE
        print(f"{row['year']}: assets - liabilities - equity = {displayed_gap:.1f}; "
              f"cash {row['cash']:.1f} >= {MIN_CASH:.1f}: "
              f"{'PASS' if cash_ok else 'FAIL'}")
        assert_balanced(row["year"], row)

    if COST_OF_EQUITY <= TERMINAL_GROWTH:
        raise ValueError("Cost of equity must exceed terminal growth")
    if SHARES <= 0:
        raise ValueError("Share count must be positive")
    pv_fcfe = sum(row["fcfe"] / (1 + COST_OF_EQUITY) ** t
                  for t, row in enumerate(results, start=1))
    last = results[-1]
    terminal_value = ((last["fcfe"] + last["repayment"])
                      * (1 + TERMINAL_GROWTH)
                      / (COST_OF_EQUITY - TERMINAL_GROWTH))
    pv_terminal = terminal_value / (1 + COST_OF_EQUITY) ** 5
    equity_value = pv_fcfe + pv_terminal
    print("\nEQUITY VALUATION")
    print(f"Equity value (USD millions): {equity_value:,.2f}")
    if equity_value == 0:
        print("Share of value after 2030: undefined (zero equity value)")
    else:
        print(f"Share of value after 2030: {pv_terminal / equity_value:.2%}")
    print(f"Value per share: ${equity_value / SHARES:,.2f}")


def main():
    print_lab09_notes()
    print_proforma()


if __name__ == "__main__":
    main()
