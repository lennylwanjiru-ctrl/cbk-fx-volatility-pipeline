import os
import pandas as pd
import numpy as np
import warnings
from arch import arch_model

# Silence optimization warnings to ensure a clean terminal dashboard presentation
warnings.filterwarnings('ignore')

def run_advanced_volatility_forecasting():
    print(" Launching Advanced Volatility Forecasting Engine...")
    
    # Path configurations
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "volatility_forecast_projections.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Run compute_returns.py first.")
        return

    df = pd.read_csv(source_file)
    
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return', 
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return', 
        'sar_ksh_log_return'
    ]
    
    forecast_records = []
    
    print(" Processing Asymmetric Risk Architectures and Out-of-Sample Projections...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        # Scale returns by 100 to stabilize numerical optimization routines
        series = df[col].dropna().values * 100
        
        # ---------------------------------------------------------------------
        # LAYER 1: EGARCH(1,1) - Asymmetric Leverage Modeling
        # ---------------------------------------------------------------------
        try:
            egarch_setup = arch_model(series, vol='EGARCH', p=1, o=1, q=1, dist='normal')
            egarch_fit = egarch_setup.fit(disp='off')
            # Extract the asymmetric leverage coefficient (typically gamma or alpha[1] in arch)
            leverage_coef = egarch_fit.params.get('alpha[1]', 0.0)
        except:
            leverage_coef = np.nan

        # ---------------------------------------------------------------------
        # LAYER 2: GJR-GARCH(1,1) with Student-t Dist & 5-Day Forecasting
        # ---------------------------------------------------------------------
        try:
            # GJR-GARCH is specified using vol='GARCH' with o=1
            gjr_setup = arch_model(series, vol='GARCH', p=1, o=1, q=1, dist='studentst')
            gjr_fit = gjr_setup.fit(disp='off')
            
            # Generate out-of-sample multi-step forecasts (1 to 5 steps ahead)
            forecast = gjr_fit.forecast(horizon=5)
            
            # Extract conditional variance projections (and take the square root for standard volatility)
            variance_forecasts = forecast.variance.iloc[-1].values
            volatility_forecasts = np.sqrt(variance_forecasts)
            
            forecast_records.append({
                "Currency": currency_label,
                "EGARCH Leverage Coef": leverage_coef,
                "Day 1 Forecast": volatility_forecasts[0],
                "Day 2 Forecast": volatility_forecasts[1],
                "Day 3 Forecast": volatility_forecasts[2],
                "Day 4 Forecast": volatility_forecasts[3],
                "Day 5 Forecast": volatility_forecasts[4]
            })
        except Exception as e:
            print(f" Optimization failed for {currency_label}: {e}")
            continue

    # Compile the final forecast analysis summary
    summary_table = pd.DataFrame(forecast_records)
    summary_table = summary_table.round(6)
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*115)
    print("                    QUANT RETAIL DASHBOARD: 5-DAY OUT-OF-SAMPLE VOLATILITY PROJECTIONS")
    print("====================================================================================================")
    print(summary_table.to_string(index=False))
    print("="*115)
    print(f" Projections successfully generated and exported to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_advanced_volatility_forecasting()