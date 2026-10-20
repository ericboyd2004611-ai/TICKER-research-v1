"""Local terminal application for the frozen NuScale decision evidence.

No network calls or third-party packages. Calculations live in the analysis
engine; this interface only displays generated output and evidence references.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


def load_record():
    path = ROOT / 'output/commercialization-output.json'
    if not path.exists():
        raise ValueError('Run python3 build_scenarios.py first.')
    record = json.loads(path.read_text())
    for name, expected in record['input_sha256'].items():
        actual = hashlib.sha256((ROOT / 'data' / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Stale output: {name} changed. Run python3 build_scenarios.py.')
    for name, expected in record['source_sha256'].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Stale output: {name} changed. Run python3 build_scenarios.py.')
    return record


def table(headers, rows):
    strings = [[str(x) for x in row] for row in [headers] + rows]
    widths = [max(len(row[i]) for row in strings) for i in range(len(headers))]
    for index, row in enumerate(strings):
        print('  '.join(cell.ljust(width) for cell, width in zip(row, widths)))
        if index == 0:
            print('  '.join('-' * width for width in widths))


def show(record, mode, scenario='central', year=None):
    print('\nNUSCALE | DECISION EVIDENCE | AI-GENERATED DRAFT')
    print('Boundary: September 1, 2026 close | USD millions except USD/share')
    print('Proposed action: WATCH / DEFER. Student review pending.')
    print('Conditional scenarios with an assumed operating exit; not fair value established by contracts.\n')
    results = record['results']
    if mode == 'summary':
        table(['Scenario', 'DCF value/share', 'Net funding', 'First funding'],
              [[r['name'], f"${r['value_per_share']:.2f}", f"${r['funding_net_m']:,.1f}m", r['first_funding_year'] or 'None'] for r in results])
        print('\nAsk: retain on watchlist; require verified net contract economics and a fundable cash plan.')
        print('Prices, margins and exit multiple are assumptions. Funding conditions must also be satisfied.')
    elif mode in ('scenario', 'bridge'):
        mapping = dict(delayed=0, central=1, stronger=2)
        r = results[mapping[scenario]]
        print(r['name'])
        if mode == 'bridge':
            for label, key in [('PV explicit FCFF', 'pv_explicit_fcff'), ('PV terminal', 'pv_terminal'),
                               ('Enterprise value', 'enterprise_value'), ('Opening liquidity', 'opening_liquidity'),
                               ('Equity before floor', 'equity_value_unfloored'), ('Gross-award shares (m)', 'gross_award_shares_m')]:
                print(f'{label:28} {r[key]:14,.3f}')
            print('Reported debt:', record['research_inputs']['usd_millions']['reported_debt'])
            print('Additional claims allowance:', r['common']['additional_equity_claims_m'])
        else:
            rows = [x for x in r['rows'] if year is None or x['year'] == year]
            if not rows:
                raise ValueError('Year must be between 2026 and 2036.')
            table(['Year', 'Modules', 'Revenue', 'PMA', 'FCFF', 'Funding', 'End cash', 'BS gap'],
                  [[x['year'], x['delivered']] + [f'{x[k]:,.2f}' for k in
                    ('revenue', 'pma_cash', 'fcff', 'funding_net', 'closing_liquidity', 'balance_gap')] for x in rows])
        print('\nFinancing shares are a separate fixed-price diagnostic; not a second DCF dilution deduction.')
        print(f"Existing-holder exit PV/share: ${r['investor_exit_value_per_initial_share']:.2f}")
        print('Share-capacity proxy exceeded:', r['share_authorization_capacity_exceeded'])
        print('Funding subscription checks:', r['funding_valuation_checks'] or 'No funding raises')
    elif mode == 'exit':
        print('Operating exit assumption: end-2036 sale; multiple of normalized 2037 EBITDA after full fees.')
        table(['Scenario', 'Multiple', 'DCF/share', 'Existing-holder exit PV/share'],
              [[r['name'], f"{r['exit_multiple']:.0f}x", f"${r['value_per_share']:.2f}",
                f"${r['investor_exit_value_per_initial_share']:.2f}"] for r in record['exit_sensitivity']])
        print('\nThe multiple is an analyst assumption; it is not a verified peer or buyer quote.')
    elif mode == 'sensitivity':
        table(['Discount rate', 'Module base price', 'Conditional DCF/share', 'Net funding'],
              [[f"{r['discount_rate']:.0%}", f"${r['module_price_m']:.0f}m", f"${r['value_per_share']:.2f}", f"${r['funding_net_m']:,.1f}m"] for r in record['sensitivity']])
        print('\nFive-percentage-point module-margin stress:')
        table(['Scenario', 'Stressed conditional DCF/share', 'Stressed funding'],
              [[x['name'], f"${x['value_per_share']:.2f}", f"${x['funding_net_m']:,.1f}m"] for x in record['margin_stress']])
    elif mode == 'reverse':
        r = record['reverse_scenario']
        print('One-input reverse scenario:', r['status'])
        print(f"Reference share price: ${r['target_price_usd']:.2f}")
        if r['solved_module_price_m'] is not None:
            print(f"Required 2026-base supplier revenue/module: ${r['solved_module_price_m']:.1f}m")
        print('Held fixed: central delivery cadence, margin, costs, taxes, working capital, fee escalation and discount rate.')
        print('The required price is an assumption hurdle; the redacted contract cap is not validated.')
    elif mode == 'sources':
        print('Historical financial inputs and precise locators: docs/verified-starting-point-draft.md')
        print('Research, boundary and contract correction: docs/source-review.md')
        print('Editable assumptions: data/commercialization-scenarios.json')
        print('2026 quarterly filing:', record['research_inputs']['filing_url'])
        print('2025 PMA: https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm')
        print('All module prices, margins and delivery schedules are unapproved analyst assumptions.')
    elif mode == 'monitoring':
        print((ROOT / 'docs/monitoring-policy.md').read_text())
    elif mode == 'readiness':
        print((ROOT / 'HANDOFF.md').read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('view', nargs='?', default='summary', choices=
                        ['summary', 'scenario', 'bridge', 'sensitivity', 'exit', 'reverse', 'sources', 'monitoring', 'readiness'])
    parser.add_argument('--scenario', default='central', choices=['delayed', 'central', 'stronger'])
    parser.add_argument('--year', type=int)
    parser.add_argument('--interactive', action='store_true', help='Show a terminal menu after the first view')
    args = parser.parse_args()
    try:
        record = load_record()
        show(record, args.view, args.scenario, args.year)
        if args.interactive:
            choices = ['summary', 'scenario', 'bridge', 'sensitivity', 'exit', 'reverse', 'sources', 'monitoring', 'readiness']
            while True:
                print('\n' + ' | '.join(f'{i+1} {name}' for i, name in enumerate(choices)) + ' | q Quit')
                answer = input('Select view: ').strip().lower()
                if answer == 'q':
                    break
                if answer.isdigit() and 1 <= int(answer) <= len(choices):
                    show(record, choices[int(answer)-1], args.scenario, args.year)
                else:
                    print('Choose a listed number or q.')
    except (ValueError, OSError, EOFError) as error:
        print(f'Application: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
