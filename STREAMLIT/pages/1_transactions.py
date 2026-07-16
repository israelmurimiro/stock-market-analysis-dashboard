import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Transaction Analysis", layout="wide")
st.title("📈 Transaction Analysis Over Time")

from utils import load_merged_data

df = load_merged_data()

date_col = None
for col in df.columns:
    if 'date' in col.lower() or 'timestamp' in col.lower() or 'time' in col.lower():
        date_col = col
        break

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    
    min_date = df[date_col].min()
    max_date = df[date_col].max()
    date_range = st.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = df[(df[date_col] >= pd.to_datetime(start_date)) & (df[date_col] <= pd.to_datetime(end_date))]
    else:
        filtered_df = df
    
    transactions_over_time = filtered_df.groupby(filtered_df[date_col].dt.date).size().reset_index(name='count')
    transactions_over_time.columns = ['date', 'count']
    
    fig = px.line(transactions_over_time, x='date', y='count', 
                  title="Total Transactions Over Time",
                  color_discrete_sequence=['#FF6B6B'],
                  template='plotly_dark')
    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("No date column found.")
    filtered_df = df

if 'Symbol' in filtered_df.columns:
    top_symbols = filtered_df['Symbol'].value_counts().head(3).reset_index()
    top_symbols.columns = ['symbol', 'count']
    st.subheader("🏆 Top 3 Symbols by Transactions")
    fig = px.bar(top_symbols, x='symbol', y='count', 
                 color='symbol', 
                 color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1'],
                 template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

sector_col = None
for col in filtered_df.columns:
    if 'sector' in col.lower():
        sector_col = col
        break

if sector_col:
    top_sectors = filtered_df[sector_col].value_counts().head(5).reset_index()
    top_sectors.columns = ['sector', 'count']
    st.subheader("🏭 Top 5 Sectors by Transactions")
    fig = px.bar(top_sectors, x='sector', y='count', 
                 color='sector', 
                 color_discrete_sequence=px.colors.qualitative.Set3,
                 template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

industry_col = None
for col in filtered_df.columns:
    if 'industry' in col.lower():
        industry_col = col
        break

if industry_col:
    top_industries = filtered_df[industry_col].value_counts().head(5).reset_index()
    top_industries.columns = ['industry', 'count']
    st.subheader("🏢 Top 5 Industries by Transactions")
    fig = px.bar(top_industries, x='industry', y='count', 
                 color='industry', 
                 color_discrete_sequence=px.colors.qualitative.Pastel,
                 template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)
