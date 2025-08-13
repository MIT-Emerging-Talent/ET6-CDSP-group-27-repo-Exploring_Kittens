# Milestone 3: Data Exploration

This folder contains notebooks and scripts for exploring the cleaned National
 Fire Database (NFDB), focusing on prescribed burns and their distribution
  across Canada.

## How to Run

1. **Ensure the cleaned dataset exists**  
   - Required file: `../1_datasets/all_fires.csv`  
   - If missing, go to **Milestone 2** and run `clean_nfdb_all.ipynb` to
      generate it.

2. **Install required Python packages** (once per environment)  
   Run:  
   pip install geopandas pandas matplotlib shapely requests

3. **Run the exploration notebook**  
   - Open `prescribed_burns_exploration.ipynb` in Jupyter Notebook, JupyterLab,
     or VS Code with the Jupyter extension.  
   - Run all cells in order.

## The PC (Parks Canada) Problem

The NFDB field `src_agency` is not always a province code — it can also be
 a federal agency such as **PC** (Parks Canada).  
Since Parks Canada operates in multiple provinces, grouping directly by
 `src_agency` would inflate PC’s numbers and hide the actual provincial distribution.
To fix this, we use a **spatial join** to assign each burn to a real province
 using its latitude and longitude.

## Outputs

- Charts showing prescribed burns per province and per selected time span.  
- Optional CSV files of prescribed burns by province and time period
  (only if you run the export cells).

## Files in this directory

- `prescribed_burns_exploration.ipynb` — main exploration notebook.  
- `guide.md` — detailed methodology, rationale, and data notes.
