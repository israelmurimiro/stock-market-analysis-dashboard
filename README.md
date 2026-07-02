```
# Stock Market Analysis & Dashboard

This project performs a comprehensive analysis of company financial data and stock prices, combining static data from a CSV file with real‑time stock quotes via the `yfinance` API. The analysis includes:

- Company selection based on student ID (or any custom key)
- Visualisation of:
  - Daily closing price trend (last 3 months)
  - Market capitalisation comparisons (sector and industry)
  - Revenue vs. net income scatter plot
  - Market cap distribution by country
- Subplot layout for a consolidated dashboard view

## Dataset

- `output.csv` – Contains financial metrics for 1,000+ companies (sourced from [source, if known]).
- The notebook filters and sorts the data to identify a specific company and its peers.

## Requirements

- Python 3.8+
- Libraries: pandas, yfinance, matplotlib, numpy

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Repository Structure

```
stock-market-dashboard/
├── data/                   – Dataset file (output.csv)
├── notebooks/              – Jupyter notebook with analysis
├── streamlit/              – Streamlit dashboard application
│   ├── app.py
│   └── pages/
├── reports/                – Generated figures and reports
│   └── figures/
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.8 or later

### Installation

```bash
pip install -r requirements.txt
```

### Dataset

Place `output.csv` inside the `data/` folder.

### Usage

**Jupyter Notebook:**
```bash
jupyter notebook notebooks/analysis.ipynb
```

**Streamlit Dashboard:**
```bash
streamlit run streamlit/app.py
```

## Author

MURIMIRO ISRAEL

