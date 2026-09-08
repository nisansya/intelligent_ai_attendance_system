import streamlit as st

def style_home_background():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #FFEDD5 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def teacher_login_background():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Playfair:ital,opsz,wght@0,5..1200,300..900;1,5..1200,300..900&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');

        /* hide top bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 30px !important;
            padding-left: 30px !important;
            padding-right: 30px !important;
            max-width: None !important;
            margin:auto;
            background-color: #c0d3fb;
        }

        /* ================= LEFT PANEL ================= */

            .st-key-left_panel {
                background-color: #dae6fe !important;
                min-height: 800px !important;
                padding: 45px 40px !important;
                border-radius: 18px 0px 0px 18px !important;
                box-sizing: border-box !important;
            }


            /* ================= RIGHT PANEL ================= */

            .st-key-right_panel {
                background-color: white !important;
                min-height: 800px !important;
                padding: 50px 45px !important;
                border-radius: 0px 18px 18px 0px !important;
                box-sizing: border-box !important;
            }


            /* ================= WELCOME TEXT ================= */

            .welcome-title {
                font-size: 36px !important;
                font-weight: 700 !important;
                color: #102a56 !important;
                font-family: 'Oswald', sans-serif !important;
                margin-top: 10px !important;
                margin-bottom: 10px !important;
                text-align: center !important;
            }

            .welcome-text {
                font-size: 18px !important;
                line-height: 1.6 !important;
                color: #52627a !important;
                font-family: 'Outfit', sans-serif !important;
                max-width: 430px !important;
                margin: auto !important;
                text-align: center !important;
            }


            /* ================= LOGIN TITLE ================= */

            .login-title {
                font-size: 38px !important;
                font-weight: 700 !important;
                color: #17233c !important;
                font-family: 'Oswald', sans-serif !important;
                margin-bottom: 35px !important;
            }


            /* ================= INPUT LABEL ================= */

            .input-label {
                font-size: 14px !important;
                font-weight: 600 !important;
                color: #33415c !important;
                font-family: 'Outfit', sans-serif !important;
                margin-bottom: 7px !important;
            }

            .password-label {
                margin-top: 18px !important;
            }


            /* ================= INPUT BOX ================= */

            div[data-baseweb="input"] {
                border-radius: 9px !important;
            }

            div[data-baseweb="input"] > div {
                border: 1px solid #d7deea !important;
                border-radius: 9px !important;
                min-height: 48px !important;
            }


            /* ================= BUTTON ================= */

            .stButton button {
                background-color: #5990ff !important;
                color: white !important;
                border-radius: 9px !important;
                width: 230px !important;
                height: 50px !important;
                border: none !important;
                font-size: 16px !important;
                font-weight: 600 !important;
                margin-top: 15px !important;
                align-items: center !important;
            }


            /* ================= DIVIDER ================= */

            .divider {
                display: flex !important;
                align-items: center !important;
                text-align: center !important;
                margin: 28px 0px !important;
                color: #8b96a8 !important;
                font-size: 14px !important;
            }

            .divider::before,
            .divider::after {
                content: '' !important;
                flex: 1 !important;
                height: 1px !important;
                background: #e1e5eb !important;
            }

            .divider span {
                padding: 0 15px !important;
            }


            /* ================= REGISTER TEXT ================= */

            .register-title {
                font-size: 38px !important;
                font-weight: 700 !important;
                color: #17233c !important;
                font-family: 'Oswald', sans-serif !important;
                margin-bottom: 35px !important;
            }
            
        </style>
                """,
                unsafe_allow_html=True
    )

def teacher_dashboard_background():

    st.set_page_config(
        page_title="Teacher Dashboard",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state= "expanded"
    )

    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Playfair:ital,opsz,wght@0,5..1200,300..900;1,5..1200,300..900&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');

        /* hide top bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden !important;
        }

        .block-container {
            padding-top: 30px !important;
            padding-left: 30px !important;
            padding-right: 30px !important;
            max-width: None !important;
            margin:auto;
            background-color: #c0d3fb;
        }

        section[data-testid="stSidebar"]{
            background-color: #f0f8ff !important;
            border-right: 1px solid #dce6f5 !important;
        }

        /* Sidebar title */
        .sidebar-title {
            font-size: 22px;
            font-weight: 700;
            color: #17365d;
            margin-bottom: 30px;
        }

        .st-key-right_panel {
            background-color: white !important;
            min-height: 800px !important;
            padding: 35px 30px !important;
            border-radius: 0px 18px 18px 0px !important;
            box-sizing: border-box !important;
        }

        /* Main heading */
        .main-title {
            font-size: 38px !important;
            font-weight: 700 !important;
            color: #142d52 !important;
            margin-bottom: 5px !important;
        }

        .subtitle {
            font-size: 18px !important;
            color: #60728f !important;
            margin-bottom: 30px !important;
        }

        /* Profile */
        .profile {
            text-align: right !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            color: #17365d !important;
            margin-bottom: 20px !important;
        }

        /* Cards */
        .card {
            padding: 25px !important;
            border-radius: 12px !important;
            min-height: 170px !important;
            border: 1px solid #dbe7f5 !important;
            margin-bottom: 20px !important;
        }

        .attendance-card {
            background-color: #edf6ff !important;
        }

        .subject-card {
            background-color: #eefbf5 !important;
        }

        .record-card {
            background-color: #f5f0ff !important;
        }

        .card-icon {
            font-size: 35px;
            margin-bottom: 10px;
        }

        .card-title {
            font-size: 21px;
            font-weight: 700;
            color: #142d52;
            margin-bottom: 8px;
        }

        .card-text {
            font-size: 15px;
            color: #60728f;
        }

        /* Section */
        .section-box {
            background-color: white;
            border: 1px solid #dbe7f5;
            border-radius: 12px;
            padding: 25px;
            margin-top: 10px;
        }

        .section-title {
            font-size: 24px;
            font-weight: 700;
            color: #142d52;
            margin-bottom: 20px;
        }

        /* Buttons */
        .stButton > button {
            border-radius: 8px !important;
            border: none !important;
            background-color: #287bea !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 10px 18px !important;
        }

        .stButton > button:hover {
            background-color: #1769d1 !important;
            color: white !important;
        }

        /* Sidebar buttons */
        section[data-testid="stSidebar"] .stButton > button {
            width: 100% !important;
            background-color: #287bea !important;
            color: white !important;
            text-align: left !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 12px !important;
            font-size: 16px !important;
        }
        
        
        button p{
            color: blue;
        }
        section[data-testid="stSidebar"] .stButton > button:hover {
            background-color: #dceaff !important;
            color: #1769d1 !important;
        }

        div[data-testid="stMain"] .stButton >button,
        div[data-testid="stMain"] .stButton >button p {
            color: white !important;
            
        }

        section[data-testid="stSidebar"] .stButton> button,
        section[data-testid="stSidebar"] .stButton> button p,
        section[data-testid="stSidebar"] .stButton> button span,
        section[data-testid="stSidebar"] .stButton> button div {
            color: #0d47a1;
        }

        </style>

        """,
        unsafe_allow_html=True
    )

