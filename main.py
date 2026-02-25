import streamlit as st
from datetime import date

# 1. Branding & Persona
st.set_page_config(page_title="Stay Up Kings", page_icon="🛡️")

st.title("🛡️ STAY UP KINGS")
st.subheader("Orien: The Self-Sovereignty Protocol")
st.write(f"**Current Deployment:** {date.today().strftime('%A, %B %d')}")

# 2. The Scorecard (The New Terminology)
st.divider()
col1, col2 = st.columns(2)

with col1:
    phys = st.checkbox("War Machine: 30m Physical Output")
    stoic = st.checkbox("Emotional Fortress: Neutrality in Conflict")

with col2:
    work = st.checkbox("Economic Expansion: 4h High-Value Work")
    house = st.checkbox("Domestic Sovereignty: Command of Environment")

# Logic
score = sum([phys, stoic, work, house])
st.progress(score / 4)

if score == 4:
    st.success("KING STATUS: Integrity Maintained. You are the Architect.")
    st.balloons()

# 3. The Victory Log
st.divider()
st.header("🏆 The Chronicle of Wins")
victory = st.text_area("Record a moment of resilience or progress:")

if st.button("Log to Chronicle"):
    st.toast("Victory recorded in current session.")

# 4. The Freedom Fund (The Bridge)
st.divider()
st.header("💰 The Freedom Fund")
st.write("Metric: Independent Mobility ($1,000 Target)")
current_fund = st.number_input("Secret Reserves ($)", min_value=0, value=0, step=10)

st.progress(min(current_fund / 1000, 1.0))
st.write(f"**${1000 - current_fund}** until full mobility is restored.")

# 5. The Sidebar (The Creed)
st.sidebar.title("The Standard")
st.sidebar.warning("REACTION IS SUBMISSION.")
st.sidebar.info("1. Detach from the feedback loop.\n2. Build in silence.\n3. Let the results speak.")
