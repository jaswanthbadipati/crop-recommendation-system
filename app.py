# crop_app.py

import streamlit as st
import numpy as np
import joblib

# Load saved model and scaler
model = joblib.load("crop_recommender_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("🌾 Crop Recommendation System")
st.markdown("Get the most suitable crop for your land based on environmental and soil conditions.")

# Inputs
N = st.number_input("Nitrogen (N)", min_value=0, max_value=140, step=1)
P = st.number_input("Phosphorus (P)", min_value=5, max_value=145, step=1)
K = st.number_input("Potassium (K)", min_value=5, max_value=205, step=1)
temperature = st.slider("Temperature (°C)", 10.0, 45.0, 25.0)
humidity = st.slider("Humidity (%)", 10.0, 100.0, 50.0)
ph = st.slider("Soil pH", 3.5, 9.5, 6.5)
rainfall = st.slider("Rainfall (mm)", 20.0, 300.0, 100.0)

# Predict button
if st.button("Predict Suitable Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    st.success(f"✅ Recommended Crop: **{prediction[0].capitalize()}**")
