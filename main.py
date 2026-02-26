import streamlit as st
from datetime import datetime
import time

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# Initialize Session Log if it doesn't exist
if 'user_logs' not in st.session_state:
    st.session_state.user_logs = []

# 2. ORIEN LUMINOUS STYLING
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
    .stButton button { 
        background-color: transparent !important; color: #00d4ff !important; border: 1px solid #00d4ff !important; 
        width: 100%; text-transform: uppercase; font-family: 'Share Tech Mono', monospace; 
    }
    .stProgress > div > div > div > div { background-color: #00d4ff; box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6); }
    .advisor-output { border-left: 3px solid #ff4b4b; background-color: rgba(255, 75, 75, 0.05); padding: 25px; margin-top: 10px; border-radius: 0 4px 4px 0; line-height: 1.6; }
    .quote-box { font-style: italic; color: #00d4ff; border-top: 1px solid rgba(0, 212, 255, 0.1); padding-top: 15px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HARD-WIRED TACTICAL LOGIC ---
def get_hardwired_advice(user_input):
    txt = user_input.lower()
    if any(w in txt for w in ["money", "broke", "job", "bills", "rent", "hungry"]):
        return {"title": "RESOURCE DEFICIT PROTOCOL", "mental": "Panic is a luxury you cannot afford.", "tactical": ["Audit all liquid dollars.", "Liquidate non-essential assets.", "Execute high-value tasks."], "quote": "'Wealth consists in having few wants.' — Epictetus"}
    elif any(w in txt for w in ["wife", "girlfriend", "fight", "argument", "she"]):
        return {"title": "INTERPERSONAL FRAME MAINTENANCE", "mental": "The objective is peace, not victory.", "tactical": ["Maintain silence.", "Detach from emotion.", "Execute your routine."], "quote": "'The best revenge is to be unlike him who performed the injury.' — Marcus Aurelius"}
    elif any(w in txt for w in ["lazy", "tired", "motivation"]):
        return {"title": "NEURAL RESISTANCE OVERRIDE", "mental": "Feelings are irrelevant to the mission.", "tactical": ["Commit to 5 minutes.", "Kill distractions.", "Physical shock (Cold water)."], "quote": "'What stands in the way becomes the way.' — Marcus Aurelius"}
    return {"title": "GENERAL STRATEGIC ADAPTATION", "mental": "Control the variables. Own the outcome.", "tactical": ["Isolate the next step.", "Focus exclusively.", "Execute."], "quote": "'The soul is dyed with the color of its thoughts.' — Marcus Aurelius"}

# 3. SIDEBAR
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY", "03 SYSTEM LOGS"])
    st.divider()
    st.error("REACTION IS SUBMISSION.")

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    st.subheader("SYSTEM DOMAINS")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_t", placeholder="Gym, Diet, Sleep...")
        with st.container(border=True):
            m_c = st.checkbox("02 // MENTAL")
            m_t = st.text_input("Evidence:", key="m_t", placeholder="Reading, Meditating...")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_t", placeholder="Deep Work, Projects...")
        with st.container(border=True):
            e_c = st.checkbox("04 // ENVIRONMENTAL")
            e_t = st.text_input("Evidence:", key="e_t", placeholder="Cleaning, Organizing...")

    # Progress Calculation
    score = sum([1 for c, t in [(p_c, p_t), (m_c, m_t), (w_c, w_t), (e_c, e_t)] if c and t.strip()])
    st.progress(score/4)

    st.divider()
    st.subheader("MOBILITY FUND")
    fund = st.number_input("RESERVE_CREDITS ($)", min_value=0, step=1)

    if st.button("EXECUTE SESSION UPLOAD"):
        # This logs the data into the Session State
        log_entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "physical": p_t if p_c else "N/A",
            "mental": m_t if m_c else "N/A",
            "work": w_t if w_c else "N/A",
            "env": e_t if e_c else "N/A",
            "credits": fund
        }
        st.session_state.user_logs.append(log_entry)
        st.success("SESSION EXECUTED. DATA ANCHORED.")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    event = st.text_area("DESCRIBE THE EVENT:", height=150, placeholder="Identify the friction point...")

    if st.button("RUN ORIEN PROTOCOL"):
        if event:
            advice = get_hardwired_advice(event)
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.write(f"### 🛡️ {advice['title']}")
            st.write(f"**🧠 MENTAL:** {advice['mental']}")
            st.write("**🛠️ TACTICAL ACTIONS:**")
            for action in advice['tactical']:
                st.write(f"• {action}")
            st.markdown(f'<div class="quote-box">{advice["quote"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: SYSTEM LOGS ---
elif page == "03 SYSTEM LOGS":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // SYSTEM_LOGS</p>', unsafe_allow_html=True)
    
    if not st.session_state.user_logs:
        st.info("No data logs found. Execute a session in Mission Control to start tracking.")
    else:
        for log in reversed(st.session_state.user_logs):
            with st.container(border=True):
                st.write(f"📅 **DATE:** {log['time']}")
                st.write(f"💪 {log['physical']} | 🧠 {log['mental']} | 💼 {log['work']} | 🏠 {log['env']}")
                st.write(f"💰 **CREDITS:** ${log['credits']}")
