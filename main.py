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
    .stCheckbox label, p, span, .stMarkdown { 
        color: #e0e0e0; 
        text-shadow: 0px 0px 5px rgba(0, 212, 255, 0.4); 
    }
    [data-testid="stVerticalBlockBorderWrapper"] { 
        background-color: #0c1017 !important; 
        border: 1px solid rgba(0, 212, 255, 0.3) !important; 
        padding: 15px !important; 
        border-radius: 4px !important; 
        box-shadow: 0px 0px 10px rgba(0, 212, 255, 0.1); 
    }
    input, textarea { 
        color: #00d4ff !important; 
        background-color: #000000 !important; 
        border: 1px solid rgba(0, 212, 255, 0.2) !important; 
        text-shadow: 0px 0px 5px rgba(0, 212, 255, 0.5) !important; 
    }
    .stButton button, .stDownloadButton button { 
        background-color: transparent !important; 
        color: #00d4ff !important; 
        border: 1px solid #00d4ff !important; 
        width: 100%; 
        text-transform: uppercase; 
        font-family: 'Share Tech Mono', monospace; 
        text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.8) !important;
    }
    .stProgress > div > div > div > div { 
        background-color: #00d4ff; 
        box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6); 
    }
    .advisor-output { 
        border-left: 3px solid #ff4b4b; 
        padding-left: 20px; 
        background-color: rgba(255, 75, 75, 0.05); 
        padding: 20px; 
        margin-top: 10px; 
        border-radius: 0 4px 4px 0;
    }
    .quote-box { 
        font-style: italic; 
        color: #999; 
        border-top: 1px solid rgba(0, 212, 255, 0.2); 
        padding-top: 15px; 
        margin-top: 20px; 
        font-size: 0.95rem; 
        line-height: 1.4;
    }
    .status-box {
        border: 1px solid #00d4ff;
        padding: 20px;
        text-align: center;
        border-radius: 4px;
        background-color: rgba(0, 212, 255, 0.05);
        margin-top: 20px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")

# --- QUOTE DATABASE ---
quotes = {
    "resource": [
        "'Wealth consists not in having great possessions, but in having few wants.' — Epictetus",
        "'The individual who says it is not possible should move out of the way of those doing it.' — Tricia Cunningham",
        "'Empty pockets never held anyone back. Only empty heads and empty hearts can do that.' — Norman Vincent Peale",
        "'Scarcity of resources is the mother of invention.' — Unknown"
    ],
    "interpersonal": [
        "'The best revenge is to be unlike him who performed the injury.' — Marcus Aurelius",
        "'You have power over your mind—not outside events. Realize this, and you will find strength.' — Marcus Aurelius",
        "'Everything that irritates us about others can lead us to an understanding of ourselves.' — Carl Jung",
        "'He who angers you, conquers you.' — Elizabeth Kenny"
    ],
    "discipline": [
        "'Self-discipline is the bridge between goals and accomplishment.' — Jim Rohn",
        "'The soul becomes dyed with the color of its thoughts.' — Marcus Aurelius",
        "'You don't get better on the days you feel like it. You get better on the days you don't.' — David Goggins",
        "'Discipline is choosing between what you want now and what you want most.' — Abraham Lincoln"
    ]
}

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
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

    # Progress Calculation
    p_v = 1 if (phys_check and phys_text.strip()) else 0
    m_v = 1 if (stoic_check and stoic_text.strip()) else 0
    w_v = 1 if (work_check and work_text.strip()) else 0
    e_v = 1 if (env_check and env_text.strip()) else 0
    total_verified = sum([p_v, m_v, w_v, e_v])
    st.progress(total_verified / 4 if total_verified > 0 else 0.0)

    st.divider()
    st.subheader("MOBILITY FUND")
    target = 1000
    current_savings = st.number_input("RESERVE_CREDITS ($)", min_value=0, value=0, step=1)
    st.progress(min(current_savings / target, 1.0))

    st.divider()
    st.subheader("USER_LOG // SESSION_DATA")
    victory_entry = st.text_area("", placeholder="Consolidate session notes...", key="log_area", label_visibility="collapsed")

    if st.button("EXECUTE SESSION UPLOAD"):
        now_t, now_d = datetime.now().strftime("%H:%M:%S"), date.today().strftime("%Y-%m-%d")
        with st.status("Syncing to Archive..."):
            time.sleep(1)
        st.success(f"**SESSION LOGGED // {now_d} // {now_t}**")
        
        summary = f"THE ORIEN PROJECT - MISSION REPORT\nTIMESTAMP: {now_d} | {now_t}\n" + "="*30 + "\n\n"
        summary += "--- SYSTEM DOMAINS ---\n\n"
        summary += f"• 01 PHYSICAL: {'[VERIFIED]' if p_v else '[INCOMPLETE]'} — {phys_text if phys_text else 'N/A'}\n\n"
        summary += f"• 02 MENTAL: {'[VERIFIED]' if m_v else '[INCOMPLETE]'} — {stoic_text if stoic_text else 'N/A'}\n\n"
        summary += f"• 03 PROFESSIONAL: {'[VERIFIED]' if w_v else '[INCOMPLETE]'} — {work_text if work_text else 'N/A'}\n\n"
        summary += f"• 04 ENVIRONMENTAL: {'[VERIFIED]' if e_v else '[INCOMPLETE]'} — {env_text if env_text else 'N/A'}\n\n"
        summary += f"--- FINANCIAL STATUS ---\nCREDITS ADDED: ${current_savings}\n\n--- NOTES ---\n{victory_entry}"
        
        st.info(summary)
        st.download_button("📥 TRANSMIT LOG", data=summary, file_name=f"Orien_{now_d}.txt")
        st.markdown('<div class="status-box"><h2 style="color: #00d4ff; margin:0; letter-spacing:3px;">MISSION COMPLETE</h2></div>', unsafe_allow_html=True)

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    st.subheader("📡 SITUATION ANALYSIS")
    problem_input = st.text_area("DESCRIBE THE EVENT:", placeholder="Input data for logic filtering...", height=150)

    if st.button("RUN ORIEN PROTOCOL"):
        if problem_input:
            with st.status("Analyzing variables..."):
                time.sleep(1.2)
            
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.write("**STRATEGIC READOUT // MULTI-TIER PROTOCOL:**")
            txt = problem_input.lower()

            # Logic Categories
            if any(w in txt for w in ["hungry", "food", "broke", "no money", "rent", "starving", "eat"]):
                cat, protocol = "resource", "RESOURCE CRISIS"
                mental = "Emergency Resource Management. Panic is a luxury you cannot afford."
                frame = "This is a logistical deficit. Do not attach shame to a resource gap; attach action to the solution."
                tactical = [
                    "Identify local 'Zero-Cost' hubs. Search for community kitchens or food pantries immediately.",
                    "Trade labor. Contact local businesses for 'day-labor' tasks that provide immediate meals or cash.",
                    "Inventory liquidation. Sell one non-essential item today to bridge the 24-hour gap."
                ]
            elif any(w in txt for w in ["wife", "partner", "petty", "she", "he", "argument", "fight", "kids"]):
                cat, protocol = "interpersonal", "INTERPERSONAL FRICTION"
                mental = "Frame Maintenance. You are the observer, not the participant in the drama."
                frame = "Their behavior is an external weather pattern. You do not get angry at the rain; you find cover."
                tactical = [
                    "Physical Exit. Remove yourself from the environment of friction for at least 60 minutes.",
                    "Monosyllabic Logistical Communication. Do not defend or explain. Only discuss objective facts.",
                    "Internal Audit. Identify why your peace was dependent on their approval."
                ]
            else:
                cat, protocol = "discipline", "UNCLASSIFIED CHALLENGE"
                mental = "Extreme Ownership and Focus."
                frame = "Is this a variable you control? If yes, solve it. If no, ignore it."
                tactical = [
                    "Re-engage Mission Control immediately. Complete one verified task to prove autonomy.",
                    "Cortisol Flush. 20 minutes of high-intensity physical movement to reset the nervous system.",
                    "Execute the next professional objective regardless of emotional state."
                ]

            # Output Formatting
            st.write(f"### 🛡️ {protocol}")
            st.write(f"**🧠 MENTAL:** {mental}")
            st.write(f"**🖼️ FRAME:** {frame}")
            st.write("**🛠️ TACTICAL ACTIONS:**")
            for action in tactical:
                st.write(f"• {action}")
            
            # Wisdom Layer
            selected_quote = random.choice(quotes[cat])
            st.markdown(f'<div class="quote-box">{selected_quote}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Data required for protocol analysis.")
