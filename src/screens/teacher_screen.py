import streamlit as st
from src.ui.base_layout import style_base_layout, teacher_login_background
from src.components.footer import footer_home
from src.components.header import header_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login_db
from src.screens.teacher_dashboard_screen import teacher_dashboard
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog

def teacher_screen():
    
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
        
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type =='logged_in':
        teacher_login()

    elif st.session_state.teacher_login_type == 'register':
        register_teacher()

def teacher_login():
    teacher_login_background()

    left, right = st.columns([5, 7], gap="small")

    # ================= LEFT SECTION =================
    with left:
        with st.container(key="left_panel"):
            st.markdown(
                """
                <div class="welcome-title">
                    Welcome, Teacher!
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
                <div class="welcome-text">
                    Login to access your dashboard and manage
                    classes & attendance.
                </div>
                """,
                unsafe_allow_html=True
            )

    # ================= RIGHT SECTION =================
    with right:
        with st.container(key="right_panel"):

            st.markdown(
                """
                <div class="login-title">
                    Teacher Login
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="input-label">Teacher ID or Email</div>',
                unsafe_allow_html=True
            )

            teacher_id = st.text_input(
                "teacher_id",
                placeholder="Enter your Teacher ID or Email",
                label_visibility="collapsed"
            )

            st.markdown(
                '<div class="input-label password-label">Password</div>',
                unsafe_allow_html=True
            )

            password = st.text_input(
                "password",
                placeholder="Enter your Password",
                type="password",
                label_visibility="collapsed"
            )
            col1,col2, col3= st.columns([3,3,3])
            with col2:
                login_button = st.button(
                    "Login →",
                    key="login_btn"
                )

            if login_button:
                
                if not teacher_id or not password:
                    st.error("All fields are required to enter.")

                else:
                    teacher= teacher_login_db(teacher_id, password)
                    if teacher:
                        st.session_state.user_role= "teacher"
                        st.session_state.teacher_data= teacher
                        st.session_state.teacher_page= "dashboard"
                        st.session_state.is_logged_in= True
                        st.success("Login successful!")

                        #st.toast("Welcome back!", icon="🎉")
                        import time 
                        time.sleep(1)
                        st.rerun()
                
                    else:
                        st.error("Invalid username and password combo")

                
            st.markdown(
                """
                <div class="divider">
                    <span>OR</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="register-text style="color: blue;">
                    Don't have an account?
                </div>
                """,
                unsafe_allow_html=True
            )

            col1,col2, col3= st.columns([3,3,3])
            with col2: 
                if st.button("Register as Teacher",key="register_btn"):
                    st.session_state.teacher_login_type = "register"

    footer_home()

def dbase_check(teacher_id, teacher_name, password, confirm_password):
    if not teacher_id or not teacher_name or not password:
        return False, "All fields are required to enter."
    if check_teacher_exists(teacher_id):
        return False, "Username already taken"
    if password!= confirm_password:
        return False, "Password doesn't match"

    try:
        create_teacher(teacher_id, password, teacher_name)
        return True, "Successfully Created! Login Now"
    
    except Exception as e:
        return False, "Unexpected Error!"

def register_teacher():
    teacher_login_background()
    left, right= st.columns([5,7], gap=0)
    
    with left:
        with st.container(key="left_panel"):
            st.markdown(
                """
                <div class="welcome-title">Welcome, Teacher!</div>
                <div class="welcome-text">Register to access your dashboard and manage classes & attendance.</div>
                
                """,
                unsafe_allow_html=True
            )

    with right:
        with st.container(key="right_panel"):
            st.markdown(
               """
            <div class="register-title">Teacher Registration</div>
            """, unsafe_allow_html=True)

            st.markdown(
                """
                <div class="input-label">
                   Teacher ID or Email
                </div>
                """,
                unsafe_allow_html=True
            ) 
            teacher_id= st.text_input(
                'teacher id', 
                placeholder= 'Enter your Teacher ID or Email', 
                label_visibility= 'collapsed'
            )
            st.markdown(
                '<div class="input-label">Teacher Name</div>', 
                unsafe_allow_html=True
            ) 
            teacher_name= st.text_input(
                'teacher name', 
                placeholder= 'Enter Name', 
                label_visibility= 'collapsed'
            )
            st.markdown(
                '<div class="input-label password-label"">Password</div>', 
                unsafe_allow_html=True
            )
            password= st.text_input(
                "password1", 
                placeholder= 'Enter your Password', 
                type= 'password', 
                label_visibility= 'collapsed'
            )
            st.markdown(
                '<div class="input-label password-label"">confirm password</div>', 
                unsafe_allow_html=True
            ) 
            confirm_password= st.text_input(
                'confirm_password', 
                placeholder= 'Confirm your Password', 
                type= 'password', 
                label_visibility= 'collapsed'
            )

            col1,col2, col3= st.columns([3,3,3])
            with col2:
                register_button= st.button('Register ->', key= 'register_btn')
            
            if register_button:
                success, message= dbase_check(teacher_id, teacher_name, password, confirm_password)
                if success:
                    st.success(message)
                    import time
                    time.sleep(2)

                    st.session_state.teacher_login_type="logged_in"
                    st.rerun()

                else:
                    st.error(message)

            st.markdown(
                    "</div>", unsafe_allow_html=True
                    ) 

            