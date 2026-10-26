DARK_THEME = """
<style>

/* ==================================================
   STREAMLIT CLEANUP
================================================== */

header {
    visibility: hidden;
}

[data-testid="stHeader"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ==================================================
   BRAND COLORS
==================================================

Background        #07111F
Surface           #0F1E36
Panel             #13263D

Azure Blue        #00C2FF
Blue              #0078D4
Gold              #FFB300
Green             #22C55E
Red               #FF4D4D

Soft Text         #D6E4F0
Muted Text        #9FB3C8

================================================== */

/* ==================================================
   APP
================================================== */

.stApp {
    background:
        radial-gradient(circle at top left, rgba(0, 194, 255, 0.12), transparent 25%),
        radial-gradient(circle at bottom right, rgba(255, 179, 0, 0.08), transparent 30%),
        #07111F;
}

/* Main layout */

.main .block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* ==================================================
   SIDEBAR
================================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #091326 0%, #0F1E36 100%);
    border-right: 1px solid #1E3A5F;
    box-shadow: 4px 0 24px rgba(0, 194, 255, 0.08);
}

section[data-testid="stSidebar"] * {
    color: #D6E4F0 !important;
}

section[data-testid="stSidebar"] .css-1d391kg,
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
    background: transparent;
}

section[data-testid="stSidebar"] a {
    border-radius: 10px;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] a:hover {
    background: rgba(0, 194, 255, 0.12);
    box-shadow: inset 0 0 0 1px rgba(0, 194, 255, 0.18);
}

section[data-testid="stSidebar"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(0, 194, 255, 0.18), rgba(255, 179, 0, 0.12));
    border: 1px solid rgba(0, 194, 255, 0.35);
    box-shadow: 0 0 18px rgba(0, 194, 255, 0.12);
}

/* ==================================================
   HEADINGS
================================================== */

h1 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

h2 {
    color: #FFB300 !important;
    font-weight: 700 !important;
}

h3 {
    color: #00C2FF !important;
    font-weight: 600 !important;
}

/* ==================================================
   GENERAL TEXT
================================================== */

p,
span,
label {
    color: #D6E4F0 !important;
}

/* ==================================================
   HERO PANEL
================================================== */

.chakra-hero {

    background: linear-gradient(
        135deg,
        #0F1E36,
        #152A46
    );

    border: 1px solid #234D76;

    border-radius: 16px;

    padding: 20px;

    margin-bottom: 20px;
}

/* ==================================================
   STATUS STRIP
================================================== */

.status-strip {

    background: linear-gradient(
        90deg,
        #0F1E36,
        #13263D
    );

    border-left: 5px solid #FFB300;
    box-shadow: 0 0 18px rgba(255, 179, 0, 0.12);

    border-radius: 12px;

    padding: 14px 24px;

    margin-bottom: 20px;

    color: white;

    font-size: 16px;

    font-weight: 600;
}

/* ==================================================
   METRIC CARDS
================================================== */

div[data-testid="metric-container"] {

    background: linear-gradient(
        180deg,
        #0F1E36,
        #13263D
    );

    border: 1px solid #234D76;

    border-radius: 16px;

    padding: 16px;

    box-shadow:
        0 6px 18px rgba(0,0,0,0.35);
}

/* metric labels */

div[data-testid="metric-container"] label {

    color: #FFB300 !important;

    font-weight: 700 !important;

    text-transform: uppercase;

    letter-spacing: 0.5px;
}

/* metric values */

div[data-testid="metric-container"]
[data-testid="stMetricValue"] {

    color: #FFFFFF !important;

    font-size: 2.4rem !important;

    font-weight: 800 !important;
}

/* ==================================================
   TEXT AREA
================================================== */

textarea {

    background-color: #0F1E36 !important;

    color: #FFFFFF !important;

    border-radius: 14px !important;

    border: 2px solid #0078D4 !important;

    box-shadow:
        0 0 12px rgba(0,120,212,0.15);
}

/* ==================================================
   BUTTONS
================================================== */

.stButton > button {

    background: linear-gradient(
        90deg,
        #0078D4,
        #00C2FF
    );

    color: white !important;

    border: none;

    font-weight: 700;

    border-radius: 12px;

    padding: 0.8rem 2rem;
}

.stButton > button:hover {

    background: linear-gradient(
        90deg,
        #0061AD,
        #009FD7
    );
}

/* ==================================================
   ALERTS
================================================== */

div.stAlert {

    border-radius: 14px;
}

/* success */

.stSuccess {

    border-left: 4px solid #22C55E;
}

/* warning */

.stWarning {

    border-left: 4px solid #FFB300;
}

/* error */

.stError {

    border-left: 4px solid #FF4D4D;
}

/* ==================================================
   PAGE SHELLS
================================================== */

.page-shell {
    background: linear-gradient(135deg, rgba(15,30,54,0.95), rgba(19,38,61,0.95));
    border: 1px solid #234D76;
    border-radius: 18px;
    padding: 22px 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25), 0 0 18px rgba(0, 194, 255, 0.08);
}

.page-hero {
    background: linear-gradient(135deg, #0F1E36, #152A46);
    border: 1px solid #234D76;
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 18px;
    box-shadow: inset 0 0 0 1px rgba(0, 194, 255, 0.08);
}

.page-hero h3 {
    margin: 0;
    color: #FFB300 !important;
    font-size: 2.1rem !important;
    font-weight: 800 !important;
}

.page-hero .subtext {
    color: #D6E4F0;
    font-size: 18px;
    margin-top: 8px;
}

.page-card {
    background: linear-gradient(180deg, #0F1E36, #13263D);
    border: 1px solid #234D76;
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
    margin-bottom: 18px;
}

.brand-card {
    background: linear-gradient(160deg, #0F1E36, #13263D);
    border: 1px solid rgba(0, 194, 255, 0.4);
    border-left: 5px solid var(--card-accent, #00C2FF);
    border-radius: 16px;
    min-height: 112px;
    padding: 18px 20px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4), 0 0 18px rgba(0,194,255,0.16);
    font-family: 'Segoe UI', sans-serif;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.brand-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 9px 22px rgba(0,0,0,0.4), 0 0 20px rgba(0,194,255,0.14);
}

.brand-card-label {
    color: #D6E4F0;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    text-shadow: 0 1px 3px rgba(0,0,0,0.6);
}

.brand-card-value {
    color: #FFFFFF;
    font-size: 2.15rem;
    font-weight: 800;
    line-height: 1.2;
    margin-top: 12px;
    overflow-wrap: anywhere;
    text-shadow: 0 0 12px var(--card-accent, #00C2FF);
}

/* ==================================================
   METRICS / DATA TABLES
================================================== */

div[data-testid="metric-container"] {
    background: linear-gradient(180deg, #0F1E36, #13263D);
    border: 1px solid #234D76;
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}

div[data-testid="metric-container"] label {
    color: #FFB300 !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 2.4rem !important;
    font-weight: 800 !important;
}

[data-testid="stDataFrame"] {
    border-radius: 14px;
    border: 1px solid #234D76;
    overflow: hidden;
    background: rgba(15,30,54,0.8);
}

[data-testid="stDataFrame"] > div {
    background: rgba(15,30,54,0.8);
}

[data-testid="stDataFrame"] table thead th {
    background: #0F1E36 !important;
    color: #FFB300 !important;
    font-weight: 700 !important;
    border-bottom: 1px solid #234D76 !important;
}

[data-testid="stDataFrame"] table tbody td {
    background: rgba(19,38,61,0.85) !important;
    color: #D6E4F0 !important;
    border-bottom: 1px solid rgba(35,77,118,0.5) !important;
}

[data-testid="stDataFrame"] table tbody tr:hover td {
    background: rgba(0,194,255,0.08) !important;
}

div[data-testid="stPlotlyChart"] {
    border-radius: 14px;
    border: 1px solid #234D76;
    overflow: hidden;
}

/* ==================================================
   DIVIDER
================================================== */

hr {

    border-color: #234D76 !important;

    margin-top: 0.8rem !important;

    margin-bottom: 0.8rem !important;
}

</style>
"""