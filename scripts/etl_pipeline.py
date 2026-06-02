from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 80)
print("BLUESTOCK MF CAPSTONE - DATA INGESTION")
print("=" * 80)

for file in files:

    filepath = RAW_DIR / file

    try:
        df = pd.read_csv(filepath)

        print("\n")
        print("=" * 60)
        print(f"Dataset: {file}")
        print("=" * 60)

        print("Shape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error loading {file}: {e}")