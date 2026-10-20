"""Accounting and valuation safeguards for the conditional SMR case."""

import unittest
from dataclasses import replace

import smr_proforma as smr


class SMRChecks(unittest.TestCase):
    def test_cash_without_interest_matches_independent_cash_budget(self):
        rows = smr.project(replace(smr.Assumptions(), cash_yield=0))
        # Opening liquid resources minus existing payable, operating spending,
        # maintenance investment and disclosed material commitments.
        expected = 1287.171 - 259.884 - 5 * (192.428 - 11.431 + .342 + .508) - 48.867
        self.assertAlmostEqual(rows[-1]["cash"], expected, places=8)
        self.assertAlmostEqual(sum(r["pma_cash"] for r in rows), -259.884)
        self.assertAlmostEqual(sum(r["investment_sales"] for r in rows), 450.754)

    def test_terminal_bridge_does_not_double_count_cash_or_operating_losses(self):
        rows = smr.project()
        result = smr.value(rows)
        expected = (rows[-1]["cash"] + 8.378 * .8 - 39.077 - 50) / 1.15**5
        self.assertAlmostEqual(result["equity_value"], expected, places=8)
        self.assertAlmostEqual(smr.SHARES, 346.764728, places=8)

    def test_insufficient_funding_is_rejected(self):
        with self.assertRaises(smr.FundingRequired):
            smr.project(replace(smr.Assumptions(), opex_growth=.10))

    def test_additional_claim_reduces_distribution_and_equity_cannot_be_negative(self):
        rows = smr.project()
        base = smr.value(rows)
        claim = smr.value(rows, replace(smr.Assumptions(), extra_terminal_claims=10))
        self.assertAlmostEqual(base["equity_value"] - claim["equity_value"], 10 / 1.15**5)
        zero = smr.value(rows, replace(smr.Assumptions(), extra_terminal_claims=1000))
        self.assertEqual(zero["per_share"], 0)

    def test_bad_balance_is_not_silently_plugged(self):
        broken = smr.OPENING | {"equity": smr.OPENING["equity"] + 1}
        with self.assertRaises(ValueError):
            smr.check_balance(broken)


if __name__ == "__main__":
    unittest.main()
