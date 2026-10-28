
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Set project folders
# --------------------------------------------------
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
REPORT_DIR = PROJECT_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 2. Load orders dataset
# --------------------------------------------------
file_path = RAW_DATA_DIR / "olist_orders_dataset.csv"

orders = pd.read_csv(file_path, low_memory=False)

date_columns = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

# Convert date columns to datetime
for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

# --------------------------------------------------
# 3. Filter eligible delivered orders
# --------------------------------------------------
delivered = orders.loc[
    orders["order_status"].eq("delivered")
].dropna(subset=date_columns).copy()

# --------------------------------------------------
# 4. Calculate delivery performance
# --------------------------------------------------

# Calendar-day delivery duration:
# Ignores hours, minutes, and seconds.
delivered["actual_delivery_days"] = (
    delivered["order_delivered_customer_date"].dt.normalize()
    - delivered["order_purchase_timestamp"].dt.normalize()
).dt.days

# Compare actual delivery date with estimated delivery date.
# Negative or zero means delivered on or before the estimate.
delivered["delivery_difference_days"] = (
    delivered["order_delivered_customer_date"].dt.normalize()
    - delivered["order_estimated_delivery_date"].dt.normalize()
).dt.days

delivered["delivery_result"] = delivered[
    "delivery_difference_days"
].apply(
    lambda days: "On time" if days <= 0 else "Late"
)

# --------------------------------------------------
# 5. Create summary metrics
# --------------------------------------------------
eligible_orders = len(delivered)

on_time_orders = int(
    (delivered["delivery_result"] == "On time").sum()
)

late_orders = int(
    (delivered["delivery_result"] == "Late").sum()
)

average_delivery_days = delivered["actual_delivery_days"].mean()

on_time_percentage = (
    on_time_orders / eligible_orders * 100
    if eligible_orders > 0
    else 0
)

summary = pd.DataFrame([{
    "eligible_delivered_orders": eligible_orders,
    "average_delivery_days": round(average_delivery_days, 2),
    "on_time_orders": on_time_orders,
    "late_orders": late_orders,
    "on_time_delivery_percentage": round(on_time_percentage, 2),
}])

# --------------------------------------------------
# 6. Save detailed data and summary CSV files
# --------------------------------------------------
details_path = OUTPUT_DIR / "delivery_order_details.csv"
summary_path = OUTPUT_DIR / "delivery_performance_summary.csv"

delivered.to_csv(details_path, index=False)
summary.to_csv(summary_path, index=False)

# --------------------------------------------------
# 7. Create delivery performance chart
# --------------------------------------------------
delivery_counts = (
    delivered["delivery_result"]
    .value_counts()
    .reindex(["On time", "Late"], fill_value=0)
)

plt.figure(figsize=(8, 5))

plt.bar(
    delivery_counts.index,
    delivery_counts.values
)

plt.title("On-Time vs Late Deliveries")
plt.xlabel("Delivery Result")
plt.ylabel("Number of Orders")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

chart_path = REPORT_DIR / "delivery_performance.png"

plt.savefig(chart_path, dpi=150)
plt.show()
plt.close()

# --------------------------------------------------
# 8. Display results
# --------------------------------------------------
print("\nDELIVERY PERFORMANCE ANALYSIS")
print("=" * 60)

print(summary.to_string(index=False))

print("\nDelivery outcome counts:")
print(delivery_counts.to_string())

print("\nFiles saved successfully:")
print(f"Detailed data: {details_path}")
print(f"Summary CSV:   {summary_path}")
print(f"Chart:         {chart_path}")

print("\nDelivery performance analysis completed.")
