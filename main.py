import streamlit as st
from datetime import date, datetime
import time
import random

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Tech CSS (The Orien Aesthetic)
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    .main-title { 
        color: #ffffff !important; font-family: 'Share Tech Mono', monospace; 
        text-transform: uppercase; letter-spacing: 5px; font-size: 2.8rem; text-align: center; 
        text-shadow: 0px 0px 20px rgba(0, 212, 255, 1); 
    }
    .sub-title { 
        color: #00d4ff; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; 
        letter-spacing: 2px; font-size: 0.8rem; text-align: center; margin-top: -5px; margin-bottom: 30px; 
    }
    h3, .stSubheader p { color: #00d4ff !important; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; }
    [data-testid="stVerticalBlockBorderWrapper"] { 
        background-color: #0c1017 !important; border: 1px solid rgba(0, 212, 255, 0.3) !important; 
        padding: 15px !important; border-radius: 4px; 
    }
    input, textarea { color: #00d4ff !important; background-color: #000000 !important; border: 1px solid rgba(0, 212, 255, 0.2) !important; }
    .stButton button, .stDownloadButton button { 
        background-color: transparent !important; color: #00d4ff !important; border: 1px solid #00d4ff !important; 
        width: 100%; text-transform: uppercase; font-family: 'Share Tech Mono', monospace; 
    }
    .stProgress > div > div > div > div { background-color: #00d4ff; box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6); }
    .advisor-output { border-left: 3px solid #ff4b4b; background-color: rgba(255, 75, 75, 0.05); padding: 25px; margin-top: 10px; border-radius: 0 4px 4px 0; }
    .quote-box { font-style: italic; color: #00d4ff; border-top: 1px solid rgba(0, 212, 255, 0.2); padding-top: 15px; margin-top: 20px; font-size: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")

# --- HARD-WIRED LOGIC ENGINE ---
def get_strategic_advice(user_input):
    txt = user_input.lower()
    
    # Resource Crisis
    if any(w in txt for w in ["hungry", "starve", "no food", "broke", "no money", "zero"]):
        return {
            "protocol": "CRITICAL RESOURCE DEFICIT",
            "mental": "Panic is a biological tax you cannot afford. Shift from 'Victim' to 'Scavenger' mode.",
            "tactical": [
                "Locate local resource hubs (Pantries, Sikhs, or Community kitchens).",
                "Offer labor at a local business for immediate sustenance.",
                "Identify one non-essential asset to liquidate immediately for a 24-hour reserve."
            ],
            "quote": "'Wealth consists not in having great possessions, but in having few wants.' — Epictetus"
        }
    
    # Interpersonal Spite/Drama
    if any(w in txt for w in ["wife", "partner", "she", "petty", "offered"]):
        return {
            "protocol": "INTERPERSONAL FRAME BREACH",
            "mental": "Your state is independent of her behavior. If you complain, you give up control.",
            "tactical": [
                "Do not comment on the action. Acquire your own meal in total silence.",
                "Immediately engage in a high-value task (Work or Gym).",
                "Maintain a neutral tone. The lack of reaction is your greatest tool."
            ],
            "quote": "'The best revenge is to be unlike him (or her) who performed the injury.' — Marcus Aurelius"
        }
    
    # General Fallback
    return {
        "protocol": "GENERAL STRATEGIC ADAPTATION",
        "mental": "Detach and analyze. Is this a variable you control?",
        "tactical": ["Isolate the immediate next step.", "Remove emotion from the data.", "Execute."],
        "quote": "'The soul becomes dyed with the color of its thoughts.' — Marcus Aurelius"
    }

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_t", placeholder="Log action...")
        with st.container(border=True):
            m_c = st.checkbox("02 // MENTAL")
            m_t = st.text_input("Evidence:", key="m_t", placeholder="Log response...")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_t", placeholder="Log output...")
        with st.container(border=True):
            e_c = st.checkbox("04 // ENVIRONMENTAL")
            e_t = st.text_input("Evidence:", key="e_t", placeholder="Log env...")

    score = sum([1 for c, t in [(p_c, p_t), (m_c, m_t), (w_c, w_t), (e_c, e_t)] if c and t.strip()])
    st.progress(score/4)

    st.subheader("MOBILITY FUND")
    fund = st.number_input("RESERVE_CREDITS ($)", min_value=0)
    
    if st.button("EXECUTE SESSION UPLOAD"):
        st.success("SESSION LOGGED.")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    event = st.text_area("DESCRIBE THE EVENT:", height=150)

    if st.button("RUN ORIEN PROTOCOL"):
        if event:
            with st.status("Deconstructing variables..."):
                time.sleep(1)
            advice = get_strategic_advice(event)
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.write(f"### 🛡️ {advice['protocol']}")
            st.write(f"**🧠 MENTAL:** {advice['mental']}")
            st.write("**🛠️ TACTICAL ACTIONS:**")
            for a in advice['tactical']:
                st.write(f"• {a}")
            st.markdown(f'<div class="quote-box">{advice["quote"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Input required for analysis.")
