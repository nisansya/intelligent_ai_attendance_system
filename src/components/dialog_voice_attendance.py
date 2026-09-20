import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject, create_attendance
from src.pipelines.voice_pipeline import process_bulk_audio
import pandas as pd
from src.components.dialog_attendance_result import show_attendance_result
from datetime import datetime

@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write("Record audio of students saying I am present. Then AI will recognise the students")
    audio_data= None
    audio_data= st.audio_input('Record classroom audio.')
    if st.button('Analyse audio', width='stretch', type='primary'):
        
        with st.spinner('Processing Audio data'):
            #voice_emb= get_voice_embedding(audio_data.read())
            enrolled_res_v= supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
            enrolled_students= enrolled_res_v.data

            if not enrolled_students:
                st.warning('No students enrolled in this course')
                return

            candidates_dict= {
                s['students']['student_id'] : s['students']['voice_embedding']
                for s in enrolled_students if s['students'].get('voice_embedding')
            }
            if not candidates_dict:
                st.error('No enrollled students have voice profiles registered')
                return
            
            audio_bytes= audio_data.read()  
            best_detected_scores= process_bulk_audio(audio_bytes, candidates_dict)
            results, attendance_to_log= [], []
            current_timestemp= datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            for node in enrolled_students:
                student= node['students']
                score= best_detected_scores.get(student['student_id'], 0.0)
                is_present= bool(score > 0)

                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": str(round(float(score), 2)) if is_present else "-",
                    "Status": "✅ Present" if is_present else "❎ Absent"
                })

                attendance_to_log.append({
                    'student_id' : student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestemp,
                    'is_present': bool(is_present)
                })

            st.session_state.voice_attendance_results= (pd.DataFrame(results), attendance_to_log)

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs= st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)
                