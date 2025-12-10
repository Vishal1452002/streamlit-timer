import time
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# --- Configuration and Initialization ---
st.set_page_config(layout="centered", page_title="Streamlit Stopwatch")

# -------------------------------------
# 1. Initialize session state
# -------------------------------------
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0
if "running" not in st.session_state:
    st.session_state.running = False


# -------------------------------------
# 2. Stopwatch control functions
# -------------------------------------
def start_stopwatch():
    if not st.session_state.running:
        st.session_state.start_time = time.time() - st.session_state.elapsed
        st.session_state.running = True

def stop_stopwatch():
    if st.session_state.running:
        st.session_state.elapsed = time.time() - st.session_state.start_time
        st.session_state.running = False

def reset_stopwatch():
    st.session_state.running = False
    st.session_state.elapsed = 0.0
    st.session_state.start_time = None


# -------------------------------------
# 3. Auto-refresh when running
# -------------------------------------
# Only run the autorefresh if needed
if st.session_state.running:
    st_autorefresh(interval=100, key="refresh_timer")


# -------------------------------------
# 4. Update elapsed time
# -------------------------------------
if st.session_state.running and st.session_state.start_time is not None:
    st.session_state.elapsed = time.time() - st.session_state.start_time


# -------------------------------------
# 5. Format time (HH:MM:SS.t)
# -------------------------------------
total_tenths = int(st.session_state.elapsed * 10)
tenths = total_tenths % 10

total_seconds = int(st.session_state.elapsed)
seconds = total_seconds % 60
minutes = (total_seconds // 60) % 60
hours = total_seconds // 3600

formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{tenths}"


# -------------------------------------
# 6. CSS Styling
# -------------------------------------
st.markdown("""
<style>
/* Global style to reduce margin/padding which can sometimes cause jitter */
[data-testid="stVerticalBlock"] {
    gap: 0rem;
}

/* Style for the main timer display */
.timer-box {
    font-family: monospace;
    font-size: 80px;
    font-weight: bold;
    color: #00ff00;
    background-color: #222;
    text-align: center;
    padding: 30px;
    border-radius: 12px;
    margin-top: 30px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    white-space: nowrap; 
}

/* Container for the buttons (Default is a row) */
.button-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-top: 30px;
}

/* --- Mobile Specific Styles (Break into a Column) --- */
@media (max-width: 600px) {
    .timer-box { 
        font-size: 55px;
        padding: 20px;
    }
    
    .button-row {
        flex-direction: column; 
        gap: 15px; 
        width: 100%;
    }
    
    .stButton>button {
        width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------
# 7. Layout and UI
# -------------------------------------
st.title("⏱️ Streamlit Stopwatch")

# *** FIX FOR FLICKERING: Create a placeholder for the timer ***
# This placeholder will be updated with the time, preventing the 
# entire app from redrawing that section every 100ms.
timer_placeholder = st.empty()


# Display the formatted time using the styled div inside the placeholder
timer_placeholder.markdown(f"<div class='timer-box'>{formatted_time}</div>", unsafe_allow_html=True)


# Button Layout (No changes needed here)
with st.container():
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    
    # START/PAUSE Button
    button_label = "Stop" if st.session_state.running else "Start"
    
    if st.button(button_label, use_container_width=True):
        if st.session_state.running:
            stop_stopwatch()
        else:
            start_stopwatch()
            
    # RESET Button
    if st.button("Reset", use_container_width=True):
        reset_stopwatch()
        
    st.markdown('</div>', unsafe_allow_html=True)
