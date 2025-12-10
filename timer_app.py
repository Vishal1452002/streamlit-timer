import streamlit as st
import time

# ---------------------------
# Initialize Session State
# ---------------------------
if "seconds" not in st.session_state:
    st.session_state.seconds = 0

if "running" not in st.session_state:
    st.session_state.running = False

if "paused" not in st.session_state:
    st.session_state.paused = False


# ---------------------------
# Timer Logic
# ---------------------------
def start_timer():
    st.session_state.running = True
    st.session_state.paused = False

def pause_timer():
    st.session_state.paused = True

def reset_timer():
    
    st.session_state.seconds = 0
    st.session_state.paused = True
    st.session_state.running = False


# ---------------------------
# UI
# ---------------------------
st.title("⏱️ Streamlit Timer")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Start"):
        start_timer()

with col2:
    if st.button("Pause"):
        pause_timer()

with col3:
    if st.button("Reset"):
        reset_timer()

# Display timer output placeholder
timer_display = st.empty()


# ---------------------------
# Update Timer
# ---------------------------
if st.session_state.running and not st.session_state.paused:
    # Run one tick
    st.session_state.seconds += 1
    timer_display.markdown(f"### Time: **{st.session_state.seconds} sec**")

    # Sleep 1 sec then rerun automatically
    time.sleep(1)
    st.rerun()

else:
    # Static display
    timer_display.markdown(f"### Time: **{st.session_state.seconds} sec**")
