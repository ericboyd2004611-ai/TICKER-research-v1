"""Rebuild the cost-of-capital, peer, and WACC/growth comparison evidence."""
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from commercialization import run
from valuation_methods import wacc, multiples, terminal_diagnostics, rate_diagnostic, gordon_cell


def main():
    read=lambda n:json.loads((ROOT/'data'/n).read_text())
    cap=read('cost-of-capital.json'); peers=read('peers.json'); config=read('commercialization-scenarios.json'); research=read('research-inputs.json')
    capital=wacc(cap);common=config['common']
    inputs=peers['smr_ttm'];sales=inputs['revenue_fy2025_m']-inputs['revenue_h12025_m']+inputs['revenue_h12026_m']
    shares=research['shares'];basic=(shares['class_a']+shares['exchangeable_llc_units'])/1e6
    gross=basic+(shares['options']+shares['rsus'])/1e6
    money=research['usd_millions'];liq=sum(money[k] for k in ('cash','short_term_investments','investments'))
    book=money['consolidated_equity']
    smr=dict(price=research['price_usd'],shares_m=basic,cash_and_marketable_m=liq,
             financial_debt_m=money['reported_debt'],other_ev_claims_m=0,book_common_m=book,ticker='SMR',**inputs)
    calculated=[]
    for peer in peers['peers']:
        p=multiples(peer)
        ev_equity=p['ev_sales']*sales+liq-money['reported_debt'] if p['ev_sales'] is not None else None
        pb_equity=p['price_book']*book if p['price_book'] is not None else None
        p.update(implied_smr_ev_sales_basic=ev_equity/basic if ev_equity is not None else None,
                 implied_smr_price_book_basic=pb_equity/basic if pb_equity is not None else None,
                 implied_smr_ev_sales_gross_award=ev_equity/gross if ev_equity is not None else None,
                 implied_smr_price_book_gross_award=pb_equity/gross if pb_equity is not None else None)
        calculated.append(p)
    rates=sorted(set([.10,capital['wacc'],.15,.20]))
    scenarios=[]
    for s in config['scenarios']:
        original=run(common,s,research)
        candidate=run(dict(common,discount_rate=capital['wacc']),s,research)
        grid=[dict(wacc=r,growth=g,**gordon_cell(original,r,g,common['pma_annual_escalation'])) for r in rates for g in (.02,.025,.03,.05,.06)]
        scenarios.append(dict(name=s['name'],reference_rate=common['discount_rate'],reference_value_per_share=original['value_per_share'],
                              capm_value_per_share=candidate['value_per_share'],terminal=terminal_diagnostics(original),
                              monotonicity=rate_diagnostic(original,rates),wacc_growth=grid))
    files=['data/cost-of-capital.json','data/peers.json','data/research-inputs.json','data/commercialization-scenarios.json','src/valuation_methods.py','src/commercialization.py','build_methods.py','docs/peer-policy.md']
    payload=dict(wacc=capital,wacc_inputs=cap,peers=calculated,smr=multiples(smr),scenarios=scenarios,
                 source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    (ROOT/'output/valuation-methods.json').write_text(json.dumps(payload,indent=2)+'\n')
    fmt=lambda x:'NM' if x is None else f'{x:,.2f}'
    lines=['# Public-company comparison and cost of capital','',
           f"CAPM: {cap['risk_free']:.2%} + {cap['beta']:.2f} × {cap['equity_risk_premium']:.2%} = {capital['cost_of_equity']:.2%} cost of equity.",
           f"Weights: equity {capital['equity_weight']:.0%}, financial debt {capital['debt_weight']:.0%}. WACC = {capital['wacc']:.2%}.",
           'Beta 2.0 is a proposed judgment, not an estimated SMR beta or a student approval. The original 15% scenario remains separately labeled.', '',
           '## Dated multiples', '',
           'Price date September 1, 2026; balance sheets June 30, 2026. USD millions except per share. TTM = FY2025 - H1 2025 + H1 2026.', '',
           '| Company | Market equity | Financial EV | TTM sales | EV / sales | Adjusted EV / sales | Price / book |',
           '|---|---:|---:|---:|---:|---:|---:|']
    for p in [payload['smr']]+calculated:
        lines.append('| '+p['ticker']+' | '+' | '.join(fmt(p[k]) for k in ('market_equity_m','enterprise_value_m','ttm_revenue_m','ev_sales','adjusted_ev_sales','price_book'))+' |')
    lines+=['','## Mechanical peer translation to SMR ($/share)','','| Peer | EV/sales: basic | P/book: basic | EV/sales: gross awards | P/book: gross awards |','|---|---:|---:|---:|---:|']
    for p in calculated:
        lines.append('| '+p['ticker']+' | '+' | '.join(fmt(p[k]) for k in ('implied_smr_ev_sales_basic','implied_smr_price_book_basic','implied_smr_ev_sales_gross_award','implied_smr_price_book_gross_award'))+' |')
    lines+=['','EV-based translation: peer EV/sales × SMR TTM revenue + June unrestricted liquidity - reported financial debt, divided by indicated economic shares. P/book translation: peer P/book × SMR consolidated common economic book, divided by the same shares. These are June-balance mechanical comparisons, not September cash reconciliations or fair-value estimates.',
            'Conventional financial EV excludes operating leases; adjusted BWXT EV adds pension and postretirement liabilities. Negative book NCI is not treated as a market claim. The entire public-company bridge is a proxy pending September share/claim roll-forwards. No peer median is used.',
            '', '## Why comps disagree with the DCF', '',
            'OKLO has only $1.210m of trailing revenue. Its very high EV/sales reflects development expectations divided by a tiny current-sales denominator; applying it to SMR can create an extreme mechanical value. BWXT has established nuclear/defense sales and profitability, so its revenue multiple transfers mature economics to an early-stage supplier. P/book largely compares financing cash and accumulated losses; it does not value reactor IP, future contracts, or future burn. The DCF instead prices an explicit delivery path, milestone fees, reinvestment, funding and an assumed exit. These methods answer different economic questions. Do not average their outputs into a target.',
            '', '## Discount-rate and terminal dependence', '',
            '| Scenario | Original 15% / share | CAPM / share | PV terminal / EV | Equity nonincreasing? | EV nonincreasing? |','|---|---:|---:|---:|---|---|']
    for s in scenarios:
        tv=s['terminal']['terminal_share_of_ev']
        lines.append(f"| {s['name']} | {s['reference_value_per_share']:.2f} | {s['capm_value_per_share']:.2f} | {tv:.1%}"+f" | {s['monotonicity']['floored_value_nonincreasing']} | {s['monotonicity']['ev_nonincreasing']} |" if tv is not None else f"| {s['name']} | {s['reference_value_per_share']:.2f} | {s['capm_value_per_share']:.2f} | NM: nonpositive EV | {s['monotonicity']['floored_value_nonincreasing']} | {s['monotonicity']['ev_nonincreasing']} |")
    lines+=['','Terminal share is PV terminal / EV, not PV terminal / equity. A ratio above 100% reflects negative explicit FCFF. With nonpositive EV it is NM.',
            'Monotonicity holds for a fixed stream of nonnegative cash flows. This development model has mixed-sign flows. The sampled EV diagnostic can fail even when the floored per-share output is flat at zero. Such a failure is disclosed, not removed.', '', '## WACC–growth grids', '',
            'A Gordon diagnostic is provided separately from the exit-multiple base. With perpetual milestone fees escalating at least 5%, a 2–3% uniform terminal-FCFF growth assumption is blocked. Conditional 5–6% cases impose uniform terminal FCFF growth and remain economically unsupported as long-run forecasts. They are sensitivity cases, not endorsed terminal values.']
    for s in scenarios:
        lines+=['',f"### {s['name']}",'','| WACC / growth | 2.0% | 2.5% | 3.0% | 5.0% | 6.0% |','|---|---:|---:|---:|---:|---:|']
        for r in rates:
            cells=[x for x in s['wacc_growth'] if x['wacc']==r]
            lines.append(f'| {r:.2%} | '+' | '.join(fmt(x['value_per_share']) if x['value_per_share'] is not None else x['status'] for x in cells)+' |')
    lines+=['','## Sources and policy','','Selection was recorded in docs/peer-policy.md before extracting multiples. This is a new October research step, not a claimed earlier lock. Exact observations, locators and URLs: data/peers.json and data/cost-of-capital.json. Inputs and source hashes: output/valuation-methods.json.']
    text='\n'.join(lines)+'\n'
    (ROOT/'output/valuation-methods.md').write_text(text)
    (ROOT/'docs/peer-analysis.md').write_text(text)
    print(f"WACC {capital['wacc']:.2%}; peers {len(calculated)}; grids {sum(len(s['wacc_growth']) for s in scenarios)} cells")


if __name__=='__main__':main()
