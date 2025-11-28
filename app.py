import streamlit as st
import requests
import datetime

# ---------------------
# 🎨 Header & intro
# ---------------------
st.title("🚕 TaxiFareModel front")
st.markdown("""
This is a simple front-end interface to test your **TaxiFareModel API**.
You can input the ride details below and retrieve the predicted fare.
""")

st.divider()

st.markdown("""
### 🕹️ Select ride parameters
""")

# ---------------------
# 🧭 User inputs
# ---------------------

# 1️⃣ Date & Time
pickup_date = st.date_input("Pickup Date", datetime.date(2014, 7, 6))
pickup_time = st.time_input("Pickup Time", datetime.time(19, 18, 0))
pickup_datetime = f"{pickup_date} {pickup_time}"

# 2️⃣ Coordinates
pickup_longitude = st.number_input("Pickup Longitude", value=-73.950655, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", value=40.783282, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.984365, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.769802, format="%.6f")

# 3️⃣ Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=2)

st.divider()

# ---------------------
# ⚙️ API call section
# ---------------------

st.markdown("### 🔮 Get fare prediction")

url = st.text_input("Enter your API URL", value="https://taxifare.lewagon.ai/predict")

if st.button("Predict fare"):
    # Build the params dictionary
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            prediction = response.json()
            fare = prediction.get("fare", "No fare found")
            st.success(f"💰 Predicted fare: **${fare:.2f}**")
        else:
            st.error(f"API returned status code {response.status_code}")
            st.text(response.text)
    except Exception as e:
        st.error(f"Error calling API: {e}")

st.divider()
