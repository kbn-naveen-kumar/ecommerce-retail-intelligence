
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

file_path = RAW_DATA_DIR / "olist_products_dataset.csv"
df = pd.read_csv(file_path)

# Check missing values in product attributes
columns_to_check = [
    "product_category_name",
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm",
]

print("=" * 65)
print("PRODUCT DATA QUALITY CHECK")
print("=" * 65)

# Count rows missing each attribute
for column in columns_to_check:
    print(f"{column}: {df[column].isna().sum():,} missing")

# Check whether the same rows are missing all four attributes
main_columns = [
    "product_category_name",
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
]

all_four_missing = df[main_columns].isna().all(axis=1).sum()
any_of_four_missing = df[main_columns].isna().any(axis=1).sum()

print("\n" + "-" * 65)
print(f"Rows missing all four attributes: {all_four_missing:,}")
print(f"Rows missing at least one of the four: {any_of_four_missing:,}")

# Check missing physical dimensions
physical_columns = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm",
]

all_physical_missing = df[physical_columns].isna().all(axis=1).sum()
print(f"Rows missing all four physical attributes: {all_physical_missing:,}")

print("\nSample products missing category:")
print(
    df.loc[
        df["product_category_name"].isna(),
        ["product_id", "product_category_name", "product_weight_g"]
    ].head(10).to_string(index=False)
)

print("\nProduct quality check completed.")
