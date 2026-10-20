"""Generate clearly labeled commercialization scenario drafts and sensitivity."""
from copy import deepcopy
import csv
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'src'))
from commercialization import run


def main():
    research_path = HERE / 'data/research-inputs.json'
    assumptions_path = HERE / 'data/commercialization-scenarios.json'
    research = json.loads(research_path.read_text())
    config = json.loads(assumptions_path.read_text())
    common = config['common']
    results = [run(common, scenario, research) for scenario in config['scenarios']]
    out = HERE / 'output'
    out.mkdir(exist_ok=True)
    sensitivity = []
    for rate in (.10, .15, .20):
        for price in (150., 200., 250.):
            c = dict(common, discount_rate=rate)
            scenario = dict(config['scenarios'][1], module_price_m=price)
            r = run(c, scenario, research)
            sensitivity.append(dict(discount_rate=rate, module_price_m=price,
                                    value_per_share=r['value_per_share'], funding_net_m=r['funding_net_m']))
    stresses = []
    for scenario in config['scenarios']:
        stressed = deepcopy(scenario)
        stressed['module_gross_margin_before_pma'] = max(0, stressed['module_gross_margin_before_pma'] - .05)
        r = run(common, stressed, research)
        stresses.append(dict(name=scenario['name'], value_per_share=r['value_per_share'],
                             funding_net_m=r['funding_net_m'], first_funding_year=r['first_funding_year']))
    exit_sensitivity = []
    for scenario in config['scenarios']:
        for multiple in (0., 4., 6., 8., 10.):
            r = run(dict(common, terminal_method='exit_multiple', exit_ebitda_multiple=multiple), scenario, research)
            exit_sensitivity.append(dict(name=scenario['name'], exit_multiple=multiple,
                    value_per_share=r['value_per_share'], pv_terminal=r['pv_terminal'],
                    investor_exit_value_per_initial_share=r['investor_exit_value_per_initial_share']))
    # Reverse scenario: solve one explicit assumption, not a calibrated forecast.
    low, high = 1.0, 1000.0
    central = config['scenarios'][1]
    target = research['price_usd']
    def price_value(price):
        return run(common, dict(central, module_price_m=price), research)['value_per_share']
    reverse = dict(target_price_usd=target, bracket_module_price_m=[low, high],
                   status='NO_SOLUTION_IN_BRACKET', solved_module_price_m=None)
    if price_value(low) <= target <= price_value(high):
        for _ in range(80):
            middle = (low + high) / 2
            if price_value(middle) < target:
                low = middle
            else:
                high = middle
        solved = (low + high) / 2
        reverse.update(status='SOLVED_ILLUSTRATIVE', solved_module_price_m=solved,
                       reproduced_value_per_share=price_value(solved))
    payload = dict(label=config['label'], research_inputs=research,
                   input_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in (research_path, assumptions_path)},
                   source_sha256={name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                                  for name in ('src/commercialization.py', 'build_scenarios.py')},
                   results=results, sensitivity=sensitivity, margin_stress=stresses,
                   reverse_scenario=reverse, exit_sensitivity=exit_sensitivity)
    (out / 'commercialization-output.json').write_text(json.dumps(payload, indent=2) + '\n')
    visible = dict(decision='SMR: whether to initiate a position for a committee with no holdings',
                   as_of=common['valuation_date'] + ' close',
                   recommendation='WATCH / DEFER - AI-generated proposal, student review pending',
                   valuation_status='Conditional valuation with an assumed operating exit; contract prices and exit multiple unverified',
                   scenario_envelope=[min(r['value_per_share'] for r in results), max(r['value_per_share'] for r in results)],
                   reversal_trigger='Verified profitable binding orders, a fundable stressed cash plan, and supported value at least 25% above price',
                   evidence_path='output/commercialization-output.json',
                   scenario_results=[{key: r[key] for key in ('name', 'value_per_share', 'funding_net_m')} for r in results])
    (HERE / 'visible_output.json').write_text(json.dumps(visible, indent=2) + '\n')
    with (out / 'commercialization-forecasts.csv').open('w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['scenario'] + list(results[0]['rows'][0]))
        writer.writeheader()
        for result in results:
            writer.writerows(dict(scenario=result['name'], **r) for r in result['rows'])
    lines = ['# NuScale commercialization scenarios — AI-generated draft', '',
             '**Conditional scenario valuations, not company guidance or a validated market price target.**', '',
             'Default: sale at the end of 2036 for six times normalized next-year operating EBITDA',
             'after a full milestone-fee burden. This is an analyst exit assumption, not a sourced',
             'peer multiple or guaranteed buyer price. Zero/4x/6x/8x/10x sensitivities are shown.', '',
             'September 1, 2026 close boundary. June financial observations and a judgmental',
             '$40m July–August cash-use allowance form the opening liquidity proxy.',
             'Intervening filings, ownership changes and contingent claims are not fully audited.', '',
             'USD millions and shares in millions, except USD/share. All results are calculated;',
             'edit `data/commercialization-scenarios.json`, then run `python3 build_scenarios.py`.', '',
             '## Scenario comparison', '',
             '| Scenario | Implied value/share | First funding year | Net equity funding | New shares, diagnostic | Existing holder fraction, diagnostic |',
             '|---|---:|---|---:|---:|---:|']
    for r in results:
        lines.append(f"| {r['name']} | ${r['value_per_share']:.2f} | {r['first_funding_year'] or 'None'} | "
                     f"{r['funding_net_m']:,.1f} | {r['diagnostic_new_shares_m']:,.1f} | {r['diagnostic_existing_holder_fraction']:.1%} |")
    values = [r['value_per_share'] for r in results]
    lines += ['', f"**Illustrative scenario envelope: ${min(values):.2f}–${max(values):.2f}/share.**",
              'No probabilities or weighted target are assigned. A zero result is a modeled',
              'equity floor, not proof the stock is worthless. Current-holder value assumes',
              'future funding on fair terms; the fixed-price financing diagnostic does not',
              'establish those terms. An infeasible funding path invalidates the scenario.', '',
              '## Inputs that define the answer', '',
              '| Scenario | Price/module | Gross margin before PMA | Deliveries 2027–2036 |',
              '|---|---:|---:|---|']
    for r in results:
        s = r['assumptions']
        lines.append(f"| {r['name']} | {s['module_price_m']:.0f} | {s['module_gross_margin_before_pma']:.0%} | " + ', '.join(map(str, s['deliveries'])) + ' |')
    lines += ['', '**Every scenario price, margin, schedule and forecast parameter is an AI-generated analyst assumption.**',
              'These are neither disclosed orders nor customer contract economics. Stronger execution',
              'is a deliberately optimistic comparator, not a statistical confidence bound.', '',
              '| Common setting | Value |', '|---|---|']
    for key, value in common.items():
        lines.append(f'| {key} | {value} |')
    lines += ['', '## Method and limitations', '',
              'FCFF = EBIT − cash tax + depreciation − capex − change in incremental working capital.',
              'Module revenue equals delivered units × assumed supplier revenue/module; this is',
              'not total nuclear power-plant construction cost. Installed-base service income starts',
              'the year after delivery. Costs exclude fuel/pass-through complexity and interest income.',
              'The model has an actual-day stub to December 2026 and year-end full-year cash flows.', '',
              'PMA fee scale is an inference from the 2025 cash installment and cohort, not a',
              'contract quote. First-cohort tranche 1 is treated as sunk; remaining tranches are paid',
              'two and one years before delivery. Later cohorts pay all tranches. The terminal',
              'run rate uses the full fee burden. Contracts, timing and repeatability need verification.', '',
              'The modeled fee increases 5% every year from its inferred 2025 base, reflecting',
              'the agreement floor; future CPI above 5% would require a larger adjustment.',
              'Module selling prices grow 2% annually from the stated 2026 assumption. A negotiated',
              'cap is redacted. Equal price/fee growth is not assumed. Contract slot/invoice timing',
              'is simplified; fixed lead years do not reproduce all legal payment conditions.', '',
              'PV of explicit FCFF plus PV of terminal operating value gives enterprise value.',
              'Add the opening unrestricted liquidity proxy once, subtract reported debt and the',
              'editable additional-claims allowance, then divide by the June gross-award share proxy.',
              'Operating commitments and leases are assumed within the cash-cost/reinvestment forecasts;',
              'that mapping is not yet reconciled contract by contract. A zero claims allowance',
              'does not mean there are no contingent or tax-agreement claims.', '',
              'Negative FCFF is already deducted in the DCF. Funding receipts stay out of enterprise',
              'value, and diagnostic new shares do not dilute the DCF denominator a second time.',
              'Funding diagnostics assume issuance at 70% of the reference market price, 3% fees,',
              'and a $50m cash floor. Availability is not guaranteed; only year-end cash is tested.',
              'Liquid investments are assumed saleable at carrying value with no investment return.', '',
              'The default operating exit equals the assumed multiple times positive normalized',
              'next-year EBITDA, after a full milestone-fee burden. Nonpositive EBITDA receives',
              'zero operating sale value; this is not a liquidation appraisal. Cash is not part',
              'of the operating multiple. It is added once in the corporate equity bridge.',
              'The perpetuity method remains optional and rejects growth below fee escalation;',
              'a mathematically valid perpetuity would still need independent economic support.', '',
              'A separate existing-holder method assumes all proceeds arrive on exit and uses',
              'forecast closing cash plus operating sale value, less claims/debt, divided by final',
              'shares and discounted. It does not subtract FCFF again. Because fixed-price raises',
              'differ from fair-value financing, this conditional result can differ from the DCF.',
              'Subscription checks compare that terminal payoff at each raise date with the',
              'assumed issue price. They flag funding assumptions the model does not support.',
              'The share-capacity screen includes current economic interests and gross awards;',
              'it is a proxy, not a legal determination of issuance capacity.', '',
              'This engine provides simplified economic income, balance-sheet and cash-flow statements.',
              'They are not GAAP forecasts. Legacy nonliquid assets and liabilities are held constant;',
              'the assumed pre-valuation burn reduces cash and equity together. Forecast equity',
              'rolls forward from economic net income plus net equity funding, never as a plug.',
              'The old linked-statement downside remains separate until dates and assumptions reconcile.', '',
              '## Enterprise-to-equity bridge', '',
              '| Scenario | PV explicit FCFF | PV terminal | EV | Opening liquidity | Claims | Equity before floor | Shares |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    for r in results:
        lines.append(f"| {r['name']} | {r['pv_explicit_fcff']:,.1f} | {r['pv_terminal']:,.1f} | {r['enterprise_value']:,.1f} | "
                     f"{r['opening_liquidity']:,.1f} | {common['additional_equity_claims_m']:.1f} | {r['equity_value_unfloored']:,.1f} | {r['gross_award_shares_m']:.3f} |")
    lines += ['', '## Operating exit and financing conditions', '',
              '| Scenario | Normalized exit EBITDA | Operating sale value | Existing-holder exit PV/share | Share capacity exceeded? | All assumed subscriptions supported? |',
              '|---|---:|---:|---:|---|---|']
    for r in results:
        checks = r['funding_valuation_checks']
        lines.append(f"| {r['name']} | {r['normalized_exit_ebitda']:,.1f} | {r['terminal_enterprise_value']:,.1f} | "
                     f"${r['investor_exit_value_per_initial_share']:.2f} | {r['share_authorization_capacity_exceeded']} | "
                     f"{all(x['subscription_supported_by_model'] for x in checks) if checks else 'No raises'} |")
    lines += ['', '## Exit-multiple sensitivity - corporate DCF value/share', '',
              '| Scenario | Zero operating exit | 4x | 6x | 8x | 10x |', '|---|---:|---:|---:|---:|---:|']
    for r in results:
        selected = [x for x in exit_sensitivity if x['name'] == r['name']]
        lines.append('| ' + r['name'] + ' | ' + ' | '.join(f"${x['value_per_share']:.2f}" for x in selected) + ' |')
    lines += ['', '## Central schedule sensitivity — value/share', '',
              '| Discount rate | $150m/module | $200m/module | $250m/module |', '|---|---:|---:|---:|']
    for rate in (.10, .15, .20):
        subset = [r for r in sensitivity if r['discount_rate'] == rate]
        lines.append(f'| {rate:.0%} | ' + ' | '.join(f"${r['value_per_share']:.2f}" for r in subset) + ' |')
    lines += ['', '## What would justify the reference market price?', '']
    if reverse['solved_module_price_m'] is not None:
        lines += [f"Holding the central delivery schedule, 35% gross margin and other inputs fixed,",
                  f"the model requires about **${reverse['solved_module_price_m']:.1f}m supplier revenue/module**",
                  f"to reproduce the ${target:.2f} reference share price.",
                  'This is an assumption hurdle, not a forecast or evidence a customer will pay it.',
                  'It must be checked against actual contracts, competitive economics and any price cap.']
    else:
        lines += ['No module-price solution was found within the stated $1m–$1,000m bracket.']
    lines += ['', '## Five-percentage-point module-margin downside', '',
              'AI-generated automated sensitivity; not the required independent locked prediction.', '',
              '| Scenario | Base value/share | Stressed value/share | Stressed net funding |', '|---|---:|---:|---:|']
    for base, stress in zip(results, stresses):
        lines.append(f"| {base['name']} | ${base['value_per_share']:.2f} | ${stress['value_per_share']:.2f} | {stress['funding_net_m']:,.1f} |")
    for r in results:
        lines += ['', f"## {r['name']} annual cash-flow schedule", '',
                  '| Year | Modules | Revenue | PMA cash | EBIT | Tax | Capex | ΔNWC | FCFF | Funding | End liquidity |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
        for row in r['rows']:
            lines.append(f"| {row['year']} | {row['delivered']} | " + ' | '.join(f'{row[k]:,.1f}' for k in
                         ('revenue', 'pma_cash', 'ebit', 'cash_tax', 'capex', 'delta_nwc', 'fcff', 'funding_net', 'closing_liquidity')) + ' |')
        lines += ['', f"Terminal normalized FCFF: {r['terminal_fcff']:,.1f}; {r['terminal_status']}."]
        lines += ['', '### Linked economic statements and checks', '',
                  '| Year | Net income | CFO | CFI | CFF | Assets | Liabilities | Equity | Balance gap |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
        for row in r['rows']:
            lines.append(f"| {row['year']} | " + ' | '.join(f'{row[k]:,.3f}' for k in
                         ('net_income', 'cfo', 'cfi', 'cff', 'assets', 'liabilities', 'equity', 'balance_gap')) + ' |')
    lines += ['', '## Evidence and review', '',
              'Financial observations: [source ledger](../docs/verified-starting-point-draft.md).',
              'PMA scale/tranches: [June 2026 10-Q, Note 9](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm).',
              'Escalation, installments and redacted cap: [PMA Sections 1(c), 1(d), 1(g)](https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm).',
              'Actual inputs, full-precision results, hashes and sensitivities: `commercialization-output.json`.',
              'No final buy/sell recommendation is inferred from unapproved scenario assumptions.', '']
    (out / 'commercialization-report.md').write_text('\n'.join(lines))
    for r in results:
        print(f"{r['name']}: illustrative ${r['value_per_share']:.2f}/share; net funding ${r['funding_net_m']:,.1f}m")
    print('Saved report, JSON and CSV in output/. Not a final fair-value range.')


if __name__ == '__main__':
    main()
