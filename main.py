import streamlit as st
from datetime import date
import time

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Enhanced Space-Tech CSS
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
    /* Fixing the Container alignment */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(0, 212, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        padding: 10px !important;
        border-radius: 8px !important;
    }
    /* Input field styling */
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

# 4. The 4 Domains (Nested in Styled Containers)
st.divider()
st.subheader("I. ACTIVE MISSION DOMAINS")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        phys_check = st.checkbox("01 // PHYSICAL")
        phys_text = st.text_input("Evidence:", key="p_text", placeholder="Action taken...", label_visibility="collapsed")
    
    with st.container(border=True):
        stoic_check = st.checkbox("02 // MENTAL")
        stoic_text = st.text_input("Evidence:", key="m_text", placeholder="Response taken...", label_visibility="collapsed")

with col2:
    with st.container(border=True):
        work_check = st.checkbox("03 // PROFESSIONAL")
        work_text = st.text_input("Evidence:", key="w_text", placeholder="Output produced...", label_visibility="collapsed")
    
    with st.container(border=True):
        env_check = st.checkbox("04 // ENVIRONMENTAL")
        env_text = st.text_input("Evidence:", key="e_text", placeholder="Space secured...", label_visibility="collapsed")

# Logic
score = sum([phys_check, stoic_check, work_check, env_check])
st.progress(score / 4 if score > 0 else 0.0)

# 5. THE MONEY TRACKER
st.divider()
st.subheader("II. MOBILITY FUND (RESERVES)")
target = 1000
current_savings = st.number_input("CREDITS ($)", min_value=0, value=0, step=10)
fund_progress = min(current_savings / target, 1.0)
st.progress(fund_progress)
st.write(f"**STATUS:** {int(fund_progress*100)}% // **CREDITS UNTIL MOBILITY:** ${target - current_savings}")

# 6. THE CHRONICLE
st.divider()
st.subheader("III. CAPTAIN'S LOG // MISSION SUMMARY")
victory_entry = st.text_area("", placeholder="Upload mission data for the Orien Archive...", key="log_area", label_visibility="collapsed")

if st.button("INITIALIZE TRANSMISSION"):
    with st.status("Transmitting..."):
        time.sleep(1)
        st.write("Verifying integrity...")
    st.success(f"**LOG SECURED // {date.today()}**")
    st.info(f"**DATA:** {victory_entry}")

# 7. Sidebar
with st.sidebar:
    st.title("DIRECTIVES")
    st.error("REACTION IS SUBMISSION.")
    st.info("The Orien Protocol: Find your heading. Move in silence.")
