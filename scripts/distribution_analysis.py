import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

def plot_return_distributions():
    print(" Executing Question 7: Returns Distribution and Normality Overlays...")
    
    # Path configurations
    source_file = os.path.join("data", "cbk_exchange_returns_final.csv")
    output_dir = os.path.join("documentation", "distribution_plots")
    
    if not os.path.exists(source_file):
        print(f" Missing source file: {source_file}. Run compute_returns.py first.")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    # Load computed returns
    df = pd.read_csv(source_file)
    
    # Core currency pairs list
    currencies = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    
    sns.set_theme(style="whitegrid")
    
    for currency in currencies:
        simple_col = f"{currency}_simple_return"
        log_col = f"{currency}_log_return"
        
        if simple_col not in df.columns or log_col not in df.columns:
            continue
            
        display_name = currency.replace('_', '/').upper()
        print(f" Generating comparison distributions for {display_name}...")
        
        # Create a clean side-by-side canvas for Simple vs Log returns
        fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=False)
        
        # Data extractions
        simple_data = df[simple_col].dropna()
        log_data = df[log_col].dropna()
        
        # --- Plot 1: Simple Returns Distribution ---
        # Draw empirical data histogram
        sns.histplot(simple_data, stat="density", bins=100, alpha=0.6, color="#1f77b4", ax=axes[0])
        # Calculate theoretical normal distribution parameters
        mu_s, std_s = simple_data.mean(), simple_data.std()
        x_s = np.linspace(simple_data.min(), simple_data.max(), 500)
        axes[0].plot(x_s, norm.pdf(x_s, mu_s, std_s), color="red", linestyle="--", linewidth=2, label="Normal Curve")
        axes[0].set_title(f"{display_name} Simple Returns vs. Normal Curve", fontsize=11, fontweight="bold")
        axes[0].set_xlabel("Daily Return Value")
        axes[0].set_ylabel("Density")
        axes[0].legend()
        
        # --- Plot 2: Log Returns Distribution ---
        # Draw empirical data histogram
        sns.histplot(log_data, stat="density", bins=100, alpha=0.6, color="#2ca02c", ax=axes[1])
        # Calculate theoretical normal distribution parameters
        mu_l, std_l = log_data.mean(), log_data.std()
        x_l = np.linspace(log_data.min(), log_data.max(), 500)
        axes[1].plot(x_l, norm.pdf(x_l, mu_l, std_l), color="red", linestyle="--", linewidth=2, label="Normal Curve")
        axes[1].set_title(f"{display_name} Log Returns vs. Normal Curve", fontsize=11, fontweight="bold")
        axes[1].set_xlabel("Daily Return Value")
        axes[1].set_ylabel("Density")
        axes[1].legend()
        
        plt.tight_layout()
        
        # Save the combined comparative figure
        save_path = os.path.join(output_dir, f"distribution_{currency}.png")
        plt.savefig(save_path, dpi=300)
        plt.close()

    print("\n" + "="*70)
    print(" ALL SEVEN DISTRIBUTION PLOTS CREATED SUCCESSFULLY!")
    print(f" Saved in folder: '{output_dir}/'")
    print("=======================================================\n")

if __name__ == "__main__":
    plot_return_distributions()