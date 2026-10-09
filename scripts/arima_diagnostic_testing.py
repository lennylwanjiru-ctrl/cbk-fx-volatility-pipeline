import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from statsmodels.tsa.stattools import adfuller

def run_arima_adf_diagnostics():
    print(" Executing ARIMA Pre-requisite: Fixed Lag ADF Diagnostics (8 Lags, Constant + Trend)...")
    
    # Path configurations
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "arima_adf_diagnostics.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Please run compute_returns.py first.")
        return

    # Load calculated returns dataset
    df = pd.read_csv(source_file)
    
    # Target log return columns for all 7 currencies
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return', 
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return', 
        'sar_ksh_log_return'
    ]
    
    diagnostic_records = []
    
    print(" Processing fixed-lag unit root regressions...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        series = df[col].dropna()
        
        # Execute ADF test forced to exactly 8 lags with constant and trend ('ct')
        # Setting autolag=None overrides automatic selection and forces exactly 8 lags
        result = adfuller(series, maxlag=8, regression='ct', autolag=None)
        
        adf_stat = result[0]
        p_value = result[1]
        crit_5pct = result[4]['5%']
        
        # Verify stationarity based on the alpha = 0.05 rule
        conclusion = "Stationary (Ready for ARIMA)" if p_value < 0.05 else "Non-Stationary (Needs Differencing)"
        
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        
        diagnostic_records.append({
            "Currency": currency_label,
            "ADF Stat (8 Lags)": adf_stat,
            "p-Value": p_value,
            "5% Critical Value": crit_5pct,
            "Stationarity Verdict": conclusion
        })
        
    # Compile metrics dataframe table
    summary_table = pd.DataFrame(diagnostic_records)
    summary_table = summary_table.round({
        "ADF Stat (8 Lags)": 4,
        "p-Value": 6,
        "5% Critical Value": 4
    })
    
    # Save the output file out to documentation folder
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*110)
    print("                       ARIMA PRE-REST DIAGNOSTIC: 8-LAG CONSTANT & TREND ADF TEST")
    print("==============================================================================================================")
    print(summary_table.to_string(index=False))
    print("="*110)
    print(f" Diagnostics successfully compiled and saved to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_arima_adf_diagnostics()