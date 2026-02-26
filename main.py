import streamlit as st
from datetime import datetime
import requests 
import json

# 1. PAGE CONFIG
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. CSS STYLING
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    .main-title { color: #ffffff !important; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; letter-spacing: 5px; font-size: 2.8rem; text-align: center; text-shadow: 0px 0px 20px rgba(0, 212, 255, 1); }
    .sub-title { color: #00d4ff; font-family: 'Share Tech Mono', monospace; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; text-align: center; margin-top: -5px; margin-bottom: 30px; }
    [data-testid="stVerticalBlockBorderWrapper"] { background-color: #0c1017 !important; border: 1px solid rgba(0, 212, 255, 0.3) !important; padding: 15px !important; border-radius: 4px; }
    input, textarea { color: #00d4ff !important; background-color: #000000 !important; border: 1px solid rgba(0, 212, 255, 0.2) !important; }
    .stButton button { background-color: transparent !important; color: #00d4ff !important; border: 1px solid #00d4ff !important; width: 100%; text-transform: uppercase; font-family: 'Share Tech Mono', monospace; }
    .advisor-output { border-left: 3px solid #ff4b4b; background-color: rgba(255, 75, 75, 0.05); padding: 25px; margin-top: 10px; border-radius: 0 4px 4px 0; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    gemini_key = st.text_input("ENTER GEMINI KEY:", type="password", placeholder="Paste AIza... key here")
    
    if gemini_key:
        st.success("KEY INJECTED")
    else:
        st.warning("AWAITING KEY")
    st.error("REACTION IS SUBMISSION.")

# --- THE "STABLE" AI ENGINE ---
def call_gemini_api(user_input, key):
    if not key:
        return "⚠️ **SYSTEM KEY REQUIRED.**"
    
    # Updated to the specific v1beta 'gemini-1.5-flash' endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    
    data = {
        "contents": [{
            "parts": [{"text": f"You are the ORIEN PROJECT STRATEGIC ADVISOR. Analyze this: {user_input}. Provide a Stoic Mental Protocol, 3 Tactical Actions, and a warrior quote."}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            return f"❌ **DIAGNOSTIC ERROR {response.status_code}:** {response.text}"
            
        res_json = response.json()
        return res_json['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ **SYSTEM CRASH:** {str(e)}"

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_t", placeholder="Logged action (e.g. Gym)...")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_t", placeholder="Logged output (e.g. Work)...")

    if st.button("EXECUTE SESSION UPLOAD"):
        st.success(f"SESSION LOGGED // {datetime.now().strftime('%H:%M:%S')}")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    event = st.text_area("DESCRIBE THE EVENT:", height=150, placeholder="E.g., Dealing with financial stress or discipline issues...")

    if st.button("RUN ORIEN PROTOCOL"):
        if event:
            with st.spinner("Establishing Neural Link..."):
                output = call_gemini_api(event, gemini_key)
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.markdown(output)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Data required for analysis.")
