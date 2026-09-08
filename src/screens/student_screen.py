import streamlit as st
from src.ui.base_layout import style_base_layout, student_login_background
from src.components.footer import footer_home
from src.components.header import header_dashboard
from src.database.db import create_student, get_all_students
from src.screens.student_dashboard_screen import student_dashboard
import numpy as np
from PIL import Image
from src.pipelines.face_pipeline import predict_attendance, get_face_embedding, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding


def student_screen():
    
    login_page()
    if "student_data" in st.session_state:
        student_dashboard() 

   # if "show_registration" not in st.session_state:
    #    st.session_state.show_registration= False

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
                show_registration= False
                photo= st.camera_input("Position your face in the frame", key="student_face_camera", label_visibility="collapsed")
                if photo:
                    img= np.array(Image.open(photo))

                    with st.spinner('AI is scanning'):
                        detected, all_ids, num_faces= predict_attendance(img)

                        if num_faces==0:
                            st.warning('Face not found!')
                        if num_faces >1:
                            st.warning('Multiple faces found!')
                        else:
                            if detected:
                                student_id= list(detected.keys())[0]
                                all_students= get_all_students()
                                student= next((s for s in all_students if s['student_id']==student_id), None) 

                                if student:
                                    st.session_state.is_logged_in= True
                                    st.session_state.user_role= 'student'
                                    st.session_state.student_data= student
                                    st.success("Login successful!")
                                    import time
                                    time.sleep(1)
                                    st.rerun()
                            else:
                                st.info('Face not recognized! You might be new student!')
                                show_registration= True
            if show_registration:
                with st.container(key="registration_box", border=True):
                    st.markdown(
                        """
                        <div class="register-title">Register with new Profile</div>
                        """, unsafe_allow_html=True)
            
                    st.markdown(
                        """
                        <div class="input-label">
                            student name
                        </div>
                        """,
                        unsafe_allow_html=True
                    ) 
                    new_name= st.text_input(
                        'new name', 
                        placeholder= 'Enter your name', 
                        label_visibility= 'collapsed'
                    )
                    #st.header('Register new Profile')
                    #new_name= st.text_input('Enter your name', placeholder='E.g. Vanshu')
                    
                    st.markdown(
                        """
                        <div class="voice-enroll-text">
                            Optional: Voice Enrollment
                        </div>
        
                        """,
                        unsafe_allow_html=True
                    )   
                    st.info("Enroll your voice for attendance")

                    audio_data= None

                    try:
                        audio_data= st.audio_input('Record a short phrase like I am present, My name is Vanshu.')
                    except Exception:
                        st.error("Audio Data failed!")

                    col1, col2, col3= st.columns([1,2,1])
                    with col2:
                        button_register= st.button('Create Account')  
                        if button_register:
                            if new_name:
                                with st.spinner("Creating profile.."):
                                    img= np.array(Image.open(photo))
                                    encoding= get_face_embedding(img) 
                                    if encoding:
                                        face_emb= encoding[0].tolist()

                                        voice_emb= None
                                        if audio_data:
                                            voice_emb= get_voice_embedding(audio_data.read())
                                    
                                        response_data= create_student(new_name, face_embedding= face_emb, voice_embedding= voice_emb)
                                        
                                        if response_data:
                                            train_classifier()
                                            st.session_state.is_logged_in= True
                                            st.session_state.user_role= 'student'
                                            st.session_state.student_data= response_data[0]
                                            st.toast(f'Prifle Created! Hi {new_name}!')
                                            import time
                                            time.sleep(1)
                                            st.rerun()
                                    else:
                                        st.error("Couldnt capture your facial features for registrations")
                                            
                            else:
                                st.warning("Please enter your name!")    
                                    

                
            
