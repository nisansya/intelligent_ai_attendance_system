import streamlit as st
from src.ui.base_layout import style_base_layout, teacher_login_background
from src.components.footer import footer_home

def student_dashboard():
    style_base_layout()
    student_data= st.session_state.student_data
    st.header(f"""Welcome, {student_data['name']}""")