import os
import pandas as pd
import numpy as np

def clean_cbk_dataset():
    print(" Initializing Data Quality and Cleaning Pipeline...")
    
    
    input_path = "data/cbkScrappeddata.csv" 
    output_path = "data/cbk_exchange_rates_clean.csv"
    
    if not os.path.exists(input_path):
        print(f" Error: Cannot find '{input_path}'. Checking path structures...")
        return

    print(f" Reading raw records from {input_path}...")
    df = pd.read_csv(input_path)
    initial_rows = len(df)
    print(f" Initial record count: {initial_rows} rows.")

    # Clean headers
    df.columns = df.columns.str.strip().str.replace('/', '_').str.replace(' ', '_').str.lower()
    
    if 'date' not in df.columns:
        df.rename(columns={df.columns[0]: 'date'}, inplace=True)

    
    df = df[df['date'].astype(str).str.lower().str.contains('date') == False]
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date']).drop_duplicates(subset=['date']).sort_values(by='date')

  
    currency_cols = [col for col in df.columns if col != 'date']
    for col in currency_cols:
        df[col] = df[col].astype(str).str.replace(',', '').str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].ffill().bfill()

    
    df.to_csv(output_path, index=False)
    print("\n=======================================================")
    print(" DATA CLEANING COMPLETED SUCCESSFULLY!")
    print(f" Cleaned rows saved: {len(df)}")
    print(f" Master copy securely deployed at: '{output_path}'")
    print("=======================================================")

if __name__ == "__main__":
    clean_cbk_dataset()