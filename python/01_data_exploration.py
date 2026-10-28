
from pathlib import Path
import pandas as pd

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Original CSV files
csv_files = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]

summary = []

print("=" * 65)
print("OLIST E-COMMERCE DATA EXPLORATION")
print("=" * 65)

for file_name in csv_files:
    file_path = RAW_DATA_DIR / file_name

    if not file_path.exists():
        print(f"\nFILE NOT FOUND: {file_name}")
        continue

    try:
        df = pd.read_csv(file_path, low_memory=False)

        missing_cells = int(df.isna().sum().sum())
        duplicate_rows = int(df.duplicated().sum())

        summary.append({
            "file_name": file_name,
            "row_count": len(df),
            "column_count": len(df.columns),
            "missing_cells": missing_cells,
            "duplicate_rows": duplicate_rows,
        })

        print(f"\nFile: {file_name}")
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print(f"Missing cells: {missing_cells:,}")
        print(f"Duplicate rows: {duplicate_rows:,}")

    except Exception as error:
        print(f"\nERROR reading {file_name}: {error}")

# Save the summary report
if summary:
    summary_df = pd.DataFrame(summary)
    output_path = PROCESSED_DIR / "python_data_quality_summary.csv"
    summary_df.to_csv(output_path, index=False)

    print("\n" + "=" * 65)
    print("SUMMARY REPORT")
    print("=" * 65)
    print(summary_df.to_string(index=False))
    print(f"\nReport saved to: {output_path}")

print("\nData exploration completed.")
