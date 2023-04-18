import streamlit as st
from src.common import *

page_setup()

st.title("Statistics for Metabolomics")

st.markdown(
    """
A web app implementation of the [statistics notebooks](https://github.com/Functional-Metabolomics-Lab/Statistical-analysis-of-non-targeted-LC-MSMS-data) for metabolomics by the [Functional Metabolomics Lab](https://github.com/Functional-Metabolomics-Lab).

These notebooks are developed by the Virtual Multi Omics Lab ([VMOL](https://vmol.org/)).


## Quickstart

Once you have completed the **Data Preparation** step, chose any of the available statistics sections.

### Data Preparation
- two tables are required: **Feature Intensity** and **Meta Data**
- supported formats: `tsv` and `txt` (tab separated), `csv` (comma separated) and `xlsx` (Excel file)
- if feature table has an optional `metabolite` column that will be taken as index (can be unique ID, contain `m/z` and `RT` information or actual metabolite name)
- feature index can be automat<ically generated if columns for `m/z` and `RT` (and optionally `row ID`) are present
- sample file names need to contain `mzML` file name extensions
- feature table needs sample file names as column names
- meta data table **requires** a `filename` column
- meta data table can contain columns with attributes (prefixed with `ATTRIBUTE_`)
- checkout the **example data** availabe in file selection
- remove blank features and impute missing values in the **Data Cleanup** section

Example feature table:
|metabolite|sample1.mzML|sample2.mzML|blank.mzML|
|---|---|---|---|
|1|1000|1100|100|
|2|2000|2200|200|

Example meta data table:
|filename|ATTRIBUTE_Sample_Type|ATTRIBUTE_Time_Point|
|---|---|---|
|sample1.mzML|Sample|1h|
|sample2.mzML|Sample|2h|
|blank.mzML|Blank|N/A|


### Available Statistics
- Univariate (ANOVA & Tukey's post hoc test)
- Principle Component Analysis (PCA)
- Multivariate analyses: (PERMANOVA & PCoA)
- Hierachial Clustering & Heatmaps
"""
)
