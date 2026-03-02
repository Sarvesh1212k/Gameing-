import streamlit as st
import re

from auth import (
    login_user,
    register_user,
    reset_password,
    init_user_data
)

def auth_page():

    st.markdown('<div class="auth-wrapper">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center'>🔐 GamePulse Login / Register</h2>", unsafe_allow_html=True)
  
   
    # ================= RESET PASSWORD =================
    if st.session_state.show_reset:
        st.subheader("🔁 Reset Password")

        email = st.text_input("Registered Email", key="reset_email")
        new_pass = st.text_input(
            "New Password",
            type="password",
            key="reset_new_password"
        )

        if st.button("Reset Password", key="reset_btn"):
            ok, msg = reset_password(email, new_pass)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

        if st.button("⬅ Back to Login", key="back_to_login"):
            st.session_state.show_reset = False
            st.rerun()

        return  # ⛔ stop here, don't render login tabs

    # ================= LOGIN / REGISTER =================
    tab1, tab2 = st.tabs(["Login", "Register"])

    # ---------------- LOGIN ----------------
    with tab1:
        user = st.text_input("Username / Email", key="login_user")
        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login", key="login_btn"):
            ok, msg, username = login_user(user, password)
            if ok:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.query_params["user"] = username
                st.query_params["auth"] = "1"
                init_user_data(username)
                st.rerun()
            else:
                st.error(msg)

        if st.button("Forgot Password?", key="forgot_password"):
            st.session_state.show_reset = True
            st.rerun()

    # ---------------- REGISTER ----------------
    with tab2:
        username = st.text_input("Username", key="reg_username")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input(
            "Password",
            type="password",
            key="reg_password"
        )

        if st.button("Register", key="register_btn"):
            if not username or not email or not password:
                st.error("❌ All fields are required")
            elif not email.endswith("@gmail.com"):
                st.error("❌ Email must end with @gmail.com")
            elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                st.error("❌ Password must contain special symbol")
            elif len(password) < 4:
                st.error("❌ Password must be at least 4 characters")
            else:
                ok, msg = register_user(username, email, password)
                if ok:
                    st.success("✅ Registration successful. You can login now.")
                else:
                    st.error(msg)