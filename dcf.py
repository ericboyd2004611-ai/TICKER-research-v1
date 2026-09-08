"""FIN 43900 — 5-Year FCFF DCF Valuation Engine
Implements the course training case using only Python's standard library.
"""

import sys

# ==============================================================================
# INPUTS (Edit these values by hand)
# ==============================================================================
STARTING_FCFF = 100.0        # Free cash flow to firm in base year (USD millions)
GROWTH_RATES = [
    0.08,                     # Year 1 growth rate (decimal)
    0.06,                     # Year 2 growth rate (decimal)
    0.05,                     # Year 3 growth rate (decimal)
    0.04,                     # Year 4 growth rate (decimal)
    0.03,                     # Year 5 growth rate (decimal)
]
WACC = 0.10                  # Weighted Average Cost of Capital (decimal)
TERMINAL_GROWTH = 0.03       # Long-run terminal growth rate (decimal)
NON_OPERATING_CASH = 50.0    # Cash and short-term liquid investments (USD millions)
DEBT = 300.0                 # Total debt and debt-like claims (USD millions)
DILUTED_SHARES = 50.0        # Diluted common shares count (millions of shares)
# ==============================================================================


def run_dcf():
    # Boundary check: terminal growth must be strictly less than WACC
    if TERMINAL_GROWTH >= WACC:
        sys.exit(
            f"Error: Terminal growth ({TERMINAL_GROWTH:.4f}) must be strictly less than "
            f"WACC ({WACC:.4f}). A terminal growth rate >= WACC implies infinite value "
            f"or causes division by zero."
        )

    if DILUTED_SHARES <= 0:
        sys.exit("Error: Diluted common shares must be positive.")

    # 1. Project explicit FCFF for Years 1 through 5
    fcff_years = []
    current_fcff = STARTING_FCFF
    for g in GROWTH_RATES:
        current_fcff = current_fcff * (1.0 + g)
        fcff_years.append(current_fcff)

    # 2. Discount explicit FCFF to present value
    pv_explicit = sum(cf / ((1.0 + WACC) ** (i + 1)) for i, cf in enumerate(fcff_years))

    # 3. Terminal value at the end of Year 5 (Gordon Growth Model)
    # TV_5 = FCFF_5 * (1 + g) / (WACC - g)
    tv_5 = fcff_years[-1] * (1.0 + TERMINAL_GROWTH) / (WACC - TERMINAL_GROWTH)

    # 4. Present value of terminal value (discounted 5 years back to Year 0)
    pv_tv = tv_5 / ((1.0 + WACC) ** 5)

    # 5. Enterprise value = sum of PV of explicit cash flows + PV of terminal value
    enterprise_value = pv_explicit + pv_tv

    # 6. Equity value = Enterprise value + non-operating cash - debt
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT

    # 7. Per-share value = Equity value / diluted shares
    value_per_share = equity_value / DILUTED_SHARES

    # 8. Terminal value share of enterprise value
    tv_share = pv_tv / enterprise_value if enterprise_value != 0 else 0.0

    # Print the twelve required labeled lines formatted to four decimals
    print(f"FCFF Year 1: {fcff_years[0]:.4f}")
    print(f"FCFF Year 2: {fcff_years[1]:.4f}")
    print(f"FCFF Year 3: {fcff_years[2]:.4f}")
    print(f"FCFF Year 4: {fcff_years[3]:.4f}")
    print(f"FCFF Year 5: {fcff_years[4]:.4f}")
    print(f"PV of explicit FCFF: {pv_explicit:.4f}")
    print(f"Terminal value at Year 5: {tv_5:.4f}")
    print(f"PV of terminal value: {pv_tv:.4f}")
    print(f"Enterprise value: {enterprise_value:.4f}")
    print(f"Equity value: {equity_value:.4f}")
    print(f"Value per diluted share: {value_per_share:.4f}")
    print(f"PV of terminal value as share of EV: {tv_share:.4f}")


if __name__ == "__main__":
    run_dcf()
