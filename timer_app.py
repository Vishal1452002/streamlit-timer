import streamlit as st
import time

# ---------------------------
# Session State Initialization
# ---------------------------
if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "running" not in st.session_state:
    st.session_state.running = False

if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0


# ---------------------------
# Stopwatch Logic
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
    st.session_state.start_time = None
    st.session_state.elapsed = 0.0
    st.session_state.running = False


# ---------------------------
# Millisecond Timer Calculation
# ---------------------------
if st.session_state.running:
    st.session_state.elapsed = time.time() - st.session_state.start_time


# ---------------------------
# Format Time (HH:MM:SS.ms)
# ---------------------------
total_ms = int(st.session_state.elapsed * 100)
ms = total_ms % 100
total_seconds = int(st.session_state.elapsed)
seconds = total_seconds % 60
minutes = (total_seconds // 60) % 60
hours = total_seconds // 3600

formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:01d}"


# ---------------------------
# UI Styling (LOOKS LIKE YOUR IMAGE)
# ---------------------------
st.markdown("""
<style>
    .timer-box {
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        color: white;
        padding: 20px;
        background-color: #333;
        border-radius: 10px;
        margin-top: 30px;
    }
    .btn-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
        flex-wrap: wrap;
    }
    @media (max-width: 600px) {
        .timer-box {
            font-size: 55px;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------
# TITLE + DISPLAY
# ---------------------------
st.title("⏱️ Stopwatch")

st.markdown(f"<div class='timer-box'>{formatted}</div>", unsafe_allow_html=True)


# ---------------------------
# BUTTONS
# ---------------------------
st.markdown("<div class='btn-row'>", unsafe_allow_html=True)

if st.button("Start"):
    start()

if st.button("Stop"):
    stop()

if st.button("Reset"):
    reset()

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------
# Auto-refresh for smooth milliseconds
# ---------------------------
if st.session_state.running:
    time.sleep(0.1)  # refresh every 100ms for smooth display
    st.experimental_rerun()
