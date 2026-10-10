"""

Module: Econometric Pre-requisites & Automated ADF Unit Root Stationarity Testing

"""

import os
import logging
import warnings
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Silence non-critical statsmodels performance warnings
warnings.filterwarnings('ignore')

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_stationarity_diagnostic_test():
    """
    Ingests daily log returns, executes automated Augmented Dickey-Fuller (ADF) unit root 
    tests via AIC minimization, and exports a structural validation registry ledger.
    """
    logging.info("Initializing automated ADF stationarity testing engine...")
    
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "stationarity_testing_summary.csv")
    
    if not os.path.exists(source_file):
        logging.error(f"Execution Aborted: Base data registry missing at destination path: {source_file}")
        return
        
    df = pd.read_csv(source_file)
    
    # Complete systemic currency log return series for validation checks
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return',
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return',
        'sar_ksh_log_return'
    ]
    
    adf_results = []
    
    logging.info("Calculating ADF statistics, critical values, and p-values...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        # Standardize labels into standard financial currency conventions (e.g., USD/KSH)
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        series = df[col].dropna()
        
        try:
            # Execute the Augmented Dickey-Fuller test with automated lag structure optimization
            result = adfuller(series, autolag='AIC')
            
            adf_stat = result[0]
            p_value = result[1]
            critical_5pct = result[4]['5%']
            
            # Formulate strict algorithmic classification tokens for relational database storage
            if p_value < 0.05:
                stationarity_token_id = "STATIONARY_REJECT_H0"
            else:
                stationarity_token_id = "NON_STATIONARY_FAIL_TO_REJECT_H0"
                
            adf_results.append({
                "Currency": currency_label,
                "ADF Statistic": adf_stat,
                "p-Value": p_value,
                "5% Critical Value": critical_5pct,
                "Test Outcome": stationarity_token_id
            })
            
        except Exception as e:
            logging.error(f"Unit Root Regression Inversion Failed for asset sequence [{currency_label}]: {str(e)}")
            continue

    # Compile measurements into a unified summary data frame
    summary_table = pd.DataFrame(adf_results)
    
    # Apply standard 6-decimal floating limits across background database records
    summary_table = summary_table.round(6)
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    logging.info(f"Stationarity testing metrics matrix successfully exported to: {output_file}")
    
    # Tweak custom visual roundings to optimize terminal display aesthetics
    summary_table = summary_table.round({
        "ADF Statistic": 4,
        "p-Value": 6,
        "5% Critical Value": 4
    })

    # Corporate Auditing Layout Reporting
    print("\n" + "="*95)
    print("ECONOMETRIC DIAGNOSTIC: AUTOMATED STATIONARITY TESTING (ADF REGRESSION MATRIX via AIC)")
    print("="*95)
    print(summary_table.to_string(index=False))
    print("="*95 + "\n")

if __name__ == "__main__":
    run_stationarity_diagnostic_test()