def student_login_background():
    

    st.set_page_config(
        page_title="Student Login",
        page_icon="🎓",
        layout="wide"
    )

    st.markdown(
        """
        <style>
                        
             /* Import Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Playfair:ital,opsz,wght@0,5..1200,300..900;1,5..1200,300..900&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');
            
            /* hide top bar of streamlit */
            #MainMenu, footer, header {
                visibility: hidden;
            }

             /* Remove Streamlit default spacing */
            .block-container {
                padding-top: 30px !important;
                padding-left: 20px !important;
                padding-right: 20px !important;
                max-width: None !important;
                margin:auto;
                background-color: #1a2b4c;
            }

            /* ================= LEFT PANEL ================= */
            
            .st-key-left_panel {
                background-color: #eef5ff;
                min-height: 550px;
                padding: 30px 20px;
                border-radius: 30px 0px 0px 30px;
                text-align: center;
            }


            /* ================= RIGHT PANEL ================= */

            .st-key-right_panel {
                background-color: #c0d3fb;
                min-height: 800px;
                padding: 35px 30px;
                border-radius: 0px 30px 30px 0px;
                border: 1px solid #e5eaf2;
                text-align: center;
            }

            /* Titles */
            .welcome-title {
                font-size: 40px;
                font-weight: 700;
                text-align: center !important;
                font-family: 'Oswald', sans-serif !important;
                color: #102a56;
                margin-top: 80px;
            }

            .welcome-text {
                font-size: 20px;
                text-align: center !important;
                font-family: 'Outfit', sans-serif !important;
                color: #52627a;
                line-height: 1.6;
                margin-top: 20px;
            }

            .login-title {
                font-size: 38px;
                font-weight: 700;
                text-align: center !important;
                font-family: 'Oswald', sans-serif !important;
                color: #17233c;
                margin-bottom: 8px;
            }

            .login-text {
                color: #60708c;
                font-size: 17px;
                text-align: center !important;
                font-family: 'Outfit', sans-serif !important;
                margin-bottom: 25px;
            }

            /* Face area */
            .st-key-face_box {
                background-color: #1a2b4c;
                border-radius: 15px;
                padding: 20px;
                margin: 0 auto;
                max-width: 380px;
            }

            .face-circle {
                width: 180px;
                height: 180px;
                border-radius: 50%;
                border: 6px solid #5990ff;
                margin: auto;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 75px;
                background-color: white;
            }

            .face-status {
                margin-top: 20px;
                font-size: 16px;
                font-family: 'Outfit', sans-serif !important;
                color: #40516e;
                text-align: center !important;
            }

            

            .register-title {
                font-size: 38px !important;
                font-weight: 700 !important;
                text-align: center !important;
                font-family: 'Oswald', sans-serif !important;
                color: #17233c !important;
                margin-bottom: 8px !important;
            }

            .input-label {
                font-size: 14px !important;
                font-weight: 600 !important;
                color: #33415c !important;
                font-family: 'Outfit', sans-serif !important;
                margin-bottom: 7px !important;
            }

            .stAudioInput label{
                color: black !important;
            }

            div[data-testid="stAlert"] *{
                color: black !important
            }


            .voice-enroll-text {
                font-size: 20px !important;
                text-align: center !important;
                font-family: 'Outfit', sans-serif !important;
                color: #52627a !important;
                line-height: 1.6 !important;
                margin-top: 20px !important; 
            }

            /* Buttons */
            .stButton > button {
                width: 250px;
                align-items: center !important;
                text-align: center !important
                height: 50px;
                border-radius: 9px;
                border: none;
                background-color: #2563eb;
                color: white;
                font-size: 16px;
                font-weight: 600;
            }

            .stButton > button:hover {
                background-color: #1d4ed8;
            }

            /* OR divider */
            .divider {
                display: flex;
                align-items: center;
                margin: 25px 0;
                color: #8b96a8;
            }

            .divider::before,
            .divider::after {
                content: "";
                flex: 1;
                height: 1px;
                background: #dfe4ec;
            }

            .divider span {
                padding: 0 15px;
            }

        </style>
        
        """,
        unsafe_allow_html=True
                                
    )

