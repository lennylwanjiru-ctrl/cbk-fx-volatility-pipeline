""""

Module: ARIMA Pre-Requisite Unit Root Stationarity Testing (Fixed 8-Lag ADF Diagnostics)
"""


import os
import logging
import warnings
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Silence non-critical futures and optimization warnings
warnings.filterwarnings('ignore', category=FutureWarning)

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_arima_adf_diagnostics():
    """
    Ingests daily exchange logs, executes forced 8-lag ADF unit root tests with 
    constant and trend attributes, and exports a stationarity validation ledger.
    """
    logging.info("Initializing ARIMA pre-requisite statistical testing suite...")
    
    # Define relative workspace path space boundaries
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "arima_adf_diagnostics.csv")
    
    if not os.path.exists(source_file):
        logging.error(f"Execution Aborted: Base data registry missing at path: {source_file}")
        return
        
    df = pd.read_csv(source_file)
    
    # Target macro-economic log return columns for all 7 active currencies
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return',
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return',
        'sar_ksh_log_return'
    ]
    
    diagnostic_records = []
    
    logging.info("Executing fixed-lag unit root regressions across currency portfolios...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        # Standardize labels into standard financial currency conventions (e.g., USD/KSH)
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        series = df[col].dropna()
        
        try:
            # Execute ADF unit root test forced to exactly 8 lags with constant and trend ('ct')
            result = adfuller(series, maxlag=8, regression='ct', autolag=None)
            
            adf_stat = result[0]
            p_value = result[1]
            crit_5pct = result[4]['5%']
            
            # Formulate strict algorithmic classification status codes for database tracking
            if p_value < 0.05:
                stationarity_status_id = "STATIONARY_READY_FOR_ARIMA"
            else:
                stationarity_status_id = "NON_STATIONARY_NEEDS_DIFFERENCING"
                
            diagnostic_records.append({
                "Currency": currency_label,
                "ADF_Stat_8_Lags": round(adf_stat, 4),
                "p_Value": round(p_value, 6),
                "Critical_Value_5pct": round(crit_5pct, 4),
                "Stationarity_Code": stationarity_status_id
            })
            
        except Exception as e:
            logging.error(f"Unit Root Regression Failed for sequence [{currency_label}]: {str(e)}")
            continue

    # Compile and serialize the final time-series validation ledger
    summary_table = pd.DataFrame(diagnostic_records)
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    logging.info(f"Diagnostics successfully compiled and saved to: {output_file}")
    
    # Corporate Auditing Layout Reporting
    print("\n" + "="*110)
    print("ARIMA PRE-TEST DIAGNOSTIC: 8-LAG CONSTANT & TREND ADF UNIT ROOT MATRIX")
    print("="*110)
    print(summary_table.to_string(index=False))
    print("="*110 + "\n")

if __name__ == "__main__":
    run_arima_adf_diagnostics()
    
