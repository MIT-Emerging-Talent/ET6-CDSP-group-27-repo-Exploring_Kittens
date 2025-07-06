# National Fire Database (NFDB) - Point Data

This folder contains a Jupyter notebook to explore historical wildfire records
 from the **Canadian National Fire Database (NFDB)**.

We use this data to analyze wildfire locations, causes, response types,
 and identify **prescribed burns** (controlled fires used to reduce risk).

---

## Required Data

Due to file size, the raw shapefile is **not included** in this repository.

To run the notebook:

1. Download the official NFDB Point shapefile (.zip) from:
   🔗 [Download Link – NFDB_point_20250519.zip](https://www.dropbox.com/scl/fi/v1as8zlybx1fc4zzk71xm/NFDB_point.zip?rlkey=zqquce868aawnmqy9xhcmnsqg&st=c3gqm0s7&dl=0)

2. Unzip it in this directory. The folder should contain files like:
NFDB_point_20250519.shp
NFDB_point_20250519.dbf
NFDB_point_20250519.shx
NFDB_point_20250519.prj

---

## What This Notebook Does

- Displays the first 50 fire records with selected metadata
- Filters fires to find those with `CAUSE == 'H-PB'` (prescribed burns)

---

## Cleaning Notes

- Some records may have incomplete dates (DAY = 1, etc.)
- Non-wildfire incidents and missing location data may need to be filtered

---

## Files in This Folder

- `explore_NFDB.ipynb` – interactive notebook for data exploration
- `README.md` – this documentation file
