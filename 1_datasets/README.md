# Wildfire & Prescribed Burn Datasets

This directory contains all data sources collected and used for **Milestone 2**
of our wildfire risk mitigation project.  
Our main research goal is to use satellite imagery and historical fire records
to support **prescribed burn planning** in Canada.

We aim to understand where wildfires have occurred, how prescribed burns are
distributed, and what data can support modeling future fire risks.

---

## Contents

### National_Fire_Database

Point-based wildfire dataset from the Canadian National Fire Database (NFDB).
This includes:

- Individual fire records with attributes such as date, location, cause,
   response type, and area burned
- Ability to identify prescribed burns using `CAUSE == 'H-PB'`
- A Jupyter Notebook to explore, filter, and analyze fires

---

## How to Use These Datasets

### Explore Point Fires (`National_Fire_Database/`)

Navigate to the `National_Fire_Database/` folder and open the included Jupyter notebook.

The notebook demonstrates how to:

- Display the first 50 fire records
- Filter for prescribed burns (e.g., `CAUSE == 'H-PB'`)
- Explore useful metadata fields (cause, agency, location, dates, etc.)
- Count and compare fire types

---

## Cleaning and Reproducibility Notes

- All scripts are designed to work with data downloaded from official sources
- Raw data files are not included in this repo due to size limits
- Instructions are provided in subdirectories for downloading and placing raw data
