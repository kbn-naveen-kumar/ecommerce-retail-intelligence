
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
REPORT_DIR = PROJECT_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load orders data
file_path = RAW_DATA_DIR / "olist_orders_dataset.csv"
orders = pd.read_csv(file_path, low_memory=False)

# Convert purchase timestamps to datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

# Remove rows with invalid purchase timestamps from this analysis only
valid_orders = orders.dropna(subset=["order_purchase_timestamp"]).copy()

# Extract month and count orders
valid_orders["purchase_month"] = (
    valid_orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
)

monthly_orders = (
    valid_orders.groupby("purchase_month")
    .size()
    .reset_index(name="total_orders")
    .sort_values("purchase_month")
)

# Save monthly results
csv_output = OUTPUT_DIR / "monthly_orders_summary.csv"
monthly_orders.to_csv(csv_output, index=False)

# Create chart
plt.figure(figsize=(13, 6))
plt.plot(
    monthly_orders["purchase_month"],
    monthly_orders["total_orders"],
    marker="o"
)

plt.title("Monthly Order Trend - Olist E-Commerce")
plt.xlabel("Purchase Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=60, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()

chart_output = REPORT_DIR / "monthly_orders_trend.png"
plt.savefig(chart_output, dpi=150)
plt.show()

print("\nMONTHLY ORDER ANALYSIS")
print("=" * 45)
print(monthly_orders.to_string(index=False))

peak_month = monthly_orders.loc[
    monthly_orders["total_orders"].idxmax()
]

print("\nPeak month:", peak_month["purchase_month"])
print("Orders in peak month:", int(peak_month["total_orders"]))
print("\nMonthly summary saved to:", csv_output)
print("Chart saved to:", chart_output)
