"""Module M1: Proof of Work Monitor."""

import streamlit as st

from api.blockchain_client import get_latest_block, get_block


def render() -> None:
    """Render the M1 panel."""
    st.header("M1 - Proof of Work Monitor")
    st.write("This module shows live Bitcoin mining data from the latest Bitcoin block.")

    if st.button("Fetch latest block", key="m1_fetch"):
        with st.spinner("Fetching data..."):
            try:
                latest = get_latest_block()
                block = get_block(latest["hash"])

                st.success("Latest block fetched successfully")

                st.subheader("Latest Block Data")
                st.write(f"**Height:** {latest.get('height')}")
                st.write(f"**Hash:** {latest.get('hash')}")
                st.write(f"**Bits:** {block.get('bits')}")
                st.write(f"**Nonce:** {block.get('nonce')}")
                st.write(f"**Number of Transactions:** {block.get('n_tx')}")
                st.write(f"**Timestamp:** {block.get('time')}")

                st.subheader("Proof of Work Interpretation")
                st.write(
                    "The block hash starts with leading zeros, which is consistent with Bitcoin Proof of Work."
                )
                st.write(
                    "The 'bits' field is the compact representation of the mining target threshold."
                )
                st.write(
                    "Miners vary the nonce to find a block hash that is below the target."
                )

            except Exception as exc:
                st.error(f"Error fetching data: {exc}")
    else:
        st.info("Click the button to fetch live Bitcoin block data.")