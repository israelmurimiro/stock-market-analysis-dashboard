import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

st.set_page_config(page_title="Stock Price Trends", layout="wide")
st.title("📉 Stock Price Trends")

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False
    st.warning("⚠️ yfinance not installed. Run: pip install yfinance")

@st.cache_data
def load_companies():
    df = pd.read_csv("data/output.csv")
    return df[['symbol', 'company_name']].drop_duplicates()

@st.cache_data
def fetch_stock_data(symbol, start, end, period):
    try:
        if period == "Max":
            data = yf.download(symbol, period="max", progress=False)
        else:
            data = yf.download(symbol, start=start, end=end, progress=False)
        
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [' '.join(col).strip() for col in data.columns.values]
        
        return data
    except Exception as e:
        st.error(f"Error in yf.download: {e}")
        return pd.DataFrame()

if YFINANCE_AVAILABLE:
    companies_df = load_companies()
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        company_symbol = st.selectbox("Select Company", companies_df['symbol'].tolist())
        company_name = companies_df[companies_df['symbol'] == company_symbol]['company_name'].values[0]
    
    with col2:
        period_options = {
            "1 Month": 30,
            "3 Months": 90,
            "6 Months": 180,
            "1 Year": 365,
            "YTD": "ytd",
            "Max": "max"
        }
        period = st.selectbox("Select Period", list(period_options.keys()))
    
    with col3:
        st.write("")
        st.write("")
        load_button = st.button("🚀 Load Stock Data", use_container_width=True, type="primary")

    end_date = datetime.now()

    if period == "YTD":
        start_date = datetime(datetime.now().year, 1, 1)
    elif period == "Max":
        start_date = None
    else:
        days = period_options[period]
        start_date = end_date - timedelta(days=days)

    use_custom = st.checkbox("Use Custom Date Range")
    if use_custom:
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", end_date - timedelta(days=90))
        with col2:
            end_date = st.date_input("End Date", end_date)

    if load_button:
        with st.spinner(f"Loading data for {company_symbol}..."):
            stock_data = fetch_stock_data(company_symbol, start_date, end_date, period)
            
            if stock_data.empty:
                st.warning(f"No data found for {company_symbol}. Check symbol or date range.")
            else:
                # Column mapping
                col_mapping = {}
                for col in stock_data.columns:
                    col_lower = col.lower()
                    if 'open' in col_lower:
                        col_mapping['Open'] = col
                    elif 'high' in col_lower:
                        col_mapping['High'] = col
                    elif 'low' in col_lower:
                        col_mapping['Low'] = col
                    elif 'close' in col_lower:
                        col_mapping['Close'] = col
                    elif 'volume' in col_lower:
                        col_mapping['Volume'] = col
                
                required = ['Open', 'High', 'Low', 'Close', 'Volume']
                if not all(k in col_mapping for k in required):
                    st.error("Downloaded data missing required columns. Found columns: " + ", ".join(stock_data.columns.tolist()))
                else:
                    open_vals = stock_data[col_mapping['Open']]
                    high_vals = stock_data[col_mapping['High']]
                    low_vals = stock_data[col_mapping['Low']]
                    close_vals = stock_data[col_mapping['Close']]
                    volume_vals = stock_data[col_mapping['Volume']]
                    
                    # Moving Average settings
                    st.subheader("Trend Line Options")
                    sma_window = st.slider("Moving Average Window (days)", min_value=2, max_value=50, value=10, step=1)
                    show_sma = st.checkbox("Show Moving Average", value=True)
                    
                    # Compute SMA
                    sma = close_vals.rolling(window=sma_window).mean()
                    
                    # Create figure
                    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                                        vertical_spacing=0.03, 
                                        row_heights=[0.7, 0.3])
                    
                    # Candlestick
                    fig.add_trace(go.Candlestick(x=stock_data.index,
                                                 open=open_vals,
                                                 high=high_vals,
                                                 low=low_vals,
                                                 close=close_vals,
                                                 name='Price',
                                                 increasing_line_color='#00FF00',
                                                 decreasing_line_color='#FF6B6B'),
                                  row=1, col=1)
                    
                    # Moving Average line
                    if show_sma:
                        fig.add_trace(go.Scatter(x=stock_data.index,
                                                 y=sma,
                                                 mode='lines',
                                                 name=f'SMA ({sma_window})',
                                                 line=dict(color='#FFD700', width=2)),
                                      row=1, col=1)
                    
                    # Volume bars
                    close_array = close_vals.values
                    open_array = open_vals.values
                    colors = ['#00FF00' if c >= o else '#FF6B6B' for c, o in zip(close_array, open_array)]
                    
                    fig.add_trace(go.Bar(x=stock_data.index,
                                         y=volume_vals,
                                         name='Volume',
                                         marker_color=colors,
                                         opacity=0.5),
                                  row=2, col=1)
                    
                    fig.update_layout(title=f"📈 {company_name} ({company_symbol}) - Stock Price",
                                      xaxis_title="Date",
                                      yaxis_title="Price (USD)",
                                      template='plotly_dark',
                                      hovermode='x unified',
                                      height=700)
                    
                    fig.update_yaxes(title_text="Price (USD)", row=1, col=1)
                    fig.update_yaxes(title_text="Volume", row=2, col=1)
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Metrics
                    latest_price = float(close_vals.iloc[-1])
                    first_price = float(close_vals.iloc[0])
                    price_change = latest_price - first_price
                    pct_change = (price_change / first_price) * 100 if first_price != 0 else 0
                    change_color = "inverse" if price_change < 0 else "normal"
                    
                    col1, col2, col3, col4, col5 = st.columns(5)
                    
                    with col1:
                        st.metric("Latest Price", f"${latest_price:.2f}", 
                                 f"{price_change:+.2f} ({pct_change:+.2f}%)", 
                                 delta_color=change_color)
                    
                    with col2:
                        st.metric("📈 High", f"${float(high_vals.max()):.2f}")
                    
                    with col3:
                        st.metric("📉 Low", f"${float(low_vals.min()):.2f}")
                    
                    with col4:
                        st.metric("📊 Avg Price", f"${float(close_vals.mean()):.2f}")
                    
                    with col5:
                        st.metric("📊 Total Volume", f"{int(volume_vals.sum()):,}")
                    
                    with st.expander("📊 Detailed Statistics"):
                        stats_col1, stats_col2, stats_col3 = st.columns(3)
                        
                        with stats_col1:
                            st.metric("Start Price", f"${first_price:.2f}")
                            st.metric("Period Return", f"{pct_change:+.2f}%")
                        
                        with stats_col2:
                            st.metric("Std Deviation", f"${float(close_vals.std()):.2f}")
                            st.metric("Trading Days", f"{len(stock_data)}")
                        
                        with stats_col3:
                            st.metric("Volume Avg", f"{int(volume_vals.mean()):,}")
                            st.metric("Volume Max", f"{int(volume_vals.max()):,}")
    else:
        st.info("👆 Click the **Load Stock Data** button to fetch and display the stock chart.")
else:
    st.info("📦 Please install yfinance to use this page: `pip install yfinance`")
