# Week 2 – Data Collection, Cleaning, and Preprocessing for Logistics Analysis

## Overview
A Python-based logistics data preprocessing project covering data inspection, cleaning, missing-value handling, outlier treatment, and normalization.

## Objectives
- Inspect a logistics dataset.
- Identify missing values and duplicate records.
- Standardize categorical and date fields.
- Detect and treat numerical outliers using the IQR method.
- Normalize numerical features using Min-Max scaling.
- Generate an analysis-ready dataset.

## Dataset Columns
- Order_ID
- Shipping_Mode
- Distance_km
- Weight_kg
- Shipping_Cost
- Delivery_Time_days
- Warehouse
- Delivery_Status
- Order_Date

The included sample dataset intentionally contains missing values, inconsistent category formatting, and a duplicate record to demonstrate preprocessing.

## Workflow
1. Load CSV with pandas.
2. Inspect shape, data types, missing values, and duplicates.
3. Remove duplicate rows.
4. Convert dates and numerical fields.
5. Standardize categorical values.
6. Fill numerical missing values with median.
7. Fill categorical missing values with mode.
8. Detect/cap outliers using IQR.
9. Normalize numerical variables using Min-Max scaling.
10. Save cleaned CSV.

## Requirements
```bash
pip install pandas scikit-learn
```

## Run
```bash
python preprocessing.py
```

## Files
- `README.md` – project documentation
- `logistics_dataset.csv` – raw/sample dataset
- `preprocessing.py` – Python preprocessing pipeline
- `cleaned_logistics_dataset.csv` – cleaned output
- `Week_2_Logistics_Data_Preprocessing_Report.docx` – detailed report

## Outcome
The preprocessing pipeline creates a cleaner and more consistent dataset suitable for further logistics analytics, KPI analysis, visualization, and machine-learning workflows.
