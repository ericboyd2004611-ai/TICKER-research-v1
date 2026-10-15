# Lab 13 — Meridian Foundation Reserve

AI-assisted working draft. Review the explanations in your own words before submitting, especially the parts assigned with AI closed. The code checks and probe below were executed; a partner exchange and personal quiz answer have not taken place.

## D — Which portfolios does the mandate permit?

A passes every rule that can be checked from the supplied holdings and weights. B fails the reserve, redemption-liquidity, and company-concentration rules. C fails the reserve rule. Passing these checks does not establish that A satisfies the entire mandate: the return objective needs supporting assumptions, turnover requires trading information, and S9 remains undefined.

Before optimization, the CIO must specify what the pilot should optimize and how risk will be measured. S2 supplies a return objective but does not itself specify an optimization criterion. S9 cannot be implemented as written.

## Statement types and IPS mapping

| Statement | Type | One-line reason and IPS role |
|---|---|---|
| S1: Seven-year horizon; annual rebalancing | Hard constraint | The horizon sets the planning period, and annual rebalancing sets the required portfolio-management schedule. |
| S2: CPI + 4% annually, net of costs, over rolling five years | Objective | It defines the desired real return, cost basis, and evaluation period; it is a target rather than a guaranteed result. |
| S3: $0.75 million quarterly; twelve months held in cash or daily-liquid government securities | Hard constraint | It requires $3 million, or 3% of this reserve, in the specified eligible holdings to support payouts. |
| S4: 60% global equities / 40% U.S. investment-grade bonds benchmark | Preference | Within the supplied categories, it is the reference portfolio for evaluation; no statement requires matching its allocation. |
| S5: Long-only; no borrowing, short sales, or derivatives | Hard constraint | It restricts the permitted positions and instruments. |
| S6: No single issuer above 8% | Hard constraint | Company exposures must be aggregated across securities and capped, subject to the stated exemptions. |
| S7: Annual turnover at most 25% without committee approval | Hard constraint | Trading above the limit requires committee approval; weights alone do not reveal annual turnover. |
| S8: At least 90% redeemable within five business days | Hard constraint | It sets a measurable portfolio-liquidity minimum. |
| S9: No calendar-year loss greater than 10%, with no measure or breach rule | Unverifiable promise | It lacks an operational risk definition and response procedure; uncertain market losses cannot be guaranteed away by checking weights. |
| S10: No sector, ESG, tax, or home-bias preference; pilot optimization target unstated | Missing | No additional preferences are imposed, but the decision criterion for optimization is absent. |

S4 is more precisely a benchmark designation than a preference for particular holdings. “Preference” is the closest of the assignment's five categories; it should not be turned into a mandatory 60/40 allocation.

## I — Checker and command

The standard-library checker is `mandate.py`. Its editable inputs contain the holdings, A–D weights, reserve size, distributions, coverage period, liquidity thresholds, and issuer exemptions. It computes the answers rather than storing the known results.

From the course folder, run:

```sh
python mandate.py
```

The payout reserve minimum is:

```text
4 × $0.75 million ÷ $100 million × 100 = 3.0%
```

The reserve calculation uses the table's reserve-eligible flag. Thus the Treasury 10-year note qualifies under the supplied definition even though its market price can fluctuate. Redemption liquidity and price stability are different properties.

Company exposure combines Acme's bonds and stock. Cash, Treasury securities, and diversified funds are exempt from the issuer cap. S9 is always printed as “requires CIO clarification” and is never tested.

### Code understanding quiz

Selected line:

```python
companies[issuer] = companies.get(issuer, 0) + weight
```

Quiz question: When B has 5% Acme bonds and 4% Acme stock, what does this line store after each position, and why does that cause an issuer-limit failure?

Your answer before explanation: **To be completed during the quiz.**

Explanation to review after answering: `get(issuer, 0)` retrieves the exposure already counted for that issuer, using zero if this is its first security. The two Acme positions accumulate to 5% and then 9%. The 9% company total exceeds the 8% limit even though neither security exceeds 8% individually.

## V — Verification against the known answer

Executed `python mandate.py` and checked the computed measures against the supplied values. Every A–C value matched.

| Rule | A | B | C |
|---|---|---|---|
| Weights sum to 100 | 100.0 pass | 100.0 pass | 100.0 pass |
| Long-only: lowest weight | 0.0 pass | 0.0 pass | 0.0 pass |
| Reserve ≥ 3.0% | 14.0 pass | 1.0 FAIL | 2.0 FAIL |
| Redeemable in five days ≥ 90% | 100.0 pass | 85.0 FAIL | 100.0 pass |
| Largest single company ≤ 8% | 0.0 pass | 9.0 FAIL | 8.0 pass |
| Calendar-year loss | requires CIO clarification | requires CIO clarification | requires CIO clarification |
| Verdict | passes every checkable rule | fails 3 rule(s) | fails 1 rule(s) |

