# Fund Performance Analytics — Bluestock Capstone

## Included deliverables
- `Performance_Analytics.ipynb` — reproducible NAV return, CAGR, risk, alpha/beta, scorecard and benchmark chart workflow.
- `fund_scorecard.csv` — 40 schemes ranked on the task's weighted 0–100 composite score.
- `alpha_beta.csv` — OLS alpha and beta against NIFTY100 daily returns.
- `Benchmark_Comparison.png` — top five scorecard funds compared with NIFTY50 and NIFTY100 over the latest available three-year window.
- `Analysis_Notes.csv` — data coverage and methodological notes.

## Input data required to rerun notebook
The three required input datasets are included in `data/raw/`. Install: `pandas numpy matplotlib scipy jupyter`.

## Methodology
- Daily return = NAV(t) / NAV(t-1) - 1.
- CAGR uses the latest NAV and the last available NAV on/before the target anniversary date.
- Alpha/beta use OLS regression of daily fund returns on NIFTY100 daily returns in the latest three-year window. Alpha is annualized intercept × 252 × 100; beta is the regression slope.
- Sharpe = (annualized fund return − 6.5% risk-free rate) / annualized daily-return volatility.
- Sortino uses annualized downside deviation from negative daily returns only.
- Maximum drawdown = minimum(NAV / running maximum − 1).
- Scorecard weights: 30% 3Y CAGR rank + 25% Sharpe rank + 20% alpha rank + 15% inverse expense rank + 10% inverse drawdown rank. Percentile ranks are scaled to 0–100.

## Data limitation
The NAV dataset spans 2022-01-03 through 2026-05-29 (about 4.4 years), so a five-year CAGR cannot be independently calculated from the supplied NAV history. The supplied `07_scheme_performance.csv` 5-year return is retained separately in the scorecard as `cagr_5yr_pct_source_reported` and is not presented as a NAV-derived result.
