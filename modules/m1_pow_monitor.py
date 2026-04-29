"""Module M1: Proof of Work Monitor."""

from datetime import datetime

import pandas as pd
import streamlit as st

from api.blockchain_client import get_block, get_latest_block

GENESIS_BITS = 0x1D00FFFF


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


def render() -> None:
    """Render the M1 panel."""
    st.header("M1 - Proof of Work Monitor")
    st.write("This module shows live Bitcoin mining data from recent Bitcoin blocks.")
    sample_size = st.slider("Blocks to analyse", 5, 10, 6, 1)


    if st.button("Refresh now", key="m1_refresh"):
        load_chain.clear()

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

    c1, c2, c3 = st.columns(3)
    c1.metric("Difficulty", f"{difficulty:,.2f}")
    c2.metric("Leading zero bits", leading_zero_bits(block_hash))
    c3.metric("Estimated hash rate", human_hashrate(hashrate))

    st.subheader("Latest block")
    st.write(f"**Height:** {latest.get('height')}")
    st.write(f"**Hash:** `{block_hash}`")
    st.write(f"**Bits:** {bits}")
    st.write(
        f"**Timestamp:** {datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')}"
    )

    st.subheader("Target threshold encoded by bits")
    st.code(f"{target:064x}", language="text")
    st.caption(
        "A valid Bitcoin block hash must be numerically lower than this 256-bit target."
    )

    st.subheader("Time between recent blocks")
    minutes = pd.Series([d / 60 for d in deltas], name="minutes")
    bins = list(range(0, 62, 2)) + [999]
    hist = pd.cut(minutes, bins=bins, right=False).value_counts().sort_index()
    hist.index = hist.index.astype(str)
    st.bar_chart(hist)

    st.caption(
        "Block arrival times should look roughly exponential, with a mean near 10 minutes."
    )

