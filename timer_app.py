import time
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# -------------------------------------
# Initialize session state
# -------------------------------------
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0
if "running" not in st.session_state:
    st.session_state.running = False


# -------------------------------------
# Functions
# -------------------------------------
def start():
    if not st.session_state.running:
        st.session_state.start_time = time.time() - st.session_state.elapsed
        st.session_state.running = True


def stop():
    if st.session_state.running:
        st.session_state.elapsed = time.time() - st.session_state.start_time
        st.session_state.running = False


def reset():
    st.session_state.running = False
    st.session_state.elapsed = 0.0
    st.session_state.start_time = None


# -------------------------------------
# Auto-refresh every 100ms if running
# -------------------------------------
if st.session_state.running:
    st_autorefresh(interval=100, key="refresh_timer")


# -------------------------------------
# Update elapsed time
# -------------------------------------
if st.session_state.running and st.session_state.start_time is not None:
    st.session_state.elapsed = time.time() - st.session_state.start_time


# -------------------------------------
# Format time (HH:MM:SS.t)
# -------------------------------------
total_tenths = int(st.session_state.elapsed * 10)
tenths = total_tenths % 10
total_seconds = int(st.session_state.elapsed)
seconds = total_seconds % 60
minutes = (total_seconds // 60) % 60
hours = total_seconds // 3600

formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{tenths}"


# -------------------------------------
# UI Styling
# -------------------------------------
st.markdown("""
<style>
.timer-box {
    font-size: 80px;
    font-weight: bold;
    color: white;
    background-color: #222;
    text-align: center;
    padding: 30px;
    border-radius: 12px;
    margin-top: 30px;
}
.buttons {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 25px;
    flex-wrap: wrap;
}
@media (max-width: 600px) {
    .timer-box { font-size: 55px; }
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------
# UI
# -------------------------------------
st.title("⏱️ Stopwatch")

st.markdown(f"<div class='timer-box'>{formatted}</div>", unsafe_allow_html=True)

st.markdown("<div class='buttons'>", unsafe_allow_html=True)
if st.button("Start"):
    start()
if st.button("Stop"):
    stop()
if st.button("Reset"):
    reset()
st.markdown("</div>", unsafe_allow_html=True)
