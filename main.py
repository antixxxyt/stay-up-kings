import streamlit as st
from datetime import date

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Luminous Tech CSS
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
        letter-spacing: 5px;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 0px;
        text-shadow: 0px 0px 20px rgba(0, 212, 255, 1), 0px 0px 10px rgba(0, 212, 255, 0.8);
    }
    .sub-title, h3, .stSubheader p {
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
    .stButton button {
        background-color: transparent !important;
        color: #00d4ff !important;
        border: 1px solid #00d4ff !important;
        text-shadow: 0px 0px 8px rgba(0, 212, 255, 0.8) !important;
        box-shadow: 0px 0px 10px rgba(0, 212, 255, 0.2) !important;
        width: 100%;
    }
    .stProgress > div > div > div > div {
        background-color: #00d4ff;
        box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. Branding
st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
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

# Logic for verified score
p_v = 1 if (phys_check and phys_text.strip()) else 0
m_v = 1 if (stoic_check and stoic_text.strip()) else 0
w_v = 1 if (work_check and work_text.strip()) else 0
e_v = 1 if (env_check and env_text.strip()) else 0

total_verified = sum([p_v, m_v, w_v, e_v])
st.progress(total_verified / 4)

# 5. MOBILITY FUND
st.divider()
st.subheader("MOBILITY FUND")
target = 1000
current_savings = st.number_input("RESERVE_CREDITS ($)", min_value=0, value=0, step=1)
fund_progress = min(current_savings / target, 1.0)
st.progress(fund_progress)

# 6. USER LOG
st.divider()
st.subheader("USER_LOG // SESSION_DATA")
victory_entry = st.text_area("", placeholder="Consolidate session notes...", key="log_area", label_visibility="collapsed")

# 7. INTEGRATED SUMMARY OUTPUT
if st.button("EXECUTE SESSION UPLOAD"):
    st.success(f"**SESSION LOGGED // {date.today()}**")
    
    # Building the Summary String
    summary = f"**DATA_ENTRY:**\n\n"
    
    # Domain Summary
    summary += "--- DOMAIN STATUS ---\n"
    summary += f"01 PHYSICAL: {'VERIFIED' if p_v else 'INCOMPLETE'} ({phys_text if phys_text else 'N/A'})\n"
    summary += f"02 MENTAL: {'VERIFIED' if m_v else 'INCOMPLETE'} ({stoic_text if stoic_text else 'N/A'})\n"
    summary += f"03 PROFESSIONAL: {'VERIFIED' if w_v else 'INCOMPLETE'} ({work_text if work_text else 'N/A'})\n"
    summary += f"04 ENVIRONMENTAL: {'VERIFIED' if e_v else 'INCOMPLETE'} ({env_text if env_text else 'N/A'})\n\n"
    
    # Finance Summary
    added_funds = current_savings if current_savings > 0 else 0
    summary += "--- FINANCIAL STATUS ---\n"
    summary += f"CREDITS ADDED: ${added_funds if added_funds > 0 else '0'}\n"
    summary += f"CURRENT RESERVES: ${current_savings} / ${target}\n\n"
    
    # Final Notes
    summary += "--- SESSION NOTES ---\n"
    summary += f"{victory_entry if victory_entry else 'No notes archived.'}"
    
    st.info(summary)

# 8. Sidebar
with st.sidebar:
    st.title("DIRECTIVES")
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")
