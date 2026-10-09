import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_individual_currency_plots():
    print(" Initiating Individual Financial Time Series Plot Engine...")
    
    # 1. Source the cleaned dataset
    clean_data_path = os.path.join("data", "cbk_exchange_rates_clean.csv")
    
    if not os.path.exists(clean_data_path):
        print(f" Error: Missing cleaned dataset tracking records at '{clean_data_path}'")
        return

    # Load data and explicitly establish the operational Date Index
    df = pd.read_csv(clean_data_path, parse_dates=['date'])
    df.set_index('date', inplace=True)
    
    # 2. Establish a dedicated output directory for individual graphics
    output_dir = os.path.join("documentation", "currency_plots")
    os.makedirs(output_dir, exist_ok=True)
    
    # List of all seven target currency tracking metrics
    currencies_to_plot = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    
    # Map raw column names to human-readable professional titles
    currency_meta = {
        'usd_ksh': ('US Dollar (USD)', '#1f77b4'),
        'eur_ksh': ('Euro (EUR)', '#ff7f0e'),
        'ukp_ksh': ('UK Sterling Pound (GBP)', '#2ca02c'),
        'swf_ksh': ('Swiss Franc (CHF)', '#d62728'),
        'jyn_ksh': ('Japanese Yen (JPY)', '#9467bd'),
        'chy_ksh': ('China Yuan (CNY)', '#8c564b'),
        'sar_ksh': ('South African Rand (ZAR)', '#e377c2')
    }

    # Set up global plotting look and feel parameters
    sns.set_theme(style="whitegrid")

    # 3. Iterate through each individual currency instrument to extract plots
    for col in currencies_to_plot:
        if col not in df.columns:
            print(f" Warning: Column '{col}' not found inside tracking matrix. Skipping.")
            continue
            
        full_name, color = currency_meta[col]
        display_label = col.replace('_', '/').upper()
        
        print(f" Rendering unique standalone chart timeline for: {display_label}...")
        
        # Initialize a fresh isolated drawing canvas
        plt.figure(figsize=(11, 5))
        
        # Plot the individual curve line
        plt.plot(df.index, df[col], label=f"{display_label} Exchange Spot", color=color, linewidth=1.5)
        
        # Style individual chart components
        plt.title(f"Historical {full_name} vs. Kenyan Shilling (2001 - 2026)", fontsize=12, fontweight='bold', pad=12)
        plt.xlabel("Timeline Horizon (Observation Dates)", fontsize=10, labelpad=8)
        plt.ylabel(f"Exchange Valuation Rate Value (KES per 1 unit)", fontsize=10, labelpad=8)
        plt.legend(loc="upper left")
        plt.tight_layout()
        
        # 4. Save each file using clean, lowercase naming footprints
        file_save_path = os.path.join(output_dir, f"plot_{col}.png")
        plt.savefig(file_save_path, dpi=300)
        plt.close() # Safely flush canvas allocations to optimize runtime resources

    print("\n=======================================================")
    print(" ALL SEVEN INDIVIDUAL PLOTS GENERATED SUCCESSFULLY!")
    print(f" Staged within project directory: '{output_dir}/'")
    print("=======================================================")

if __name__ == "__main__":
    generate_individual_currency_plots()