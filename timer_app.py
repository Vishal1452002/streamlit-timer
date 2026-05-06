import time
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Page setup
st.set_page_config(layout="centered", page_title="Stopwatch")

# ---- Session State ----
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0
if "running" not in st.session_state:
    st.session_state.running = False

# ---- Logic ----
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

# ---- Auto Refresh ----
if st.session_state.running:
    st_autorefresh(interval=100, key="timer")

# ---- Update Time ----
if st.session_state.running:
    st.session_state.elapsed = time.time() - st.session_state.start_time

# ---- Format ----
total = st.session_state.elapsed
h = int(total // 3600)
m = int((total % 3600) // 60)
s = int(total % 60)
t = int((total * 10) % 10)

time_display = f"{h:02d}:{m:02d}:{s:02d}.{t}"

# ---- UI ----
st.title("⏱️ Stopwatch")

st.markdown(
    f"""
    <div style="
        font-size:60px;
        text-align:center;
        background:#222;
        color:#00ff00;
        padding:20px;
        border-radius:10px;">
        {time_display}
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Stop" if st.session_state.running else "Start", use_container_width=True):
        stop() if st.session_state.running else start()

with col2:
    if st.button("Reset", use_container_width=True):
        reset()
