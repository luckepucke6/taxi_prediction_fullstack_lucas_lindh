import streamlit as st
import httpx

st.markdown(
    """
    <p style="
        text-align: center;
        font-size: 50px;
        font-weight: 600;
        margin-bottom: 0;
    ">
        TAXI PRICE PREDICTOR
    </p>
    """,
    unsafe_allow_html=True
)


API_URL = "http://127.0.0.1:8000/predict"

def main():
    # df = pd.read_json(response.text) # Konvertera JSON-svar till dataframe
    # st.dataframe(df)

    time_of_day = st.selectbox("Time of day", ["Morning", "Afternoon", "Evening", "Night"])
    day_of_week = st.selectbox("Day of week", ["Weekday", "Weekend"])
    traffic = st.selectbox("Traffic conditions", ["Low", "Medium", "High"])
    distance = st.number_input("Trip distance (km)", min_value=0.1)

    if st.button("Predict price"):
        st.write("Checking price...")

        payload = {
            "Time_of_Day": time_of_day,
            "Day_of_Week": day_of_week,
            "Traffic_Conditions": traffic,
            "Trip_Distance_km": distance
        }
    
        response = httpx.post(API_URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            st.success(
                f"Estimated price {data['predicted_price_usd']:.2f} USD"
                f" (~{data['predicted_price_sek']:.2f} SEK)"
            )
        else:
            st.error("Prediction failed")

if __name__ == "__main__":
    main()