
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
REPORT_DIR = PROJECT_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load the required CSV files
items = pd.read_csv(
    RAW_DATA_DIR / "olist_order_items_dataset.csv"
)

products = pd.read_csv(
    RAW_DATA_DIR / "olist_products_dataset.csv"
)

translations = pd.read_csv(
    RAW_DATA_DIR / "product_category_name_translation.csv"
)

# Add English category names to the product data
products = products.merge(
    translations,
    on="product_category_name",
    how="left"
)

# Use English category where available.
# Keep the original category when translation is unavailable.
products["category"] = (
    products["product_category_name_english"]
    .fillna(products["product_category_name"])
    .fillna("unknown_category")
)

# Join order items with product categories
merged = items.merge(
    products[["product_id", "category"]],
    on="product_id",
    how="left",
    validate="many_to_one"
)

# Aggregate sales by category
category_sales = (
    merged.groupby("category", as_index=False)
    .agg(
        total_items=("order_item_id", "count"),
        total_orders=("order_id", "nunique"),
        item_sales_value=("price", "sum")
    )
    .sort_values("item_sales_value", ascending=False)
)

# Select the top 10 categories
top_10 = category_sales.head(10).copy()

# Save complete category analysis
category_sales.to_csv(
    OUTPUT_DIR / "product_category_sales.csv",
    index=False
)

top_10.to_csv(
    OUTPUT_DIR / "top_10_product_categories.csv",
    index=False
)

# Plot the top 10 categories
plot_data = top_10.sort_values("item_sales_value")

plt.figure(figsize=(12, 7))
plt.barh(
    plot_data["category"],
    plot_data["item_sales_value"]
)

plt.title("Top 10 Product Categories by Item Sales Value")
plt.xlabel("Item Sales Value (BRL)")
plt.ylabel("Product Category")
plt.tight_layout()

chart_path = REPORT_DIR / "top_10_product_categories.png"
plt.savefig(chart_path, dpi=150)
plt.show()

# Display results
print("\nTOP 10 PRODUCT CATEGORIES")
print("=" * 80)
print(top_10.to_string(index=False))

print("\nTotal item rows analyzed:", len(merged))
print(
    "Total item sales value (BRL):",
    round(merged["price"].sum(), 2)
)

print("\nFull category report saved to:")
print(OUTPUT_DIR / "product_category_sales.csv")

print("\nTop 10 report saved to:")
print(OUTPUT_DIR / "top_10_product_categories.csv")

print("\nChart saved to:")
print(chart_path)
