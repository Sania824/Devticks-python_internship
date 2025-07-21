from database import add_user,check_user
import streamlit as st

def register():
    st.title("New Admin Registration")
    with st.form("register_form"):
         username = st.text_input("Enter Username")
         password = st.text_input("Choose Password", type="password")
         confirm_pass = st.text_input("Confirm Password", type="password")

         if st.form_submit_button("Register"):
             if password != confirm_pass:
                 st.error("Passwords don't match!")
             else:
                 if add_user(username, password):  # From database.py
                     st.success("Registration successful! Please login")
                     st.session_state.show_login = True
                     st.rerun()
                 else:
                     st.error("Username already exists")


def login():
    st.title("🔑 Login to HMS")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Login"):
            user = check_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.rerun()  # Refresh to show main app
            else:
                st.error("Invalid credentials")


def logout():
    """Clears login session"""
    st.session_state.logged_in = False
    st.success("Logged out successfully!")
    st.rerun()