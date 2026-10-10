"""

Module: Return Distributions & Empirical Normality Parametric Overlays Analysis

"""

import os
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configure enterprise logger interface for execution tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_return_distributions():
    """
    Ingests financial asset records, loops across currency simple/log returns,
    and maps empirical histograms overlaid with theoretical Gaussian parametric curves.
    """
    logging.info("Initializing financial return distribution and normality analysis suite...")
    
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_dir = os.path.join("documentation", "distribution_plots")
    
    if not os.path.exists(source_file):
        logging.error(f"Execution Aborted: Base data registry missing at destination path: {source_file}")
        return
        
    df = pd.read_csv(source_file)
    
    currencies = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    
    # Establish a professional corporate visual grid layout
    sns.set_theme(style="whitegrid")
    os.makedirs(output_dir, exist_ok=True)
    
    logging.info("Iterating through portfolios to generate comparative distribution overlays...")
    for currency in currencies:
        simple_col = f"{currency}_simple_return"
        log_col = f"{currency}_log_return"
        
        if simple_col not in df.columns or log_col not in df.columns:
            logging.warning(f"Target distribution columns for asset [{currency}] missing from workspace. Skipping.")
            continue
            
        display_name = currency.replace('_', '/').upper()
        
        # Ingest and clean specialized sub-arrays
        simple_data = df[simple_col].dropna()
        log_data = df[log_col].dropna()
        
        # Initialize side-by-side canvas axes layout to avoid dimension overlaps
        fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=False)
        
     
        # PLOT 1: SIMPLE RETURNS DISTRIBUTION
       
        sns.histplot(simple_data, stat="density", bins=100, alpha=0.6, color="#1f77b4", ax=axes[0])
        
        # Calculate matching theoretical Gaussian parameters
        mu_s, std_s = simple_data.mean(), simple_data.std()
        x_s = np.linspace(simple_data.min(), simple_data.max(), 500)
        axes[0].plot(x_s, stats.norm.pdf(x_s, mu_s, std_s), color="red", linestyle="--", linewidth=2, label="Normal Curve")
        
        # Formatting metadata for Canvas 1
        axes[0].set_title(f"{display_name} Simple Returns vs. Normal Curve", fontsize=11, fontweight='bold')
        axes[0].set_xlabel("Daily Return Value", fontsize=10)
        axes[0].set_ylabel("Density", fontsize=10)
        axes[0].legend()
        
       
        # PLOT 2: LOG RETURNS DISTRIBUTION
        
        sns.histplot(log_data, stat="density", bins=100, alpha=0.6, color="#2ca02c", ax=axes[1])
        
        # Calculate matching theoretical Gaussian parameters
        mu_l, std_l = log_data.mean(), log_data.std()
        x_l = np.linspace(log_data.min(), log_data.max(), 500)
        axes[1].plot(x_l, stats.norm.pdf(x_l, mu_l, std_l), color="red", linestyle="--", linewidth=2, label="Normal Curve")
        
        # Formatting metadata for Canvas 2
        axes[1].set_title(f"{display_name} Log Returns vs. Normal Curve", fontsize=11, fontweight='bold')
        axes[1].set_xlabel("Daily Return Value", fontsize=10)
        axes[1].set_ylabel("Density", fontsize=10)
        axes[1].legend()
        
        plt.tight_layout()
        
        # Serialize structural assets straight to the target folder
        save_path = os.path.join(output_dir, f"distribution_{currency}.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
        
    # Corporate Auditing Layout Reporting
    print("\n" + "="*80)
    print("STOCHASTIC GRAPHICS REGISTER: COMPARATIVE VISUAL MATRIX AUDIT COMPLETE")
    print("="*80)
    print(" -> All comparative empirical vs. parametric overlays executed successfully.")
    print(f" -> High-resolution time-series density graphs saved to: {output_dir}/")
    print("="*80 + "\n")

if __name__ == "__main__":
    plot_return_distributions()
    
