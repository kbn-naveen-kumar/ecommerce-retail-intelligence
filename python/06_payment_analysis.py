
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
REPORT_DIR = PROJECT_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load payment records
payments = pd.read_csv(
    RAW_DATA_DIR / "olist_order_payments_dataset.csv"
)

# Aggregate payment records by method
payment_summary = (
    payments.groupby("payment_type", as_index=False)
    .agg(
        payment_records=("order_id", "size"),
        distinct_orders=("order_id", "nunique"),
        total_payment_value=("payment_value", "sum"),
        average_payment_record=("payment_value", "mean")
    )
    .sort_values("total_payment_value", ascending=False)
)

# Calculate each method's share of recorded payment value
total_value = payment_summary["total_payment_value"].sum()

payment_summary["value_share_pct"] = (
    payment_summary["total_payment_value"] / total_value * 100
).round(2)

payment_summary["total_payment_value"] = (
    payment_summary["total_payment_value"].round(2)
)

payment_summary["average_payment_record"] = (
    payment_summary["average_payment_record"].round(2)
)

# Save results
csv_path = OUTPUT_DIR / "payment_method_summary.csv"
payment_summary.to_csv(csv_path, index=False)

# Create a bar chart
plot_data = payment_summary.sort_values("total_payment_value")

plt.figure(figsize=(10, 6))
plt.barh(
    plot_data["payment_type"],
    plot_data["total_payment_value"]
)
plt.title("Total Recorded Payment Value by Payment Method")
plt.xlabel("Payment Value (BRL)")
plt.ylabel("Payment Method")
plt.tight_layout()

chart_path = REPORT_DIR / "payment_method_analysis.png"
plt.savefig(chart_path, dpi=150)
plt.show()

print("\nPAYMENT METHOD ANALYSIS")
print("=" * 75)
print(payment_summary.to_string(index=False))
print(f"\nTotal recorded payment value: R$ {total_value:,.2f}")
print(f"\nCSV report saved to: {csv_path}")
print(f"Chart saved to: {chart_path}")
