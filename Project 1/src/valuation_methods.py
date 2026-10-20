"""Explicit cost of capital, peer bridges, and discounted-cash-flow diagnostics."""
import math


def wacc(inputs):
    keys = ('risk_free', 'equity_risk_premium', 'beta', 'debt_weight', 'pre_tax_debt_cost', 'tax_rate')
    if any(not math.isfinite(inputs[k]) for k in keys):
        raise ValueError('Nonfinite cost-of-capital input')
    if not 0 <= inputs['debt_weight'] <= 1 or not 0 <= inputs['tax_rate'] <= 1:
        raise ValueError('Capital weights and tax must be between zero and one')
    if any(inputs[k] < 0 for k in ('risk_free', 'equity_risk_premium', 'beta', 'pre_tax_debt_cost')):
        raise ValueError('Negative cost-of-capital input')
    ke = inputs['risk_free'] + inputs['beta'] * inputs['equity_risk_premium']
    wd = inputs['debt_weight']
    return dict(cost_of_equity=ke, equity_weight=1-wd, debt_weight=wd,
                after_tax_debt_cost=inputs['pre_tax_debt_cost']*(1-inputs['tax_rate']),
                wacc=ke*(1-wd)+inputs['pre_tax_debt_cost']*(1-inputs['tax_rate'])*wd)


def multiples(peer):
    sales = peer['revenue_fy2025_m'] - peer['revenue_h12025_m'] + peer['revenue_h12026_m']
    equity = peer['price'] * peer['shares_m']
    ev = equity + peer['financial_debt_m'] - peer['cash_and_marketable_m']
    adjusted = ev + peer['other_ev_claims_m']
    return dict(ticker=peer['ticker'], market_equity_m=equity, enterprise_value_m=ev,
                adjusted_ev_m=adjusted, ttm_revenue_m=sales,
                ev_sales=ev/sales if sales > 0 else None,
                adjusted_ev_sales=adjusted/sales if sales > 0 else None,
                price_book=equity/peer['book_common_m'] if peer['book_common_m'] > 0 else None)


def terminal_diagnostics(result):
    ev, pv = result['enterprise_value'], result['pv_terminal']
    return dict(pv_terminal_m=pv, enterprise_value_m=ev,
                terminal_share_of_ev=pv/ev if ev > 0 else None,
                status='DEFINED' if ev > 0 else 'NM: nonpositive EV; percentage would mislead',
                note='A percentage over 100% is possible when explicit PV cash flows are negative.')


def rate_diagnostic(result, rates):
    """Reprice fixed cash flows; expose actual monotonicity rather than assume it."""
    points=[]
    for rate in sorted(rates):
        pv = sum(row['fcff']/(1+rate)**row['discount_years'] for row in result['rows'])
        pv += result['terminal_enterprise_value']/(1+rate)**result['rows'][-1]['discount_years']
        raw = pv + result['opening_liquidity'] - result.get('reported_debt_m',0) - result['common']['additional_equity_claims_m']
        points.append(dict(wacc=rate, ev=pv, unfloored_equity_m=raw,
                           value_per_share=max(0,raw)/result['gross_award_shares_m']))
    return dict(points=points,
                floored_value_nonincreasing=all(b['value_per_share'] <= a['value_per_share']+1e-9 for a,b in zip(points,points[1:])),
                ev_nonincreasing=all(b['ev'] <= a['ev']+1e-9 for a,b in zip(points,points[1:])),
                note='Nonnegative cash flows guarantee decreasing PV. Mixed-sign development cash flows do not. A zero equity floor can hide an EV failure.')


def gordon_cell(result, rate, growth, fee_floor):
    """Conditional normalized FCFF perpetuity; blocked if fee path is inconsistent."""
    if rate <= growth:
        return dict(status='BLOCKED: WACC must exceed growth', value_per_share=None)
    if growth < fee_floor:
        return dict(status='BLOCKED: growth below contractual fee escalation', value_per_share=None)
    if result['terminal_fcff'] <= 0:
        return dict(status='NM: normalized terminal FCFF is nonpositive', value_per_share=None)
    # terminal_fcff already describes next year; no second multiplication by 1+g.
    tv=result['terminal_fcff']/(rate-growth)
    pv=sum(row['fcff']/(1+rate)**row['discount_years'] for row in result['rows'])
    pv+=tv/(1+rate)**result['rows'][-1]['discount_years']
    raw=pv+result['opening_liquidity']-result.get('reported_debt_m',0)-result['common']['additional_equity_claims_m']
    return dict(status='CONDITIONAL: entire terminal FCFF grows at g; not a base forecast',
                value_per_share=max(0,raw)/result['gross_award_shares_m'])
