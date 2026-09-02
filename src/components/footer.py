import streamlit as st

def footer_home():
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 0; position: fixed; z-index: 9999; bottom: 0; left:0; width: 100%;">
            <p id="footer-text">🔐 Secure & Encrypted Connection | ©️ 2026 Your App </p>
            <p id="footer-text"> Created with ❤️ by Nisansya</p>
        </div>
    """, unsafe_allow_html= True )