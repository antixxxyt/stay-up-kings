import streamlit as st
from datetime import date

# 1. Page Branding
st.set_page_config(page_title="Stay Up Kings", page_icon="👑")

st.title("👑 STAY UP KINGS")
st.subheader("Action-Based Autonomy")
st.write(f"**The Daily Standard:** {date.today().strftime('%A, %b %d')}")

# 2. The Daily Scorecard
st.divider()
col1, col2 = st.columns(2)

with col1:
    phys = st.checkbox("Physical: 30m Movement")
    stoic = st.checkbox("Stoic: Neutrality in Conflict") # <--- This is for the food situation.

with col2:
    work = st.checkbox("Professional: 4h Deep Work")
    house = st.checkbox("Duty: Silent House Management")

# Logic
score = sum([phys, stoic, work, house])
st.progress(score / 4)

if score == 4:
    st.success("INTEGRITY MAINTAINED.")
    st.balloons()

# 3. NEW: The Victory Log
st.divider()
st.header("🏆 Daily Victory Log")
victory = st.text_area("What did you win today? (e.g., 'Stayed calm when disrespected', 'Finished code')")

if st.button("Log Victory"):
    st.toast(f"Victory Recorded: {victory}")
    st.info("Note: For now, this stays on screen until you refresh. We'll save it to a database next.")

# 4. The Mobility Fund
st.divider()
st.header("🚀 Mobility Fund")
current_fund = st.number_input("Secret Savings ($)", min_value=0, value=0, step=10)
target = 1000

st.progress(min(current_fund / target, 1.0))
st.write(f"**${target - current_fund}** remaining to freedom.")

# 5. Sidebar Creed
st.sidebar.title("The King's Creed")
st.sidebar.warning("REACTION IS SUBMISSION. Stay neutral. Stay focused.")
st.sidebar.info("1. No Performance for Praise.\n2. Silence is Strength.\n3. Action is the Only Metric.")
