import streamlit as st
import httpx

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/predict.py", title="Price prediction")
]

pg = st.navigation(pages)
pg.run()
