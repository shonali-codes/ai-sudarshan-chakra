import html

import pandas as pd
import streamlit as st

from db.database import get_events
from theme import DARK_THEME

st.markdown(
    DARK_THEME,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="page-shell">
        <div class="page-hero">
            <h3>Governance History</h3>
            <div class="subtext">Review events, decisions and risk signals over time</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

events = get_events()

df = pd.DataFrame(
    events,
    columns=[
        "ID",
        "Timestamp",
        "Prompt",
        "Risk Score",
        "Decision"
    ]
)

def render_brand_card(label, value, accent):
    st.markdown(
        f"""
        <div class="brand-card" style="--card-accent:{accent};">
            <div class="brand-card-label">{html.escape(str(label))}</div>
            <div class="brand-card-value">{html.escape(str(value))}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


total_events = len(df)
blocked_events = int((df["Decision"] == "BLOCK").sum()) if total_events else 0
average_risk = round(df["Risk Score"].mean(), 2) if total_events else 0
latest_decision = df.iloc[0]["Decision"] if total_events else "—"

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_brand_card("Total Reviews", total_events, "#00C2FF")

with c2:
    render_brand_card("Blocked Requests", blocked_events, "#FF4D4D")

with c3:
    render_brand_card("Average Risk", average_risk, "#FFB300")

with c4:
    latest_accent = "#FF4D4D" if latest_decision == "BLOCK" else "#22C55E"
    render_brand_card("Latest Decision", latest_decision, latest_accent)

st.markdown("## Governance Event Log")

if df.empty:
    st.info("No governance events yet.")
else:
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )