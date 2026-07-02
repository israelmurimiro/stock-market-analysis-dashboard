# 📈 Stock Market Analysis & Dashboard

A professional-grade financial analysis suite that bridges static historical data with real-time market insights. This project utilizes a hybrid data processing pipeline to perform multi-factor company analysis, sector benchmarking, and time-series visualization.

---

## 🏗️ Technical Architecture
The system employs a **Hybrid Data Retrieval Model**, merging local batch-processed CSV data with live-streamed financial market data via the `yfinance` REST API.



### Analytical Workflow
1.  **Data Ingestion & Cleaning:** The pipeline normalizes `output.csv` (1,000+ entries) using `pandas` to ensure data integrity across disparate financial metrics.
2.  **API Integration:** Real-time `OHLCV` (Open, High, Low, Close, Volume) data is fetched on-demand based on the user's selected ticker.
3.  **Visualization Engine:** A multi-layered plotting framework uses `matplotlib` to render trend lines, scatter plots, and distribution histograms for high-fidelity reporting.

---

## 📂 Repository Structure

```text
stock-market-dashboard/
├── data/               # Persistent data layer (output.csv)
├── notebooks/          # Exploratory data analysis (EDA) & feature engineering
├── streamlit/          # Production dashboard application
│   ├── app.py          # Main application logic & state management
│   └── pages/          # Modular dashboard sub-views
├── reports/            # Exported analytical outputs
├── requirements.txt    # Project dependencies
└── .gitignore          # Version control exclusions

```

---

## ⚙️ Core Logic & Execution

The dashboard is powered by **Streamlit**, which maintains high performance through intelligent caching mechanisms:

* **Caching Strategy:** The application utilizes `@st.cache_data` decorators to memoize API calls, drastically reducing latency when toggling between company peers and preventing API rate-limit exhaustion.
* **State Management:** The "Company Selection" identifier acts as a global filter, syncing the local CSV dataset with live market data to ensure parity in visual reports.
* **Vectorized Processing:** Large datasets are processed using `numpy` and `pandas` vectorization, ensuring that subplots remain responsive during complex financial comparisons.

---

## 🚀 Installation & Deployment

### 1. Requirements

Ensure you are using **Python 3.8+**. It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 2. Setup

Install the necessary infrastructure libraries:

```bash
pip install -r requirements.txt

```

### 3. Execution

Launch the interactive dashboard to begin analysis:

```bash
streamlit run streamlit/app.py

```

---

## 📊 Feature Highlights

* **Peer Analysis:** Filtered company benchmarking against industry and sector averages.
* **Correlation Modeling:** Revenue vs. Net Income scatter plots to determine financial efficiency.
* **Market Capitalization Distribution:** Geographical insights into market concentration.
* **Trend Smoothing:** 3-month rolling averages applied to closing prices to filter market noise.

---

## 👤 Author

**MURIMIRO ISRAEL**

