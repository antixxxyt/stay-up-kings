import streamlit as st
from datetime import date, datetime
import time
import requests 
import json

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. ORIEN LUMINOUS STYLING (CSS)
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
    .advisor-output { border-left: 3px solid #ff4b4b; background-color: rgba(255, 75, 75, 0.05); padding: 25px; margin-top: 10px; border-radius: 0 4px 4px 0; line-height: 1.6; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION & API SETUP
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    gemini_key = st.text_input("ENTER GEMINI KEY:", type="password", help="Get your key at aistudio.google.com")
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")

# --- THE AI ENGINE (Direct Web Request) ---
def call_gemini_api(user_input, key):
    if not key:
        return "⚠️ **SYSTEM KEY REQUIRED.** Please enter your Gemini API key in the sidebar to activate the AI brain."
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    
    # Precise instructions for the AI behavior
    prompt_context = f"""
    You are the ORIEN PROJECT STRATEGIC ADVISOR. 
    Analyze this situation: "{user_input}"
    Provide a Stoic Mental Protocol, 3 specific Tactical Actions, and a highly relevant warrior/philosophy quote.
    Format your response clearly with bold headers and bullet points. Be surgical, practical, and intense.
    """
    
    data = {"contents": [{"parts": [{"text": prompt_context}]}]}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = response.json()
        # Parsing the specific Gemini response structure
        return response_data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"**Connection Error:** Ensure your API key is correct and you have internet access. Details: {str(e)}"

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    st.subheader("SYSTEM DOMAINS")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_t", placeholder="Action log...")
        with st.container(border=True):
            m_c = st.checkbox("02 // MENTAL")
            m_t = st.text_input("Evidence:", key="m_t", placeholder="Response log...")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_t", placeholder="Output log...")
        with st.container(border=True):
            e_c = st.checkbox("04 // ENVIRONMENTAL")
            e_t = st.text_input("Evidence:", key="e_t", placeholder="Env log...")

    # Verified Progress Logic
    score = sum([1 for c, t in [(p_c, p_t), (m_c, m_t), (w_c, w_t), (e_c, e_t)] if c and t.strip()])
    st.progress(score/4)

    st.divider()
    st.subheader("MOBILITY FUND")
    fund = st.number_input("RESERVE_CREDITS ($)", min_value=0)
    st.progress(min(fund / 1000, 1.0)) # Visualizing progress toward a $1k goal

    if st.button("EXECUTE SESSION UPLOAD"):
        now = datetime.now().strftime("%H:%M:%S")
        st.success(f"SESSION LOGGED AT {now}. ALL SYSTEMS NOMINAL.")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    event = st.text_area("DESCRIBE THE EVENT IN DETAIL:", height=150, placeholder="Input crisis data for strategic readout...")

    if st.button("RUN ORIEN PROTOCOL"):
        if event:
            with st.status("Accessing Gemini Intelligence Nodes..."):
                output = call_gemini_api(event, gemini_key)
            
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.markdown(output)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Data required for protocol analysis. Please describe the event.")
