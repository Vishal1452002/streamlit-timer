import time
import streamlit as st
# Import the autorefresh component
from streamlit_autorefresh import st_autorefresh

# --- Configuration and Initialization ---
# Set the page configuration for better mobile appearance
st.set_page_config(layout="centered", page_title="Streamlit Stopwatch")

# -------------------------------------
# 1. Initialize session state
# -------------------------------------
# Initialize state variables if they don't exist
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0
if "running" not in st.session_state:
    st.session_state.running = False


# -------------------------------------
# 2. Stopwatch control functions (using Streamlit's callback system)
# -------------------------------------
def start_stopwatch():
    """Starts the stopwatch or resumes from a paused state."""
    if not st.session_state.running:
        # Calculate start_time by subtracting elapsed time from current time
        st.session_state.start_time = time.time() - st.session_state.elapsed
        st.session_state.running = True

def stop_stopwatch():
    """Stops the stopwatch and saves the elapsed time."""
    if st.session_state.running:
        # Save the current elapsed time before stopping
        st.session_state.elapsed = time.time() - st.session_state.start_time
        st.session_state.running = False

def reset_stopwatch():
    """Resets the stopwatch to zero."""
    st.session_state.running = False
    st.session_state.elapsed = 0.0
    st.session_state.start_time = None


# -------------------------------------
# 3. Auto-refresh when running
# -------------------------------------
# Only run the autorefresh component if the stopwatch is currently running.
# The interval of 100ms (1/10th of a second) provides a smooth update for the tenths digit.
if st.session_state.running:
    st_autorefresh(interval=100, key="refresh_timer")


# -------------------------------------
# 4. Update elapsed time
# -------------------------------------
# This must run on every rerun *before* formatting the time.
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
# 6. CSS Styling (Updated for Column Layout on Mobile)
# -------------------------------------
# -------------------------------------
# CSS Styling (Updated with nowrap)
# -------------------------------------
st.markdown("""
<style>
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
    
    /* === ADD THIS LINE TO PREVENT LINE BREAKS === */
    white-space: nowrap; 
    /* =========================================== */
}

/* Container for the buttons */
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
    
    /* Change the button layout from row to column on small screens */
    .button-row {
        flex-direction: column; 
        gap: 15px; 
        width: 100%;
    }
    
    /* Ensure Streamlit buttons in the column take full width */
    .stButton>button {
        width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------
# 7. Layout and UI
# -------------------------------------
st.title("⏱️ Simple Streamlit Stopwatch")

# Display the formatted time using the styled div
st.markdown(f"<div class='timer-box'>{formatted_time}</div>", unsafe_allow_html=True)


# Use Streamlit columns to create the button layout.
# This is the idiomatic Streamlit way to group elements.
# The custom CSS with `flex-direction: column` for mobile will handle the responsiveness.
col1, col2, col3 = st.columns(3)

# Use st.button() with the 'button-row' class to trigger the custom CSS
with st.container():
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    
    # -------------------------------------
    # START/PAUSE Button
    # -------------------------------------
    # Use different labels based on state for better UX
    button_label = "Stop" if st.session_state.running else "Start"
    
    # Use a single button with a conditional callback
    if st.button(button_label, use_container_width=True):
        if st.session_state.running:
            stop_stopwatch()
        else:
            start_stopwatch()
            
    # -------------------------------------
    # RESET Button
    # -------------------------------------
    if st.button("Reset", use_container_width=True):
        reset_stopwatch()
        
    st.markdown('</div>', unsafe_allow_html=True)

# Note: The separate columns layout (col1, col2, col3) is usually for positioning. 
# Here, we use a single st.container() and apply the custom CSS to the inner HTML div 
# to manage the flexible layout, which is more robust for switching between row/column.

