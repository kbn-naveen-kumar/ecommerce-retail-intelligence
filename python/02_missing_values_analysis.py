
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

files_to_check = [
    "olist_orders_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
]

results = []

for file_name in files_to_check:
    file_path = RAW_DATA_DIR / file_name
    df = pd.read_csv(file_path, low_memory=False)

    missing_counts = df.isna().sum()

    print("\n" + "=" * 60)
    print(f"FILE: {file_name}")
    print("=" * 60)

    columns_with_missing = missing_counts[missing_counts > 0]

    if columns_with_missing.empty:
        print("No missing values found.")
    else:
        for column, count in columns_with_missing.items():
            percentage = (count / len(df)) * 100

            print(
                f"{column}: {count:,} missing "
                f"({percentage:.2f}%)"
            )

            results.append({
                "file_name": file_name,
                "column_name": column,
                "missing_count": int(count),
                "missing_percentage": round(percentage, 2),
            })

if results:
    report = pd.DataFrame(results)
    output_path = OUTPUT_DIR / "missing_values_by_column.csv"
    report.to_csv(output_path, index=False)
    print(f"\nDetailed report saved to:\n{output_path}")

print("\nMissing-value analysis completed.")
