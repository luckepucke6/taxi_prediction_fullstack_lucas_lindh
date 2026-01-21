import streamlit as st
import httpx
import pandas as pd

ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImNlNWEyMzA2MDZhMTRjZDdhYWU4MzM3NzEwYmQzYjVkIiwiaCI6Im11cm11cjY0In0="


def geocode_place(place_name):
    response = httpx.get("https://api.openrouteservice.org/geocode/search",
                         params={
                             "api_key": ORS_API_KEY,
                             "text": place_name})
    data = response.json()
    coords = data["features"][0]["geometry"]["coordinates"]
    return coords[1], coords[0]


st.markdown(
    """
    <p style="
        text-align: center;
        font-size: 50px;
        font-weight: 600;
        margin-bottom: 0;
    ">
        MAP
    </p>
    """,
    unsafe_allow_html=True
)


start_location = st.text_input("From")
end_location = st.text_input("To")

if st.button("Show route"):
    if not start_location or not end_location:
        st.warning("Please emter both start and destination")
        st.stop()
    
    st.write("Fetching route...")
    
    start_coords = geocode_place(start_location)
    end_coords = geocode_place(end_location)

    st.write("From:", start_coords)
    st.write("To:", end_coords)

    map_data = pd.DataFrame(
        [
            {"lat": start_coords[0], "lon": start_coords[1]},
            {"lat": end_coords[0], "lon": end_coords[1]}
        ])

    st.map(map_data)