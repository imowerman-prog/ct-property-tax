# fetch_ct_mill_rates.py
import requests
import pandas as pd
import os

API_URL = "https://data.ct.gov/resource/emyx-j53e.json?$limit=10000"

def fetch_and_save():
    print("Fetching CT mill rate data...")
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data)

    # Clean and convert
    df['grand_list_year'] = pd.to_numeric(df['grand_list_year'], errors='coerce').astype('Int64')
    df['fiscal_year'] = pd.to_numeric(df['fiscal_year'], errors='coerce').astype('Int64')
    numeric_cols = ['mill_rate', 'mill_rate_real_personal', 'mill_rate_motor_vehicle']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Save as parquet (fast + small)
    os.makedirs("data", exist_ok=True)
    df.to_parquet("data/ct_mill_rates.parquet", index=False)
    print(f"Data saved! {len(df):,} rows → data/ct_mill_rates.parquet")

if __name__ == "__main__":
    fetch_and_save()