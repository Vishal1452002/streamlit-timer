import streamlit as st
import time

# ---------------------------
# Session State
# ---------------------------
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "running" not in st.session_state:
    st.session_state.running = False
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0

# ---------------------------
# Controls
# ---------------------------
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

# ---------------------------
# Auto refresh system
# ---------------------------
if st.session_state.running:
    st.autorefresh(interval=100, key="refresh")  # refresh every 100ms

# Update elapsed time
if st.session_state.running:
    st.session_state.elapsed = time.time() - st.session_state.start_time

# ---------------------------
# Time Format (HH:MM:SS.t)
# ---------------------------
total_ms = int(st.session_state.elapsed * 10)
ms = total_ms % 10
total_seconds = int(st.session_state.elapsed)
seconds = total_seconds % 60
minutes = (total_seconds // 60) % 60
hours = total_seconds // 3600

formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms}"

# ---------------------------
# UI Styling (Matches Your Screenshot)
# ---------------------------
st.markdown("""
<style>
.timer-box {
    font-size: 80px;
    text-align: center;
    font-weight: bold;
    color: white;
    background-color: #222;
    padding: 30px;
    border-radius: 10px;
    margin-top: 30px;
}
.buttons {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 25px;
}
@media (max-width: 600px) {
    .timer-box { font-size: 50px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Render UI
# ---------------------------
st.title("⏱️ Stopwatch")

st.markdown(f"<div class='timer-box'>{formatted}</div>", unsafe_allow_html=True)

st.markdown("<div class='buttons'>", unsafe_allow_html=True)

if st.button("Start"): start()
if st.button("Stop"): stop()
if st.button("Reset"): reset()

st.markdown("</div>", unsafe_allow_html=True)
