import os
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def run_stationarity_diagnostic_test():
    print(" Running Augmented Dickey-Fuller (ADF) Stationarity Test Engine...")
    
    # Path configurations
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "stationarity_testing_summary.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Run compute_returns.py first.")
        return

    # Load calculated returns data
    df = pd.read_csv(source_file)
    
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return', 
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return', 
        'sar_ksh_log_return'
    ]
    
    adf_results = []
    
    print(" Calculating ADF statistics, critical values, and p-values...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        # Extract series and drop any missing rows
        series = df[col].dropna()
        
        # Execute the Augmented Dickey-Fuller test
        # maxlag=None lets statsmodels automatically find the best lag structure using AIC
        result = adfuller(series, autolag='AIC')
        
        adf_stat = result[0]
        p_value = result[1]
        critical_5pct = result[4]['5%']
        
        # Determine stationary outcome based on 5% alpha threshold
        is_stationary = "Stationary (Reject H0)" if p_value < 0.05 else "Non-Stationary (Fail to Reject H0)"
        
        # Clean currency label for presentation output layout
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        
        adf_results.append({
            "Currency": currency_label,
            "ADF Statistic": adf_stat,
            "p-Value": p_value,
            "5% Critical Value": critical_5pct,
            "Test Outcome": is_stationary
        })
        
    # Compile summary table dataframe
    summary_table = pd.DataFrame(adf_results)
    
    # Round statistical figures to 6 decimals for cleaner portfolio formatting
    summary_table = summary_table.round({
        "ADF Statistic": 4,
        "p-Value": 6,
        "5% Critical Value": 4
    })
    
    # Save output to documentation folder
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*95)
    print("                         ECONOMETRIC DIAGNOSTIC: STATIONARITY TESTING (ADF)")
    print("===============================================================================================")
    print(summary_table.to_string(index=False))
    print("="*95)
    print(f" Stationarity testing report successfully saved to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_stationarity_diagnostic_test()