### Negative-weight probe

Temporarily changed A's cash weight to −2% and global equity weight to 64% in memory, ran the checker, and restored the original inputs. The total remained 100%; only long-only failed.

| Measure | Probe result |
|---|---|
| Weight total | 100.0 pass |
| Lowest weight | −2.0 FAIL |
| Reserve-eligible weight | 10.0 pass |
| Redeemable within five days | 100.0 pass |
| Largest company | 0.0 pass |
| Verdict | fails 1 rule(s) |

The probe reserve is −2 + 2 + 10 = 10%. The saved A remains 2% cash and 60% global equities.

## E — Attack the checker

Candidate D uses only the permitted holdings:

| Holding | D weight |
|---|---:|
| Cash | 100% |
| Treasury bills | 0% |
| Treasury 10-year note | 0% |
| Global equity index fund | 0% |
| Investment-grade bond fund | 0% |
| Private real estate fund | 0% |
| Acme Corp bonds | 0% |
| Acme Corp stock | 0% |

D was added to the checker and run. Its total is 100.0%, lowest weight 0.0%, reserve 100.0%, five-day liquidity 100.0%, and largest company exposure 0.0%; it passes every checkable rule.

### Two-sentence judgment — draft to review independently

The objection holds as a suitability concern because passing the allocation checks does not demonstrate that 100% cash can credibly achieve the required real return. S2 decides the objection: the CIO can reasonably reject D for lacking a supported path to CPI + 4% net over rolling five-year periods, although the supplied data cannot prove its future return will miss that target.

### Partner exchange

No partner portfolio has been supplied, so a completed exchange cannot be reported. When reviewing it, cite the actual statement implicated: for example, S3 for inadequate eligible reserves, S6 for combined company exposure, or S2 for an unsupported return strategy even when the numerical checks pass.

## One question for the CIO — draft to review independently

**Should we minimize portfolio risk while targeting CPI + 4% net, or maximize expected return within an agreed risk limit?**

If the CIO prioritizes lower risk, I would favor more government securities and less equity, provided the return target remains credible. If the CIO prioritizes higher expected return, I would consider more equity within the agreed risk limit.

## Investment policy statement — explanation

An investment policy statement is the written agreement that translates a client's purpose into portfolio objectives, limits, and management responsibilities. It gives the CIO and investment team a consistent basis for constructing, monitoring, and evaluating the portfolio.

Objectives describe what the portfolio should accomplish, such as S2's real-return target. Constraints bound the permitted choices: S1 sets timing, S3 and S8 address cash needs and liquidity, S5 restricts instruments and positions, S6 limits concentration, and S7 governs turnover and approval. S4 supplies a performance reference. S9 needs a usable risk definition, and S10 exposes the missing optimization criterion. The statement-type table above maps all ten statements to these roles.

## Reflection — draft to personalize

A portfolio can pass every checkable rule and still be wrong for the client because the checker sees only the supplied weights and holding attributes. It does not estimate net real returns, model loss probabilities, evaluate trading history, or resolve the client's priorities. D illustrates the gap: abundant liquidity and no company concentration do not establish a credible strategy for the return objective. A's passing verdict likewise means only that it clears the five checks.

The statement type that is most ambiguous is S4. A benchmark looks like a portfolio allocation, but the CIO named it as a comparison standard rather than requiring those exact weights. I would classify it as a preference within the given choices while explaining its more precise role as a benchmark.

## Project 2 mandate — provisional draft

This is a proposed starting point for a speculative-growth company research portfolio, not a statement of a real client's confirmed needs. Replace or confirm these assumptions with the actual Project 2 client.

**Objective:** Seek long-term capital growth over seven years and evaluate net performance against a broad global equity benchmark.

**Hard constraints:** Fully funded and long-only; no borrowing, short sales, or derivatives; no company above 8% of total portfolio value across its securities; at least 90% redeemable within five business days; review annually. Any spending reserve must be sized from the client's actual withdrawals before investing the remainder.

**One question for the client:** What temporary loss can you tolerate without needing to sell or abandon the plan?

The answer changes the design: a lower tolerance would call for more cash and government securities and less equity exposure; a higher tolerance could support more diversified equity exposure. The return objective and these constraints remain provisional until the client confirms the horizon, cash needs, and risk tolerance.

## GitHub checkout

Files have been created locally; this draft has not been committed or pushed. After completing the personal quiz, independent review, partner exchange, and client-specific mandate, push the finished files and submit their GitHub links in the Lab 13 quiz.

Expected links after publishing to `main` (confirm the branch):

- Markdown: https://github.com/ericboyd2004611-ai/TICKER-research-v1/blob/main/Week%2008/lab%2013.md
- Checker: https://github.com/ericboyd2004611-ai/TICKER-research-v1/blob/main/mandate.py
