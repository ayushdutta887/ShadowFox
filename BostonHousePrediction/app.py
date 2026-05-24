import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Page Configuration
st.set_page_config(
    page_title="Boston House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("Boston House Price Prediction")

st.write("Adjust the values below to predict house price.")

# =========================
# Input Sliders
# =========================

RM = st.slider(
    "Average Number of Rooms",
    min_value=1.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

LSTAT = st.slider(
    "Lower Status Population %",
    min_value=1.0,
    max_value=40.0,
    value=12.0,
    step=0.1
)

PTRATIO = st.slider(
    "Pupil-Teacher Ratio",
    min_value=10.0,
    max_value=30.0,
    value=18.0,
    step=0.1
)

CRIM = st.slider(
    "Crime Rate",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)

TAX = st.slider(
    "Property Tax Rate",
    min_value=100.0,
    max_value=800.0,
    value=300.0,
    step=1.0
)

# =========================
# Prediction
# =========================

if st.button("Predict Price"):

    # Arrange features in same order as training
    features = np.array([[
        RM,
        LSTAT,
        PTRATIO,
        CRIM,
        TAX
    ]])

    # Scale features
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)

    # Display prediction
    st.success(
        f"Predicted House Price: ${prediction[0]*1000:,.2f}"
    )