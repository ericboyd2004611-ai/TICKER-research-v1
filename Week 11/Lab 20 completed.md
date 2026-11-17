# Lab 20 — Project 2 readiness audit

**Committee decision:** Pilot the energy ETF strategy without allocating capital; reject it if it cannot consistently satisfy the 40% single-fund cap or validation fails to support its return objective.

## Changed-input prediction — recorded before this run

Recorded 2026-11-17 13:51 EST. Creator and reviewer: Codex, at the user's explicit direction. This is an AI-authored prediction and AI-run exercise, not independent student or partner work. It does not meet the course's human-authored, AI-closed locked-record requirement. Earlier Lab 15 results were already available, so this is not a blind prediction.

Change the AMLP annualized expected return estimate by **−1.00 percentage point**, from its full precision five-year historical mean to that mean less 1.00 percentage point (approximately **18.61% to 17.61% per year**). Keep the prices, estimated covariance, 8% annual return objective, long-only weights, 5-percentage-point grid and 40% per-fund cap unchanged.

Prediction: the constrained allocation and estimated volatility will remain unchanged because the 8% objective has substantial slack. The portfolio's estimated annual return will fall by 0.40 percentage point if its reported 40% AMLP weight remains unchanged. The mandate check should still pass and the decision should remain a no-capital pilot: this one estimate does not resolve missing validation and implementation evidence.

The prediction is based on the previously documented capped mix, not an independent new forecast. Baseline and changed calculations follow only after recording this prediction.

## Actual before/after results and reconciliation

Prediction commit: `129c0fe8e833402ef5a27c9e5dbda2b2fb7f0d51`, pushed to `origin/lab20-readiness` before this run. The portfolio source and data were untracked local files at test time and were not included in that commit: the commit locks the written prediction, not the model or input snapshot. Their SHA-256 hashes were `6cc8b672334d451b771e3fdced94f6a141b8c0611f43b435e48aac015a8d5f6c` for `Lab 15/portfolio.py` and `c7c39b97894fe0cfa4074cfbbbd68de0edb84fb6d983a884fff3d7c6a784313e` for `Lab 15/prices.csv`.

Data: 60 monthly returns between September 2021 and September 2026; historical estimates, not forecasts. These were downloaded October 22, 2026 according to Lab 15. Annualized AMLP estimate changed from **18.614822% to 17.614822%**.

| Executed result | Before | After |
|---|---:|---:|
| XLE / XOP / AMLP / ICLN / NLR | 15 / 0 / 40 / 25 / 20% | 15 / 0 / 40 / 25 / 20% |
| Estimated annual return | 15.198581% | 14.798581% |
| Estimated annual volatility | 17.138330% | 17.138330% |
| Largest fund | 40% | 40% |
| 8% objective and 40% cap | Pass | Pass |
| Eligible 5-point-grid portfolios | 3,951 | 3,951 |

The prediction matched: the allocation and volatility did not change, and 40% × −1.00 percentage point = **−0.40 percentage point** in estimated portfolio return. The objective remains slack and covariance is unchanged; the minimum-volatility feasible mix therefore remains the same in this grid. The no-capital pilot decision remains unchanged. This is a narrow sensitivity, not proof of robustness to risk, correlations, costs, timing or a different mandate. The separate calculation applies the 40% cap; the existing app itself does not.

Reproduce this calculation from the repository root with Python 3, using the local files whose hashes appear above:

```sh
python3 -B - <<'PY'
import sys
sys.path.insert(0, 'Lab 15')
import portfolio as p
x = p.estimate_from_prices('Lab 15/prices.csv')
cov = p.covariance_matrix(x['correlation'], x['volatilities'])
i = x['names'].index('AMLP')
print('Assets:', x['names'], 'dates:', x['first_price_date'], x['last_price_date'])
print('AMLP annual return before/after:', x['returns'][i], x['returns'][i] - 0.01)
for label, delta in [('baseline', 0), ('changed', -0.01)]:
    returns = x['returns'].copy()
    returns[i] += delta
    candidates = []
    for weights in p.long_only_mixes(len(returns)):
        expected = p.portfolio_return(weights, returns)
        if max(weights) <= 0.4 + 1e-9 and expected >= 0.08 - 1e-9:
            candidates.append((p.portfolio_volatility(weights, cov), weights, expected))
    volatility, weights, expected = min(candidates, key=lambda row: row[0])
    print(label, 'weights', weights, 'return', expected, 'volatility', volatility,
          'cap pass', max(weights) <= 0.4 + 1e-9, 'eligible', len(candidates))
PY
```

