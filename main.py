import streamlit as st
from datetime import date

# 1. Page Config
st.set_page_config(page_title="Stay Up Kings", page_icon="🚀", layout="centered")

# 2. Space-Tech CSS
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #0d1b2a 0%, #010203 100%);
        color: #00d4ff;
    }
    h1, h2, h3 {
        color: #00d4ff !important;
        font-family: 'Share Tech Mono', monospace;
        text-shadow: 0px 0px 12px rgba(0, 212, 255, 0.8);
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    .stCheckbox {
        background-color: rgba(0, 212, 255, 0.07);
        padding: 20px;
        border-radius: 8px;
        border: 1px solid rgba(0, 212, 255, 0.3);
        margin-bottom: 10px;
    }
    .stTextArea textarea, .stNumberInput input {
        background-color: #010203 !important;
        color: #00d4ff !important;
        border: 1px solid #00d4ff !important;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00d4ff , #00b4d8);
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. HUD Header
st.title("🛰️ ORIEN // STAY UP KINGS")
st.write(f"**STARDATE:** {date.today()} // **STATUS:** UNSTOPPABLE")

# 4. The 4 Domains
st.divider()
st.header("CORE PROTOCOLS")
col1, col2 = st.columns(2)
with col1:
    phys = st.checkbox("01 // PHYSICAL")
    stoic = st.checkbox("02 // MENTAL")
with col2:
    work = st.checkbox("03 // PROFESSIONAL")
    env = st.checkbox("04 // ENVIRONMENTAL")

score = sum([phys, stoic, work, env])
st.progress(score / 4)

# 5. THE MONEY TRACKER
st.divider()
st.header("💰 FREEDOM FUND")
target = 1000
current_savings = st.number_input("Current Credits ($)", min_value=0, value=0, step=10)
fund_progress = min(current_savings / target, 1.0)
st.progress(fund_progress)
st.write(f"**RESERVES:** ${current_savings} / ${target}")

# 6. THE LOG
st.divider()
st.header("📡 THE CHRONICLE")
victory_entry = st.text_area("Daily Victory Log", placeholder="Record your win...", label_visibility="collapsed")
if st.button("UPLOAD DATA"):
    st.toast("Victory encrypted.")
    st.info(f"Logged: {victory_entry}")

# 7. Sidebar
with st.sidebar:
    st.title("DIRECTIVES")
    st.error("REACTION IS SUBMISSION.")
    st.info("Build in silence.")
