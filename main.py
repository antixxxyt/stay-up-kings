import streamlit as st
from datetime import date

# 1. Page Config & Custom Theme
st.set_page_config(page_title="Stay Up Kings", page_icon="🛡️", layout="centered")

# Custom CSS Injection
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    /* Gold headers */
    h1, h2, h3 {
        color: #d4af37 !important;
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    /* Customizing the checkboxes */
    .stCheckbox {
        background-color: #1a1c23;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }
    /* The Progress Bar color */
    .stProgress > div > div > div > div {
        background-color: #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Section
st.title("🛡️ STAY UP KINGS")
st.write(f"**PROTOCOL ACTIVE:** {date.today().strftime('%A, %B %d')}")

# 3. The 4 Domains (Clean Grid)
st.divider()
st.subheader("Daily Domains")

col1, col2 = st.columns(2)

with col1:
    phys = st.checkbox("01 // PHYSICAL")
    stoic = st.checkbox("02 // MENTAL")

with col2:
    work = st.checkbox("03 // PROFESSIONAL")
    env = st.checkbox("04 // ENVIRONMENTAL")

# Score Logic
score = sum([phys, stoic, work, env])
progress = score / 4
st.progress(progress)

if score == 4:
    st.success("INTEGRITY MAINTAINED. ALL DOMAINS SECURED.")
    st.balloons()

# 4. The Freedom Fund
st.divider()
st.subheader("💰 FREEDOM FUND")
target = 1000
current = st.number_input("Reserves ($)", min_value=0, value=0, step=10)

# Visual Progress for Fund
fund_progress = min(current / target, 1.0)
st.progress(fund_progress)
st.write(f"STATUS: **${current} / ${target}**")

# 5. The Chronicle
st.divider()
st.subheader("🏆 THE CHRONICLE")
victory = st.text_area("", placeholder="Enter your victory for the record...", label_visibility="collapsed")
if st.button("LOG ENTRY"):
    st.toast("Victory cached in session memory.")

# 6. Sidebar
with st.sidebar:
    st.title("THE STANDARD")
    st.error("REACTION IS SUBMISSION.")
    st.info("Build in silence. Let the work prove them wrong.")
