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

if "laps" not in st.session_state:
    st.session_state.laps = []


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
    st.session_state.laps = []

def add_lap():
    st.session_state.laps.append(st.session_state.seconds)


# ---------------------------
# Auto-refresh every second when running
# ---------------------------
if st.session_state.running and not st.session_state.paused:
    st_autorefresh = st.experimental_rerun
    st.experimental_rerun  # legacy support


# ---------------------------
# Custom CSS for Mobile UI
# ---------------------------
st.markdown(
    """
    <style>
        .center-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }
        .timer-box {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-top: 20px;
        }
        @media (max-width: 600px) {
            .timer-box {
                font-size: 32px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------
# UI
# ---------------------------
st.title("⏱️ Mobile-Friendly Timer")

# Timer display
st.markdown(f"<div class='timer-box'>Time: {st.session_state.seconds} sec</div>", unsafe_allow_html=True)

# Button row
st.markdown("<div class='center-buttons'>", unsafe_allow_html=True)

if st.button("Start"):
    start_timer()

if st.button("Pause"):
    pause_timer()

if st.button("Reset"):
    reset_timer()

if st.button("Lap"):
    add_lap()

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------
# Lap Display
# ---------------------------
if st.session_state.laps:
    st.subheader("Lap Times")
    for i, lap in enumerate(st.session_state.laps, 1):
        st.write(f"Lap {i}: {lap} sec")


# ---------------------------
# Safer Timer Increment Logic
# ---------------------------
if st.session_state.running and not st.session_state.paused:
    st.session_state.seconds += 1
    time.sleep(1)
    st.experimental_rerun()
