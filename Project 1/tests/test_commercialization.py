"""Independent financial invariants for the illustrative scenario engine."""
from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import unittest

from commercialization import run

ROOT = Path(__file__).resolve().parents[1]


class CommercializationChecks(unittest.TestCase):
    def setUp(self):
        self.research = json.loads((ROOT / 'data/research-inputs.json').read_text())
        config = json.loads((ROOT / 'data/commercialization-scenarios.json').read_text())
        self.common = config['common']
        self.scenario = config['scenarios'][1]

    def test_no_operations_equals_cash_less_explicit_claims(self):
        c = dict(self.common, annual_cash_opex_m=0, minimum_annual_capex_m=0,
                 annual_existing_services_revenue_m=0, opening_ppe_m=0,
                 additional_equity_claims_m=10)
        s = dict(self.scenario, deliveries=[0]*10)
        r = run(c, s, self.research)
        expected_cash = 766.460 + 305.688 + 820.849 - 40
        self.assertAlmostEqual(r['enterprise_value'], 0)
        self.assertAlmostEqual(r['equity_value'], expected_cash - 10)
        self.assertEqual(r['funding_net_m'], 0)

    def test_standalone_cash_budget_matches_every_year(self):
        r = run(self.common, self.scenario, self.research)
        cash = r['opening_liquidity']
        for row in r['rows']:
            cash += row['fcff'] + row['funding_net']
            self.assertAlmostEqual(cash, row['closing_liquidity'])
            self.assertGreaterEqual(cash + 1e-8, self.common['minimum_cash_m'])
        self.assertAlmostEqual(cash, r['opening_liquidity'] +
                               sum(x['fcff'] + x['funding_net'] for x in r['rows']))

    def test_linked_economic_statements_reconcile_without_equity_plug(self):
        r = run(self.common, self.scenario, self.research)
        for row in r['rows']:
            self.assertAlmostEqual(row['assets'], row['liabilities'] + row['equity'])
            self.assertAlmostEqual(row['equity'] - row['opening_equity'], row['net_income'] + row['cff'])
            self.assertAlmostEqual(row['cfo'] + row['cfi'], row['fcff'])
            self.assertAlmostEqual(row['closing_liquidity'] - row['opening_liquidity'],
                                   row['cfo'] + row['cfi'] + row['cff'])

    def test_sunk_first_tranche_is_not_paid_twice(self):
        s = dict(self.scenario, deliveries=[0, 0, 6] + [0]*7)
        r = run(self.common, s, self.research)
        implied_fee = 247.509 / .50 / 72 / .15
        self.assertAlmostEqual(r['total_explicit_pma_cash'], 6 * implied_fee * (.35 * 1.05**2 + .50 * 1.05**3))
        by_year = {x['year']: x for x in r['rows']}
        self.assertAlmostEqual(by_year[2027]['pma_cash'], 6 * implied_fee * .35 * 1.05**2)
        self.assertAlmostEqual(by_year[2028]['pma_cash'], 6 * implied_fee * .50 * 1.05**3)

    def test_contractual_fee_escalation_reduces_value(self):
        base = run(self.common, self.scenario, self.research)
        unscaled = run(dict(self.common, pma_annual_escalation=0), self.scenario, self.research)
        self.assertGreater(base['total_explicit_pma_cash'], unscaled['total_explicit_pma_cash'])
        self.assertLessEqual(base['value_per_share'], unscaled['value_per_share'])

    def test_funding_price_changes_diagnostic_dilution_not_fcff_value(self):
        base = run(self.common, self.scenario, self.research)
        changed = run(dict(self.common, funding_issue_price_fraction_market=.35), self.scenario, self.research)
        self.assertGreater(base['diagnostic_new_shares_m'], 0)
        self.assertAlmostEqual(changed['diagnostic_new_shares_m'], base['diagnostic_new_shares_m'] * 2)
        self.assertAlmostEqual(changed['equity_value'], base['equity_value'])

    def test_margin_shock_reduces_value_and_increases_funding(self):
        base = run(self.common, self.scenario, self.research)
        stress = run(self.common, dict(self.scenario, module_gross_margin_before_pma=.30), self.research)
        self.assertLess(stress['equity_value_unfloored'], base['equity_value_unfloored'])
        self.assertLessEqual(stress['value_per_share'], base['value_per_share'])
        self.assertGreaterEqual(stress['funding_net_m'], base['funding_net_m'])

    def test_discount_timing_and_bridge(self):
        r = run(self.common, self.scenario, self.research)
        start = date(2026, 9, 1)
        pv = sum(x['fcff'] / 1.15 ** ((date(x['year'], 12, 31) - start).days / 365.25)
                 for x in r['rows'])
        self.assertAlmostEqual(pv, r['pv_explicit_fcff'])
        self.assertAlmostEqual(r['equity_value_unfloored'], pv + r['pv_terminal'] + r['opening_liquidity'])

    def test_invalid_inputs_fail(self):
        for overrides in ({'terminal_growth': .15}, {'equity_issuance_fee': 1},
                          {'cash_tax_rate': -1}, {'annual_cash_opex_m': float('nan')}):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                run(dict(self.common, **overrides), self.scenario, self.research)
        bad = deepcopy(self.scenario)
        bad['deliveries'][0] = -1
        with self.assertRaises(ValueError):
            run(self.common, bad, self.research)

    def test_unsupported_terminal_growth_cannot_ignore_fee_escalation(self):
        with self.assertRaises(ValueError):
            run(dict(self.common, terminal_method='perpetuity'), self.scenario, self.research)
        result = run(dict(self.common, terminal_method='none'), self.scenario, self.research)
        self.assertEqual(result['pv_terminal'], 0)
        self.assertEqual(result['terminal_status'], 'WITHHELD_UNSUPPORTED_STEADY_STATE')

    def test_exit_multiple_adds_only_discounted_operating_sale_value(self):
        config = json.loads((ROOT / 'data/commercialization-scenarios.json').read_text())
        scenario = config['scenarios'][2]
        none = run(dict(self.common, terminal_method='none'), scenario, self.research)
        exit_case = run(dict(self.common, terminal_method='exit_multiple', exit_ebitda_multiple=6), scenario, self.research)
        expected = max(0, exit_case['normalized_exit_ebitda']) * 6 / 1.15 ** exit_case['rows'][-1]['discount_years']
        self.assertAlmostEqual(exit_case['equity_value_unfloored'] - none['equity_value_unfloored'], expected)
        self.assertEqual(exit_case['funding_net_m'], none['funding_net_m'])

    def test_investor_value_does_not_charge_operating_losses_twice(self):
        result = run(self.common, self.scenario, self.research)
        expected = result['terminal_equity_proceeds'] / result['final_economic_shares_m'] / 1.15 ** result['rows'][-1]['discount_years']
        self.assertAlmostEqual(result['investor_exit_value_per_initial_share'], expected)
        self.assertEqual(result['share_authorization_capacity_exceeded'],
                         result['final_economic_shares_m'] > self.common['authorized_class_a_shares_m'])


if __name__ == '__main__':
    unittest.main()
