
# Prescribed Burns and Wildfire Risk Mitigation in Canada

## Project Overview

Wildfires are becoming more frequent and severe in Canada due to climate change.
One method used to reduce risk is prescribed burning: controlled fires that
reduce fuel loads in forests. Our project explores whether satellite imagery
and open data can help identify areas suitable for future prescribed burns,
 using historical fire patterns and environmental features.

## Research Question

**How does the integration of satellite imagery improve the outcomes of
prescribed burning programs in mitigating wildfire risk in Canada?**

## Problem Modeling Approach

We are modeling our problem by combining multiple datasets to identify patterns
in areas treated with prescribed burns and those impacted by wildfires.
Since precise data on prescribed burn locations is limited,
 we are constructing a proxy dataset using:

- Parks Canada records for annual prescribed burn area
- ONFIRE dataset to estimate approximate locations and timeframes of prescribed burns
- Satellite imagery before and after the estimated burn period to extract
- environmental and visual features (e.g., vegetation density, moisture, fire scars)

By comparing features from these regions with those from areas affected by large
wildfires, we aim to train a model that can recommend suitable regions for
future prescribed burns.

## Data Sources Used

We are leveraging the following publicly available datasets:

- Canadian National Fire Database (CNFDB) for historical wildfire locations and sizes
- Parks Canada prescribed burn records for yearly treatment area information
- ONFIRE gridded dataset, which includes coarse-resolution prescribed burn indicators
- Satellite imagery (e.g., Sentinel-2, Landsat) to analyze pre- and post-burn conditions

## Modeling Strategy

Our strategy includes the following steps:

1. Identify likely prescribed burn locations using ONFIRE gridded fire records
    marked as prescribed burns (H-PB).
2. Cross-reference with Parks Canada reported burn areas to refine potential
   prescribed sites.
3. Download satellite images for estimated burn areas, both before and after
    the burn date.
4. Extract features such as vegetation indices (NDVI), land cover types,
    and burn severity indicators.
5. Build a machine learning model that compares these areas to known wildfire
    zones without prescribed burns.
6. Use the model to highlight areas where prescribed burning could reduce the
    risk of future uncontrolled wildfires.

## Assumptions and Limitations

In this project, we made several assumptions:

- ONFIRE grid cells marked as prescribed burns are reasonably accurate
   representations of actual burn areas.
- Parks Canada data provides a valid proxy for regional prescribed burn
   activity, even though it lacks spatial granularity.
- Satellite imagery reflects observable changes due to prescribed burning,
   and these changes are detectable using available features.
- Our analysis may not capture smaller or undocumented burns and excludes local
   management or socio-political constraints.

We acknowledge that data on prescribed burn locations is not always detailed or
 complete. This presents limitations in spatial precision and may affect model
 accuracy. We will document and evaluate these limitations as part of our
 project outcomes.

## Future Work

In future stages of the project, we aim to:

- Improve identification of prescribed burn areas through spatial analysis and
   enhanced remote sensing techniques
- Test our model on selected high-risk regions to evaluate predictive performance
- Engage with fire management experts or agencies to validate assumptions and
   potentially acquire more granular data
- Expand the model to incorporate additional environmental variables,
   including weather and topography
