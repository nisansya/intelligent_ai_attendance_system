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

def style_dashboard_background():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #bedbf6 !important;
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
                    font-weight: 700;
                    font-size: 3.5rem !important;
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