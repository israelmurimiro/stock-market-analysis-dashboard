import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Financial Dashboard", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for 3D-like panels and visual appeal
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 50%, #0d1b2a 100%);
    }
    
    .panel-3d {
        background: linear-gradient(145deg, rgba(20, 30, 60, 0.95), rgba(10, 15, 35, 0.98));
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(100, 200, 255, 0.15);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.05),
            0 0 40px rgba(0, 100, 255, 0.05);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .panel-3d:hover {
        transform: translateY(-4px);
        box-shadow: 
            0 12px 48px rgba(0, 0, 0, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.08),
            0 0 60px rgba(0, 100, 255, 0.1);
        border-color: rgba(100, 200, 255, 0.3);
    }
    
    .glow-text {
        background: linear-gradient(135deg, #00d4ff, #0088ff, #7b2ffc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        text-shadow: 0 0 60px rgba(0, 136, 255, 0.3);
    }
    
    .glow-subtitle {
        color: #8899bb;
        font-size: 1.1rem;
        letter-spacing: 2px;
    }
    
    .nav-card {
        background: linear-gradient(145deg, rgba(25, 40, 75, 0.9), rgba(15, 25, 50, 0.95));
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        border: 1px solid rgba(100, 200, 255, 0.08);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
        text-align: center;
    }
    
    .nav-card:hover {
        transform: translateY(-3px) scale(1.02);
        border-color: rgba(100, 200, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 100, 255, 0.2);
    }
    
    .nav-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .nav-title {
        color: #ffffff;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .nav-desc {
        color: #8899bb;
        font-size: 0.8rem;
        margin-top: 0.2rem;
    }
    
    .stat-box {
        background: rgba(10, 20, 45, 0.6);
        border-radius: 12px;
        padding: 0.8rem 1.2rem;
        border: 1px solid rgba(100, 200, 255, 0.06);
        text-align: center;
    }
    
    .stat-number {
        font-size: 1.6rem;
        font-weight: 700;
        color: #00d4ff;
    }
    
    .stat-label {
        color: #667799;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .glow-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 136, 255, 0.3), rgba(123, 47, 252, 0.3), transparent);
        margin: 2rem 0;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #080c24 0%, #0d1a35 100%);
        border-right: 1px solid rgba(100, 200, 255, 0.08);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #8899bb;
    }
    
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(10, 15, 35, 0.5);
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #0088ff, #7b2ffc);
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="font-size: 3rem;">📊</div>
        <div style="font-size: 1.5rem; font-weight: 700; color: #ffffff;">Financial</div>
        <div style="font-size: 1.2rem; font-weight: 300; color: #0088ff;">Dashboard</div>
        <div style="font-size: 0.7rem; color: #667799; margin-top: 0.3rem;">v2.0 · Interactive Analytics</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="color: #8899bb; font-size: 0.8rem; padding: 0.5rem 0;">
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.3rem 0;">
            <span style="color: #00d4ff;">●</span> Real-time data
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.3rem 0;">
            <span style="color: #00d4ff;">●</span> Multi-page analysis
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.3rem 0;">
            <span style="color: #00d4ff;">●</span> Interactive charts
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.3rem 0;">
            <span style="color: #00d4ff;">●</span> Stock tracking
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="color: #667799; font-size: 0.7rem; text-align: center; padding: 0.5rem 0;">
        Data sourced from financial markets<br>
        Updated in real-time
    </div>
    """, unsafe_allow_html=True)

# MAIN CONTENT
st.markdown("""
<div style="text-align: center; padding: 1rem 0 2rem 0;">
    <div class="glow-text">📈 Financial Dashboard</div>
    <div class="glow-subtitle">Comprehensive Market Analytics & Transaction Insights</div>
    <div style="color: #445566; font-size: 0.85rem; margin-top: 0.5rem;">
        Built by ISRAEL MURIMIRO with Streamlit · Powered by Python · Data-driven Decisions
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Stats Row
try:
    df = pd.read_csv("data/account-statement-1-1-2024-12-31-2024.csv", sep=';')
    total_transactions = len(df)
    unique_symbols = df['Symbol'].nunique()
    top_symbols = df['Symbol'].value_counts().head(3).index.tolist()
    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    if not df['Date'].isna().all():
        date_range = f"{df['Date'].min().strftime('%b %d, %Y')} - {df['Date'].max().strftime('%b %d, %Y')}"
    else:
        date_range = "N/A"
    
    # Format numbers for display
    if isinstance(total_transactions, int):
        total_display = f"{total_transactions:,}"
    else:
        total_display = str(total_transactions)
    
    if isinstance(unique_symbols, int):
        unique_display = f"{unique_symbols:,}"
    else:
        unique_display = str(unique_symbols)
    
    top_display = ', '.join(top_symbols[:3]) if top_symbols else "N/A"
    
except Exception as e:
    total_display = "N/A"
    unique_display = "N/A"
    top_display = "N/A"
    date_range = "N/A"

stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{total_display}</div>
        <div class="stat-label">Total Transactions</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{unique_display}</div>
        <div class="stat-label">Unique Symbols</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number" style="font-size: 1.2rem;">{top_display}</div>
        <div class="stat-label">Top Traded Symbols</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number" style="font-size: 1rem;">{date_range}</div>
        <div class="stat-label">Data Period</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="glow-divider"></div>', unsafe_allow_html=True)

# Navigation Cards
st.markdown('<div style="text-align: center; color: #8899bb; font-size: 0.9rem; margin-bottom: 1.5rem;">🔍 Select a module to explore</div>', unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    st.markdown("""
    <a href="/1_transactions" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">📈</div>
            <div class="nav-title">Transactions</div>
            <div class="nav-desc">Time-based transaction analysis</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with nav_col2:
    st.markdown("""
    <a href="/2_country" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">🌍</div>
            <div class="nav-title">Country Analysis</div>
            <div class="nav-desc">Geographic transaction insights</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with nav_col3:
    st.markdown("""
    <a href="/3_financials" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">📊</div>
            <div class="nav-title">Financials</div>
            <div class="nav-desc">Company financial comparisons</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with nav_col4:
    st.markdown("""
    <a href="/4_stock" target="_self" style="text-decoration: none;">
        <div class="nav-card">
            <div class="nav-icon">📉</div>
            <div class="nav-title">Stock Prices</div>
            <div class="nav-desc">Real-time price tracking</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown('<div class="glow-divider"></div>', unsafe_allow_html=True)

# Information Panels
info_col1, info_col2 = st.columns(2)

with info_col1:
    st.markdown("""
    <div class="panel-3d">
        <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.8rem;">
            <span style="font-size: 2rem;">🚀</span>
            <div>
                <div style="color: #ffffff; font-weight: 600; font-size: 1.1rem;">Getting Started</div>
                <div style="color: #667799; font-size: 0.85rem;">Quick tips for using this dashboard</div>
            </div>
        </div>
        <div style="color: #8899bb; font-size: 0.9rem; line-height: 1.8;">
            <div>1️⃣ Use the sidebar to navigate between analysis modules</div>
            <div>2️⃣ Each page provides interactive filters for deep dives</div>
            <div>3️⃣ Hover over charts for detailed tooltips</div>
            <div>4️⃣ Export data and reports as needed</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with info_col2:
    st.markdown("""
    <div class="panel-3d">
        <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.8rem;">
            <span style="font-size: 2rem;">💡</span>
            <div>
                <div style="color: #ffffff; font-weight: 600; font-size: 1.1rem;">Key Features</div>
                <div style="color: #667799; font-size: 0.85rem;">What you can do with this tool</div>
            </div>
        </div>
        <div style="color: #8899bb; font-size: 0.9rem; line-height: 1.8;">
            <div>📈 Track transaction volumes over time</div>
            <div>🌍 Analyze activity by country</div>
            <div>📊 Compare company financial metrics</div>
            <div>📉 Monitor stock price trends in real-time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Bottom info
st.markdown("""
<div style="text-align: center; color: #445566; font-size: 0.75rem; padding: 2rem 0 0.5rem 0;">
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <span>📊 Built with Streamlit</span>
        <span>🐍 Python · Pandas · Plotly</span>
        <span>📈 Real-time Analytics</span>
    </div>
    <div style="margin-top: 0.5rem; color: #334455;">
        © 2024 Financial Dashboard · All Rights Reserved
    </div>
</div>
""", unsafe_allow_html=True)

