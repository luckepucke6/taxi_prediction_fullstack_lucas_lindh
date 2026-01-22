import streamlit as st
import httpx
import pandas as pd
import math

ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImNlNWEyMzA2MDZhMTRjZDdhYWU4MzM3NzEwYmQzYjVkIiwiaCI6Im11cm11cjY0In0="


def geocode_place(place_name):
    response = httpx.get("https://api.openrouteservice.org/geocode/search",
                         params={
                             "api_key": ORS_API_KEY,
                             "text": place_name})
    data = response.json()
    coords = data["features"][0]["geometry"]["coordinates"]
    return coords[1], coords[0]

def distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    R = 6371 # earth radius in km

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c



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
    try:
        start_coords = geocode_place(start_location)
        end_coords = geocode_place(end_location)
    except Exception:
        st.error("Could not fins one or both locations. Try again.")
        st.stop()
    
    distance_km = distance(start_coords, end_coords)

    st.write("From:", start_coords)
    st.write("To:", end_coords)
    st.write(f"Distance between {start_location.title()} - {end_location.title()}: {distance_km:.2f} km")

    map_data = pd.DataFrame(
        [
            {"lat": start_coords[0], "lon": start_coords[1]},
            {"lat": end_coords[0], "lon": end_coords[1]}
        ])

    st.map(map_data)