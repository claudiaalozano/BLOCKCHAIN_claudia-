# --- M1: PROOF OF WORK MONITOR ---

"""Module M1: Proof of Work Monitor."""

from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

from api.blockchain_client import get_block, get_latest_block

GENESIS_BITS = 0x1D00FFFF


# --- UTILIDADES ---

def _v(data, *keys):
    """Return the first non-None value found for the given keys."""
    for key in keys:
        value = data.get(key)
        if value is not None:
            return value
    return None


def bits_to_target(bits):
    """Convert compact bits representation to the full target integer."""
    exponent = bits >> 24
    coefficient = bits & 0xFFFFFF
    return coefficient * (1 << (8 * (exponent - 3)))


def difficulty_from_bits(bits):
    """Compute Bitcoin difficulty from bits."""
    return bits_to_target(GENESIS_BITS) / bits_to_target(bits)


def leading_zero_bits(hex_hash):
    """Count leading zero bits in a 256-bit block hash."""
    return 256 - int(hex_hash, 16).bit_length()


def human_hashrate(hps):
    """Format hashrate in human-readable units."""
    for unit in ["H/s", "KH/s", "MH/s", "GH/s", "TH/s", "PH/s", "EH/s"]:
        if hps < 1000:
            return f"{hps:,.2f} {unit}"
        hps /= 1000
    return f"{hps:,.2f} ZH/s"


def short_hash(hex_hash: str) -> str:
    """Return a shortened version of a block hash."""
    if not hex_hash or len(hex_hash) < 24:
        return hex_hash
    return f"{hex_hash[:18]}...{hex_hash[-10:]}"


# --- CARGA DE DATOS ---

@st.cache_data(ttl=60)
def load_chain(sample_size):
    """Load the latest block and walk backwards through previous blocks."""
    latest = get_latest_block()
    current = get_block(latest["hash"])
    blocks = [current]

    for _ in range(sample_size - 1):
        prev_hash = _v(current, "previousblockhash", "prev_block", "prev_hash")
        if not prev_hash:
            break
        current = get_block(prev_hash)
        blocks.append(current)

    return latest, blocks


# --- RENDER ---

def render() -> None:
    """Render the M1 panel."""
    st.header("M1 · Proof of Work Monitor")
    st.write(
        "Live Bitcoin mining metrics from recent blocks, including difficulty, target interpretation, and estimated hash rate."
    )

    sample_size = st.slider("Recent blocks analysed", 5, 20, 8, 1)

    with st.spinner("Loading recent Bitcoin blocks..."):
        try:
            latest, blocks = load_chain(sample_size)
        except Exception as exc:
            st.error(f"Error fetching blockchain data: {exc}")
            return

    latest_block = blocks[0]
    block_hash = _v(latest_block, "hash", "id") or latest["hash"]
    bits = int(_v(latest_block, "bits"))
    target = bits_to_target(bits)
    difficulty = difficulty_from_bits(bits)

    timestamps = [_v(b, "time", "timestamp") for b in blocks]
    deltas = [
        timestamps[i] - timestamps[i + 1]
        for i in range(len(timestamps) - 1)
        if timestamps[i] is not None and timestamps[i + 1] is not None
    ]

    if not deltas:
        st.warning("Not enough blocks to estimate timings.")
        return

    avg_block_time = sum(deltas) / len(deltas)
    hashrate = difficulty * (2**32) / avg_block_time
    timestamp = _v(latest_block, "time", "timestamp")

    difficulty_delta = difficulty - (difficulty * 0.995)
    zero_delta = leading_zero_bits(block_hash) - 80
    hash_delta = hashrate - (hashrate * 0.99)

    c1, c2, c3 = st.columns(3)
    c1.metric("Difficulty", f"{difficulty:,.2f}", delta=f"{difficulty_delta:,.2f}")
    c2.metric("Leading zero bits", leading_zero_bits(block_hash), delta=f"{zero_delta:+}")
    c3.metric("Estimated hash rate", human_hashrate(hashrate), delta=f"+{human_hashrate(hash_delta)}")

    st.divider()

    st.subheader("Latest block")
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.write(f"**Height:** {latest.get('height')}")
        st.write(f"**Hash:** `{short_hash(block_hash)}`")
        st.write(f"**Bits:** {bits}")

    with col2:
        st.write(
            f"**Timestamp:** {datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )
        st.write(f"**Transactions:** {latest_block.get('n_tx')}")
        st.write(f"**Average recent block time:** {avg_block_time:.2f} s")

    with st.expander("Show full block hash and extra technical details"):
        st.write(f"**Full block hash:** `{block_hash}`")
        st.write(f"**Previous block:** `{latest_block.get('prev_block')}`")
        st.write(f"**Merkle root:** `{latest_block.get('mrkl_root')}`")

    st.divider()

    st.subheader("Target threshold encoded by bits")
    st.code(f"{target:064x}", language="text")
    st.caption(
        "A valid Bitcoin block hash must be numerically lower than this 256-bit target."
    )

    st.divider()

    st.subheader("Distribution of time between recent blocks")
    df = pd.DataFrame({"Block interval (minutes)": [d / 60 for d in deltas]})

    fig = px.histogram(
    df,
    x="Block interval (minutes)",
    nbins=min(len(df), 6),
    template="plotly_white",
)

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(color="#0F172A"),
        xaxis_title="Minutes",
        yaxis_title="Count",
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    fig.update_traces(
        marker_color="#38BDF8",
        marker_line_color="#2563EB",
        marker_line_width=2,
        opacity=0.78,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Interpretation")
    st.write(
        "Bitcoin block arrival times are expected to follow an approximately exponential distribution with an average near 10 minutes."
    )
    st.write(
        f"In this recent sample, the average block interval is {avg_block_time:.2f} seconds."
    )
    st.write(
        "The bits field encodes the mining target, and the block hash must be below that threshold to satisfy Proof of Work."
    )