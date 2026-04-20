"""Starter file for module M1."""

import streamlit as st

from api.blockchain_client import get_latest_block


def render() -> None:
    """Render the M1 panel."""
    st.header("M1 - Proof of Work Monitor")
    st.write("This module shows live Bitcoin mining data from the latest block.")

    if st.button("Fetch latest block", key="m1_fetch"):
        with st.spinner("Fetching data..."):
            try:
                block = get_latest_block()

                st.success("Latest block fetched successfully")

                st.write("### Latest Block Data")
                st.write(f"**Height:** {block.get('height')}")
                st.write(f"**Hash:** {block.get('hash')}")
                st.write(f"**Time:** {block.get('time')}")
                st.write(f"**Number of Transactions:** {block.get('txIndexes') and len(block.get('txIndexes'))}")

            except Exception as exc:
                st.error(f"Error fetching data: {exc}")
    else:
        st.info("Click the button to test the API connection.")

