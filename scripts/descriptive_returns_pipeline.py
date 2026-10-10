"""
Module: Macroeconomic Financial Time-Series Visualizations & Plot Engine
""""

import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_individual_currency_plots():
    
    Ingests cleaned financial records, sets up unified plotting parameters via Seaborn,
    and isolates standalone high-resolution charts for each target currency asset.
   
    logging.info("Initializing financial time-series visualization engine...")
    
    clean_data_path = os.path.join("data", "cbk_exchange_rates_clean.csv")
    output_dir = os.path.join("documentation", "currency_plots")
    
    if not os.path.exists(clean_data_path):
        logging.error(f"Execution Aborted: Cleaned dataset registry missing at path: {clean_data_path}")
        return

    # Ingest baseline structural data frames and anchor the operational index
    df = pd.read_csv(clean_data_path, parse_dates=['date'])
    df.set_index('date', inplace=True)
    
    os.makedirs(output_dir, exist_ok=True)

    # Dictionary containing standardized financial asset labels and assigned aesthetic hex colors
    currency_meta = {
        'usd_ksh': ('US Dollar (USD)', '#1f77b4'),
        'eur_ksh': ('Euro (EUR)', '#ff7f0e'),
        'ukp_ksh': ('UK Sterling Pound (GBP)', '#2ca02c'),
        'swf_ksh': ('Swiss Franc (CHF)', '#d62728'),
        'jyn_ksh': ('Japanese Yen (JPY)', '#9467bd'),
        'chy_ksh': ('China Yuan (CNY)', '#8c564b'),
        'sar_ksh': ('South African Rand (ZAR)', '#e377c2')
    }
    
    currencies_to_plot = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    
    # Establish a unified, professional corporate aesthetic grid layout
    sns.set_theme(style="whitegrid")
    
    logging.info("Iterating through individual currency instruments to map trend dimensions...")
    for col in currencies_to_plot:
        if col not in df.columns:
            logging.warning(f"Target dimension matrix column [{col}] missing from current workspace frame. Skipping.")
            continue
            
        full_name, color_code = currency_meta[col]
        display_label = col.replace('_', '/').upper()
        
        # Initialize an isolated drawing canvas to eliminate plotting crossovers
        plt.figure(figsize=(11, 5))
        
        # Plot continuous valuation line properties
        plt.plot(df.index, df[col], label=f"{display_label} Exchange Spot", color=color_code, linewidth=1.5)
        
        # Apply strict corporate auditing styling guidelines
        plt.title(f"Historical {full_name} vs. Kenyan Shilling (2001 - 2026)", fontsize=12, fontweight='bold', pad=12)
        plt.xlabel("Timeline Horizon (Observation Dates)", fontsize=10, labelpad=8)
        plt.ylabel("Exchange Valuation Rate Value (KES per 1 Unit)", fontsize=10, labelpad=8)
        plt.legend(loc="upper left", fontsize=10)
        plt.tight_layout()
        
        # Serialize structural assets straight to the target repository folder
        file_save_path = os.path.join(output_dir, f"plot_{col}.png")
        plt.savefig(file_save_path, dpi=300)
        
        # Flush canvas matrix data from memory to preserve system stability
        plt.close()
        
    # Corporate Auditing Layout Reporting
    print("\n" + "="*80)
    print("FINANCIAL GRAPHICS REGISTER: PORTFOLIO PLOT ENGINE RECONCILIATION")
    print("="*80)
    print(" -> All individual currency trend series successfully processed.")
    print(f" -> High-resolution graphic assets materialized inside: {output_dir}/")
    print("="*80 + "\n")

if __name__ == "__main__":
    generate_individual_currency_plots()
   
