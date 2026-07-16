import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Financial Metrics Comparison", layout="wide")
st.title("📊 Financial Metrics Comparison")

@st.cache_data
def load_financials():
    return pd.read_csv("data/output.csv")

df = load_financials()
df = df.dropna(subset=['sector', 'industry'])

sectors = sorted(df['sector'].unique())
selected_sector = st.selectbox("Select Sector", sectors)
sector_df = df[df['sector'] == selected_sector]

industries = sorted(sector_df['industry'].unique())
selected_industry = st.selectbox("Select Industry", industries)
industry_df = sector_df[sector_df['industry'] == selected_industry]

top_companies = industry_df.nlargest(10, 'market_cap')
industry_avg = industry_df['market_cap'].mean()

companies = sorted(industry_df['company_name'].unique())
selected_company = st.selectbox("Select Company to Highlight", ["None"] + companies)

# Colorful bar chart with gradient
fig1 = px.bar(top_companies, x='company_name', y='market_cap', 
              title=f"Top 10 Companies by Market Cap in {selected_industry}",
              labels={'company_name': 'Company', 'market_cap': 'Market Cap (USD)'},
              color='market_cap',
              color_continuous_scale='Viridis',
              template='plotly_dark',
              text_auto='.2s')

fig1.add_hline(y=industry_avg, line_dash="dash", line_color="#FF6B6B", 
               annotation_text=f"Industry Avg: ${industry_avg/1e9:.2f}B", 
               annotation_position="top right")
st.plotly_chart(fig1, use_container_width=True)

# Scatter plot with color by sector
fig2 = px.scatter(sector_df, x='total_revenue', y='net_income', 
                  title=f"Revenue vs Net Income in {selected_sector} Sector",
                  labels={'total_revenue': 'Total Revenue (USD)', 'net_income': 'Net Income (USD)'},
                  hover_data=['company_name'],
                  color='company_name',
                  template='plotly_dark',
                  size='market_cap',
                  size_max=20)

if selected_company != "None":
    selected_row = sector_df[sector_df['company_name'] == selected_company]
    if not selected_row.empty:
        fig2.add_scatter(x=selected_row['total_revenue'], 
                         y=selected_row['net_income'],
                         mode='markers',
                         marker=dict(size=30, color='#FF6B6B', symbol='star'),
                         name=f"⭐ {selected_company}")
st.plotly_chart(fig2, use_container_width=True)
