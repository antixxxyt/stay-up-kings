import streamlit as st
from datetime import date
import time

# 1. Page Config
st.set_page_config(page_title="Orien", page_icon="🧭", layout="centered")

# 2. Refined Tech CSS
st.markdown("""
    <style>
    /* Deep Space Background */
    .stApp {
        background: radial-gradient(circle, #0a1128 0%, #000000 100%);
        color: #e0e0e0;
    }
    
    /* Subtle Outer Glow for Headers */
    .main-title {
        color: #ffffff !important;
        font-family: 'Share Tech Mono', monospace;
        text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.4);
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .sub-title {
        color: #00d4ff;
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.85rem;
        text-align: center;
        margin-top: -5px;
        margin-bottom: 30px;
        opacity: 0.8;
    }

    /* Styled Containers for Domains */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(0, 212, 255, 0.03) !important;
        border: 1px solid rgba(0, 212, 255, 0.15) !important;
        padding: 12px !important;
        border-radius: 6px !important;
        box-shadow: 0px 0px 10px rgba(0, 212, 255, 0.05);
    }

    /* Input Fields */
    input, textarea {
        color: #00d4ff !important;
        background-color: rgba(0, 0, 0, 0.4) !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
    }

    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00d4ff , #0077b6);
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Branding Header
st.markdown('<p class="main-title">ORIEN</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">STAY UP KINGS // SYSTEM_ACTIVE</p>', unsafe_allow_html=True)

# 4. The 4 Domains
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

# Domain Progress Logic
score = sum([phys_check, stoic_check, work_check, env_check])
st.progress(score / 4 if score > 0 else 0.0)

# 5. THE MONEY TRACKER
st.divider()
st
