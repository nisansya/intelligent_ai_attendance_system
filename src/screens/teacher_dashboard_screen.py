import streamlit as st
from src.ui.base_layout import style_base_layout, teacher_dashboard_background
from src.components.footer import footer_home
from src.components.dialog_create_subject import create_subject_dialog 
from src.components.subject_card import subject_card
from src.database.db import get_teacher_subjects
from src.components.dialog_share_subject import share_subject_dialog


def teacher_dashboard():
    teacher_dashboard_background()
    teacher_data= st.session_state.teacher_data

    if "page" not in st.session_state:
        st.session_state.page="home"

    if "active_section" not in st.session_state:
        st.session_state.active_section= None

    #st.header(f"""Welcome, {teacher_data['name']}""") 
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-title">
                🎓 Teacher Dashboard
            </div>
        
            """,
            unsafe_allow_html=True
        )

        if st.button("🏠 Home", type='secondary', width='stretch'):
            st.session_state.page= "home"

        if st.button("👥 Take Attendance", type='secondary', width='stretch'):
            st.session_state.page= "Take Attendance"

        if st.button("📓 Manage Subjects", type='secondary', width='stretch'):
            st.session_state.page= "Manage Subjects"

        if st.button("📄 Attendance Records", type='secondary', width='stretch'):
            st.session_state.page= "Attendance Records"

        st.markdown(" <br><br><br><br><br>", unsafe_allow_html=True)

        if st.button("-> Logout", type='primary', width='stretch'):
            st.session_state.page= "logout"

    if st.session_state.page=="home":
        with st.container(key="right_panel"):
        
            st.markdown(
                f"""
                <div class="profile"> 
                    👤 Ms. {teacher_data['name']} 
                </div>

                <div class="main-title"> 
                    Welcome, Teacher!
                </div>

                <div class="subtitle">
                    Manage your classes and attendance easily. 
                </div>
                """,
                unsafe_allow_html=True
            )

            col1,col2,col3= st.columns(3)

            with col1:
                with st.container(key="card attendance-card"):
                    st.markdown(
                        """
                        <div class="card-icon">👥<div>

                        <div class="card-title">
                            Take Attendance
                        </div>

                        <div class="card-text">
                            Mark attendance for your class.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button("Take Attendance ->", key="home_attendance"):
                        st.session_state.active_section= "Attendance"
                        st.rerun()

            with col2:
                with st.container(key="card subject-card"):
                    st.markdown(
                        """
                        <div class="card-icon">📓<div>

                        <div class="card-title">
                            Manage Subjects
                        </div>

                        <div class="card-text">
                            Add, edit or view subjects.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button("Manage Subjects ->", key="home_subject"):
                        st.session_state.active_section= "Subjects"
                        
                        st.rerun()

            with col3:
                with st.container(key="card record-card"):
                    st.markdown(
                        """
                        <div class="card-icon">📄<div>

                        <div class="card-title">
                            View Attendance Records
                        </div>

                        <div class="card-text">
                            Check past attendance details.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button("View Records ->", key="home_records"):
                        st.session_state.active_section= "Attendance Records" 
                        st.rerun()
            if st.session_state.active_section == "Attendance":
                teacher_tab_take_attendance()

            elif st.session_state.active_section == "Subjects":
                st.markdown(
                    "<div style='height: 30px;'></div>",
                    unsafe_allow_html=True
                )
                teacher_tab_manage_subjects()

            if st.session_state.active_section == "Attendance Records":
                teacher_tab_attendance_records()


def teacher_tab_take_attendance():
    st.header("Take AI Attendance")

def teacher_tab_manage_subjects():

    
    teacher_id= st.session_state.teacher_data['teacher_id'] 
    col1, col2= st.columns(2)

    with col1:
        st.header("Manage Subjects", width='stretch') 

    with col2:
        if st.button('Create New subject', width='stretch'):
            create_subject_dialog(teacher_id)

    # List all subjects
    subjects= get_teacher_subjects(teacher_id) 
    if subjects:
        for sub in subjects:
            stats= [
                ("👥", "students", sub['total_students']),
                ("⌚", "classes", sub['total_classes']),
            ]

        def share_btn():
            if st.button(f"Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", icon=":material/share:"):
                share_subject_dialog(sub['name'], sub['subject_code'])
            st.space()

        subject_card(
            name= sub['name'],
            code= sub['subject_code'],
            section= sub['section'],
            stats= stats,
            footer_callback= share_btn
        )

    
                    
def teacher_tab_attendance_records():
    st.header('Attendance Record')


                

                    


        