import os
import numpy as np
import pandas as pd
from scipy import stats

def run_mean_return_hypothesis_test():
    print(" Running statistical hypothesis testing engine (Alpha = 0.05)...")
    
    # Path settings
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "hypothesis_testing_summary.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Run log_returns_analytics.py first.")
        return

    # Load computed returns dataframe
    df = pd.read_csv(source_file)
    
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return', 
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return', 
        'sar_ksh_log_return'
    ]
    
    test_results = []
    
    print(" Calculating t-statistics and p-values...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        # Extract the specific currency series and drop any null values
        series = df[col].dropna()
        
        # Sample parameters needed for testing formulas
        sample_mean = series.mean()
        sample_std = series.std()
        n_obs = len(series)
        
        # Execute standard 1-sample t-test against an expected mean of 0
        # H0: mu = 0 vs Ha: mu != 0
        t_stat, p_value = stats.ttest_1samp(series, popmean=0)
        
        # Determine rejection outcome based on the 5% alpha threshold
        reject_h0 = "Reject H0 (Not Zero)" if p_value < 0.05 else "Fail to Reject H0 (Zero)"
        
        # Format name for presentation output
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        
        test_results.append({
            "Currency": currency_label,
            "Sample Mean": sample_mean,
            "Sample StdDev": sample_std,
            "Observations": n_obs,
            "t-Statistic": t_stat,
            "p-Value": p_value,
            "Conclusion (5% Alpha)": reject_h0
        })
        
    # Compile table summary 
    results_table = pd.DataFrame(test_results)
    
    # Round statistical figures cleanly for the professional layout
    results_table = results_table.round({
        "Sample Mean": 6, 
        "Sample StdDev": 6, 
        "t-Statistic": 4, 
        "p-Value": 6
    })
    
    # Save the output file out to documentation folder
    os.makedirs("documentation", exist_ok=True)
    results_table.to_csv(output_file, index=False)
    
    print("\n" + "="*115)
    print("                            HYPOTHESIS TESTING SUMMARY: MEAN DAILY LOG RETURNS")
    print("====================================================================================================")
    print(results_table.to_string(index=False))
    print("="*115)
    print(f" Statistical testing table successfully exported to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_mean_return_hypothesis_test()