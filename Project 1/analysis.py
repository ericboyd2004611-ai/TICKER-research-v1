"""Export the inherited conditional downside case; no final valuation implied."""
from dataclasses import asdict
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'src'))
import smr_proforma as model


def main():
    assumptions = model.Assumptions()
    rows = model.project(assumptions)
    output = {
        'status': 'INCOMPLETE_PROJECT_CONDITIONAL_DOWNSIDE_ONLY',
        'balance_sheet_date': '2025-12-31',
        'information_basis': '2025 annual report published 2026-02-26; retrospective',
        'final_valuation_date': None,
        'units': 'USD millions; shares in millions; per-share values in USD',
        'case': 'Services-only through 2030, followed by wind-down',
        'student_initial_position': 'watch/defer; final recommendation not validated',
        'opening': model.OPENING,
        'assumptions': asdict(assumptions),
        'constants': {key: getattr(model, key) for key in
                      ('BASE_REVENUE', 'BASE_MARGIN', 'NORMALIZED_OPEX',
                       'CASH_OPEX', 'CLASS_A', 'EXCHANGEABLE_UNITS',
                       'RSUS', 'OPTIONS', 'SHARES', 'LLM_PURCHASES')},
        'forecast': rows,
        'conditional_value': model.value(rows, assumptions),
        'limitations': [
            'No successful module commercialization scenario or valuation range.',
            'No valuation-date market price comparison.',
            'Historical inputs require complete source-ledger verification.',
            'Not the required human-authored locked changed-input exercise.',
        ],
    }
    destination = HERE / 'output'
    destination.mkdir(exist_ok=True)
    (destination / 'downside-output.json').write_text(json.dumps(output, indent=2) + '\n')
    (destination / 'downside-report.md').write_text(model.render())
    print('Exported output/downside-report.md and output/downside-output.json')
    print('Conditional downside value/share:', round(output['conditional_value']['per_share'], 4))
    print('Project incomplete: this result is not a full company valuation.')


if __name__ == '__main__':
    main()
