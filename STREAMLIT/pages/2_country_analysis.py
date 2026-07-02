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
# STEP 3 - Combine with Country
# ------------------------------------------------------------------------------
symbols_df = symbols_df.copy()
filtered_df = transactions_df.merge(symbols_df[['symbol', 'sector', 'industry', 'country']],
                                   on='symbol', how='left')

# ------------------------------------------------------------------------------
# STEP 4 - Country Filter
# ------------------------------------------------------------------------------
st.sidebar.header("Country Filter")
list_countries = filtered_df['country'].dropna().unique().tolist()
selected_country = st.sidebar.selectbox("Select Country", list_countries)

filtered_by_country = filtered_df[filtered_df['country'] == selected_country]

# ------------------------------------------------------------------------------
# STEP 5 - Transactions over Time by Country
# ------------------------------------------------------------------------------
transactions_count = filtered_by_country.groupby('Date').size().reset_index(name='Count')

fig_count = px.line(transactions_count, x='Date', y='Count',
                    title='Total Transactions in Country Over Time',
                    markers=True)
st.plotly_chart(fig_count, use_container_width=True)


# ------------------------------------------------------------------------------
# STEP 6 - Top Industries by BUY Transactions
# ------------------------------------------------------------------------------
filtered_buy = filtered_by_country[filtered_by_country['TransactionType'].str.upper() == 'BUY']

top_industries_buy = filtered_buy.groupby('industry').size().sort_values(ascending=False).head(5).reset_index(name='Count')

fig_industries_buy = px.bar(top_industries_buy, x='industry', y='Count',
                            title='Top Industries by BUY Transactions')
st.plotly_chart(fig_industries_buy, use_container_width=True)


# ------------------------------------------------------------------------------
# STEP 7 - Top Industries by SELL Transactions
# ------------------------------------------------------------------------------
filtered_sell = filtered_by_country[filtered_by_country['TransactionType'].str.upper() == 'SELL']

top_industries_sell = filtered_sell.groupby('industry').size().sort_values(ascending=False).head(5).reset_index(name='Count')

fig_industries_sell = px.bar(top_industries_sell, x='industry', y='Count',
                             title='Top Industries by SELL Transactions')
st.plotly_chart(fig_industries_sell, use_container_width=True)