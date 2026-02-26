import streamlit as st
from datetime import date, datetime
import time
import random

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Luminous Tech CSS
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    .main-title { 
        color: #ffffff !important; 
        font-family: 'Share Tech Mono', monospace; 
        text-transform: uppercase; 
        letter-spacing: 5px; 
        font-size: 2.8rem; 
        text-align: center; 
        margin-bottom: 0px; 
        text-shadow: 0px 0px 20px rgba(0, 212, 255, 1), 0px 0px 10px rgba(0, 212, 255, 0.8); 
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
        text-shadow: 0px 0px 5px rgba(0, 212, 255, 0.4); 
    }
    h3, .stSubheader p { 
        color: #00d4ff !important; 
        font-family: 'Share Tech Mono', monospace; 
        text-transform: uppercase; 
        text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.6) !important; 
    }
    [data-testid="stVerticalBlockBorderWrapper"] { 
        background-color: #0c1017 !important; 
        border: 1px solid rgba(0, 212, 255, 0.3) !important; 
        padding: 15px !important; 
        border-radius: 4px !important; 
    }
    input, textarea { 
        color: #00d4ff !important; 
        background-color: #000000 !important; 
        border: 1px solid rgba(0, 212, 255, 0.2) !important; 
    }
    .stButton button, .stDownloadButton button { 
        background-color: transparent !important; 
        color: #00d4ff !important; 
        border: 1px solid #00d4ff !important; 
        width: 100%; 
        text-transform: uppercase; 
        font-family: 'Share Tech Mono', monospace; 
    }
    .stProgress > div > div > div > div { background-color: #00d4ff; }
    .advisor-output { 
        border-left: 3px solid #ff4b4b; 
        background-color: rgba(255, 75, 75, 0.05); 
        padding: 20px; 
        margin-top: 10px; 
    }
    .quote-box { font-style: italic; color: #999; border-top: 1px solid rgba(0, 212, 255, 0.2); padding-top: 15px; margin-top: 20px; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Master Control)
with st.sidebar:
    st.title("SYSTEM MENU")
    # Using a key here ensures the state is preserved
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"], key="nav_menu")
    st.divider()
    st.error("REACTION IS SUBMISSION.")

# --- DATA & LOGIC ---
quotes = {
    "resource": ["'Wealth consists not in having great possessions, but in having few wants.' — Epictetus"],
    "interpersonal": ["'The best revenge is to be unlike him who performed the injury.' — Marcus Aurelius"],
    "discipline": ["'Self-discipline is the bridge between goals and accomplishment.' — Jim Rohn"]
}

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
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

    # Progress Calculation
    p_v = 1 if (phys_check and phys_text.strip()) else 0
    m_v = 1 if (stoic_check and stoic_text.strip()) else 0
    w_v = 1 if (work_check and work_text.strip()) else 0
    e_v = 1 if (env_check and env_text.strip()) else 0
    st.progress(sum([p_v, m_v, w_v, e_v]) / 4)

    st.divider()
    current_savings = st.number_input("RESERVE_CREDITS ($)", min_value=0, value=0, step=1)
    victory_entry = st.text_area("CONSOLIDATE SESSION NOTES:", placeholder="Final report data...", key="log_area")

    if st.button("EXECUTE SESSION UPLOAD"):
        now_t, now_d = datetime.now().strftime("%H:%M:%S"), date.today().strftime("%Y-%m-%d")
        st.success(f"**SESSION LOGGED // {now_d} // {now_t}**")
        
        summary = f"THE ORIEN PROJECT - MISSION REPORT\nTIMESTAMP: {now_d} | {now_t}\n" + "="*30 + "\n"
        summary += f"• PHYSICAL: {phys_text if p_v else 'N/A'}\n• MENTAL: {stoic_text if m_v else 'N/A'}\n"
        summary += f"• PROFESSIONAL: {work_text if w_v else 'N/A'}\n• ENV: {env_text if e_v else 'N/A'}\n"
        summary += f"RESERVE: ${current_savings}\nNOTES: {victory_entry}"
        
        st.info("DATA PREPARED FOR TRANSMISSION.")
        st.download_button("📥 TRANSMIT LOG", data=summary, file_name=f"Orien_{now_d}.txt")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    problem_input = st.text_area("DESCRIBE THE EVENT:", placeholder="Input data for logic filtering...", height=150)

    if st.button("RUN ORIEN PROTOCOL"):
        if problem_input:
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            txt = problem_input.lower()

            if any(w in txt for w in ["money", "broke", "rent", "eat"]):
                cat, protocol = "resource", "RESOURCE CRISIS"
                tactical = ["Identify 'Zero-Cost' hubs.", "Trade labor for immediate needs.", "Inventory liquidation."]
            elif any(w in txt for w in ["wife", "she", "fight", "argument"]):
                cat, protocol = "interpersonal", "INTERPERSONAL FRICTION"
                tactical = ["Physical Exit (60 mins).", "Logistical communication only.", "Internal audit."]
            else:
                cat, protocol = "discipline", "UNCLASSIFIED CHALLENGE"
                tactical = ["Complete one Mission Control task.", "20-min Cortisol Flush.", "Execute professional objective."]

            st.write(f"### 🛡️ {protocol}")
            for action in tactical:
                st.write(f"• {action}")
            st.markdown(f'<div class="quote-box">{random.choice(quotes[cat])}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
