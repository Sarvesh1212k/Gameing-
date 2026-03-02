import streamlit as st
from auth_page import auth_page
from main_app import main_app
from styles import STYLE


st.set_page_config(
    page_title="🎮 GamePulse - PC & Mobile Analytics",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown(STYLE, unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "show_reset" not in st.session_state:
    st.session_state.show_reset = False
if "selected_game" not in st.session_state:
    st.session_state.selected_game = None

# =========================
# RESTORE LOGIN FROM URL
# =========================
if "auth" in st.query_params and st.query_params["auth"] == "1":
    st.session_state.logged_in = True

if not st.session_state.username:
    user_from_url = st.query_params.get("user")
    if user_from_url:
        st.session_state.username = user_from_url
        st.session_state.logged_in = True


if st.session_state.logged_in:
    main_app()
else:
    auth_page()