import mysql.connector
import hashlib
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        #   host="localhost",
        # user="root",
        # password="root",
        # database="user_db",
        # port=3306
         host="sql12.freesqldatabase.com",
        user="sql12818533t",
        password="Yt6FcCCRRf",
        database="sql12818533",
        port=3306
    )

def init_user_data(username):
    st.session_state["username"] = username
    

def register_user(username, email, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username=%s OR email=%s", (username, email))
    if cur.fetchone():
        conn.close()
        return False, "Username or Email already exists"

    hashed = hashlib.sha256(password.encode()).hexdigest()
    cur.execute(
        "INSERT INTO users (username,email,password) VALUES (%s,%s,%s)",
        (username, email, hashed)
    )
    conn.commit()
    conn.close()
    return True, "Registration successful"

def login_user(user, password):
    conn = get_connection()
    cur = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()

    cur.execute(
        "SELECT username FROM users WHERE (username=%s OR email=%s) AND password=%s",
        (user, user, hashed)
    )
    row = cur.fetchone()
    conn.close()

    if row:
        return True, "Login successful", row[0]
    return False, "Invalid credentials", None

def reset_password(email, new_password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE email=%s", (email,))
    if not cur.fetchone():
        conn.close()
        return False, "Email not registered"

    hashed = hashlib.sha256(new_password.encode()).hexdigest()
    cur.execute(
        "UPDATE users SET password=%s WHERE email=%s",
        (hashed, email)
    )
    conn.commit()
    conn.close()
    return True, "Password updated"
