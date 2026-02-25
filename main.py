import streamlit as st
from datetime import date
import time

# 1. Page Config
st.set_page_config(page_title="Orien", page_icon="🧭", layout="centered")

# 2. Ultra-Clean Tech CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #05070a;
        color: #e0e0e0;
    }
    .main-title {
        color: #ffffff !important;
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #00d4ff;
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        text-align: center;
        margin-top: -5px;
        margin-bottom: 30px;
    }
    /* Sharp Boxes */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0c1017 !important;
        border: 1px solid #1f2937 !important;
        padding: 15px !important;
        border-radius: 4px !important;
    }
    input, textarea {
        color: #00d4ff !important;
        background-color: #000000 !important;
        border: 1px solid #30363d !important;
    }
    .stProgress > div > div > div > div {
        background-color: #00d4ff;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Branding
st.markdown('<p class="main-title">ORIEN</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">STAY UP KINGS // SYSTEM_ACTIVE</p>', unsafe_allow_html=True)

# 4. Domains
st.subheader("SYSTEM DOMAINS")
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        phys_check = st.checkbox("01 // PHYSICAL")
        phys_text = st.text_input("Evidence:", key="p_text", placeholder="Action log...", label_visibility="collapsed")
    
    with st.container(border=True):
        stoic_check = st.checkbox("02 // MENTAL")
        stoic_text = st.text_input("Evidence:", key="m_text", placeholder="Response log...", label_visibility="collapsed")

with col2:
    with st.container(border=True):
        work_check = st.checkbox("03 // PROFESSIONAL")
        work_text = st.text_input("Evidence:", key="w_text", placeholder="Output log...", label_visibility="collapsed")
    
    with st.container(border=True):
        env_check = st.checkbox("04 // ENVIRONMENTAL")
        env_text = st.text_input("Evidence:", key="e_text", placeholder="Env log...", label_visibility="collapsed")

score = sum([phys_check, stoic_check, work_check, env_check])
st.progress(score / 4 if score > 0 else 0.0)

# 5. MOBILITY FUND
st.divider()
st.subheader("MOBILITY FUND")
target = 1000
current_savings = st.number_input("RESERVE_CREDITS ($)", min_value=0, value=0, step=10)
fund_progress = min(current_savings / target, 1.0)
st.progress(fund_progress)
st.write(f"**STATUS:** {int(fund_progress*100)}% // **DELTA:** ${target - current_savings}")

# 6. USER LOG
st.divider()
st.subheader("USER_LOG // SESSION_DATA")
victory_entry = st.text_area("", placeholder="Consolidate session notes...", key="log_area", label_visibility="collapsed")

if st.button("EXECUTE SESSION U
