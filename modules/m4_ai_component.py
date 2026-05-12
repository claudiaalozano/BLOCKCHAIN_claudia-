"""Module M4: AI anomaly detector for Bitcoin block inter-arrival times."""

from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

from api.blockchain_client import get_block, get_latest_block


def _v(data, *keys):
    for key in keys:
        value = data.get(key)
        if value is not None:
            return value
    return None


@st.cache_data(ttl=120)
def load_recent_blocks(sample_size: int):
    latest = get_latest_block()
    current = get_block(latest["hash"])
    blocks = [current]

    for _ in range(sample_size - 1):
        prev_hash = _v(current, "previousblockhash", "prev_block", "prev_hash")
        if not prev_hash:
            break
        current = get_block(prev_hash)
        blocks.append(current)

    return blocks


def build_intervals_dataframe(blocks):
    rows = []

    for i in range(len(blocks) - 1):
        current_block = blocks[i]
        previous_block = blocks[i + 1]

        current_time = _v(current_block, "time", "timestamp")
        previous_time = _v(previous_block, "time", "timestamp")

        if current_time is None or previous_time is None:
            continue

        interval = current_time - previous_time

        rows.append(
            {
                "Block Height": _v(current_block, "height"),
                "Block Hash": _v(current_block, "hash", "id"),
                "Timestamp": datetime.utcfromtimestamp(current_time),
                "Inter-arrival Time (s)": interval,
            }
        )

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    mean_interval = df["Inter-arrival Time (s)"].mean()
    std_interval = df["Inter-arrival Time (s)"].std()

    if std_interval == 0 or pd.isna(std_interval):
        df["Z-Score"] = 0.0
    else:
        df["Z-Score"] = (df["Inter-arrival Time (s)"] - mean_interval) / std_interval

    df["Anomaly"] = df["Z-Score"].abs() > 2
    df["Deviation from 600s"] = df["Inter-arrival Time (s)"] - 600

    return df


def render() -> None:
    st.header("M4 · AI Anomaly Detector")
    st.write("Detection of unusual Bitcoin block inter-arrival times using a simple statistical model.")

    sample_size = st.slider(
        "Recent blocks to analyse",
        min_value=20,
        max_value=100,
        value=40,
        step=10,
        key="m4_sample_size",
    )

    with st.spinner("Analysing recent Bitcoin blocks..."):
        try:
            blocks = load_recent_blocks(sample_size)
            df = build_intervals_dataframe(blocks)

            if df.empty:
                st.warning("No interval data could be computed.")
                return

            total_intervals = len(df)
            anomaly_count = int(df["Anomaly"].sum())
            mean_interval = df["Inter-arrival Time (s)"].mean()

            c1, c2, c3 = st.columns(3)
            c1.metric("Intervals analysed", total_intervals)
            c2.metric("Anomalies detected", anomaly_count)
            c3.metric("Average block time", f"{mean_interval:.2f} s")

            st.markdown("### Inter-arrival Time Distribution")
            fig = px.scatter(
                df,
                x="Timestamp",
                y="Inter-arrival Time (s)",
                color="Anomaly",
                hover_data=["Block Height", "Z-Score"],
                title="Bitcoin Block Inter-arrival Times",
            )
            fig.add_hline(y=600, line_dash="dash")
            st.plotly_chart(fig, use_container_width=True)

            anomalies = df[df["Anomaly"]].copy()

            st.markdown("### Anomalous Blocks")
            if anomalies.empty:
                st.success("No anomalies detected with the current threshold.")
            else:
                anomalies["Z-Score"] = anomalies["Z-Score"].round(2)
                anomalies["Deviation from 600s"] = anomalies["Deviation from 600s"].round(2)
                st.dataframe(
                    anomalies[
                        [
                            "Block Height",
                            "Timestamp",
                            "Inter-arrival Time (s)",
                            "Deviation from 600s",
                            "Z-Score",
                        ]
                    ],
                    use_container_width=True,
                )

            with st.expander("Model explanation and evaluation"):
                st.write(
                    "The baseline assumption is that Bitcoin block times roughly follow an exponential distribution with expected mean 600 seconds."
                )
                st.write(
                    "This detector uses z-scores. Intervals with absolute z-score greater than 2 are flagged as anomalous."
                )
                st.write(
                    f"In this sample, {anomaly_count} out of {total_intervals} intervals were flagged as anomalous."
                )

        except Exception as exc:
            st.error(f"Error running anomaly detection: {exc}")