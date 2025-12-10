# -------------------------------------
# MOBILE-PROOF HORIZONTAL BUTTON ROW
# -------------------------------------
st.markdown("""
<style>
.button-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;
    margin-top: 30px;
}

.btn-custom {
    background-color: #333;
    color: white;
    border: 1px solid #555;
    padding: 12px 24px;
    border-radius: 10px;
    font-size: 18px;
    cursor: pointer;
}

.btn-custom:active {
    background-color: #444;
}
</style>

<div class="button-row">
    <form action="#" method="post">
        <button class="btn-custom" name="action" value="start">Start</button>
    </form>
    <form action="#" method="post">
        <button class="btn-custom" name="action" value="stop">Stop</button>
    </form>
    <form action="#" method="post">
        <button class="btn-custom" name="action" value="reset">Reset</button>
    </form>
</div>
""", unsafe_allow_html=True)
