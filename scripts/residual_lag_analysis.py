import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox

def analyze_residual_lags():
    print(" Executing ARIMA Part (ii): Residual Autocorrelation Analysis (First 20 Lags)...")
    
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "residual_lag_analysis_summary.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Please run compute_returns.py first.")
        return

    df = pd.read_csv(source_file)
    
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return', 
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return', 
        'sar_ksh_log_return'
    ]
    
    residual_records = []
    
    print(" Reconstructing ADF regressions and testing residual white noise...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        series = df[col].dropna().values
        n = len(series)
        
        # Reconstruct the ADF(8) model matrix: Delta Y_t = alpha + beta*t + gamma*Y_{t-1} + sum(delta_i * Delta Y_{t-i})
        # For simple and clean implementation, we extract the residuals by fitting an AR(8) with trend
        dy = np.diff(series)
        n_dy = len(dy)
        
        # Target variable: Delta Y_t (from index 8 to end)
        Y = dy[8:]
        
        # Regressors matrix
        X = []
        t_steps = np.arange(9, n_dy + 1)
        
        for t in range(8, n_dy):
            row = [1, t_steps[t-8], series[t]] # Constant, Trend, Y_{t-1}
            for lag in range(1, 9):
                row.append(dy[t-lag]) # Lags of Delta Y
            X.append(row)
            
        X = np.array(X)
        
        # Fit OLS regression to mimic ADF equation model exactly
        model = sm.OLS(Y, X).fit()
        residuals = model.resid
        
        # Perform the Ljung-Box Q-test up to lag 20 on the residuals
        # Box-Pierce or Ljung-Box test for residual serial correlation
        lb_test = acorr_ljungbox(residuals, lags=[20], return_df=True)
        lb_stat = lb_test['lb_stat'].values[0]
        lb_pvalue = lb_test['lb_pvalue'].values[0]
        
        conclusion = "Sufficient Lags (White Noise)" if lb_pvalue > 0.05 else "Insufficient Lags (Patterns Left)"
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        
        residual_records.append({
            "Currency": currency_label,
            "Ljung-Box Stat (Lag 20)": lb_stat,
            "p-Value": lb_pvalue,
            "Verdict": conclusion
        })
        
    summary_table = pd.DataFrame(residual_records)
    summary_table = summary_table.round({
        "Ljung-Box Stat (Lag 20)": 4,
        "p-Value": 6
    })
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*95)
    print("                       ARIMA PART (ii): RESIDUAL SERIAL CORRELATION TEST (LAG 20)")
    print("===============================================================================================")
    print(summary_table.to_string(index=False))
    print("="*95)
    print(f" Residual analysis saved to:\n '{output_file}'\n")

if __name__ == "__main__":
    analyze_residual_lags()