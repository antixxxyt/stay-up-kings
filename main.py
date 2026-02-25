import streamlit as st
from datetime import date

# 1. Branding
st.set_page_config(page_title="Stay Up Kings", page_icon="🛡️")

st.title("🛡️ STAY UP KINGS")
st.subheader("The Orien Protocol")
st.write(f"**Standard for:** {date.today().strftime('%A, %b %d')}")

# 2. The 4 Domains (Categorical & General)
st.divider()
col1, col2 = st.columns(2)

with col1:
    phys = st.checkbox("Domain 1: Physical") # Movement, health, output
    stoic = st.checkbox("Domain 2: Mental/Stoic") # Response to conflict, focus

with col2:
    work = st.checkbox("Domain 3: Professional") # Career, skills, income
    house = st.checkbox("Domain 4: Environmental") # Space, chores, territory

# Logic
score = sum([phys, stoic, work, house])
st.progress(score / 4)

if score == 4:
    st.success("KING STATUS: The day is won.")
    st.balloons()

# 3. The Chronicle
st.divider()
st.header("🏆 The Chronicle")
victory = st.text_area("Log a specific win or note for today:", placeholder="I stayed neutral when...")

if st.button("Commit to History"):
    st.toast("Victory cached.")

# 4. The Bridge
st.divider()
st.header("💰 The Freedom Fund")
current_fund = st.number_input("Secret Savings ($)", min_value=0, value=0, step=10)
target = 1000

st.progress(min(current_fund / target, 1.0))
st.write(f"**${target - current_fund}** until mobility is restored.")

# 5. The Sidebar
st.sidebar.title("The Standard")
st.sidebar.warning("REACTION IS SUBMISSION.")
st.sidebar.info("• Detach from the loop\n• Build in silence\n• Trust the work")
