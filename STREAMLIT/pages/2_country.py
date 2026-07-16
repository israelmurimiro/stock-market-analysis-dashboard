import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Country Analysis", layout="wide")
st.title("🌍 Country-Based Transaction Analysis")

@st.cache_data
def load_merged_data():
    transactions = pd.read_csv("data/account-statement-1-1-2024-12-31-2024.csv", sep=';')
    symbols = pd.read_csv("data/symbols.csv", sep=';')
    merged = transactions.merge(symbols, left_on='Symbol', right_on='symbol', how='left')
    return merged

df = load_merged_data()

# Convert date
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

# Check if country column exists
if 'country' in df.columns:
    countries = df['country'].unique()
    countries = [c for c in countries if pd.notna(c) and str(c) != 'nan']
    
    if len(countries) > 0:
        selected_country = st.selectbox("Select Country", sorted(countries))
        filtered_df = df[df['country'] == selected_country]
        
        # Transactions over time for selected country
        country_time = filtered_df.groupby(filtered_df['Date'].dt.date).size().reset_index(name='count')
        country_time.columns = ['date', 'count']
        
        fig = px.line(country_time, x='date', y='count', 
                      title=f"📊 Transactions Over Time in {selected_country}",
                      color_discrete_sequence=['#FF6B6B'],
                      template='plotly_dark')
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, use_container_width=True)
        
        # Buying vs Selling by Industry
        if 'TransactionType' in filtered_df.columns and 'industry' in filtered_df.columns:
            col1, col2 = st.columns(2)
            
            with col1:
                buying_industries = filtered_df[filtered_df['TransactionType'] == 'BUY']['industry'].value_counts().head(10).reset_index()
                if not buying_industries.empty:
                    buying_industries.columns = ['industry', 'count']
                    st.subheader(f"🟢 Top 10 Industries - Buying Activity")
                    fig = px.bar(buying_industries, x='industry', y='count', 
                                 color='count', 
                                 color_continuous_scale='Greens',
                                 template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                selling_industries = filtered_df[filtered_df['TransactionType'] == 'SELL']['industry'].value_counts().head(10).reset_index()
                if not selling_industries.empty:
                    selling_industries.columns = ['industry', 'count']
                    st.subheader(f"🔴 Top 10 Industries - Selling Activity")
                    fig = px.bar(selling_industries, x='industry', y='count', 
                                 color='count', 
                                 color_continuous_scale='Reds',
                                 template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)
        
        # Country summary stats
        st.subheader(f"📈 Summary for {selected_country}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Transactions", f"{len(filtered_df):,}")
        with col2:
            buy_count = len(filtered_df[filtered_df['TransactionType'] == 'BUY'])
            st.metric("Buy Transactions", f"{buy_count:,}")
        with col3:
            sell_count = len(filtered_df[filtered_df['TransactionType'] == 'SELL'])
            st.metric("Sell Transactions", f"{sell_count:,}")
    else:
        st.warning("No valid country data found.")
else:
    st.warning("No country column found. Please check if symbols.csv has a 'country' column.")
    with st.expander("📊 Available Columns"):
        st.write(df.columns.tolist())
        st.dataframe(df.head())
