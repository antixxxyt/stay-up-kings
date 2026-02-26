import streamlit as st
from datetime import datetime
import time

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. ORIEN LUMINOUS STYLING (The Aesthetic is back)
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
    
    # Financial/Resource Crisis
    if any(w in txt for w in ["money", "broke", "job", "bills", "rent", "hungry"]):
        return {
            "title": "RESOURCE DEFICIT PROTOCOL",
            "mental": "Panic is a luxury you cannot afford. Emotional thinking leads to poor math.",
            "tactical": [
                "Audit all accounts and list every liquid dollar.",
                "Identify one high-value skill you can trade for immediate cash.",
                "Cut non-survival overhead to zero until reserves are restored."
            ],
            "quote": "'Wealth consists not in having great possessions, but in having few wants.' — Epictetus"
        }
    
    # Conflict/Relationship Friction
    elif any(w in txt for w in ["wife", "girlfriend", "fight", "argument", "she", "he", "they"]):
        return {
            "title": "INTERPERSONAL FRAME MAINTENANCE",
            "mental": "The objective is peace, not victory. Do not be the source of chaos.",
            "tactical": [
                "Go silent. Listen more than you speak for the next 60 minutes.",
                "Remove your ego from the equation; assess the actual grievance.",
                "Maintain your routine regardless of the emotional climate."
            ],
            "quote": "'The best revenge is to be unlike him who performed the injury.' — Marcus Aurelius"
        }
    
    # Discipline/Lazy/Resistance
    elif any(w in txt for w in ["lazy", "procrastinate", "tired", "motivation", "don't want to"]):
        return {
            "title": "NEURAL RESISTANCE OVERRIDE",
            "mental": "Motivation is a feeling. Discipline is a command. Feelings are irrelevant to the mission.",
            "tactical": [
                "Commit to the first 5 minutes of the task immediately.",
                "Remove your phone from your physical environment.",
                "Execute one 'hard' physical act (pushups/cold water) to break the mental stall."
            ],
            "quote": "'At dawn, when you have trouble getting out of bed, tell yourself: I have to go to work—as a human being.' — Marcus Aurelius"
        }

    # Default Strategy
    return {
        "title": "GENERAL STRATEGIC ADAPTATION",
        "mental": "Isolate the variables you control. Ignore the ones you don't.",
        "tactical": [
            "Write down the single most important next step.",
            "Remove distractions and focus exclusively on that step.",
            "Evaluate the outcome and pivot if necessary."
        ],
        "quote": "'The impediment to action advances action. What stands in the way becomes the way.' — Marcus Aurelius"
    }

# 3. SIDEBAR
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    st.subheader("SYSTEM DOMAINS")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_t", placeholder="Logged action (e.g., 5am Gym)...")
        with st.container(border=True):
            m_c = st.checkbox("02 // MENTAL")
            m_t = st.text_input("Evidence:", key="m_t", placeholder="Logged response (e.g., Cold shower)...")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_t", placeholder="Logged output (e.g., Deep Work)...")
        with st.container(border=True):
            e_c = st.checkbox("04 // ENVIRONMENTAL")
            e_t = st.text_input("Evidence:", key="e_t", placeholder="Logged env (e.g., Cleaned Desk)...")

    score = sum([1 for c, t in [(p_c, p_t), (m_c, m_t), (w_c, w_t), (e_c, e_t)] if c and t.strip()])
    st.progress(score/4)

    st.divider()
    st.subheader("MOBILITY FUND")
    fund = st.number_input("RESERVE_CREDITS ($)", min_value=0, step=1)

    if st.button("EXECUTE SESSION UPLOAD"):
        st.success(f"SESSION LOGGED // {datetime.now().strftime('%H:%M:%S')}")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    event = st.text_area("DESCRIBE THE EVENT:", height=150, placeholder="Identify the friction point...")

    if st.button("RUN ORIEN PROTOCOL"):
        if event:
            with st.spinner("Deconstructing variables..."):
                time.sleep(1) # Simulation of thought
                advice = get_hardwired_advice(event)
            
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.write(f"### 🛡️ {advice['title']}")
            st.write(f"**🧠 MENTAL:** {advice['mental']}")
            st.write("**🛠️ TACTICAL ACTIONS:**")
            for action in advice['tactical']:
                st.write(f"• {action}")
            st.markdown(f'<div class="quote-box">{advice["quote"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Please provide data for analysis.")
