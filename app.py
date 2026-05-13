# --- APP PRINCIPAL ---

"""Main Streamlit entry point for the Blockchain Dashboard project."""

import streamlit as st

from modules.m1_pow_monitor import render as render_m1
from modules.m2_block_header import render as render_m2
from modules.m3_difficulty_history import render as render_m3
from modules.m4_ai_component import render as render_m4

# --- CONFIGURACIÓN GENERAL ---

st.set_page_config(
    page_title="CryptoChain Analyzer Dashboard",
    page_icon="⛓️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ESTILOS GLOBALES ---

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0,191,255,0.08), transparent 30%),
            linear-gradient(180deg, #0D1117 0%, #111827 100%);
        color: #F0F4F8;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #0F172A 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #F0F4F8 !important;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1.3rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #F0F4F8 !important;
        letter-spacing: -0.02em;
    }

    p, label, li, div {
        color: #C9D1D9;
    }

    .hero-box {
        background: linear-gradient(135deg, rgba(30,42,56,0.92), rgba(17,24,39,0.96));
        border: 1px solid rgba(0,191,255,0.22);
        border-radius: 22px;
        padding: 1.6rem 1.7rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.28);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #F0F4F8;
        margin: 0;
    }

    .hero-subtitle {
        font-size: 1.02rem;
        color: #A9B4C2;
        margin-top: 0.45rem;
        margin-bottom: 0;
        line-height: 1.6;
    }

    .info-card {
        background: rgba(30,42,56,0.82);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        min-height: 170px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.22);
        margin-bottom: 1rem;
    }

    .info-card h3 {
        margin-top: 0.1rem;
        margin-bottom: 0.55rem;
        color: #F0F4F8 !important;
        font-size: 1.08rem;
    }

    .info-card p {
        margin: 0;
        color: #B8C4D1;
        line-height: 1.6;
    }

    [data-testid="stMetric"] {
        background: rgba(30,42,56,0.9);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 16px 18px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.20);
    }

    [data-testid="stMetricLabel"] {
        color: #9FB1C1 !important;
        font-size: 0.92rem;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: #F0F4F8 !important;
        font-size: 1.9rem;
        font-weight: 800;
    }

    [data-testid="stMetricDelta"] {
        color: #00D68F !important;
        font-weight: 700;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.35rem;
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #AAB7C4;
        border-radius: 10px 10px 0 0;
        padding: 0.6rem 0.9rem;
    }

    .stTabs [aria-selected="true"] {
        color: #00BFFF !important;
        border-bottom: 2px solid #00BFFF !important;
    }

    .stExpander {
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.08);
        background: rgba(30,42,56,0.65);
    }

    .stCodeBlock, code {
        border-radius: 14px !important;
    }

    .stDataFrame {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.08);
    }

    hr.custom-divider {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0,191,255,0.45), transparent);
        margin: 1.3rem 0 1rem 0;
    }

    .footer-box {
        margin-top: 1.4rem;
        padding: 1rem 1.2rem;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.08);
        background: rgba(17,24,39,0.92);
        color: #94A3B8;
        font-size: 0.92rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SIDEBAR ---

with st.sidebar:
    st.markdown("## ⛓️ Navigation")
    st.caption("Blockchain analytics dashboard")

    st.markdown("### Sections")
    st.write("**Overview**")
    st.write("**M1** · Proof of Work Monitor")
    st.write("**M2** · Block Header Analyzer")
    st.write("**M3** · Difficulty History")
    st.write("**M4** · AI Anomaly Detector")

    st.divider()

    st.markdown("### Context")
    st.write("**Blockchain:** Bitcoin")
    st.write("**Theme:** Cryptography + Security")
    st.write("**AI approach:** Statistical anomaly detection")

    st.divider()

    st.info(
        "This app combines live Bitcoin blockchain data, cryptographic verification, "
        "difficulty analysis, and a lightweight AI anomaly detector."
    )

# --- HERO ---

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">₿ CryptoChain Analyzer Dashboard</div>
        <p class="hero-subtitle">
            Real-time Bitcoin cryptographic metrics, Proof of Work verification,
            difficulty adjustment analysis, and anomaly detection in a professional
            blockchain analytics interface.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

tabs = st.tabs(
    [
        "Overview",
        "M1 · PoW Monitor",
        "M2 · Block Header",
        "M3 · Difficulty History",
        "M4 · AI Anomaly Detector",
    ]
)

# --- OVERVIEW ---

with tabs[0]:
    st.header("Project Overview")
    st.write(
        "This dashboard analyses live Bitcoin blockchain data and connects the results "
        "to key cryptographic concepts such as Proof of Work, difficulty adjustment, "
        "block headers, and anomaly detection."
    )

    c1, c2 = st.columns(2)
    c1.metric("Blockchain", "Bitcoin")
    c2.metric("AI Approach", "Anomaly detection")

    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    st.subheader("What this project does")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>M1 · Proof of Work Monitor</h3>
                <p>Displays live mining metrics such as difficulty, leading zero bits, target interpretation, and estimated network hash rate.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="info-card">
                <h3>M2 · Block Header Analyzer</h3>
                <p>Reconstructs the 80-byte Bitcoin block header and verifies the block hash locally using double SHA-256.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>M3 · Difficulty History</h3>
                <p>Explores real difficulty-adjustment periods and compares actual mining time with the 600-second protocol target.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="info-card">
                <h3>M4 · AI Anomaly Detector</h3>
                <p>Flags unusual block inter-arrival times using a statistical anomaly detector based on z-scores.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    st.subheader("Project Focus")
    st.write(
        "The objective is to combine live blockchain data, cryptographic validation, "
        "historical difficulty analysis, and an AI-based interpretation layer into a "
        "single polished dashboard."
    )

# --- MÓDULOS ---

with tabs[1]:
    render_m1()

with tabs[2]:
    render_m2()

with tabs[3]:
    render_m3()

with tabs[4]:
    render_m4()

# --- FOOTER ---

st.markdown(
    """
    <div class="footer-box">
        CryptoChain Analyzer Dashboard · Streamlit + Python · Blockchain / Cryptography Project
    </div>
    """,
    unsafe_allow_html=True,
)