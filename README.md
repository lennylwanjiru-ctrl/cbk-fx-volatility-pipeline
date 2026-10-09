# Central Bank of Kenya (CBK) FX Volatility Pipeline & Econometric Analytics Engine

An enterprise-grade financial data engineering pipeline and quantitative risk-forecasting engine built to process multi-currency historical exchange rates versus the Kenyan Shilling (KES) across a 25-year timeline horizon (2001 - 2026).


---

##  Business & Actuarial Value Proposition
In corporate treasury, banking, and insurance sectors, managing currency risk waves is critical for solvency and asset-liability matching. This project provides a robust framework to:
* **Automate Data Integrity**: Strip out anomalies from unstructured historical tracking data to deliver a single source of truth for downstream business intelligence.
* **Identify Structural Risk Breakpoints**: Mathematically prove structural non-stationarity versus mean-reverting behaviors across foreign reserve asset pairs.
* **Model Asymmetric Shocks**: Capture the "leverage effect"—the financial reality that negative macroeconomic updates drive currency volatility waves harder than positive ones.
* **Deploy Out-of-Sample Projections**: Generate an explicit 5-day predictive risk horizon to optimize hedging, pricing, and Value-at-Risk (VaR) allocations.

---

##  Architecture & Pipeline Engineering Component

The repository enforces a strict separation of concerns, transitioning an academic workflow into a production-ready software environment:

* **`data/`**: Staging layer containing processed clean currency records and generated mathematical return matrices.
* **`scripts/`**: Core production-grade automated engineering and forecasting modules:
    * `clean_data.py`: **Data Quality Layer**. Programmatically normalizes nested scrape headers, sanitizes text strings containing formatting commas, removes duplicated date records to secure primary key constraints, and applies forward-fill (`ffill`) rules to smoothly patch market closure gaps.
    * `compute_returns.py`: **Feature Engineering Engine**. Transforms raw daily spot levels into independent arrays for both simple percentage changes and continuously compounded geometric Log Returns (\(\ln(P_t/P_{t-1})\)).
    * `hypothesis_testing.py`: **Inference Testing Engine**. Executes formal 1-sample t-tests at an α = 0.05 threshold to verify the zero-mean random walk properties of daily innovations.
    * `stationarity_testing.py`: **Econometric Diagnostics**. Runs Augmented Dickey-Fuller (ADF) models to test for unit roots and ensure the statistical stability of data prior to predictive scaling.
    * `volatility_diagnostic_testing.py`: **Variance Validation Engine**. Executes Engle’s ARCH-LM test up to 40 lags to evaluate conditional variance fluctuations and map volatility clustering.
    * `advanced_volatility_forecasting.py`: **Predictive Risk Model**. Fits asymmetric **EGARCH(1,1)** and **GJR-GARCH(1,1)** architectures paired with heavy-tailed Student-t distributions to output 5-day ahead conditional standard deviation forecasts.
* **`documentation/`**: Houses independent high-resolution graphic plots, density distribution subplots overlaying theoretical normal distributions, and the master `project_specs.md` detailing simple English findings for stakeholder reporting.

---

##  Enterprise Tech Stack
* **Language Layer**: Python 3.10+ (Core execution environment)
* **Data Engineering & Visualization**: `pandas`, `numpy`, `matplotlib`, `seaborn`
* **Advanced Financial Econometrics**: `scipy.stats`, `statsmodels.tsa`, `arch`
* **Downstream Integration Capable**: Ready for structured schema injection via SQL (PostgreSQL/MySQL) and live connection streaming to Power BI executive dashboards.

---

##  High-Impact Analytical Milestones

1. **Perfect Stationarity Achieved**: While raw currency spot rates exhibit long-term deterministic trends, the feature engineering pipeline successfully stabilizes the data. The log return series achieved an ADF p-value of **0.000000** across all 7 tracked currencies, satisfying the primary prerequisite for time-series forecasting.
2. **Volatility Clustering Proven**: The ARCH-LM diagnostic test strongly rejected the constant variance hypothesis across all lag checkpoints (10 up to 40 lags) with p-values of **0.000000** and exceptionally high LM statistics (peaking at 863.66). This mathematically proves that risk travels in clusters and waves, validating the use of GARCH family models over basic linear regressions.
3. **Out-of-Sample Volatility Expansion**: The final forecasting system isolates the structural leverage effects (e.g., USD/KSH leverage coefficient of **0.285491**) and maps an expanding daily risk matrix for the upcoming trading week. This offers quantitative teams clear, actionable visibility into how risk spreads cascade dynamically day-by-day.
4.