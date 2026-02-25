import streamlit as st
from datetime import date

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Space-Tech CSS (Refined Neon)
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #0a1128 0%, #000000 100%);
        color: #00d4ff;
    }
    .main-title {
        color: #ffffff !important;
        font-family: 'Share Tech Mono', monospace;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.9);
        text-transform: uppercase;
        letter-spacing: 6px;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #00d4ff;
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 0.9rem;
        text-align: center;
        margin-top: -5px;
        margin-bottom: 30px;
    }
    .stCheckbox {
        background-color: rgba(0, 212, 255, 0.05);
        padding: 15px;
        border-radius: 5px;
        border: 1px solid rgba(0, 212, 255, 0.2);
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00d4ff , #0077b6);
        box-shadow: 0px 0px 8px #00d4ff;
    }
    /* Input field text color fix */
    input, textarea {
        color: #00d4ff !important;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Branding Header
st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">STAY UP KINGS // FIND YOUR HEADING</p>', unsafe_allow_html=True)

st.write(f"**LOG DATE:** {date.today()} // **AUTH:** SECURE")

# 4. The 4 Domains
st.divider()
st.subheader("I. DAILY OPERATIONAL DOMAINS")
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
st.subheader("II. MOBILITY FUND (RESERVES)")
target = 1000
current_savings = st.number_input("CREDITS ($)", min_value=0, value=0, step=10)
fund_progress = min(current_savings / target, 1.0)
st.progress(fund_progress)
st.write(f"**STATUS:** {int(fund_progress*100)}% TOWARD MOBILITY")

# 6. THE CHRONICLE
st.divider()
st.subheader("III. THE CHRONICLE")
victory_entry = st.text_area("", placeholder="Upload mission data...", label_visibility="collapsed")
if st.button("EXECUTE UPLOAD"):
