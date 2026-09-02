import streamlit as st
from src.ui.base_layout import style_base_layout

def teacher_screen():
    st.header('teacher screen')

    if st.button('Back'):
        st.session_state['login_type']= None