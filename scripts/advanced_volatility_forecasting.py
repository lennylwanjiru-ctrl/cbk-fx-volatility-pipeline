
Project: Central Bank of Kenya (CBK) Foreign Exchange Volatility Pipeline
Module: Econometric Volatility Modeling (EGARCH & GJR-GARCH Parameter Projections)
Analyst: Lenny Wanjiru (DeKUT Actuarial Science)


import os
import logging
import numpy as np
import pandas as pd
import warnings
from arch import arch_model

# Silence optimization telemetry warnings to ensure clean log outputs
warnings.filterwarnings('ignore')

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_advanced_volatility_forecasting():
    """
    Ingests daily log returns, fits asymmetric volatility models to capture
    leverage dynamics, and exports a 5-day out-of-sample forecasting matrix.
    """
    logging.info("Initializing advanced macroeconomic volatility forecasting engine...")
    
    # Define relative workspace path space boundaries
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_file = os.path.join("documentation", "volatility_forecast_projections.csv")
    
    if not os.path.exists(source_file):
        logging.error(f"Execution Aborted: Base data registry missing at destination path: {source_file}")
        return
        
    df = pd.read_csv(source_file)
    
    # Complete systemic currency log return series
    log_return_cols = [
        'usd_ksh_log_return', 'eur_ksh_log_return', 'ukp_ksh_log_return',
        'swf_ksh_log_return', 'jyn_ksh_log_return', 'chy_ksh_log_return',
        'sar_ksh_log_return'
    ]
    
    forecast_records = []
    
    logging.info("Processing structural asymmetric risk profiles and out-of-sample path projections...")
    for col in log_return_cols:
        if col not in df.columns:
            continue
            
        # Standardize labels into standard financial currency conventions (e.g., USD/KSH)
        currency_label = col.replace('_log_return', '').replace('_', '/').upper()
        
        # Scale array values by 100 to prevent internal numeric optimization limits
        series = df[col].dropna().values * 100
        
        # Implementation A: EGARCH(1,1) Parameter Mapping for Asymmetric Leverage Detection
        try:
            egarch_setup = arch_model(series, vol='EGARCH', p=1, o=1, q=1, dist='normal')
            egarch_fit = egarch_setup.fit(disp='off')
            leverage_coef = egarch_fit.params.get('alpha[1]', 0.0)
        except Exception:
            leverage_coef = np.nan
            
        # Implementation B: GJR-GARCH(1,1) with Student-t Errors for 5-Day Volatility Projections
        try:
            gjr_setup = arch_model(series, vol='GARCH', p=1, o=1, q=1, dist='studentst')
            gjr_fit = gjr_setup.fit(disp='off')
            
            # Extract out-of-sample forward projections across the target 5-day horizon
            forecast = gjr_fit.forecast(horizon=5)
            variance_forecasts = forecast.variance.iloc[-1].values
            volatility_forecasts = np.sqrt(variance_forecasts)
            
            forecast_records.append({
                "Currency": currency_label,
                "EGARCH_Leverage_Coef": leverage_coef,
                "Day_1_Forecast": volatility_forecasts[0],
                "Day_2_Forecast": volatility_forecasts[1],
                "Day_3_Forecast": volatility_forecasts[2],
                "Day_4_Forecast": volatility_forecasts[3],
                "Day_5_Forecast": volatility_forecasts[4]
            })
        except Exception as e:
            logging.error(f"Optimization Routine Failed for asset sequence [{currency_label}]: {str(e)}")
            continue

    # Compile and serialize the final econometric forecast matrix
    summary_table = pd.DataFrame(forecast_records).round(6)
    
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    logging.info(f"Econometric forecast table safely written to destination: {output_file}")
    
    # Corporate Auditing Layout Reporting
    print("\n" + "="*95)
    print("MACRO FINTECH COMMAND LEDGER: 5-DAY OUT-OF-SAMPLE EXCHANGE VOLATILITY SHOCK FORECASTS")
    print("="*95)
    print(summary_table.to_string(index=False))
    print("="*95 + "\n")

if __name__ == "__main__":
    run_advanced_volatility_forecasting()
    
