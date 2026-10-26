import html
import sqlite3

import pandas as pd
import streamlit as st

from theme import DARK_THEME

st.markdown(
    DARK_THEME,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="page-shell">
        <div class="page-hero">
            <h3>Governance Dashboard</h3>
            <div class="subtext">Risk posture overview across all governance reviews</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
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


conn = sqlite3.connect(
    "events.db"
)

df = pd.read_sql_query(
    "SELECT * FROM governance_events",
    conn
)

conn.close()

total_reviews = len(df)
blocked_requests = int((df["decision"] == "BLOCK").sum()) if total_reviews else 0
average_risk = round(df["risk_score"].mean(), 2) if total_reviews else 0
threat_rate = round((blocked_requests / total_reviews) * 100, 2) if total_reviews else 0

c1, c2, c3, c4 = st.columns(4)

with c1:
    render_brand_card("Total Reviews", total_reviews, "#00C2FF")

with c2:
    render_brand_card("Blocked Requests", blocked_requests, "#FF4D4D")

with c3:
    render_brand_card("Average Risk", average_risk, "#FFB300")

with c4:
    render_brand_card("Threat Rate", f"{threat_rate}%", "#00D4B4")

if df.empty:
    st.info("No governance events yet.")
else:
    st.markdown("## Governance Events")

    st.bar_chart(
        df["decision"].value_counts()
    )