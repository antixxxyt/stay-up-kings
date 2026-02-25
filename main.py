import streamlit as st
from datetime import date

# 1. Page Branding
st.set_page_config(page_title="Stay Up Kings", page_icon="👑", layout="centered")

# Custom CSS for the "King" aesthetic (Dark/Gold/Clean)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #d4af37 !important; } /* Gold headers */
    .stCheckbox { font-size: 20px; }
    </style>
    """, unsafe_allow_id=True)

st.title("👑 STAY UP KINGS")
st.subheader("Action-Based Autonomy")
st.write(f"**Date:** {date.today().strftime('%A, %B %d, %Y')}")

# 2. The Daily Scorecard (The "Work")
st.divider()
st.header("The Daily Standard")

col1, col2 = st.columns(2)

with col1:
    phys = st.checkbox("Physical: 30m Movement")
    stoic = st.checkbox("Stoic: Neutrality in Conflict")

with col2:
    work = st.checkbox("Professional: 4h Deep Work")
    house = st.checkbox("Duty: Silent House Management")

# Logic for the Progress Bar
score = sum([phys, stoic, work, house])
total = 4
progress = score / total

st.progress(progress)
if score == total:
    st.success("KING STATUS: Integrity Maintained.")
    st.balloons()
else:
    st.info(f"Progress: {int(progress*100)}% — Finish the day.")

# 3. The Mobility Fund (The "Bridge")
st.divider()
st.header("The Bridge to $1,000")
st.write("Target: Independent Transportation & Mobility")

# This is a manual input for now to track your "Secret Savings"
current_fund = st.number_input("Current Secret Fund ($)", min_value=0, value=0, step=10)
target = 1000

if current_fund < target:
    st.progress(current_fund / target)
    st.write(f"Remaining: **${target - current_fund}** to Freedom.")
else:
    st.success("Target Met. Mobility Secured.")

# 4. The "Scorecard" Motto
st.sidebar.title("The King's Creed")
st.sidebar.info("""
1. No Performance for Praise.
2. Silence is Strength.
3. Action is the Only Metric.
""")
