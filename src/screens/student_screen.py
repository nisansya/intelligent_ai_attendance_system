import streamlit as st
from src.ui.base_layout import style_base_layout, style_dashboard_background
from src.components.footer import footer_home
from src.components.header import header_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login_db
from src.screens.teacher_dashboard_screen import teacher_dashboard


def student_screen():
    pass