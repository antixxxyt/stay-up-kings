import streamlit as st
from datetime import date

# 1. Page Config
st.set_page_config(page_title="Stay Up Kings", page_icon="🚀", layout="centered")

# 2. Space-Tech CSS
st.markdown("""
    <style>
    /* Deep Space Background */
    .stApp {
        background: radial-gradient(circle, #1b2735 0%, #090a0f 100%);
        color: #00d4ff;
    }
    /* Neon Blue Tech Headers */
    h1, h2, h3 {
        color: #00d4ff !important;
        font-family: 'Share Tech Mono', monospace;
        text-shadow: 0px 0px 10px rgba(0, 212, 255, 0.7);
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    /* Tech-Card Checkboxes */
    .stCheckbox {
        background-color: rgba(0, 212, 255, 0.05);
        padding: 20px;
        border-radius: 5px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        transition: 0.3s;
    }
    .stCheckbox:hover {
        border: 1px solid #00d4ff;
        background-color: rgba(0, 212, 255, 0.1);
    }
    /* Cyberpunk Progress Bar */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00d4ff , #005f73);
    }
    /* Input Fields */
    .stTextArea textarea, .stNumberInput input {
        background-color: #090a0f !important;
        color: #00d4ff !important;
        border: 1px solid #00d4ff !important;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. HUD Header
st.title("🛰️ ORIEN // STAY UP")
st.write(f"**SYSTEM STATUS:** ONLINE // **STARDATE:** {date.today()}")

# 4. The 4 Domains (The Protocol)
st.divider()
st.subheader("Mission Parameters")

col1, col2 = st.columns(2)

with col1:
    phys = st.checkbox("DATA_01 // PHYSICAL")
    stoic = st.checkbox("DATA_02 // MENTAL")

with col2:
    work = st.checkbox("DATA_03 // PROFESSIONAL")
