import streamlit as st
from src.ui.base_layout import style_base_layout,  student_dashboard_background
from src.components.footer import footer_home
from src.components.dialog_enroll_subject import enroll_subject_dialog
from src.database.db import get_student_subjects, get_subject_attendance, get_total_student_subjects, get_total_attendance

def student_dashboard():
    student_data= st.session_state.student_data
    
    student_dashboard_background()


    if "page" not in st.session_state:
        st.session_state.page="Home"

    if "active_section" not in st.session_state:
        st.session_state.active_section= None

                

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-title">
                🎓 Student Dashboard
            </div>
        
            """,
            unsafe_allow_html=True
        )

        if st.button("🏠 Home", type='secondary', width='stretch'):
            st.session_state.page= "Home"

        if st.button("📓 My Subjects", type='secondary', width='stretch'):
            st.session_state.page= "Subjects"

        if st.button("👤 Profile", type='secondary', width='stretch'):
            st.session_state.page= "Profile"

        st.markdown(" <br><br><br><br><br>", unsafe_allow_html=True)

        if st.button("-> Logout", type='primary', width='stretch'):
            st.session_state.page= "Logout"
            st.rerun()

    if st.session_state.page == "Subjects":
            student_tab_subjects()
        

    if st.session_state.page=="Home":
        with st.container(key="right_panel"):
        
            st.markdown(
                f"""
                <div class="profile"> 
                    👤 Ms. {student_data['name']} 
                </div>

                <div class="main-title"> 
                    Welcome, Student!
                </div>

                <div class="subtitle">
                    Here's your attendance overview. 
                </div>
                """,
                unsafe_allow_html=True
            )

            col1,col2,col3= st.columns(3)

            with col1:
                with st.container(key="card_box1"):
                    st.markdown(
                        """
                        <div class="card-icon">📚<div>

                        <div class="card-title">
                            Subjects
                        </div>
                    
                        """,
                        unsafe_allow_html=True
                    )
                    total_subjects= get_total_student_subjects(student_data['student_id'])
                    st.markdown(f'<div class="card-text">{total_subjects}</div>', unsafe_allow_html=True)
                    #st.subheader(total_subjects)
                        
            with col2:
                with st.container(key="card_box2"):
                    st.markdown(
                        """
                        <div class="card-icon">📊<div>

                        <div class="card-title">
                            Overall Attendance
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    total_attendance= get_total_attendance(student_data['student_id'])
                    st.markdown(f'<div class="card-text">{total_attendance}</div>', unsafe_allow_html=True)
                    #st.subheader("Total lecture attended by you: {total_attendance}")

            # with col3:
            #     with st.container(key="card record-card"):
            #         st.markdown(
            #             """
            #             <div class="card-icon">📄<div>

            #             <div class="card-title">
            #                 View Attendance Records
            #             </div>

            #             <div class="card-text">
            #                 Check past attendance details.
            #             </div>
            #             """,
            #             unsafe_allow_html=True
            #         )

            if st.button("➕ Enroll in Subject", key="enrollsubject", type="primary", width='stretch'):
                st.session_state.active_section= "enroll in subject" 
                st.rerun()

            if st.button("📷 Mark Attendance", key="markattendance", type="primary", width='stretch'):
                st.session_state.active_section= "mark attendance" 
                st.rerun() 

            if st.session_state.active_section == "enroll in subject":
                st.markdown(
                    "<div style='height: 40px;'></div>",
                    unsafe_allow_html=True
                )
                student_tab_enroll_subject()

            
                

            # elif st.session_state.active_section == "Subjects":
            #     st.markdown(
            #         "<div style='height: 30px;'></div>",
            #         unsafe_allow_html=True
            #     )
            #     teacher_tab_manage_subjects()

            # if st.session_state.active_section == "Attendance Records":
            #     teacher_tab_attendance_records()


def teacher_tab_take_attendance():
    st.header("Take AI Attendance")

def student_tab_enroll_subject():   

    
    student_id= st.session_state.student_data['student_id'] 
    enroll_subject_dialog(student_id)
    

    # List all subjects
    # subjects= get_student_subjects(student_id) 
    
    # if subjects:
    #     for sub in subjects:
    #         subject_name= sub['subjects']['name']
    #         teacher_name= sub['subjects']['teachers']['name']
    #         logs= get_subject_attendance(student_id, sub['subject_id'])
            
    #         with st.container(key="my_subjects"):
    #             st.info(subject_name)
    #             st.markdown(
    #                 f"""
    #                 <div class="my_sub_subheading1'>
    #                     {subject_name}
    #                 </div>
    #                 """,
    #                 unsafe_allow_html=True
    #             )
    #             col1, col2= st.columns(2)
    #             with col1:
    #                 st.info(teacher_name)
    #                 st.markdown(
    #                 f"""
    #                 <div class="my_sub_subheading2'>
    #                     Teacher : {teacher_name}
    #                 </div>
    #                 """, 
    #                 unsafe_allow_html= True
    #                 )

    #             with col2:
    #                 st.markdown(
    #                 f"""
    #                 <div class="my_attendance'>
    #                     Total attended lecture : {logs}
    #                 </div>
    #                 """, 
    #                 unsafe_allow_html= True
    #                 )

    # else:
    #     st.info("No subjects enrolled")
            # stats= [
            #     ("👥", "students", sub['total_students']),
            #     ("⌚", "classes", sub['total_classes']),
            # ]

        # def share_btn():
        #     if st.button(f"Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", icon=":material/share:"):
        #         share_subject_dialog(sub['name'], sub['subject_code'])
        #     st.space()

        # subject_card(
        #     name= sub['name'],
        #     code= sub['subject_code'],
        #     section= sub['section'],
        #     stats= stats,
        #     footer_callback= share_btn
        # )

        
                    
def student_tab_subjects():
    student_dashboard_background()
    with st.container(key='right_panel'):
        student_id= st.session_state.student_data['student_id'] 
        st.markdown(
            """
            <h1 class="title" style= "color: black;">📙 My Subjects</h1>
            <p class="titlepara" style= "color: black;">
                <b>Subjects you are currently enrolled in.</b> 
            </p>
            """,unsafe_allow_html=True
        )
        subjects= get_student_subjects(student_id)
        if not subjects:
            st.info('You have not enrolled in any subject yet.')

        else:
            for subject in subjects:
                subject_name= subject['subjects']['name']
                subject_code= subject['subjects']['subject_code']
                teacher_name= subject['subjects']['teachers']['name']
                logs= get_subject_attendance(student_id, subject['subject_id'])
                st.markdown(
                    f"""
                    <div style="
                        background-color: gray;
                        padding: 20px;
                        margin-bottom: 15px;
                        border-radius: 10px;
                        border: 2px solid #e5e7eb';
                        ">
                        <h3 style= "margin-top: 0;">
                            📖 {subject_name}
                        </h3>
                        <p>
                            <b> Teacher: </b> {teacher_name}
                        </p>
                        <p>
                            <b> Subject Code: </b> {subject_code}
                        </p>
                        <p>
                            <b> Total attended lecture: </b> {logs}
                        </p>
                    </div>
                        
                """,
                unsafe_allow_html=True
                )




                

                    


        