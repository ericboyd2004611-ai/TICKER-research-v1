"""FIN 43900 — 5-Year FCFF DCF Valuation Engine
Implements the course training case using only Python's standard library.
"""

import sys

# ==============================================================================
# INPUTS (Edit these values by hand)
# ==============================================================================
STARTING_FCFF = -460.118     # SMR 2025 FCFF: CFO + after-tax interest - capex (USD millions)
GROWTH_RATES = [
    0.08,                     # PLACEHOLDER: unresolved; training value retained
    0.06,                     # PLACEHOLDER: unresolved; training value retained
    0.05,                     # PLACEHOLDER: unresolved; training value retained
    0.04,                     # PLACEHOLDER: unresolved; training value retained
    0.03,                     # PLACEHOLDER: unresolved; training value retained
]
WACC = 0.10                  # PLACEHOLDER: unresolved; training value retained
TERMINAL_GROWTH = 0.03       # Forecast: long-run nominal economic growth (decimal)
NON_OPERATING_CASH = 836.417 # Cash and cash equivalents at 2025-12-31 (USD millions)
DEBT = 0.0                   # SMR reported no debt at 2025-12-31 (USD millions)
DILUTED_SHARES = 163.731673  # 2025 diluted weighted-average Class A shares (millions)
# ==============================================================================

# Sensitivity and reverse-DCF controls (edit these values by hand)
SENSITIVITY_WACCS = [0.09, 0.10, 0.11]
SENSITIVITY_TERMINAL_GROWTH_RATES = [0.02, 0.03, 0.04]
TARGET_SHARE_PRICE = 10.81
REVERSE_SHIFT_LOWER = -0.05  # -5 percentage points
REVERSE_SHIFT_UPPER = 0.10   # +10 percentage points


def calculate_dcf(growth_rates, wacc, terminal_growth):
    """Return the DCF components without printing them."""
    fcff_years = []
    current_fcff = STARTING_FCFF
    for growth_rate in growth_rates:
        current_fcff = current_fcff * (1.0 + growth_rate)
        fcff_years.append(current_fcff)

    pv_explicit = sum(
        cash_flow / ((1.0 + wacc) ** (year + 1))
        for year, cash_flow in enumerate(fcff_years)
    )
    terminal_value = (
        fcff_years[-1]
        * (1.0 + terminal_growth)
        / (wacc - terminal_growth)
    )
    pv_terminal_value = terminal_value / ((1.0 + wacc) ** 5)
    enterprise_value = pv_explicit + pv_terminal_value
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
    value_per_share = equity_value / DILUTED_SHARES

    return {
        "fcff_years": fcff_years,
        "pv_explicit": pv_explicit,
        "terminal_value": terminal_value,
        "pv_terminal_value": pv_terminal_value,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
    }


def print_sensitivity_grid():
    """Print value per share for each valid WACC/terminal-growth pair."""
    print("\nSensitivity grid — value per diluted share ($)")
    first_column_width = 8
    value_column_width = 12
    header = "WACC \\ g".ljust(first_column_width)
    header += "".join(
        f"{terminal_growth:.0%}".rjust(value_column_width)
        for terminal_growth in SENSITIVITY_TERMINAL_GROWTH_RATES
    )
    print(header)

    for wacc in SENSITIVITY_WACCS:
        row = f"{wacc:.0%}".ljust(first_column_width)
        for terminal_growth in SENSITIVITY_TERMINAL_GROWTH_RATES:
            if terminal_growth >= wacc:
                cell = "invalid"
            else:
                result = calculate_dcf(GROWTH_RATES, wacc, terminal_growth)
                cell = f"{result['value_per_share']:.2f}"
            row += cell.rjust(value_column_width)
        print(row)


def shifted_value_per_share(shift):
    """Value per share after adding a uniform shift to all explicit growth rates."""
    shifted_growth_rates = [growth_rate + shift for growth_rate in GROWTH_RATES]
    if any(growth_rate <= -1.0 for growth_rate in shifted_growth_rates):
        raise ValueError("A shifted annual growth rate is -100% or below.")
    return calculate_dcf(shifted_growth_rates, WACC, TERMINAL_GROWTH)[
        "value_per_share"
    ]


def print_reverse_dcf():
    """Solve for a uniform explicit-growth shift using bounded bisection."""
    print("\nReverse DCF — uniform shift to all five explicit growth rates")
    print(f"Target share price: ${TARGET_SHARE_PRICE:.4f}")
    print(
        "Held fixed: starting FCFF, WACC, terminal growth, "
        "non-operating cash, debt, and diluted shares"
    )
    print(
        "Bracket: "
        f"{REVERSE_SHIFT_LOWER:+.2%} to {REVERSE_SHIFT_UPPER:+.2%}"
    )

    shifted_at_lower = [g + REVERSE_SHIFT_LOWER for g in GROWTH_RATES]
    shifted_at_upper = [g + REVERSE_SHIFT_UPPER for g in GROWTH_RATES]
    if any(g <= -1.0 for g in shifted_at_lower + shifted_at_upper):
        print("Solved shift: no solution — bracket creates growth of -100% or below")
        return

    lower = REVERSE_SHIFT_LOWER
    upper = REVERSE_SHIFT_UPPER
    lower_difference = shifted_value_per_share(lower) - TARGET_SHARE_PRICE
    upper_difference = shifted_value_per_share(upper) - TARGET_SHARE_PRICE

    if lower_difference == 0.0:
        solved_shift = lower
    elif upper_difference == 0.0:
        solved_shift = upper
    elif lower_difference * upper_difference > 0.0:
        print("Solved shift: no solution in the stated bracket")
        return
    else:
        for _ in range(100):
            midpoint = (lower + upper) / 2.0
            midpoint_difference = (
                shifted_value_per_share(midpoint) - TARGET_SHARE_PRICE
            )
            if abs(midpoint_difference) < 1e-10:
                lower = midpoint
                upper = midpoint
                break
            if lower_difference * midpoint_difference <= 0.0:
                upper = midpoint
            else:
                lower = midpoint
                lower_difference = midpoint_difference
        solved_shift = (lower + upper) / 2.0

    solved_value = shifted_value_per_share(solved_shift)
    print(f"Solved shift: {solved_shift:+.4%}")
    print(f"Solved value per diluted share: ${solved_value:.4f}")


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

    result = calculate_dcf(GROWTH_RATES, WACC, TERMINAL_GROWTH)
    fcff_years = result["fcff_years"]
    pv_explicit = result["pv_explicit"]
    tv_5 = result["terminal_value"]
    pv_tv = result["pv_terminal_value"]
    enterprise_value = result["enterprise_value"]
    equity_value = result["equity_value"]
    value_per_share = result["value_per_share"]

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
    print_sensitivity_grid()
    print_reverse_dcf()


if __name__ == "__main__":
    run_dcf()
