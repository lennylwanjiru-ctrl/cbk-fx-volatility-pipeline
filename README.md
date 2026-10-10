# Central Bank of Kenya (CBK) Foreign Exchange Volatility Pipeline & Econometric Forecasting Engine
**Lead Analyst:** Lenny Wanjiru | *Dedan Kimathi University of Technology (DeKUT)*  
**Core Stack:** Python, SQLite, `arch`, `statsmodels`, `scipy`, `seaborn`, `matplotlib`



##  The Problem Being Solved (In Simple English)
Commercial banks, import-export companies, and government offices in Kenya constantly struggle with a major issue: **unpredictable changes in foreign exchange rates**. When the Kenyan Shilling (KES) suddenly drops or spikes against major world currencies like the US Dollar or the Euro, it instantly disrupts business operations. Importers face unexpected extra costs for goods, local companies struggle to budget for raw materials, and institutional investors risk losing millions due to market shifts. 

Traditional tracking models fail because they try to project currency movements using a simple, predictable straight line. In reality, financial markets don't move in a straight line; they experience volatile clusters where wild ups and downs feed on each other over time. 

I built this quantitative data pipeline to solve this exact issue. The system cleans historical Central Bank of Kenya exchange rates, checks the data for core statistical properties, and deploys advanced time-series forecasting models (ARIMA and GARCH). By converting raw daily price records into a clear 5-day out-of-sample volatility forecast, this platform allows organizations to mathematically predict currency risk shifts, enabling them to protect their money and stabilize operations ahead of market shocks.



##  Who Will Benefit From This Platform?
This framework translates complex macroeconomic anomalies into clear, actionable metrics to protect multiple stakeholders:

*   **Corporate Treasury Teams (e.g., Safaricom, EABL):** Provides clear cash flow risk metrics to help managers time currency conversions and budget for international supply chain shipments without facing surprise losses.
*   **Commercial Bank Risk Managers (e.g., NCBA, Equity Bank):** Delivers precise mathematical volatility estimates to guide currency traders, set optimal asset-liability margins, and manage regulatory capital reserves safely.
*   **Import-Export Business Owners:** Gives non-technical managers a straightforward risk outlook to help them negotiate stable contract pricing with international partners.
*   **Macroeconomic Policy Advisors:** Generates structural trend analytics to help analysts study exchange stability and track the real-world impact of central bank interventions.



##  The 6-Phase Technical Roadmap
To audit or execute this forecasting engine, run the operational scripts sequentially within your terminal to preserve data file dependencies across the environment:

1.  **`clean_data.py`** *(Data Quality Layer)*  
    Ingests raw scrapped currency logs, normalizes column headers to a uniform standard, and fixes data gaps using a clean forward-backward interpolation padding loop.
2.  **`simple_returns_analytics.py` & `log_returns_analytics.py`** *(Feature Engineering Core)*  
    Transforms raw asset price arrays into daily percentage changes and continuous log returns, executing a robust 9-point statistical distribution matrix.
3.  **`distribution_analysis.py` & `hypothesis_testing.py`** *(Exploratory Inferences)*  
    Generates empirical histograms overlaid with theoretical Gaussian parametric curves and runs a 1-sample t-test against a population mean of 0 to isolate true risk relativities.
4.  **`stationarity_testing.py` & `arima_diagnostic_testing.py`** *(Pre-requisite Regressions)*  
    Executes automated and fixed 8-lag Augmented Dickey-Fuller (ADF) unit root regressions to check for mathematical stationarity before launching forecasting models.
5.  **`arma_model_selection.py` & `residual_lag_analysis.py`** *(Model Optimization Suite)*  
    Runs an automated grid search to find optimal lag orders based on minimum AIC checks, and performs a 20-lag Ljung-Box Q-test on residuals to verify white noise behavior.
