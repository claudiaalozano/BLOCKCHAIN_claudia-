"""Module M4: AI Component."""

import streamlit as st


def render() -> None:
    """Render the M4 panel."""
    st.header("M4 - AI Component")
    st.write("This module contains the AI component of the dashboard.")

    st.subheader("Chosen AI approach")
    st.success("Anomaly detector for Bitcoin block inter-arrival times")

    st.write(
        "Bitcoin block arrival times are expected to roughly follow an exponential distribution. "
        "This module will identify unusually fast or slow blocks as anomalies."
    )

    st.subheader("Why this approach")
    st.write(
        "This option fits the blockchain data already used in M1 and M3, because those modules "
        "already work with recent block timestamps and block-time intervals."
    )

    st.subheader("Data to use")
    st.markdown(
        """
        - Recent Bitcoin block timestamps from the blockchain API
        - Inter-block times computed from consecutive blocks
        - Historical samples used as a baseline
        """
    )

    st.subheader("Planned evaluation")
    st.markdown(
        """
        - Baseline: exponential distribution with expected mean block time of 600 seconds
        - Output: anomaly score for each block interval
        - Evaluation idea: compare flagged intervals against the expected distribution
        """
    )

    st.subheader("Current status")
    st.info(
        "Skeleton ready for the checkpoint. Next step: compute anomaly scores and show flagged blocks in a chart and table."
    )

    st.subheader("Next implementation steps")
    st.markdown(
        """
        1. Load recent block timestamps from the API.
        2. Compute inter-arrival times between consecutive blocks.
        3. Detect unusually fast or slow intervals.
        4. Visualise anomalies in this tab.
        """
    )
