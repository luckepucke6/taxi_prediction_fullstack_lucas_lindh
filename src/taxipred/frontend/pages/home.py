import streamlit as st
from pathlib import Path

taxi_path = Path(__file__).parents[2] / "data" / "taxi.jpg"

st.markdown(
    "<p style='text-align: center; font-size: 50px; font-weight: 600;'>Taxipred App</p>",
    unsafe_allow_html=True
)
st.markdown("### This is a streamlit app that consumes a FastAPI about taxi prices. With the app you can predict the cost of taxi rides. Put in the information about your trip and you will get a price prediction.")
st.image(taxi_path)