import pandas as pd
import streamlit as st

@st.cache_data
def load_transactions():
    df = pd.read_csv("data/account-statement-1-1-2024-12-31-2024.csv", sep=';')
    return df

@st.cache_data
def load_symbols():
    try:
        return pd.read_csv("data/symbols.csv")
    except:
        return pd.DataFrame()

@st.cache_data
def load_countries():
    try:
        return pd.read_csv("data/country.csv")
    except:
        return pd.DataFrame()

@st.cache_data
def load_merged_data():
    transactions = load_transactions()
    symbols = load_symbols()
    countries = load_countries()
    
    if not symbols.empty and 'Symbol' in transactions.columns:
        symbol_col = None
        for col in symbols.columns:
            if 'symbol' in col.lower():
                symbol_col = col
                break
        if symbol_col:
            merged = transactions.merge(symbols, left_on='Symbol', right_on=symbol_col, how='left')
        else:
            merged = transactions
    else:
        merged = transactions
    
    if not countries.empty:
        for col in merged.columns:
            if 'country' not in col.lower():
                for ccol in countries.columns:
                    if col.lower() == ccol.lower():
                        merged = merged.merge(countries, on=col, how='left')
                        break
        
        if 'country' not in merged.columns and 'country' in countries.columns:
            merged['country'] = countries['country'].iloc[0] if not countries.empty else 'Unknown'
    
    return merged
