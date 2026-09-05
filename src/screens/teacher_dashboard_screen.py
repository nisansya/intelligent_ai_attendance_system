import streamlit as st
from src.ui.base_layout import style_base_layout, style_dashboard_background
from src.components.footer import footer_home

def teacher_dashboard():
    teacher_data= st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data['name']}""")