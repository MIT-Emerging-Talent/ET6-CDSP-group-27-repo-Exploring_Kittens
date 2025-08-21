# Milestone 3 Guide: Prescribed Burns Exploration

This guide explains the purpose, reasoning, and methodology behind exploring
prescribed burns in the NFDB.

## Objectives

- Investigate how prescribed burns are distributed across provinces and territories.
- Resolve the `src_agency` issue: some NFDB records list agencies such as `PC`
  (Parks Canada) instead of a province.  
- Assign each burn to the correct province using geographic coordinates.  
- Compare prescribed burn activity across multiple time spans:  
  - 2005–2015 vs 2015–2025  
- Identify the province with the most prescribed burns in recent decades to
  guide the next stage.

## The PC (Parks Canada) Problem

- The NFDB `src_agency` field can be either a province/territory code
  (e.g., AB, BC) or a federal agency (e.g., **PC** for Parks Canada).  
- Because Parks Canada operates in multiple provinces, grouping burns by
  `src_agency` alone would overcount PC and distort results.  
- **Solution:** perform a **point-in-polygon spatial join** between
  each burn’s coordinates and Canadian province boundaries to assign the
  correct `province` field.

## Method Summary

1. Load cleaned NFDB data from `../1_datasets/all_fires.csv`.  
2. Filter for prescribed burns (`cause == "H-PB"`).  
3. Download a lightweight Canadian provinces/territories boundary dataset
  from Natural Earth.  
4. Ensure both datasets use the same coordinate system (WGS84 / EPSG:4326).  
5. Convert burn records to point geometries using their `longitude` and `latitude`.
6. Perform a point-in-polygon spatial join to assign the correct province.  
7. Aggregate counts per province and across defined time ranges.  
8. Optionally export CSV files for further analysis.

## Data Sources

- **NFDB Cleaned Dataset**: `../1_datasets/all_fires.csv` (created in Milestone 2).
- **Province Boundaries**: Natural Earth Admin-1 States/Provinces dataset,
  filtered for Canada and saved as `../1_datasets/boundaries/canada_provinces.geojson`.

## Outputs (if export cells are run)

- CSVs per province for each selected time range (saved under `../1_datasets/`).
- Charts and tables comparing provincial activity in each time span.

## Limitations and Notes

- Missing or inaccurate coordinates may prevent assigning some burns to a province.
- Parks Canada sites near provincial borders are assigned based on point location.
- Time span boundaries are inclusive — check if they match your research criteria.

For quick setup and running instructions, see `README.md`. For full methodology
and reasoning, use this guide.
