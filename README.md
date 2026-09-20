# Intelligent AI Attendance System – Face & Voice Based

A secure, AI-powered attendance automation system that marks subject-wise attendance using Face and Voice biometrics.

**Problem it solves:** Manual attendance is time-consuming and proxy attendance is common. This system automates it using a single classroom photo + voice verification.

---

## System Overview

The application has two roles with separate access.

### 1. Teacher Module
Teachers can Register/Login to the system.

**- Take Attendance (Subject-Wise)**
  To take attendance, teacher first selects a particular subject. After that, attendance can be taken in two ways:
    * **Classroom Photo:** Upload one group photo of the classroom. System detects all faces and marks attendance.
    * **Voice:** Uses voice recognition to verify students.

**- Manage Subjects**
  Teacher can create new subjects, edit existing subjects and view all subjects.

**- Attendance Records**
  All student records are displayed according to the subject. For example, in one subject how many number of students are present, absent and total strength. The data is filterable by subject and date.

### 2. Student Module
Students can Register/Login via their photo and voice. This photo and voice will be used to scan for attendance.

**- Subject Enrollment**
  Student can enroll in subjects created by teachers.

**- Dashboard**
  Student can see in how many subjects they are enrolled and how many attendance are there in each enrolled subject.
  Example: Total Enrolled: 5 | DBMS: 14/16 | OS: 10/12

---

## Technical Implementation

**Face Recognition Pipeline:**
- `dlib` for face detection from classroom images.
- `face_recognition` model for 128-dimensional face embeddings.
- `SVC (Support Vector Classifier)` trained on student embeddings for multi-face classification. SVC is used because it performs better than simple distance matching for group photos.

**Voice Recognition Pipeline:**
- `Librosa` for audio preprocessing and MFCC feature extraction.
- `Resemblyzer` for generating 256-d speaker embeddings and voice verification.

**Database:**
All embeddings and records are stored on `Supabase` – including student profiles, subject mappings and attendance logs.

## Tech Stack
`Python | Streamlit | dlib | face_recognition | SVC | Resemblyzer | Librosa | OpenCV | Supabase`

## Supabase Tables
- `teachers (id, name, email)`
- `students (id, roll_no, name, face_embedding, voice_embedding)`
- `subjects (id, subject_code, subject_name, teacher_id)`
- `student_subjects (student_id, subject_id)`
- `attendance_records (student_id, subject_id, date, status)`

### 🚀 Live Demo: [Click Here to Test the App](https://iaias-main.streamlit.app/)

> No installation needed. Open the link and test as Teacher or Student.


