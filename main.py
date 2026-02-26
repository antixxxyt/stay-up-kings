import streamlit as st
from datetime import date, datetime
import time
import google.generativeai as genai  # Requires: pip install google-generativeai

# 1. Page Config
st.set_page_config(page_title="The Orien Project", page_icon="🧭", layout="centered")

# 2. Luminous Tech CSS
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
    .advisor-output { border-left: 3px solid #ff4b4b; background-color: rgba(255, 75, 75, 0.07); padding: 25px; margin-top: 10px; border-radius: 0 4px 4px 0; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation & Gemini Setup
with st.sidebar:
    st.title("SYSTEM MENU")
    page = st.radio("SELECT MODULE:", ["01 MISSION CONTROL", "02 TACTICAL ADVISORY"])
    st.divider()
    gemini_key = st.text_input("ENTER GEMINI KEY:", type="password", help="Get your key at aistudio.google.com")
    st.error("REACTION IS SUBMISSION.")
    st.info("Orien: Control the variables. Own the outcome.")

# --- GEMINI LOGIC ENGINE ---
def get_gemini_strategy(user_input, key):
    if not key:
        return "⚠️ SYSTEM KEY REQUIRED. Please enter your Gemini API key in the sidebar to activate the Tactical Advisor."
    
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        You are the ORIEN PROJECT STRATEGIC ADVISOR. 
        Analyze this situation: "{user_input}"
        
        Provide a response for a man pursuing high-level discipline ('Stay Up Kings' philosophy). 
        You must address the specific details of the event provided. No generic fluff.
        
        Format your response exactly like this:
        ### 🛡️ STRATEGIC PROTOCOL
        **🧠 MENTAL:** [Stoic/Logical mindset to stop emotional spiraling]
        
        **🖼️ FRAME:** [How to view this situation to maintain power/control]
        
        **🛠️ TACTICAL ACTIONS:**
        * [Immediate practical action 1]
        * [Specific logistical/resource solution 2]
        * [Long-term preventative step 3]
        
        **📜 LEGACY DIRECTIVE:**
        "[A powerful, highly applicable quote from a historical figure, warrior, or philosopher that fits this EXACT scenario]"
        — [Author]
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"ERROR CONNECTING TO NODES: {str(e)}"

# --- PAGE 1: MISSION CONTROL ---
if page == "01 MISSION CONTROL":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // MISSION_CONTROL</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            p_c = st.checkbox("01 // PHYSICAL")
            p_t = st.text_input("Evidence:", key="p_t", placeholder="Logs...")
        with st.container(border=True):
            m_c = st.checkbox("02 // MENTAL")
            m_t = st.text_input("Evidence:", key="m_t", placeholder="Logs...")
    with col2:
        with st.container(border=True):
            w_c = st.checkbox("03 // PROFESSIONAL")
            w_t = st.text_input("Evidence:", key="w_t", placeholder="Logs...")
        with st.container(border=True):
            e_c = st.checkbox("04 // ENVIRONMENTAL")
            e_t = st.text_input("Evidence:", key="e_t", placeholder="Logs...")

    score = sum([1 for c, t in [(p_c, p_t), (m_c, m_t), (w_c, w_t), (e_c, e_t)] if c and t.strip()])
    st.progress(score/4)

    st.subheader("MOBILITY FUND")
    fund = st.number_input("RESERVE_CREDITS ($)", min_value=0)
    
    if st.button("EXECUTE SESSION UPLOAD"):
        st.success(f"SESSION LOGGED // {datetime.now().strftime('%H:%M:%S')}")

# --- PAGE 2: TACTICAL ADVISORY ---
elif page == "02 TACTICAL ADVISORY":
    st.markdown('<p class="main-title">THE ORIEN PROJECT</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">STAY UP KINGS // TACTICAL_ADVISORY</p>', unsafe_allow_html=True)
    
    event = st.text_area("DESCRIBE THE EVENT IN DETAIL:", height=150, placeholder="E.g., Financial crisis, relationship friction, or internal resistance...")

    if st.button("RUN ORIEN PROTOCOL"):
        if event:
            with st.status("Consulting Gemini Intelligence..."):
                output = get_gemini_strategy(event, gemini_key)
            
            st.markdown('<div class="advisor-output">', unsafe_allow_html=True)
            st.markdown(output)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Please describe the situation to initiate protocol.")
