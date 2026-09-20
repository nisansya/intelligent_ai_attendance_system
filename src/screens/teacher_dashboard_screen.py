import streamlit as st
from src.ui.base_layout import style_base_layout, teacher_dashboard_background
from src.components.footer import footer_home
from src.components.dialog_create_subject import create_subject_dialog 
from src.components.subject_card import subject_card
from src.database.db import get_teacher_subjects, get_attendance_for_teacher
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photo_dialog
from src.pipelines.face_pipeline import predict_attendance
from src.database.config import supabase
from datetime import datetime
from src.components.dialog_attendance_result import attendance_result_dialog
import numpy as np
import pandas as pd
from src.components.dialog_add_photo import add_photo_dialog
from src.pipelines.voice_pipeline import get_voice_embedding, process_bulk_audio
from src.components.dialog_voice_attendance import voice_attendance_dialog


def teacher_dashboard():
    teacher_dashboard_background()
    teacher_data= st.session_state.teacher_data

    if "page" not in st.session_state:
        st.session_state.page="home"

    if "active_section" not in st.session_state:
        st.session_state.active_section= None

     
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
            st.session_state.page= "Subjects"
            

        if st.button("📄 Attendance Records", type='secondary', width='stretch'):
            st.session_state.page= "Attendance Records"

        st.markdown(" <br><br><br><br><br>", unsafe_allow_html=True)

        if st.button("-> Logout", type='primary', width='stretch'):
            st.session_state.clear()
            st.switch_page("app.py")

    with st.container(key="right_panel"):
        
            st.markdown(
                f"""
                <div class="profile"> 
                    👤 {teacher_data['name']} 
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
            if st.session_state.page=='home':
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
                            st.session_state.page= "Take Attendance"
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
                            st.session_state.page= "Subjects"
                            
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
                            st.session_state.page= "Attendance Records" 
                            st.rerun()

            if st.session_state.page == "Take Attendance":
                teacher_tab_take_attendance()
                
            if st.session_state.page == "Subjects":
                st.markdown(
                    "<div style='height: 30px;'></div>",
                    unsafe_allow_html=True
                )
                teacher_tab_manage_subjects()
            
            if st.session_state.page == "Attendance Records":
                teacher_tab_attendance_records()

   
    
def teacher_tab_take_attendance():
    
    teacher_id= st.session_state.teacher_data['teacher_id']
    st.header("Take AI Attendance")

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images=[]

    subjects= get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You have not created any subject yet! Please create one to begin!')
        return 

    subject_options= {f"{s['name']}  -{s['subject_code']}": s['subject_id'] for s in subjects} 

    col1, col2= st.columns([3,1], vertical_alignment='bottom')
    with col1:
        selected_subject_label= st.selectbox('Select Subject', options=list(subject_options.keys()))

    with col2:   
        if st.button('Add Photos', type='primary', width= 'stretch'):
            add_photo_dialog()

    selected_subject_id= subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols= st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width='stretch', caption=f'Photo{idx+1}')

    has_photos= bool(st.session_state.attendance_images)
    
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('Clear all photos', width='stretch', type='primary', disabled=not has_photos):
            st.session_state.attendance_images= []
            st.rerun() 

    with c2:
        
        if st.button('Analyse Images', width='stretch', type='primary', disabled=not has_photos):
            with st.spinner('Deep scanning classroom photos...'):
                all_detected_ids= {}

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np= np.array(img.convert('RGB'))

                    detected, _, _ = predict_attendance(img_np)

                    if detected:
                        for sid in detected.keys():
                            student_id= int(sid)

                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

                enrolled_res= supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
                enrolled_students= enrolled_res.data
                

                if not enrolled_students:
                    st.warning('No students enrolled in this course')

                else:
                    results, attendance_to_log= [], []

                    current_timestemp= datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student= node['students']
                        sources= all_detected_ids.get(int(student['student_id']), [])
                        is_present= len(sources) > 0

                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "✅ Present" if is_present else "❎ Absent"
                        })

                        attendance_to_log.append({
                            'student_id' : student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestemp,
                            'is_present': bool(is_present) 
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('Use Voice Attandance', type='primary', width='stretch'):
            st.session_state.show_voice= True
            audio_data= None

        if st.session_state.get("show_voice", False):
            voice_attendance_dialog(selected_subject_id)
            


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
    teacher_id= st.session_state.teacher_data['teacher_id'] 
    records= get_attendance_for_teacher(teacher_id)

    if not records:
        return 

    data= []

    for r in records:
        ts= r.get('timestamp')

        data.append({
            "ts_group" : ts.split(".")[0] if ts else None,
            "Time" : datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
            "Subject" : r['subjects']['name'],
            "Subject Code" : r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })

    df= pd.DataFrame(data)



    summary= (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(
            Present_count= ('is_present', 'sum'),
            Total_count= ('is_present', 'count') 
        )
    ).reset_index()

    summary['Attendance Stats'] = (
        "✅" + summary['Present_count'].astype(str) + " /"
        +summary['Total_count'].astype(str) + " Students"
    )

    display_df= (summary.sort_values(by='ts_group', ascending= False)
                 [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
                )

    st.dataframe(display_df, width='stretch', hide_index= True)




                

                    


        