import streamlit as st
import pandas as pd

def main():
    st.header("This is title")
    name= st.text_input("enter your name:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('display my name', type= 'primary', width= 'content'):
            print("hi", name)

    with col2:
        if st.button('display my name', type= 'secondary', key= 'btn2', width='stretch'):
            print('bye', name)

    st.markdown("""
        <div>
            <h1>Snap class<h1>
        </div>
   """, unsafe_allow_html= True )


main()