import streamlit as st
import plotly.express as px
import pandas as pd

# ------------------------------------------------------------------------------
# STEP 1 - Loading data
# ------------------------------------------------------------------------------
symbols_df = pd.read_csv('data/symbols.csv', sep=';')
transactions_df = pd.read_csv('data/account-statement-1-1-2024-12-31-2024.csv', sep=';')
transactions_df.columns = transactions_df.columns.str.strip()
symbols_df.columns = symbols_df.columns.str.strip()

# ------------------------------------------------------------------------------
# STEP 2 - Transforming data
# ------------------------------------------------------------------------------
transactions_df = transactions_df.copy()
transactions_df = transactions_df.rename(columns={'Symbol': 'symbol'})
transactions_df = transactions_df[['IDTransaction', 'Date', 'TransactionType', 'symbol', 'Unit']]
transactions_df['Date'] = pd.to_datetime(transactions_df['Date'], errors='coerce')

# ------------------------------------------------------------------------------
# STEP 3 - Filter by Date
# ------------------------------------------------------------------------------
st.sidebar.header("Time Filter")
start = st.sidebar.date_input("Start Date", pd.to_datetime("2024-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("2024-12-31"))

filtered_df = transactions_df[
    (transactions_df['Date'] >= pd.to_datetime(start)) & 
    (transactions_df['Date'] <= pd.to_datetime(end))
]

# ------------------------------------------------------------------------------
# STEP 4 - Transactions Count over Time
# ------------------------------------------------------------------------------
transactions_count = filtered_df.groupby('Date').size().reset_index(name='Count')

fig_count = px.line(transactions_count, x='Date', y='Count',
                    title='Total Number of Transactions Over Time',
                    markers=True)
st.plotly_chart(fig_count, use_container_width=True)

# ------------------------------------------------------------------------------
# STEP 5 - Top 3 Symbols by Transactions
# ------------------------------------------------------------------------------
top_symbols = filtered_df.groupby('symbol').size().sort_values(ascending=False).head(3).reset_index(name='Count')

fig_symbols = px.bar(top_symbols, x='symbol', y='Count',
                     title='Top 3 Symbols by Number of Transactions')
st.plotly_chart(fig_symbols, use_container_width=True)

# ------------------------------------------------------------------------------
# STEP 6 - Top 5 Sectors by Transactions
# ------------------------------------------------------------------------------
filtered_df = filtered_df.merge(symbols_df[['symbol', 'sector']],
                                on='symbol', how='left')

top_sectors = filtered_df.groupby('sector').size().sort_values(ascending=False).head(5).reset_index(name='Count')

fig_sectors = px.bar(top_sectors, x='sector', y='Count',
                    title='Top 5 Sectors by Number of Transactions')
st.plotly_chart(fig_sectors, use_container_width=True)

# ------------------------------------------------------------------------------
# STEP 7 - Top 5 Industries by Transactions
# ------------------------------------------------------------------------------
filtered_df = filtered_df.merge(symbols_df[['symbol', 'industry']],
                                on='symbol', how='left')

top_industries = filtered_df.groupby('industry').size().sort_values(ascending=False).head(5).reset_index(name='Count')

fig_industries = px.bar(top_industries, x='industry', y='Count',
                        title='Top 5 Industries by Number of Transactions')
st.plotly_chart(fig_industries, use_container_width=True)