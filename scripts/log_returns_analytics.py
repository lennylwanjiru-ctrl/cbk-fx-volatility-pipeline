import os
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

def run_log_returns_analysis():
    print(" Executing Question 5: Continuous Log Returns Descriptive Statistics...")
    
    # Locate cleaned source data file paths
    source_file = os.path.join("data", "cbk_exchange_rates_clean.csv")
    output_file = os.path.join("documentation", "question_5_log_returns.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing file: {source_file}. Please run your cleaning script first.")
        return

    # Load cleaned dataset matrix
    df = pd.read_csv(source_file)
    
    # Active currency columns list matching our core tracking framework
    currency_cols = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    
    stats_records = []
    
    for col in currency_cols:
        if col not in df.columns:
            continue
            
        prices = df[col].astype(float)
        
        # Calculate continuous log returns: ln(P_t / P_{t-1})
        log_returns = np.log(prices / prices.shift(1)).dropna()
        
        # Compute the 9 requested econometric statistical calculations
        mean_val = log_returns.mean()
        variance_val = log_returns.var()
        std_dev_val = log_returns.std()
        median_val = log_returns.median()
        skew_val = skew(log_returns)
        raw_kurt = kurtosis(log_returns, fisher=False)  # Regular kurtosis
        excess_kurt = kurtosis(log_returns, fisher=True) # Excess kurtosis
        min_val = log_returns.min()
        max_val = log_returns.max()
        
        # Format name for clear table display presentation style
        display_name = col.replace('_', '/').upper()
        
        # Build our row data record dictionary
        stats_records.append({
            "Currency": display_name,
            "Mean": mean_val,
            "Variance": variance_val,
            "Std Deviation": std_dev_val,
            "Median": median_val,
            "Skewness": skew_val,
            "Kurtosis": raw_kurt,
            "Excess Kurtosis": excess_kurt,
            "Minimum": min_val,
            "Maximum": max_val
        })

    # Group measurements into a structured dataframe
    summary_table = pd.DataFrame(stats_records)
    
    # Round figures to 6 decimal places for exact consistent presentation format
    summary_table = summary_table.round(6)
    
    # Save the resulting summary matrix out to documentation folder
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*110)
    print("                    QUESTION 5: DAILY LOG RETURNS DESCRIPTIVE STATISTICS")
    print("="*110)
    print(summary_table.to_string(index=False))
    print("="*110)
    print(f"🏆 Table successfully exported and saved to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_log_returns_analysis()