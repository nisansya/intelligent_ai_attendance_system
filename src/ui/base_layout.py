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

        /* ================= LEFT PANEL ================= */

            .st-key-left_panel {
                background-color: #dae6fe !important;
                min-height: 800px !important;
                padding: 55px 45px !important;
                border-radius: 18px 0px 0px 18px !important;
                box-sizing: border-box !important;
            }


            /* ================= RIGHT PANEL ================= */

            .st-key-right_panel {
                background-color: white !important;
                min-height: 800px !important;
                padding: 70px 70px !important;
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
                width: 180px !important;
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