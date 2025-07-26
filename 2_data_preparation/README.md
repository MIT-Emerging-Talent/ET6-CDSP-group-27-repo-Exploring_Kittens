# Milestone 2: Data Preparation

This folder contains the scripts and outputs for
**Milestone 2 – Data Collection and Cleaning**.

## Objective

The goal of this stage is to prepare a **clean, standardized dataset**
from the **National Fire Database (NFDB)**, which will serve as the
foundation for later analysis.

The cleaned dataset will allow us to:

- Identify prescribed burns (`CAUSE == "H-PB"`) along with their **location,
   and date** for NDVI vegetation recovery studies.

---

## NFDB Data Cleaning Process

### **Original Data**

- The **raw NFDB files** (`NFDB_point_20250519.shp` and associated files)
   are not included in this repository due to size.
Download them from:
  🔗 [Download Link – NFDB_point_20250519.zip](https://www.dropbox.com/scl/fi/v1as8zlybx1fc4zzk71xm/NFDB_point.zip?rlkey=zqquce868aawnmqy9xhcmnsqg&st=c3gqm0s7&dl=0)

---

### **Steps Performed**

1. **Loaded Raw NFDB Point Shapefile**  
   File: `NFDB_point_20250519.shp`

2. **Standardized Column Names**  
   All column names were converted to `snake_case` for consistency.

3. **Kept Only Relevant Columns**
   nfdbfireid(Unique identifier for each fire), src_agency, fire_id, latitude,
   longitude,year, month, day, rep_date, out_date,size_ha
   (Burned area size in hectares ), cause(Key for identifying
   prescribed burns (H-PB)), fire_type, prescribed

4. **Dropped Irrelevant Columns**  
Administrative or free-text fields not relevant for analysis:
nat_park, fire_name, cause2, attk_date, response,
protzone, more_info, cfs_note1, cfs_note2, acq_date,
layer, omit

5. **Converted Data Types**  

- Dates (`rep_date`, `out_date`) → ISO format (`YYYY-MM-DD`)  
- Numeric (`size_ha`, `year`) → appropriate numeric types

6. **Handled Missing Values**

- Rows missing **latitude**, **longitude**, or **year** were dropped.  
- Other missing values were left as `NaN` for transparency.

7. **Saved Cleaned Dataset**  
Output file: `../1_datasets/all_fires.csv`

---

## Scripts

- **`clean_nfdb_all.ipynb`**  
Reads the raw NFDB shapefile, cleans and processes it, and outputs the cleaned CSV.
