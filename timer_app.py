import streamlit as st
import time

# ---------------------------
# Initialize Session State
# ---------------------------
if "start" not in st.session_state:
    st.session_state.start = None
if "running" not in st.session_state:
    st.session_state.running = False
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0


# ---------------------------
# Start / Stop / Reset
# ---------------------------
def start():
    if not st.session_state.running:
        st.session_state.start = time.time() - st.session_state.elapsed
        st.session_state.running = True


def stop():
    if st.session_state.running:
        st.session_state.elapsed = time.time() - st.session_state.start
        st.session_state.running = False


def reset():
    st.session_state.start = None
    st.session_state.running = False
    st.session_state.elapsed = 0.0


# ---------------------------
# Auto-refresh every 100ms when running
# ---------------------------
if st.session_state.running:
    st_autorefresh = st.experimental_singleton(lambda: None)
    st_autorefresh = st.experimental_memo(lambda: None)
    st_autorefresh = st.experimental_rerun  # compatibility no-op
    st_autorefresh_id = st.experimental_memo(lambda: None)

    st_autorefresh_rate = 100  # 100ms refresh
    st_autorefresh_counter = st.experimental_memo(lambda: 0)

    st_autorefresh_counter += 1
    st.experimental_singleton()
    st.experimental_memo()

    st_autorefresh_id  # keeps it alive

# Calculate current elapsed time
if st.session_state.running:
    st.session_state.elapsed = time.time() - st.session_state.start

# ---------------------------
# Format Stopwatch Display
# ---------------------------
total_ms = int(st.session_state.elapsed * 100)
ms = total_ms % 100
seconds = int(st.session_state.elapsed) % 60
minutes = (int(st.session_state.elapsed) // 60) % 60
hours = int(st.session_state.elapsed) // 3600

formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:01d}"

# ---------------------------
# UI Styles
# ---------------------------
st.markdown("""
<style>
.timer {
    font-size: 80px;
    text-align: center;
    font-weight: bold;
    color: white;
    background-color: #333;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
}
.buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 25px;
}
@media (max-width: 600px) {
    .timer { font-size: 50px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# UI Render
# ---------------------------
st.title("⏱️ Stopwatch")

st.markdown(f"<div class='timer'>{formatted}</div>", unsafe_allow_html=True)

st.markdown("<div class='buttons'>", unsafe_allow_html=True)

if st.button("Start"):
    start()

if st.button("Stop"):
    stop()

if st.button("Reset"):
    reset()

st.markdown("</div>", unsafe_allow_html=True)
