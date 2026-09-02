import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_home_background

def home_screen():

    header_home()

    style_base_layout()
    style_home_background()

    st.markdown(
        """
        <h3 style="text-align: center; color: #80aafd">Choose your role to continue</h3>
        """,
        unsafe_allow_html=True
    )
    if st.button('👩🏼‍🏫 Teacher'):
        st.session_state['login_type'] = 'Teacher'
        st.rerun()
    
    if st.button('🎓 Student'):
        st.session_state['login_type'] = 'Student'
        st.rerun()

    footer_home()