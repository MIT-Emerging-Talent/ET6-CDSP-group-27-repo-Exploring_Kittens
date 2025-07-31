# 2_data_preparation/filter_prescribed_burns.py
import pandas as pd
from pathlib import Path
import sys

# 1) Figure out repo root no matter where you run this from
root = Path(__file__).resolve().parents[1]

# 2) Point to your files
infile = root / "1_datasets" / "all_fires.csv"
outfile = root / "1_datasets" / "prescribed_burns.csv"

# 3) Recheck
if not infile.exists():
    sys.exit(f"❌ Can't find {infile}")

# 4) Load and filter by the correct column name
df = pd.read_csv(infile, dtype=str)
# (if you want to double‐check column names, uncomment the next line)
# print("Columns in CSV:", df.columns.tolist())

prescribed = df[df["cause"] == "H-PB"]

# 5) Save the result
outfile.parent.mkdir(exist_ok=True, parents=True)
prescribed.to_csv(outfile, index=False)

print(f"✅ Wrote {len(prescribed):,} rows to {outfile}")
