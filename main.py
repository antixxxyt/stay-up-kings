import streamlit as st
from datetime import date, datetime
import time
import random

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Luminous Tech CSS (Fully Restored)
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    .main-title { 
        color: #ffffff !important; font-family: 'Share Tech Mono', monospace; 
        text-transform: uppercase; letter-spacing: 5px; font-size: 2.8rem; text-align: center; 
        margin-bottom: 0px; text-shadow: 0px 0px 20px rgba(0, 212, 255, 1), 0px 0px 10px rgba(0, 212, 255, 0.8); 
    }
    .sub-title { 
        color: #00d4ff; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; 
        letter-spacing: 2px; font-size: 0.8rem; text-align: center; margin-top: -5px; margin-bottom: 30px; 
    }
    h3, .stSubheader p { 
        color: #00d4ff !important; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; 
    }
    [data-testid="stVerticalBlockBorderWrapper"] { 
        background-color: #0c1017 !important; border: 1px solid rgba(0, 212, 255, 0.3) !important; 
        padding: 15px !important; border-radius: 4px !important; 
    }
    input, textarea { 
        color: #00d4ff !important; background-color: #000000 !important; border: 1px solid rgba(0, 212, 255, 0.2) !important; 
    }
    .stButton button, .stDownloadButton button { 
        background-color: transparent !important; color: #00d4ff !important; border: 1px solid #00d4ff !important; 
        width: 100%; text-transform: uppercase; font-family: 'Share Tech Mono', monospace; 
    }
    .stProgress > div > div > div > div { background-color: #00d4ff; box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6); }
    .advisor-output { 
        border-left: 3px solid #ff4b4b; background-color: rgba(255, 75, 75, 0.05); 
        padding: 25px; margin-top: 10px; border-radius: 0 4px 4px 0; line-height: 1.6;
    }
    .quote-box { font-style: italic; color: #999; border-top: 1px solid rgba(0, 212, 255, 0.2); padding-top: 15px; margin-top: 20px; }
    .status-box { border: 1px solid #00d4ff; padding: 20px; text-align: center; border-radius: 4px; background-color: rgba(0, 212, 255, 0.05); margin-top: 20px; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Stable Choice)
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"], key="nav_menu")
    st.divider()
    st.error("REACTION IS SUBMISSION.")

# --- QUOTE DATABASE ---
quotes = {
    "resource": ["'Wealth consists not in having great possessions, but in having few wants.' — Epictetus", "'Scarcity of resources is the mother of invention.' — Unknown"],
    "interpersonal": ["'The best revenge is to be unlike him who performed the injury.' — Marcus Aurelius", "'He who angers you, conquers you.' — Elizabeth Kenny"],
    "discipline": ["'Self-discipline is the bridge between goals and accomplishment.' — Jim Rohn", "'What stands in the way becomes the way.' — Marcus Aurelius"]
}

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    st.subheader("SYSTEM DOMAINS")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_text", placeholder="Action log...", label_visibility="collapsed")
        with st.container(border=True):
            m_c = st.checkbox("02 // MENTAL")
            m_t = st.text_input("Evidence:", key="m_text", placeholder="Response log...", label_visibility="collapsed")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_text", placeholder="Output log...", label_visibility="collapsed")
        with st.container(border=True):
            e_c = st.checkbox("04 // ENVIRONMENTAL")
            e_t = st.text_input("Evidence:", key="e_text", placeholder="Env log...", label_visibility="collapsed")

    # Progress Calculation
    p_v = 1 if (p_c and p_t.strip()) else 0
    m_v = 1 if (m_c and m_t.strip()) else 0
    w_v = 1 if (w_c and w_t.strip()) else 0
    e_v = 1 if (e_c and e_t.strip()) else 0
    st.progress(sum([p_v, m_v, w_v, e_v]) / 4)

    st.divider()
    current_savings = st.number_input("RESERVE_CREDITS ($)", min_value=0, value=0, step=1)
    victory_entry = st.text_area("USER_LOG // SESSION_DATA", placeholder="Consolidate session notes...", key="log_area")

    if st.button("EXECUTE SESSION UPLOAD"):
        now_t, now_d = datetime.now().strftime("%H:%M:%S"), date.today().strftime("%Y-%m-%d")
        with st.status("Syncing to Archive..."):
            time.sleep(1)
        st.success(f"**SESSION LOGGED // {now_d} // {now_t}**")
        
        summary = f"THE ORIEN PROJECT - MISSION REPORT\nTIMESTAMP: {now_d} | {now_t}\n" + "="*30 + "\n\n"
        summary += f"• PHYSICAL: {p_t if p_v else 'N/A'}\n• MENTAL: {m_t if m_v else 'N/A'}\n"
        summary += f"• PROFESSIONAL: {w_t if w_v else 'N/A'}\n• ENV: {e_t if e_v else 'N/A'}\n"
        summary += f"RESERVE: ${current_savings}\nNOTES: {victory_entry}"
        
        st.info(summary)
        st.download_button("📥 TRANSMIT LOG", data=summary, file_name=f"Orien_{now_d}.txt")
        st.markdown('<div class="status-box"><h2 style="color: #00d4ff; margin:0; letter-spacing:3px;">MISSION COMPLETE</h2></div>', unsafe_allow_html=True)

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    problem_input = st.text_area("DESCRIBE THE EVENT:", placeholder="Input data for logic filtering...", height=150)

    if st.button("RUN ORIEN PROTOCOL"):
        if problem_input:
            with st.status("Analyzing variables..."):
                time.sleep(1.2)
            
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.write("**STRATEGIC READOUT // MULTI-TIER PROTOCOL:**")
            txt = problem_input.lower()

            # Fully Restored Logic Branches
            if any(w in txt for w in ["hungry", "food", "broke", "money", "rent", "eat"]):
                cat, protocol = "resource", "RESOURCE CRISIS"
                mental = "Emergency Resource Management. Panic is a luxury you cannot afford."
                frame = "This is a logistical deficit. Do not attach shame; attach action."
                tactical = ["Identify local 'Zero-Cost' hubs.", "Trade labor for immediate meals/cash.", "Inventory liquidation."]
            elif any(w in txt for w in ["wife", "she", "fight", "argument", "partner"]):
                cat, protocol = "interpersonal", "INTERPERSONAL FRICTION"
                mental = "Frame Maintenance. You are the observer, not the victim."
                frame = "Their behavior is a weather pattern. You find cover; you don't fight the rain."
                tactical = ["Physical Exit (60 mins).", "Logistical communication only.", "Internal Audit."]
            else:
                cat, protocol = "discipline", "UNCLASSIFIED CHALLENGE"
                mental = "Extreme Ownership and Focus."
                frame = "Variable check: Do you control this? If yes, solve. If no, ignore."
                tactical = ["Re-engage Mission Control.", "20-min Cortisol Flush.", "Execute professional objective."]

            st.write(f"### 🛡️ {protocol}")
            st.write(f"**🧠 MENTAL:** {mental}")
            st.write(f"**🖼️ FRAME:** {frame}")
            st.write("**🛠️ TACTICAL ACTIONS:**")
            for action in tactical:
                st.write(f"• {action}")
            
            st.markdown(f'<div class="quote-box">{random.choice(quotes[cat])}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Data required for analysis.")
