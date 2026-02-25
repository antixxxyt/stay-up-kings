import streamlit as st
from datetime import date
import time

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Space-Tech CSS
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
    .domain-container {
        background-color: rgba(0, 212, 255, 0.05);
        padding: 15px;
        border-radius: 8px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        margin-bottom: 15px;
    }
    input, textarea {
        color: #00d4ff !important;
        background-color: #000000 !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00d4ff , #0077b6);
        box-shadow: 0px 0px 8px #00d4ff;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Branding Header
st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">STAY UP KINGS // MISSION ACCOUNTABILITY</p>', unsafe_allow_html=True)

# 4. The 4 Domains
st.divider()
st.subheader("I. ACTIVE MISSION DOMAINS")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="domain-container">', unsafe_allow_html=True)
    phys_check = st.checkbox("01 // PHYSICAL")
    phys_text = st.text_input("Evidence:", key="p_text", placeholder="Activity details...")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="domain-container">', unsafe_allow_html=True)
    stoic_check = st.checkbox("02 // MENTAL")
    stoic_text = st.text_input("Evidence:", key="m_text", placeholder="Response details...")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="domain-container">', unsafe_allow_html=True)
    work_check = st.checkbox("03 // PROFESSIONAL")
    work_text = st.text_input("Evidence:", key="w_text", placeholder="Progress details...")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="domain-container">', unsafe_allow_html=True)
    env_check = st.checkbox("04 // ENVIRONMENTAL")
    env_text = st.text_input("Evidence:", key="e_text", placeholder="Space details...")
    st.markdown('</div>', unsafe_allow_html=True)

score = sum([phys_check, stoic_check, work_check, env_check])
st.progress(score / 4 if score > 0 else 0.0)

# 5. THE MONEY TRACKER
st.divider()
st.subheader("II. MOBILITY FUND (RESERVES)")
target = 1000
current_savings = st.number_input("CREDITS ($)", min_value=0, value=0, step=10)
fund_progress = min(current_savings / target, 1.0)
st.progress(fund_progress)
st.write(f"**RESERVE STATUS:** {int(fund_progress*100)}% TOWARD MOBILITY")

# 6. THE CHRONICLE
st.divider()
st.subheader("III. CAPTAIN'S LOG // MISSION SUMMARY")
victory_entry = st.text_area("", placeholder="Consolidate mission notes...", key="log_area", label_visibility="collapsed")

if st.button("INITIALIZE TRANSMISSION"):
    with st.status("Transmitting to Orien Archive..."):
        time.sleep(1)
        st.write("Verifying integrity...")
    st.success(f"**MISSION LOG SECURED:** {date.today()}")
    st.info(f"**DAILY TRANSMISSION:** {victory_entry}")

# 7. Sidebar
with st.sidebar:
    st.title("DIRECTIVES")
    st.error("REACTION IS SUBMISSION.")
    st.info("The Orien Protocol: Find your heading. Move in silence.")
