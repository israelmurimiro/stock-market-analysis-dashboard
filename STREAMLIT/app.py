# app.py
# Streamlit application for analyzing financial transactions
# BY ISRAEL MURIMIRO

import streamlit as st

# ------------------------------------------------------------------------------
# Streamlit page configuration
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title='Financial Transactions Dashboard',
    layout='wide',
    initial_sidebar_state='expanded'
)

# ------------------------------------------------------------------------------
# Title and Summary
# ------------------------------------------------------------------------------
st.title("Financial Transactions Dashboard")

st.write("""
**This application by ISRAEL MURIMIRO is designed to enable financial analysts, traders, and stakeholders to explore financial transactions in depth.**  

Using this platform, you can:
- View total number of transactions over time.
- Identify the most traded symbols, sectors, and industries.
- Filter data by country and view country-specific trends in transactions.
- Compare buying and selling activity across different industries.

This tool aims to aid in data-informed decision making and policy formulation related to financial markets.
""")

# ------------------------------------------------------------------------------
# Side panel with a note or signature
# ------------------------------------------------------------------------------
st.sidebar.success("Select a page above.")
st.sidebar.info("**BY ISRAEL MURIMIRO**")