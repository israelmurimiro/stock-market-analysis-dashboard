# 📊 Financial Dashboard

> **A comprehensive multi-page Streamlit dashboard for financial transaction analysis, company comparisons, and stock price tracking.**

🔹 **By Israel Murimiro** 🔹

---

## 📚 Description

This application is designed to enable financial analysts, traders, and stakeholders to explore financial transactions and company performance in depth. The dashboard combines **transaction data**, **company financials**, and **live stock prices** into a single interactive platform.

### With this dashboard, you can:

- 📈 **Analyze transaction volumes** over time with interactive date filtering
- 🌍 **Explore country-specific transaction patterns** with buy/sell activity breakdowns
- 📊 **Compare company financial metrics** including market cap, revenue, and net income
- 📉 **Track live stock prices** with candlestick charts and moving averages
- 🔍 **Identify top trading symbols**, sectors, and industries at a glance

---

## 🚀 Features

### 📈 **Transaction Analysis Page**
- Filter transactions by date range
- View total transaction volume over time
- Identify top 3 most traded symbols
- View top 5 sectors and top 5 industries by transaction count

### 🌍 **Country Analysis Page**
- Filter by country of origin
- View transaction trends over time for selected country
- Analyze buying and selling activity by industry
- View summary metrics for each country

### 📊 **Financial Metrics Page**
- Compare top companies by market cap within a selected industry
- Visualize industry average with dashed reference line
- Scatter plot of total revenue vs. net income by sector
- Highlight a specific company for detailed comparison

### 📉 **Stock Price Trends Page**
- Search and select any company from the dataset
- View candlestick charts with volume bars
- Add moving average trend lines (adjustable window)
- View key metrics: latest price, high, low, average price, total volume
- Expandable detailed statistics section

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Streamlit |
| **Language** | Python 3.14 |
| **Data Processing** | Pandas |
| **Visualization** | Plotly Express & Plotly Graph Objects |
| **Stock Data** | yfinance |
| **Styling** | Custom CSS (3D panels, gradients, glow effects) |
| **Deployment** | Streamlit Community Cloud |

---

## 📁 Project Structure

```
STREAMLIT/
├── app.py                    # Main entry point with navigation
├── utils.py                  # Shared data loading functions
├── requirements.txt          # Python dependencies
├── pages/
│   ├── 1_transactions.py     # Transaction analysis page
│   ├── 2_country.py          # Country-based analysis page
│   ├── 3_financials.py       # Financial metrics comparison page
│   └── 4_stock.py            # Stock price trends page
├── data/
│   ├── account-statement-1-1-2024-12-31-2024.csv   # Transaction data
│   ├── symbols.csv           # Symbol metadata (sector, industry, country)
│   ├── output.csv            # Company financial metrics
│   └── country.csv           # Country reference data
└── streamlit/
    └── config.toml           # Streamlit configuration
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/israelmurimiro/stock-market-analysis-dashboard.git
cd stock-market-analysis-dashboard/STREAMLIT
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

---

## 🌐 Deployment

This dashboard is deployed on **Streamlit Community Cloud**:

[**Live Demo**](https://israelmurimiro-stock-market-analysis-dashbo-streamlitapp-gvsrru.streamlit.app/stock)

### Deploy your own:

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **"New app"** and select your repository
5. Set the main file path to `STREAMLIT/app.py` (or just `app.py` if deployed from the root)
6. Click **"Deploy"**

---

## 📊 Data Sources

- **Transactions**: `account-statement-1-1-2024-12-31-2024.csv` – Transaction records with date, symbol, type, and unit
- **Symbols**: `symbols.csv` – Mapping of symbols to company name, sector, industry, and country
- **Financials**: `output.csv` – Company financial metrics from stock market analysis (market cap, revenue, net income, etc.)
- **Stock Prices**: Live data via `yfinance` API

---

## 🎨 Visual Design

- **Dark theme** with gradient backgrounds
- **3D panel effects** with hover animations
- **Glowing text** and borders
- **Color-coded metrics** (green/red for price changes)
- **Interactive Plotly charts** with tooltips
- **Responsive layout** for all screen sizes

---

## 📈 Future Enhancements

- [ ] Add portfolio tracking functionality
- [ ] Include earnings and dividend data
- [ ] Add technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Implement user authentication
- [ ] Enable data export (CSV, PDF reports)
- [ ] Add news sentiment analysis
- [ ] Machine learning price predictions

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

**Israel Murimiro**  
GitHub: [israelmurimiro](https://github.com/israelmurimiro)  
Email: [israelmurimiro@gmail.com](mailto:israelmurimiro@gmail.com)

---

## 🙏 Acknowledgements

- Streamlit for the amazing framework
- yfinance for free stock data
- Plotly for interactive visualizations
- All open-source contributors

---

⭐ **If you found this project useful, please give it a star on GitHub!** ⭐
```

---
