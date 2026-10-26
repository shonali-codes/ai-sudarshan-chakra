import html

import streamlit as st

from core.pipeline import run

from database import (
    init_db,
    log_event
)

from theme import DARK_THEME


# =========================================================
# HELPERS
# =========================================================


def safe_html(value):
    return html.escape(str(value), quote=True)


def kpi_card(title, value, color):
    safe_title = safe_html(title)
    safe_value = safe_html(value)
    safe_color = safe_html(color)

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(180deg, #0F1E36, #13263D);
            border: 1px solid {safe_color};
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            min-height: 120px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.35);
            font-family: 'Segoe UI', sans-serif;
        ">
            <div style="
                color: #9FB3C8;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 1px;
                font-weight: 700;
            ">{safe_title}</div>
            <div style="
                color: {safe_color};
                font-size: 40px;
                font-weight: 800;
                margin-top: 15px;
            ">{safe_value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def agent_panel(title, color, status, findings):
    safe_title = safe_html(title)
    safe_status = safe_html(status)
    safe_color = safe_html(color)

    findings_html = ""
    if findings:
        for item in findings:
            findings_html += f"<li>{safe_html(item)}</li>"
    else:
        findings_html = "<li>No findings detected</li>"

    st.markdown(
        f"""
        <div style="
            background:#13263D;
            border-left:6px solid {safe_color};
            border-radius:14px;
            padding:20px;
            min-height:220px;
            font-family: 'Segoe UI', sans-serif;
        ">
            <h3 style="margin-top:0; color:{safe_color};">{safe_title}</h3>
            <div style="color:white; font-weight:700; margin-bottom:15px;">{safe_status}</div>
            <ul style="color:#D6E4F0; padding-left: 1.2rem; margin:0;">{findings_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Sudarshan Chakra",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# INIT
# =========================================================

init_db()

st.markdown(
    DARK_THEME,
    unsafe_allow_html=True
)

# =========================================================
# SESSION STATE
# =========================================================

if "result" not in st.session_state:
    st.session_state.result = None

# =========================================================
# HEADER
# =========================================================

col1, col2 = st.columns([1.4, 4])

with col1:

    st.image(
        "assets/SudarshanChakraLogo.png",
        width=180
    )

with col2:

    st.markdown(
        """
# AI Sudarshan Chakra

### AI Agents Governing AI Agents
"""
    )

# =========================================================
# HERO BANNER
# =========================================================

st.markdown(
    """
<div class="chakra-hero">

<h3 style="margin:0;color:#FFB300;">
AI Immune System for Enterprise AI Governance
</h3>

<div style="
color:#D6E4F0;
font-size:18px;
margin-top:8px;
">
Enterprise AI Governance, Red Teaming &
Observability Platform
</div>

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# STATUS STRIP
# =========================================================

st.markdown(
    """
<div class="status-strip">

🟢 Governance Engine Online |
🛡 Observer Active |
⚡ Red Team Active |
⭐ Governance Controls Active

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# PROMPT INPUT
# =========================================================

prompt = st.text_area(
    "🔍 Enter Prompt for Governance Review",
    height=180,
    placeholder="Enter prompt here..."
)

# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button("🚀 Analyze Request"):

    if prompt.strip():

        st.session_state.result = run(prompt)

        log_event(
            prompt,
            st.session_state.result["risk"]["overall_risk"],
            st.session_state.result["decision"]
        )

# =========================================================
# RESULTS
# =========================================================

if st.session_state.result:

    result = st.session_state.result

    risk = result["risk"]["overall_risk"]

    decision = result["decision"]

    # =====================================================
    # THREAT BANNER
    # =====================================================

    banner_color = "#22C55E"
    banner_text = "LOW RISK"

    if risk >= 80:
        banner_color = "#FF4D4D"
        banner_text = "HIGH RISK"

    elif risk >= 60:
        banner_color = "#FFB300"
        banner_text = "ELEVATED RISK"

    elif risk >= 30:
        banner_color = "#FFA726"
        banner_text = "MEDIUM RISK"

    st.markdown(
        f"""
        <div style="
            background:#13263D;
            border-left:6px solid {safe_html(banner_color)};
            border-radius:14px;
            padding:20px;
            margin-top:20px;
            margin-bottom:20px;
            font-family: 'Segoe UI', sans-serif;
        ">
            <div style="color:{safe_html(banner_color)}; font-size:28px; font-weight:800;">
                THREAT LEVEL: {safe_html(banner_text)}
            </div>
            <div style="color:#D6E4F0; margin-top:6px;">
                Current Governance Risk Score: {safe_html(risk)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "AI Sudarshan Chakra Governance Engine: "
        "Observe → Challenge → Assess → Explain → Protect"
    )

    # =====================================================
    # GOVERNANCE OPERATIONS CENTER
    # =====================================================

    st.markdown(
        """
## Governance Operations Center

Real-Time Governance • Risk • Compliance
"""
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            "Risk Score",
            risk,
            "#FFB300"
        )

    with c2:
        kpi_card(
            "Sensitive Data",
            "YES" if result["observer"]["sensitive_request"] else "NO",
            "#FF4D4D" if result["observer"]["sensitive_request"] else "#22C55E"
        )

    with c3:
        kpi_card(
            "Prompt Injection",
            "YES" if result["redteam"]["prompt_injection"] else "NO",
            "#FF4D4D" if result["redteam"]["prompt_injection"] else "#22C55E"
        )

    with c4:
        kpi_card(
            "Decision",
            decision,
            "#FF4D4D" if decision == "BLOCK" else "#22C55E"
        )

    st.write("")

    # =====================================================
    # AGENT ANALYSIS
    # =====================================================

    st.markdown("## Agent Analysis")

    left, right = st.columns(2)

    with left:

        agent_panel(
            "🛡 Observer Agent",
            "#00C2FF",
            "Monitoring Sensitive Content",
            result["observer"]["findings"]
        )

    with right:

        agent_panel(
            "⚡ Red Team Agent",
            "#FF4D4D",
            "Threat Detection & Validation",
            result["redteam"]["findings"]
        )

    st.write("")

    # =====================================================
    # RISK ASSESSMENT
    # =====================================================

    st.markdown("## Risk & Compliance Assessment")

    r1, r2, r3 = st.columns(3)

    with r1:

        kpi_card(
            "Security Risk",
            result["risk"]["security_risk"],
            "#FF4D4D"
        )

    with r2:

        kpi_card(
            "Privacy Risk",
            result["risk"]["privacy_risk"],
            "#FFB300"
        )

    with r3:

        kpi_card(
            "Compliance Risk",
            result["risk"]["compliance_risk"],
            "#00D4B4"
        )

    st.progress(risk / 100)

    # =====================================================
    # GOVERNANCE HUB
    # =====================================================

    st.markdown("## Governance Decision Hub")

    if decision == "BLOCK":

        st.error("🔴 BLOCKED")

    elif decision == "ESCALATE":

        st.warning("🟠 ESCALATE TO HUMAN REVIEW")

    elif decision == "WARN":

        st.warning("🟡 WARNING")

    else:

        st.success("🟢 ALLOWED")

    # =====================================================
    # EXPLAINABILITY REPORT
    # =====================================================

    st.markdown("## Explainability Report")

    reasons = result["explanation"]["reasons"]

    if reasons:

        for reason in reasons:
            st.markdown(
                f"""
                <div style="
                    background:#13263D;
                    border-left:4px solid #00D4B4;
                    padding:15px;
                    border-radius:10px;
                    margin-bottom:10px;
                    color:#D6E4F0;
                    font-family: 'Segoe UI', sans-serif;
                ">
                    {safe_html(reason)}
                </div>
                """,
                unsafe_allow_html=True,
            )

    else:

        st.success(
            "No Governance Concerns Detected"
        )

    st.markdown(
        f"""
        <div style="
            background:#0F1E36;
            border:1px solid #234D76;
            border-radius:14px;
            padding:18px;
            margin-top:15px;
            font-family: 'Segoe UI', sans-serif;
        ">
            <strong style="color:#FFB300;">Final Governance Risk Score:</strong>
            <span style="color:white; font-size:24px; margin-left:12px;">{safe_html(result['explanation']['risk_score'])}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )