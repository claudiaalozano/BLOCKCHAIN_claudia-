# --- M3: DIFFICULTY HISTORY ---

"""Module M3: Difficulty History."""

import pandas as pd
import plotly.express as px
import streamlit as st

from api.blockchain_client import get_block_by_height, get_latest_height

BLOCKS_PER_PERIOD = 2016
TARGET_BLOCK_TIME = 600
TARGET_PERIOD_TIME = BLOCKS_PER_PERIOD * TARGET_BLOCK_TIME


# --- CÁLCULO DE PERIODOS DE AJUSTE ---

@st.cache_data(ttl=300)
def build_adjustment_periods(n_periods: int) -> pd.DataFrame:
    """Build a dataframe with real Bitcoin difficulty-adjustment periods."""
    latest_height = get_latest_height()
    last_completed_boundary = latest_height - (latest_height % BLOCKS_PER_PERIOD)

    rows = []

    for i in range(n_periods):
        end_height = last_completed_boundary - i * BLOCKS_PER_PERIOD
        start_height = end_height - BLOCKS_PER_PERIOD

        if start_height < 0:
            break

        start_block = get_block_by_height(start_height)
        end_block = get_block_by_height(end_height)

        actual_period_time = end_block["time"] - start_block["time"]
        ratio = actual_period_time / TARGET_PERIOD_TIME

        rows.append(
            {
                "Start Height": start_height,
                "End Height": end_height,
                "Start Time": pd.to_datetime(start_block["time"], unit="s"),
                "End Time": pd.to_datetime(end_block["time"], unit="s"),
                "Difficulty": end_block.get("difficulty"),
                "Actual Period Time (s)": actual_period_time,
                "Target Period Time (s)": TARGET_PERIOD_TIME,
                "Actual/Target Ratio": ratio,
                "Avg Block Time (s)": actual_period_time / BLOCKS_PER_PERIOD,
            }
        )

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values("End Height").reset_index(drop=True)

    return df


# --- RENDER ---

def render() -> None:
    """Render the M3 panel."""
    st.header("M3 · Difficulty History")
    st.write(
        "This module shows Bitcoin difficulty over the latest completed adjustment periods (1 period = 2016 blocks)."
    )

    n_periods = st.slider(
        "Completed adjustment periods",
        min_value=3,
        max_value=12,
        value=6,
        key="m3_periods",
    )

    with st.spinner("Loading adjustment-period analysis..."):
        try:
            df = build_adjustment_periods(n_periods)

            if df.empty:
                st.warning("No adjustment-period data could be loaded.")
                return

            latest_ratio = df["Actual/Target Ratio"].iloc[-1] - 1

            c1, c2, c3 = st.columns(3)
            c1.metric("Periods analysed", len(df))
            c2.metric("Latest difficulty", f"{df['Difficulty'].iloc[-1]:,.0f}")
            c3.metric(
                "Latest avg block time",
                f"{df['Avg Block Time (s)'].iloc[-1]:.2f} s",
                delta=f"{latest_ratio:+.4f} vs target ratio",
            )

            st.divider()

            st.subheader("Difficulty at Adjustment Boundaries")
            fig1 = px.line(
                df,
                x="End Time",
                y="Difficulty",
                markers=True,
                template="plotly_white",
                height=420,
            )
            fig1.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="#FFFFFF",
                font=dict(color="#0F172A"),
                xaxis_title="Adjustment date",
                yaxis_title="Difficulty",
                margin=dict(l=20, r=20, t=20, b=20),
            )

            st.subheader("Adjustment Ratio vs Target")
            fig2 = px.bar(
                df,
                x="End Time",
                y="Actual/Target Ratio",
                hover_data=[
                    "Start Height",
                    "End Height",
                    "Actual Period Time (s)",
                    "Avg Block Time (s)",
                ],
                template="plotly_white",
                height=420,
            )
            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="#FFFFFF",
                font=dict(color="#0F172A"),
                xaxis_title="Adjustment date",
                yaxis_title="Ratio",
                margin=dict(l=20, r=20, t=20, b=20),
            )

            with st.expander("Show summary table"):
                table_df = df[
                    [
                        "Start Height",
                        "End Height",
                        "End Time",
                        "Difficulty",
                        "Actual Period Time (s)",
                        "Avg Block Time (s)",
                        "Actual/Target Ratio",
                    ]
                ].copy()

                table_df["Difficulty"] = table_df["Difficulty"].round(2)
                table_df["Avg Block Time (s)"] = table_df["Avg Block Time (s)"].round(2)
                table_df["Actual/Target Ratio"] = table_df["Actual/Target Ratio"].round(4)

                st.dataframe(table_df, use_container_width=True)

            st.divider()

            st.subheader("Interpretation")
            st.write(
                "Bitcoin adjusts difficulty every 2016 blocks to keep the average block time close to 600 seconds."
            )
            st.write(
                "If the ratio is below 1, blocks were mined faster than the target on average."
            )
            st.write(
                "If the ratio is above 1, blocks were mined more slowly than expected."
            )

        except Exception as exc:
            st.error(f"Error loading exact adjustment analysis: {exc}")