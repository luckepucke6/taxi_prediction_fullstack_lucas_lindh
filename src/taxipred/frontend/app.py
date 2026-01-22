import streamlit as st

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/predict.py", title="Price prediction"),
    st.Page("pages/map.py", title="Map")
]

pg = st.navigation(pages)
pg.run()