6.  **`volatility_diagnostic_testing.py` & `advanced_volatility_forecasting.py`** *(Volatility Predictions)*  
    Scans for variance clustering using an Engle ARCH-LM test up to 40 lags, fits advanced EGARCH(1,1) and GJR-GARCH(1,1) asymmetric models, and exports the final 5-day currency volatility forecast matrix.

---

## Econometric Metrics & High-Impact Milestones
*   **Perfect Stationarity Achieved:** While raw currency spot rates exhibit long-term trends, the feature engineering scripts successfully stabilize the data. The log return series achieved an ADF p-value of **0.000000** across all 7 tracked currencies, satisfying the primary stationarity prerequisite for time-series forecasting.
*   **Volatility Clustering Proven:** The ARCH-LM diagnostic test rejected the constant variance hypothesis across all lag checkpoints (peaking at a high LM statistic of **863.66**). This mathematically proves that exchange rate risk travels in wave clusters, validating the use of advanced GARCH models over simple linear alternatives.
*   **Asymmetric Leverage Extraction:** Out-of-sample volatility engines capture true structural leverage effects (e.g., the USD/KES leverage coefficient of **0.285491**), exposing how negative macroeconomic updates drive currency volatility waves harder than positive news.



##  Project Repository Directory Structure
```text
cbk-fx-volatility-pipeline/
├── data/
│   ├── cbkScrappeddata.csv               # Raw unstructured historical exchange records
│   ├── cbk_exchange_rates_clean.csv      # Cleaned daily currency master records
│   └── cbk_exchange_returns_final.csv    # Final processed simple and log return series
├── documentation/
│   ├── currency_plots/                   # Standalone high-resolution currency trend graphs
│   ├── distribution_plots/               # Empirical vs. normal curve overlay charts
│   ├── log_returns_descriptive_statistics.csv # 9-point descriptive statistical tables
│   ├── arima_adf_diagnostics.csv         # Unit root stationarity validation registries
│   ├── arch_lm_test_summary.csv          # Engle ARCH-LM volatility clustering logs
│   └── volatility_forecast_projections.csv # Final 5-day out-of-sample econometric forecasts
├── scripts/
│   ├── clean_data.py                     # Schema standardization and normalization script
│   ├── simple_returns_analytics.py       # Daily simple returns feature compiler
│   ├── log_returns_analytics.py          # Continuous log returns mathematical transformer
│   ├── descriptive_returns_pipeline.py   # High-resolution time-series plotting engine
│   ├── distribution_analysis.py          # Empirical histogram visualization builder
│   ├── hypothesis_testing.py             # 1-sample t-test inferential statistics core
│   ├── stationarity_testing.py           # Automated ADF stationarity diagnostic script
│   ├── arima_diagnostic_testing.py      # Forced 8-lag trend ADF unit root matrix analyzer
│   ├── arma_model_selection.py           # Automated ARMA(p,q) parameter grid search compiler
│   ├── residual_lag_analysis.py          # ADF(8) regression and Ljung-Box Q-test utility
│   ├── volatility_diagnostic_testing.py  # ARIMA filtering and Engle ARCH-LM test engine
│   └── advanced_volatility_forecasting.py # Asymmetric EGARCH and GJR-GARCH forecasting core
└── README.md                             # Master repository presentation layout brief
```



##  Quick Start Execution Guide
Ensure you have your required Python dependencies active within your local terminal environment before running the operational pipeline modules sequentially:

```bash
# Install core quantitative and time-series dependencies
pip install pandas numpy scipy statsmodels arch matplotlib seaborn

# Run the complete data analytics and volatility pipeline in order
python scripts/clean_data.py
python scripts/simple_returns_analytics.py
python scripts/log_returns_analytics.py
python scripts/descriptive_returns_pipeline.py
python scripts/distribution_analysis.py
python scripts/hypothesis_testing.py
python scripts/stationarity_testing.py
python scripts/arima_diagnostic_testing.py
python scripts/arma_model_selection.py
python scripts/residual_lag_analysis.py
python scripts/volatility_diagnostic_testing.py
python scripts/advanced_volatility_forecasting.py
```
