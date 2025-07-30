# Data Preparation: Guide

## Guide for Generating `all_fires.csv`

The cleaned dataset `all_fires.csv` is not included in this repository because
 of its large size.
Follow these steps to generate it locally:

## Steps

1. **Download the raw NFDB files**
   Download the official NFDB point shapefiles from:  
   🔗 [NFDB Point Shapefile – Download Link](https://www.dropbox.com/scl/fi/v1as8zlybx1fc4zzk71xm/NFDB_point.zip?rlkey=zqquce868aawnmqy9xhcmnsqg&st=c3gqm0s7&dl=0)

2. **Extract the files into the correct folder**  
   Place the following files into the **root directory of `2_data_preparation`**:
   - `NFDB_point_20250519.shp`  
   - `NFDB_point_20250519.dbf`  
   - `NFDB_point_20250519.shx`  
   - `NFDB_point_20250519.prj`

3. **Run the notebook**  
   Open and run the Jupyter notebook `clean_nfdb_all.ipynb`.
   The notebook will load the raw NFDB data, clean it,
   and export a standardized CSV.
   After running the notebook, the cleaned dataset will be generated as:
   `1_datasets/all_fires.csv`
