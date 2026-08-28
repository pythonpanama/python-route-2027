"""Exercise 5: read a small CSV file with the standard library.

Run this file from the repository root:
    python exercises/05_csv_summary.py
"""

from collections import defaultdict
from csv import DictReader
from pathlib import Path

data_file = Path(__file__).parents[1] / "data" / "transactions.csv"
totals = defaultdict(float)

with data_file.open(encoding="utf-8", newline="") as file:
    for row in DictReader(file):
        totals[row["category"]] += float(row["amount"])

for category, amount in sorted(totals.items()):
    print(f"{category}: {amount:.2f}")
