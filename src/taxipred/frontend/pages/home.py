import streamlit as st
from taxipred.utils.constants import TAXI_PATH


st.markdown(
    "<p style='text-align: center; font-size: 50px; font-weight: 600;'>Taxipred App</p>",
    unsafe_allow_html=True
)
st.markdown("### This is a streamlit app that consumes a FastAPI about taxi prices. With the app you can predict the cost of taxi rides. Put in the information about your trip and you will get a price prediction.")
st.image(TAXI_PATH)