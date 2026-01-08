import streamlit as st
import pandas as pd
import httpx

API_URL = "http://127.0.0.1:8000/taxi"

def main():
    st.markdown("## Taxi Price Prediction Dashboard")
    response = httpx.get(API_URL)
    df = pd.read_json(response.text) # Konvertera JSON-svar till dataframe
    st.dataframe(df)

if __name__ == "__main__":
    main()