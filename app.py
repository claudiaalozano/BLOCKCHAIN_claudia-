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
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1350px;
    }

    h1 {
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.25rem !important;
        color: #111827 !important;
    }

    h2 {
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin-top: 0.5rem !important;
        color: #111827 !important;
    }

    h3 {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
    }

    p, li, label, div {
        color: #374151;
    }

    [data-testid="stMetric"] {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        padding: 16px 18px;
        border-radius: 16px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.95rem;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: 750;
        color: #111827;
    }

    .hero-box {
        padding: 1.5rem 1.6rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #f8fafc, #eef2ff);
        border: 1px solid #e5e7eb;
        margin-bottom: 1.2rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #4b5563;
        margin-top: 0.35rem;
        margin-bottom: 0;
    }

    .info-card {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1rem 1.1rem;
        height: 100%;
        margin-bottom: 1rem;
    }

    .stExpander {
        border-radius: 14px;
        border: 1px solid #e5e7eb;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-box">
        <h1>₿ CryptoChain Analyzer Dashboard</h1>
        <p class="hero-subtitle">
            Real-time Bitcoin cryptographic metrics, Proof of Work verification,
            difficulty adjustment analysis, and anomaly detection.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Navigation")
    st.write("Use the tabs to explore the project modules.")

tabs = st.tabs(
    [
        "Overview",
        "M1 · PoW Monitor",
        "M2 · Block Header",
        "M3 · Difficulty History",
        "M4 · AI Anomaly Detector",
    ]
)

with tabs[0]:
    st.header("Project Overview")
    st.write(
        "This dashboard analyses live Bitcoin blockchain data and connects the results to core cryptographic concepts studied in class."
    )

    c1, c2, c3 = st.columns([1, 1, 0.2])
    c1.metric("Blockchain", "Bitcoin")
    c2.metric("AI Approach", "Anomaly detection")

    st.markdown("### What this project does")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>M1 · Proof of Work Monitor</h3>
                <p>Shows live mining-related data such as the latest block information, target representation, and Proof of Work interpretation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="info-card">
                <h3>M2 · Block Header Analyzer</h3>
                <p>Displays the Bitcoin block header fields, reconstructs the 80-byte header, and verifies the Proof of Work locally using double SHA-256.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>M3 · Difficulty History</h3>
                <p>Shows how Bitcoin difficulty evolves over real adjustment periods and compares actual mining time with the 600-second target.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="info-card">
                <h3>M4 · AI Anomaly Detector</h3>
                <p>Detects unusual block inter-arrival times using a simple statistical model and highlights potentially abnormal timing behaviour.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Project focus")
    st.write(
        "The goal of this project is to combine live blockchain data, cryptographic verification, visual analysis, and an AI-based interpretation layer in a single dashboard."
    )

with tabs[1]:
    render_m1()

with tabs[2]:
    render_m2()

with tabs[3]:
    render_m3()

with tabs[4]:
    render_m4()