## Repository and manifest audit

The 12-row list below is a readiness audit, not a completed Project 2 manifest. No Project 2 Brightspace assignment page or confirmed final Project 2 repository was found in the local files searched. The local course studio guide says submission mechanics and deadlines are on Brightspace.

| Row | Evidence found | Readiness / remaining action |
|---|---|---|
| Research-Evolution.pdf | None identified | Missing or unverified: original Edition A/receipt, Edition B and reconciliation. Locate and preserve the original; do not recreate a receipt. |
| Repository | Local `Lab 15/` files; `origin/lab20-readiness` has the prediction file | Final Project 2 repository and instructional-team access not established. The test's model/data were untracked and not in the prediction commit. |
| Visible executed output | Before/after table above | Visible in this file locally; output is not yet established as part of the final Project 2 repository. |
| Decision memo or deck | Decision line above; no Project 2 memo identified | A final memo/deck with matching numbers, date, conditions, monitoring and reversal remains unverified. |
| Validation-and-AI-Use.pdf | Lab 15 documents tests; this AI-run sensitivity | Final PDF, complete evidence and qualifying locked record not found. |
| Video 1 | None identified | Actual recording, link, title, duration, index and access unverified; maximum 3 minutes. |
| Transcript Video 1 | None identified | Corrected transcript of actual recording missing/unverified. |
| Video 2 | None identified | Actual recording, link, title, duration, index and access unverified; maximum 5 minutes. |
| Transcript Video 2 | None identified | Corrected transcript of actual recording missing/unverified. |
| Video 3 | None identified | Actual recording, link, title, duration, index and access unverified; maximum 5 minutes. |
| Transcript Video 3 | None identified | Corrected transcript of actual recording missing/unverified. |
| Optional deployed output | None identified | Optional unless the Brightspace brief says otherwise. |

**Tool and cold run:** `Lab 15/Lab 15.md` documents `streamlit run app.py` from `Lab 15/`, after installing Streamlit. Streamlit was not installed in the Python environment checked on November 17, so a clean interactive run was not completed. The README-only cold run, one-control mandate verdict and second-account access remain unverified. The app's documented missing 40% cap is a substantive failure. The pure-Python calculation above ran successfully and imposed that cap explicitly.

**Validation gaps:** No Project 2 frozen holdout, selection ledger, transaction-cost model, capacity analysis, implementation boundary, or complete monitoring/kill-rule record was identified. The reported 8% objective and 40% fund cap are provisional AI-assisted assumptions, not confirmed client terms. Lab 17 quarantines the proposed BAA signal pending decision-date vintage and release-time checks; the signal must not be used as if it were an ETF total return. Historical estimates are not forecasts.

## Partner challenge — simulated by Codex

**Challenge:** If the optimization app omits the 40% cap, why should the committee accept its 70% AMLP answer merely because it is stable to a return estimate?

**Creator response:** It should not. The unconstrained answer violates the working cap. A separate capped grid gives the 40% AMLP portfolio above; its single-input test passes the two specified numerical checks, but the application still needs to enforce the mandate and the broader validation gaps prevent an allocation recommendation. This is an AI-simulated review, not a real partner exchange.

## Must-fix actions and ownership

1. **Project owner:** identify the actual Project 2 submission, repository, Brightspace brief and deadline; verify the 12 manifest rows and access.
2. **Project owner:** confirm the mandate and implement and test the cap in the actual tool; complete a clean README-only run and publish matching output and memo.
3. **Project owner:** assemble baseline, holdout, timing, cost, capacity, selection, monitoring and reversal evidence; resolve or explicitly limit unsupported claims.
4. **Student:** supply the original Edition A and receipt, and any authentic human prediction, locked snapshot and AI-closed run required by the course. This AI-authored exercise must not be represented as satisfying that requirement.
5. **Student:** make the actual three distinct recordings and corrected transcripts, then verify links, durations and instructional-team access. No recordings or partner participation are claimed here.

AI disclosure: Codex drafted this file, made the prediction, performed the calculation and simulated the challenge at the user's request. The current activity is not a substitute for independent human authorship or a human partner.
