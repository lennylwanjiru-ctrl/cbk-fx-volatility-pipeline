"""

Module: Data Transformations & Mathematical Descriptive Statistics Core

"""

import os
import logging
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_log_returns_statistical_analysis():
    """
    Ingests standardized daily currency prices, transforms continuous values into log returns,
    and maps an expansive 9-point econometric descriptive statistics matrix.
    """
    logging.info("Initializing continuous log returns descriptive statistical engine...")
    
    source_file = os.path.join("data", "cbk_exchange_rates_clean.csv")
    output_file = os.path.join("documentation", "log_returns_descriptive_statistics.csv")
    
    if not os.path.exists(source_file):
        logging.error(f"Execution Aborted: Cleaned dataset missing at destination path: {source_file}")
        return

    df = pd.read_csv(source_file)
    
    # Active currency columns tracking framework
    currency_cols = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    stats_records = []

    logging.info("Computing requested econometric statistical calculations across portfolios...")
    for col in currency_cols:
        if col not in df.columns:
            continue
            
        # Format name strings to professional currency presentation layouts (e.g., USD/KSH)
        display_name = col.upper().replace('_', '/')
        prices = df[col].astype(float)
        
        # Calculate continuous log returns: ln(P_t / P_{t-1})
        log_returns = np.log(prices / prices.shift(1)).dropna()
        
        # Extract individual descriptive distribution attributes
        mean_val = log_returns.mean()
        variance_val = log_returns.var()
        std_dev_val = log_returns.std()
        median_val = log_returns.median()
        skew_val = skew(log_returns)
        
        # Compute both regular Pearson kurtosis and fisher-corrected excess kurtosis
        raw_kurt = kurtosis(log_returns, fisher=False)
        excess_kurt = kurtosis(log_returns, fisher=True)
        
        min_val = log_returns.min()
        max_val = log_returns.max()

        # Build structural record row dictionary to preserve mathematical telemetry
        stats_records.append({
            "Currency": display_name,
            "Mean": mean_val,
            "Variance": variance_val,
            "Std_Deviation": std_dev_val,
            "Median": median_val,
            "Skewness": skew_val,
            "Kurtosis": raw_kurt,
            "Excess_Kurtosis": excess_kurt,
            "Minimum": min_val,
            "Maximum": max_val
        })

    # Compile measurements into an unified summary data frame
    summary_table = pd.DataFrame(stats_records)
    
    # Force strict 6-decimal point floating numeric limits for professional layout audits
    summary_table = summary_table.round(6)
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    logging.info(f"Descriptive statistics matrix successfully exported to: {output_file}")

    # Corporate Auditing Layout Reporting
    print("\n" + "="*110)
    print("FINANCIAL ECONOMETRICS LEDGER: CONTINUOUS LOG RETURNS 9-POINT DESCRIPTIVE STATISTICS")
    print("="*110)
    print(summary_table.to_string(index=False))
    print("="*110 + "\n")

if __name__ == "__main__":
    run_log_returns_statistical_analysis()
   
