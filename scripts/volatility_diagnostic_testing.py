import os
import pandas as pd
import numpy as np
import warnings
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.stats.diagnostic import het_arch

# Silence model convergence logs to keep terminal presentation clean
warnings.filterwarnings('ignore')

def run_arch_lm_tests():
    print(" Executing ARIMA Part (v): ARCH-LM Volatility Cluster Testing...")
    
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "arch_lm_test_summary.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Run compute_returns.py first.")
        return

    df = pd.read_csv(source_file)
    
    # Active currency configs and their matching optimal ARMA(p,q) orders from Part (iii)
    currency_models = {
        'usd_ksh_log_return': (2, 2),
        'eur_ksh_log_return': (2, 0),
        'ukp_ksh_log_return': (2, 0),
        'swf_ksh_log_return': (2, 0),
        'jyn_ksh_log_return': (0, 2),
        'chy_ksh_log_return': (2, 0),
        'sar_ksh_log_return': (3, 3)
    }
    
    # Specific lag milestones requested by the question
    target_lags = [10, 15, 20, 25, 30, 35, 40]
    arch_records = []
    
    for col, (p, q) in currency_models.items():
        if col not in df.columns:
            continue
            
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        print(f" Fitting ARMA({p},{q}) and testing variance lags for {currency_label}...")
        
        series = df[col].dropna().values
        
        # Fit the optimal ARMA model to extract clean filtered residuals
        model = ARIMA(series, order=(p, 0, q)).fit()
        residuals = model.resid
        
        # Run the ARCH-LM test at each requested lag milestone
        for lag in target_lags:
            # het_arch returns: (lm_stat, lm_pvalue, f_stat, f_pvalue)
            lm_stat, lm_pvalue, _, _ = het_arch(residuals, nlags=lag)
            
            verdict = "Heteroskedastic (A)" if lm_pvalue < 0.05 else "Homoskedastic (B)"
            
            arch_records.append({
                "Currency": currency_label,
                "Lag Checked": lag,
                "LM Statistic": lm_stat,
                "p-Value": lm_pvalue,
                "Verdict (5% Level)": verdict
            })
            
    summary_table = pd.DataFrame(arch_records)
    summary_table = summary_table.round({"LM Statistic": 4, "p-Value": 6})
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*95)
    print("                           ARIMA PART (v): ARCH-LM VOLATILITY DIAGNOSTIC")
    print("===============================================================================================")
    # Print out a slice or full grid for immediate verification
    print(summary_table.to_string(index=False))
    print("="*95)
    print(f" ARCH-LM test logs successfully compiled and saved to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_arch_lm_tests()