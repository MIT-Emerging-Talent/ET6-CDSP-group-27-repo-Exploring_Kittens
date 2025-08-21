from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display


def summarize_by_province_for_range(
    df: pd.DataFrame,
    start_year: int,
    end_year: int,
    top_n: Optional[int] = None,
    title_suffix: str = "",
) -> pd.Series:
    df = df.copy()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    subset = df[(df["year"] >= start_year) & (df["year"] <= end_year)]
    counts = subset["province"].value_counts(dropna=False).sort_values(ascending=False)
    to_show = counts.head(top_n) if top_n is not None else counts
    display(to_show.rename("count").to_frame())

    plt.figure(figsize=(11, 6))
    to_show.plot(kind="bar")
    plt.title(f"Prescribed Burns per Province {title_suffix} ({start_year}–{end_year})")
    plt.xlabel("Province / Territory")
    plt.ylabel("Number of Prescribed Burns")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return counts
