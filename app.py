"""Main Streamlit entry point for the Blockchain Dashboard project."""

import streamlit as st

from modules.m1_pow_monitor import render as render_m1
from modules.m2_block_header import render as render_m2
from modules.m3_difficulty_history import render as render_m3
from modules.m4_ai_component import render as render_m4

# --- CONFIGURACIÓN GENERAL ---

st.set_page_config(
    page_title="CryptoChain Analyzer Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ESTILOS GLOBALES LIGHT / FINTECH ---

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0,191,255,0.06), transparent 28%),
            linear-gradient(180deg, #F8FAFC 0%, #EEF3F8 100%);
        color: #0F172A;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #EAF4FF 0%, #F5FAFF 100%);
        border-right: 1px solid rgba(37,99,235,0.10);
    }

    section[data-testid="stSidebar"] * {
        color: #0F172A !important;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1.3rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #0F172A !important;
        letter-spacing: -0.02em;
    }

    p, label, li, div {
        color: #334155;
    }

    .hero-box {
        background: linear-gradient(135deg, #FFFFFF, #F4F9FF);
        border: 1px solid rgba(37,99,235,0.14);
        border-radius: 22px;
        padding: 1.6rem 1.7rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 30px rgba(15,23,42,0.08);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #0F172A;
        margin: 0;
    }

    .hero-subtitle {
        font-size: 1.02rem;
        color: #475569;
        margin-top: 0.45rem;
        margin-bottom: 0;
        line-height: 1.6;
    }

    .info-card {
        background: #FFFFFF;
        border: 1px solid rgba(37,99,235,0.12);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        min-height: 170px;
        box-shadow: 0 8px 24px rgba(15,23,42,0.06);
        margin-bottom: 1rem;
    }

    .info-card h3 {
        margin-top: 0.1rem;
        margin-bottom: 0.55rem;
        color: #0F172A !important;
        font-size: 1.08rem;
    }

    .info-card p {
        margin: 0;
        color: #475569;
        line-height: 1.6;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F8FBFF 100%);
        border: 1px solid rgba(37,99,235,0.12);
        border-radius: 18px;
        padding: 16px 18px;
        box-shadow: 0 8px 22px rgba(15,23,42,0.06);
    }

    [data-testid="stMetricLabel"] {
        color: #64748B !important;
        font-size: 0.92rem;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: #0F172A !important;
        font-size: 1.9rem;
        font-weight: 800;
    }

    [data-testid="stMetricDelta"] {
        color: #00B27A !important;
        font-weight: 700;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.35rem;
        border-bottom: 1px solid rgba(37,99,235,0.10);
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #64748B;
        border-radius: 10px 10px 0 0;
        padding: 0.6rem 0.9rem;
    }

    .stTabs [aria-selected="true"] {
        color: #2563EB !important;
        border-bottom: 2px solid #2563EB !important;
    }

    .stExpander {
        border-radius: 16px;
        border: 1px solid rgba(37,99,235,0.10);
        background: #FFFFFF;
    }

    .stDataFrame {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(37,99,235,0.10);
    }

    hr.custom-divider {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(37,99,235,0.35), transparent);
        margin: 1.3rem 0 1rem 0;
    }

    .footer-box {
        margin-top: 1.4rem;
        padding: 1rem 1.2rem;
        border-radius: 16px;
        border: 1px solid rgba(37,99,235,0.10);
        background: #FFFFFF;
        color: #64748B;
        font-size: 0.92rem;
        text-align: center;
        box-shadow: 0 6px 16px rgba(15,23,42,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SIDEBAR ---

with st.sidebar:
    st.markdown("## Navigation:")
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

# --- HERO ---

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">₿ CryptoChain Analyzer Dashboard</div>
        <p class="hero-subtitle">
            Real-time Bitcoin cryptographic metrics, Proof of Work verification,
            difficulty adjustment analysis, and anomaly detection in a clean
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

    st.info(
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