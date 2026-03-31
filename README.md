# Federated Budget Validator

## Overview

This project is a web-based tool that cleans, validates, and standardizes budget Excel files for federated organizations. It automates the preprocessing of complex financial spreadsheets, ensuring consistent structure and accurate totals.

## Key Features

* Automatic detection of header rows in unstructured Excel files
* Cleaning and normalization of monetary values (₡ format)
* Extraction of monthly budget data
* Validation of totals by indicator
* Export of clean, ready-to-use dataset

## Tech Stack

* Python
* Pandas
* Streamlit

## Workflow

1. Upload raw budget Excel file
2. Automatically detect structure and clean data
3. Normalize monetary values and remove inconsistencies
4. Validate totals
5. Download cleaned file

## Key Logic

* Dynamic header detection using pattern matching
* Column filtering based on month names
* Currency normalization (₡ → float)
* Automatic removal of summary rows

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Use Case

Designed for federations and organizations that handle structured budget submissions and require fast, reliable validation of financial data.

## Author

Edgar Antonio Zeledón Pérez
