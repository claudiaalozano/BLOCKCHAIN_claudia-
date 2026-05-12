"""Main Streamlit entry point for the Blockchain Dashboard project."""

import streamlit as st

from modules.m1_pow_monitor import render as render_m1
from modules.m2_block_header import render as render_m2
from modules.m3_difficulty_history import render as render_m3
from modules.m4_ai_component import render as render_m4

st.set_page_config(
    page_title="CryptoChain Analyzer Dashboard",
    page_icon="₿",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #1f2937;
    }
    [data-testid="stMetricValue"] {
        font-size: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("₿ CryptoChain Analyzer Dashboard")
st.caption("Real-time Bitcoin cryptographic metrics, Proof of Work analysis, difficulty history, and anomaly detection.")

with st.sidebar:
    st.header("Dashboard Info")
    st.write("Cryptography Project")
    st.write("Student: Claudia Lozano")
    st.write("Blockchain: Bitcoin")
    st.write("Framework: Streamlit")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "M1 · PoW Monitor",
        "M2 · Block Header",
        "M3 · Difficulty History",
        "M4 · AI Anomaly Detector",
    ]
)

with tab1:
    render_m1()

with tab2:
    render_m2()

with tab3:
    render_m3()

with tab4:
    render_m4()