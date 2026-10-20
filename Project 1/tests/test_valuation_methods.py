"""Known-answer method checks and live calculation failure/recovery."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'src'))
from valuation_methods import wacc,multiples,gordon_cell,rate_diagnostic,terminal_diagnostics
from workbench import calculate,defaults


class ValuationMethodChecks(unittest.TestCase):
    def test_capm_and_leveraged_blend_known_answers(self):
        inputs=dict(risk_free=.04,equity_risk_premium=.05,beta=1.2,debt_weight=.25,pre_tax_debt_cost=.06,tax_rate=.25)
        result=wacc(inputs)
        self.assertAlmostEqual(result['cost_of_equity'],.10)
        self.assertAlmostEqual(result['wacc'],.08625)
        self.assertAlmostEqual(wacc(dict(inputs,debt_weight=0))['wacc'],.10)

    def test_comps_use_ttm_and_correct_bridge(self):
        p=dict(ticker='TEST',price=10,shares_m=20,financial_debt_m=30,cash_and_marketable_m=10,
               other_ev_claims_m=5,book_common_m=100,revenue_fy2025_m=80,revenue_h12025_m=30,revenue_h12026_m=50)
        m=multiples(p)
        self.assertAlmostEqual(m['ttm_revenue_m'],100)
        self.assertAlmostEqual(m['ev_sales'],2.2)
        self.assertAlmostEqual(m['adjusted_ev_sales'],2.25)
        self.assertAlmostEqual(m['price_book'],2)
        self.assertIsNone(multiples(dict(p,book_common_m=-1))['price_book'])

    def test_live_driver_recalculates_engine_and_reset_recovers(self):
        base=defaults(2);r=calculate(base)
        self.assertTrue(r['valid'])
        changed=calculate(dict(base,module_price_m=300))
        self.assertGreater(changed['result']['value_per_share'],r['result']['value_per_share'])
        self.assertNotEqual(changed['result']['rows'][-1]['revenue'],r['result']['rows'][-1]['revenue'])
        failed=calculate(dict(base,pma_annual_escalation=.04))
        self.assertFalse(failed['valid']);self.assertIsNone(failed['result'])
        self.assertEqual(calculate(base)['result'],r['result'])

    def test_invalid_api_inputs_cannot_bypass_controls(self):
        for changes in (dict(discount_rate=float('nan')),dict(module_price_m=401),dict(scenario_index=-1),dict(module_price_m='300'),dict(unknown=1)):
            self.assertFalse(calculate(changes)['valid'])

    def test_perpetuity_fee_floor_and_rate_guard(self):
        base=defaults(2)
        self.assertFalse(calculate(dict(base,terminal_method='perpetuity'))['valid'])
        self.assertFalse(calculate(dict(base,terminal_method='perpetuity',discount_rate=.08,terminal_growth=.08))['valid'])
        r=calculate(base)['result']
        self.assertIsNone(gordon_cell(r,.15,.025,.05)['value_per_share'])
        cell=gordon_cell(r,.15,.05,.05)
        expected=sum(x['fcff']/1.15**x['discount_years'] for x in r['rows'])
        expected+=r['terminal_fcff']/(.15-.05)/1.15**r['rows'][-1]['discount_years']
        expected+=r['opening_liquidity']
        self.assertAlmostEqual(cell['value_per_share'],expected/r['gross_award_shares_m'])

    def test_terminal_percentage_handles_negative_ev(self):
        self.assertIsNone(terminal_diagnostics(dict(enterprise_value=-10,pv_terminal=20))['terminal_share_of_ev'])
        self.assertAlmostEqual(terminal_diagnostics(dict(enterprise_value=10,pv_terminal=20))['terminal_share_of_ev'],2)

    def test_monotonicity_detects_negative_cash_flow_counterexample(self):
        r=dict(rows=[dict(fcff=-100,discount_years=1)],terminal_enterprise_value=0,opening_liquidity=200,
               gross_award_shares_m=10,common=dict(additional_equity_claims_m=0))
        d=rate_diagnostic(r,[.1,.2])
        self.assertFalse(d['ev_nonincreasing'])
        self.assertFalse(d['floored_value_nonincreasing'])
        positive=deepcopy(r);positive['rows'][0]['fcff']=100
        self.assertTrue(rate_diagnostic(positive,[.1,.2])['ev_nonincreasing'])


if __name__=='__main__':unittest.main()
