import os
import pandas as pd
from scipy.stats import skew, kurtosis

def run_simple_returns_analysis():
    print(" Executing Question 4: Simple Returns Descriptive Statistics...")
    
    # Locate cleaned source data file
    source_file = os.path.join("data", "cbk_exchange_rates_clean.csv")
    output_file = os.path.join("documentation", "question_4_simple_returns.csv")
    
    if not os.path.exists(source_file):
        print(f" Missing file: {source_file}. Please run your cleaning script first.")
        return

    # Load cleaned dataset
    df = pd.read_csv(source_file)
    
    # Define all active currency columns from our data setup
    currency_cols = ['usd_ksh', 'eur_ksh', 'ukp_ksh', 'swf_ksh', 'jyn_ksh', 'chy_ksh', 'sar_ksh']
    
    stats_records = []
    
    for col in currency_cols:
        if col not in df.columns:
            continue
            
        # Calculate daily simple returns: (P_t - P_{t-1}) / P_{t-1}
        simple_returns = df[col].astype(float).pct_change().dropna()
        
        # Calculate all 9 requested statistical measurements
        mean_val = simple_returns.mean()
        variance_val = simple_returns.var()
        std_dev_val = simple_returns.std()
        median_val = simple_returns.median()
        skew_val = skew(simple_returns)
        raw_kurt = kurtosis(simple_returns, fisher=False)  # Regular kurtosis
        excess_kurt = kurtosis(simple_returns, fisher=True) # Excess kurtosis
        min_val = simple_returns.min()
        max_val = simple_returns.max()
        
        # Format currency name for standard reporting presentation style
        display_name = col.replace('_', '/').upper()
        
        # Build our row asset record dictionary
        stats_records.append({
            "Currency": display_name,
            "Mean": mean_val,
            "Variance": variance_val,
            "Std Deviation": std_dev_val,
            "Median": median_val,
            "Skewness": skew_val,
            "Kurtosis": raw_kurt,
            "Excess Kurtosis": excess_kurt,
            "Minimum": min_val,
            "Maximum": max_val
        })

    # Group measurements into a clean data frame table structure
    summary_table = pd.DataFrame(stats_records)
    
    # Round figures cleanly to 6 decimal places 
    summary_table = summary_table.round(6)
    
    # Save the resulting summary matrix out to documentation folder
    os.makedirs("documentation", exist_ok=True)
    summary_table.to_csv(output_file, index=False)
    
    print("\n" + "="*110)
    print("                    QUESTION 4: DAILY SIMPLE RETURNS DESCRIPTIVE STATISTICS")
    print("="*110)
    print(summary_table.to_string(index=False))
    print("="*110)
    print(f"🏆 Table successfully exported and saved to:\n📂 '{output_file}'\n")

if __name__ == "__main__":
    run_simple_returns_analysis()