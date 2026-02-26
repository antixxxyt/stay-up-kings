import streamlit as st
from datetime import date, datetime
import time

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Tech CSS
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    .main-title { color: #ffffff !important; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; letter-spacing: 5px; font-size: 2.8rem; text-align: center; margin-bottom: 0px; text-shadow: 0px 0px 20px rgba(0, 212, 255, 1); }
    .sub-title { color: #00d4ff; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; text-align: center; margin-top: -5px; margin-bottom: 30px; text-shadow: 0px 0px 5px rgba(0, 212, 255, 0.4); }
    h3, .stSubheader p { color: #00d4ff !important; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.6) !important; }
    [data-testid="stVerticalBlockBorderWrapper"] { background-color: #0c1017 !important; border: 1px solid rgba(0, 212, 255, 0.3) !important; padding: 15px !important; border-radius: 4px !important; }
    input, textarea { color: #00d4ff !important; background-color: #000000 !important; border: 1px solid rgba(0, 212, 255, 0.2) !important; }
    .stButton button { background-color: transparent !important; color: #00d4ff !important; border: 1px solid #00d4ff !important; width: 100%; text-transform: uppercase; font-family: 'Share Tech Mono', monospace; }
    .advisor-output { border-left: 3px solid #ff4b4b; padding-left: 20px; background-color: rgba(255, 75, 75, 0.05); padding: 15px; margin-top: 10px; border-radius: 0 4px 4px 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")

# --- PAGE 1: MISSION CONTROL (Condensed for brevity) ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    # ... (Your Domains, Progress, and Fund code remains exactly as before)
    st.info("Awaiting mission data. Use the sidebar to switch to Tactical Advisory if needed.")

# --- PAGE 2: TACTICAL ADVISORY (The Infinite Guider) ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    st.subheader("📡 SITUATION ANALYSIS")
    problem_input = st.text_area("DESCRIBE THE EVENT IN DETAIL:", placeholder="What happened? What is your current emotional state?", height=150)

    if st.button("RUN ORIEN PROTOCOL"):
        if problem_input:
            with st.status("Analyzing variables..."):
                time.sleep(1.0)
                st.write("Filtering emotional noise...")
                time.sleep(1.0)
                st.write("Applying core directives...")

            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.write("**STRATEGIC READOUT // ACTION REQUIRED:**")
            
            # BROAD LOGIC FILTER
            txt = problem_input.lower()
            
            # Categorization Logic
            if any(word in txt for word in ["wife", "girlfriend", "partner", "she", "her", "friend", "pettiness"]):
                st.write("• **CATEGORY:** Interpersonal Friction")
                st.write("• **DIRECTIVE:** Frame Maintenance. Do not attempt to fix her mood; fix your focus.")
                st.write("• **TACTIC:** Total indifference is your greatest tool. Accomplish a task she doesn't expect.")
            
            elif any(word in txt for word in ["work", "boss", "money", "job", "career", "fired", "client"]):
                st.write("• **CATEGORY:** Professional/Financial Risk")
                st.write("• **DIRECTIVE:** Anti-Fragility. Use the pressure to increase output.")
                st.write("• **TACTIC:** Identify the single most productive action available right now. Execute it.")
            
            elif any(word in txt for word in ["tired", "lazy", "sad", "unmotivated", "depressed", "gave up"]):
                st.write("• **CATEGORY:** Internal Resistance")
                st.write("• **DIRECTIVE:** Discipline over Motivation. The body leads the mind.")
                st.write("• **TACTIC:** 20 minutes of high-intensity physical movement. Clear the cortisol.")
                
            else:
                st.write("• **CATEGORY:** Unclassified External Chaos")
                st.write("• **DIRECTIVE:** Detachment. Is this a Variable of Control? If no, it is irrelevant.")
                st.write("• **TACTIC:** Return to the Mission Control page. Log a win. Re-establish momentum.")
                
            st.write("\n*Remember: You do not control the event. You only control the response.*")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Input required for protocol analysis.")
