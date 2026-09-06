import streamlit as st
from src.ui.base_layout import style_base_layout, student_login_background
from src.components.footer import footer_home
from src.components.header import header_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login_db
from src.screens.teacher_dashboard_screen import teacher_dashboard
import numpy as np
from PIL import Image




def student_screen():
    
    login_page()

def login_page():
    student_login_background()
    
    left, right = st.columns([5, 7], gap="small")

    with left:
        with st.container(key="left_panel"):
            st.markdown(
                r"""
                <div style="font-size:20px; color: black;">
                    🎓 Student Portal
                </div>
                
                <div class="welcome-title">
                    Welcome, Students!
                </div>
                
                <div class="welcome-text">
                    Access your account securely using Face ID
                </div>

                """,
                unsafe_allow_html=True
            )
            with st.container(key="picture", border=True):
    
                col1,col2,col3= st.columns([1,2,1])
                with col2:
                    st.image("assets/face-recog-logo.jpg", width=220)

            st.markdown(
                """
                
                <div style="margin-top: 100px; font-size: 18px; text-align: center; color: #40516e;">
                    🔐 Your data is secure with us
                </div>
                
                <div style="margin-top: 15px; text-align: center; color:#60708c; line-height: 1.5;">
                    We use secure face recognition technology for authentication.
                </div>
                
                """,
                unsafe_allow_html=True
            )

    with right:
        with st.container(key="right_panel"):
            st.markdown(
                """
                <div class="login-title"> Student-login</div>
                <div class="login-text"> Login using Face ID to continue</div>
                """,
                unsafe_allow_html=True
            )
            with st.container(key="face_box", border=True):

                photo= st.camera_input("Position your face in the frame", key="student_face_camera", label_visibility="collapsed")
                if photo:
                    np.array(Image.open(photo))

                    
                st.markdown(
                    """
                    <div class="face-status">
                        <span class="green-dot">.</span>
                            Face Detected
                    </div>

                    <div style="margin-top:8px; color: #60708c;">
                        Position your face in the frame
                    </div>

                    """,
                    unsafe_allow_html=True
                )

            col1, col2, col3= st.columns([3,3,3])
            with col2:    
                button_login_face= st.button("Login with Face ID", key="face_login")
            if button_login_face:
                st.success("Face detected! Logging in...") 

            
