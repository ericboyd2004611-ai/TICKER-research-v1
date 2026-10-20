# Lab 14 — Meridian Simple Portfolios

**Question:** What does each simple portfolio earn and risk, and does any of them meet the Meridian mandate?

**Answer:** Equal weight and inverse volatility are the two diversified portfolios that pass every Meridian rule these numbers can test. Neither can be shown to meet the whole mandate. CPI + 4% net can't be confirmed without CPI and cost data, and the "no calendar-year loss over 10%" promise can't be guaranteed by any portfolio. 100% GovBond also passes the testable rules but earns only 4.00%.

## What each portfolio earns and risks

Annualized, before costs. Run `python3 lab14_portfolio.py` in this folder to reproduce.

| Portfolio | GovBond | CorpBond | USEquity | IntlEquity | Expected return | Volatility | Chance of a loss worse than −10%* |
|---|---:|---:|---:|---:|---:|---:|---:|
| 100% GovBond | 100% | 0% | 0% | 0% | 4.00% | 6.00% | 0.98% |
| 100% CorpBond | 0% | 100% | 0% | 0% | 5.50% | 9.00% | 4.25% |
| 100% USEquity | 0% | 0% | 100% | 0% | 8.50% | 18.00% | 15.20% |
| 100% IntlEquity | 0% | 0% | 0% | 100% | 8.00% | 20.00% | 18.41% |
| Equal weight | 25.0% | 25.0% | 25.0% | 25.0% | 6.50% | 9.80% | 4.62% |
| Inverse volatility | 43.5% | 29.0% | 14.5% | 13.0% | 5.61% | 6.80% | 1.09% |
| 60/40 benchmark (30/30/20/20 split) | 20.0% | 20.0% | 30.0% | 30.0% | 6.85% | 11.27% | 6.75% |

*Assumes normally distributed yearly returns. This is an illustration, not a forecast.

Diversification lowers risk: equal weight's 9.80% volatility is well below the 13.25% average of its four assets' volatilities. GovBond moves slightly opposite to both equity classes (correlations −0.10 and −0.05), so it partly offsets them.

## Does any meet the Meridian mandate?

| Meridian rule | 100% GovBond | 100% CorpBond | 100% US/Intl Equity | Equal weight | Inverse volatility | 60/40 benchmark |
|---|---|---|---|---|---|---|
| Long-only, sums to 100% | pass | pass | pass | pass | pass | pass |
| ≥ 3% payout reserve in government securities† | pass | **FAIL** | **FAIL** | pass (25%) | pass (43.5%) | pass (20%) |
| CPI + 4% net of costs | covers CPI up to 0.00% | 1.50% | 4.50% / 4.00% | 2.50% | 1.61% | 2.85% |
| No calendar-year loss > 10% | cannot be guaranteed by any portfolio | | | | | |
| Issuer ≤ 8%, 90% redeemable in 5 days, turnover ≤ 25% | not testable without holdings data | | | | | |

†Treats GovBond as the reserve-eligible government securities.

The CPI row shows the highest inflation each portfolio's return covers before costs: expected return minus 4%. For example, equal weight meets CPI + 4% only if inflation is 2.5% or lower and costs are zero.

## Checks

The inputs pass every validation check:
- the correlation matrix is symmetric, with 1s on the diagonal
- the covariance matrix is valid (positive semidefinite)
- there are no missing values

Hand checks match the code:
- equal-weight return: (4.0 + 5.5 + 8.5 + 8.0) ÷ 4 = 6.50%
- equal-weight volatility: √(0.15382 ÷ 16) = 9.80%
- one covariance cell: 0.18 × 0.75 × 0.20 = 0.027

## Explain the code — portfolio.py

### Function 1: covariance_matrix()

```python
def covariance_matrix(corr, vols):
    """cov[i][j] = correlation[i][j] x volatility[i] x volatility[j]."""
    n = len(vols)
    return [[corr[i][j] * vols[i] * vols[j] for j in range(n)] for i in range(n)]
```

This function takes the correlations and individual asset volatilities and uses them to create a covariance matrix.

- `def covariance_matrix(corr, vols):` takes two inputs: the correlation matrix, which shows how the assets move relative to each other, and the volatility of each asset.
- The docstring explains the formula the function uses. It is only a description and does not affect the calculations.
- `n = len(vols)` determines how many assets are in the portfolio. Since there are four assets, n equals 4.
- The return statement creates a 4 × 4 matrix by multiplying the correlation between two assets by each of their volatilities.

The matrix includes two types of values:

- **Diagonal values:** These represent each asset's individual variance. For example, equity has a volatility of 16%, so its variance is 1 × 0.16 × 0.16 = 0.0256.
- **Off-diagonal values:** These represent the covariance between different assets. For IG bonds and equity, the calculation is 0.25 × 0.06 × 0.16 = 0.0024.

The matrix is also symmetric, meaning the covariance between IG bonds and equity is the same as the covariance between equity and IG bonds.

### Function 2: portfolio_volatility()

```python
def portfolio_volatility(weights, cov):
    n = len(weights)
    variance = sum(weights[i] * weights[j] * cov[i][j] for i in range(n) for j in range(n))
    return math.sqrt(variance)
```

This function calculates the overall portfolio volatility using the asset weights and the covariance matrix from the previous function.

- `n = len(weights)` counts the number of assets in the portfolio, which is four in this case.
- `variance = sum(...)` is the main calculation. It goes through all 16 combinations of assets in the covariance matrix. For each combination, it multiplies the two asset weights by their covariance and adds everything together. This gives us the portfolio's total variance.
- `return math.sqrt(variance)` takes the square root of the variance to calculate the portfolio's standard deviation, also known as volatility.

The important part is that this function accounts for both the individual risks of each asset and how the assets move together. Without including the correlations, the portfolio volatility would not be calculated correctly.

### Example: Benchmark Portfolio (40% IG Bonds, 60% Equity)

For the benchmark, 40% is invested in IG bonds and 60% in equity. The other two assets have weights of zero, so they do not contribute to the calculation.

| Asset combination | Calculation | Result |
|---|---|---:|
| IG bonds × IG bonds | 0.4 × 0.4 × 0.0036 | 0.000576 |
| Equity × Equity | 0.6 × 0.6 × 0.0256 | 0.009216 |
| IG bonds × Equity | 0.4 × 0.6 × 0.0024 | 0.000576 |
| Equity × IG bonds | 0.6 × 0.4 × 0.0024 | 0.000576 |
| **Total variance** | | **0.010944** |

Finally, we take the square root: √0.010944 = 0.1046 = **10.46%**

This means the benchmark portfolio has an annual volatility of approximately 10.46%.

### How I would explain it to my partner

The first function, covariance_matrix, calculates how the assets move together using their correlations and volatilities. It creates a matrix that contains the variance of each individual asset and the covariance between different assets.

The second function, portfolio_volatility, takes that matrix and combines it with the portfolio weights. It multiplies each pair of weights by the corresponding covariance, adds the results, and takes the square root to get the portfolio's overall volatility.

For our benchmark, this comes out to 10.46%. We also tested what happens when we leave out the correlation terms, and the result was only 9.90%. This shows why including the relationships between assets is important when measuring portfolio risk.

### Partner question and my answer

**Question:** Why does the loop count IG–equity twice?

**Answer:** The loop counts IG bonds and equity twice because the covariance matrix includes both [2][3] (IG bonds with equity) and [3][2] (equity with IG bonds). Even though these represent the same relationship, both are included in the calculation. This is equivalent to multiplying the covariance term by 2 in the standard portfolio variance formula: 2 × weight of IG × weight of equity × covariance.
