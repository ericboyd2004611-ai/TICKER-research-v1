"""AI-generated draft: transparent arithmetic, not a completed valuation."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    inputs = json.loads((HERE / 'data/research-inputs.json').read_text())
    money, shares = inputs['usd_millions'], inputs['shares']
    liquidity = sum(money[k] for k in ('cash', 'short_term_investments', 'investments'))
    economic = shares['class_a'] + shares['exchangeable_llc_units']
    gross_awards = economic + shares['options'] + shares['rsus']
    # Both market-cap figures use the same traded Class A price as an explicit proxy.
    # Neither subtracts book NCI after including exchangeable economic interests.
    output = {
        'label': inputs['label'],
        'inputs': inputs,
        'reported_unrestricted_cash_and_investments_m': round(liquidity, 6),
        'economic_shares_before_awards': economic,
        'gross_award_share_proxy': gross_awards,
        'june_class_a_market_cap_proxy_m': shares['class_a'] / 1e6 * inputs['price_usd'],
        'june_if_converted_market_value_proxy_m': economic / 1e6 * inputs['price_usd'],
        'gross_award_market_value_proxy_m': gross_awards / 1e6 * inputs['price_usd'],
        'cash_adjusted_if_converted_market_value_proxy_m':
            economic / 1e6 * inputs['price_usd'] - liquidity,
        'h1_cash_use_excluding_identified_pma_settlement_m':
            -money['first_half_operating_cash_flow'] - money['first_half_pma_settlement'],
        'status': 'DIAGNOSTIC_ONLY_NOT_ENTERPRISE_VALUE_OR_FAIR_VALUE',
    }
    assert abs(liquidity - 1892.997) < 1e-8
    assert economic == 429701540
    assert gross_awards == 439138602
    # Restricted cash is outside the selected asset categories; do not subtract it twice.
    assert liquidity > 0 and gross_awards > economic > shares['class_a']
    (HERE / 'output/research-bridge.json').write_text(json.dumps(output, indent=2) + '\n')
    print(f'Cash and investments: USD {liquidity:,.3f} million')
    print(f'June if-converted economic interests: {economic:,}')
    print(f'Gross-award proxy: {gross_awards:,}; not treasury-stock-method dilution')
    print('Saved output/research-bridge.json; arithmetic checks passed.')


if __name__ == '__main__':
    main()
