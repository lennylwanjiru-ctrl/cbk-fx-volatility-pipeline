import os
import pandas as pd
import numpy as np
import warnings
from statsmodels.tsa.arima.model import ARIMA

# Silence convergence warnings to keep the terminal output clean and professional
warnings.filterwarnings('ignore')

def optimize_arma_models():
    print(" Executing ARIMA Part (iii): Automated ARMA(p,q) Grid Search Optimization...")
    
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "arma_model_selection_summary.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Please run compute_returns.py first.")
        return

    df = pd.read_csv(source_file)
    
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return', 
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return', 
        'sar_ksh_log_return'
    ]
    
    selection_records = []
    
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        print(f" Optimizing lag parameters for {currency_label}...")
        
        series = df[col].dropna().values
        
        best_aic = float("inf")
        best_order = (0, 0)
        
        # Grid search over p (AR terms) and q (MA terms) from 0 to 3
        for p in range(4):
            for q in range(4):
                try:
                    # Fit ARMA(p, q) model on stationary log returns
                    model = ARIMA(series, order=(p, 0, q)).fit()
                    current_aic = model.aic
                    
                    if current_aic < best_aic:
                        best_aic = current_aic
                        best_order = (p, q)
                except:
                    continue
                    
        best_p, best_q = best_order
        
        selection_records.append({
            "Currency": currency_label,
            "Best Model Order": f"ARMA({best_p}, {best_q})",
            "AR Terms (p)": best_p,
            "MA Terms (q)": best_q,
            "Optimal AIC": best_aic
        })
        
    summary_table = pd.DataFrame(selection_records)
    summary_table = summary_table.round({"Optimal AIC": 2})
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*85)
    print("                    ARIMA PART (iii): AUTOMATED OPTIMAL ARMA ORDER SELECTION")
    print("=====================================================================================")
    print(summary_table.to_string(index=False))
    print("="*85)
    print(f" Optimal ARMA configurations saved to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    optimize_arma_models()