def style_base_layout():
    st.markdown(
            """
            <style>
                
                /* Import Google Fonts */
                @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Playfair:ital,opsz,wght@0,5..1200,300..900;1,5..1200,300..900&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');
                
                /* hide top bar of streamlit */
                #MainMenu, footer, header {
                    visibility: hidden;
                }

                .block-container {
                    padding-top: 1.5rem !important;
                    padding-bottom: 1rem !important;
                    padding-left: 5rem !important;
                    padding-right: 5rem !important;
                    background-color: #FFEDD5 !important;
                }

                h1{
                    font-family: 'Oswald', sans-serif !important;
                    font-weight: 700;
                    font-size: 3.5rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #72a1fd !important;
                    text-align: center !important;
                }

                h2{
                    font-family: 'Oswald', sans-serif !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: black !important;
                }

                #footer-text{
                    font-family: 'outfit', sans-serif !important;
                    color: #716e6e !important;
                }

                p{
                    font-family: 'outfit', sans-serif !important;
                    color: white !important;
                    
                }

                div[data-testid="stButton"]{
                    display: flex !important;
                    justify-content: center !important;}

                button[kind= "primary"] {               
                    background: #5990ff; !important;
                    color: white !important;
                    border-radius: 1.5rem !important;
                    padding: 10px 20px!important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                    justify-content: center !important;
                    font-size: 50px !important;
                    font-weight: 700 !important;
                    
                }

                button[kind= "secondary"] {
                    background: #5990ff; !important;
                    color: white !important;
                    border-radius: 1.5rem !important;
                    padding: 10px 20px!important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                    height: 50px !important;
                    width: 600px !important;
                }

                button[kind= "tertiary"] {
                    background: #5990ff; !important;
                    color: white !important;
                    border-radius: 1.5rem !important;
                    padding: 10px 20px!important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover {
                    transform: scale(1.05) !important;
                    background-color: #938989 !important;
                }

            </style>
            """
            ,unsafe_allow_html=True
        )