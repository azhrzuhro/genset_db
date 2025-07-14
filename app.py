import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load('model/random_forest_genset.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')

# UI
st.set_page_config(page_title="Prediksi Status Genset", layout="centered")
st.title("⚡ Prediksi Status Genset")
st.markdown("Masukkan nilai sensor untuk mengetahui kondisi genset (Normal, Anomaly, Failure)")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        oilPressure = st.number_input("Oil Pressure", 0.0, 10.0, 3.5)
        coolantTemperature = st.number_input("Coolant Temperature (°C)", 0.0, 120.0, 30.0)
        engineRPM = st.number_input("Engine RPM", 0, 3000, 1500)
        engineVibration = st.number_input("Engine Vibration", 0, 200, 50)
        batteryVoltageDC = st.number_input("Battery Voltage DC", 0.0, 24.0, 13.0)

    with col2:
        gensetVoltageAC = st.number_input("Genset Voltage AC", 0.0, 300.0, 230.0)
        gensetCurrentAC = st.number_input("Genset Current AC", 0.0, 50.0, 15.0)
        gensetFrequencyAC = st.number_input("Genset Frequency AC", 0.0, 60.0, 50.0)
        gensetPowerAC = st.number_input("Genset Power AC (W)", 0.0, 20000.0, 12000.0)

    submitted = st.form_submit_button("Prediksi")

# Proses prediksi
if submitted:
    input_data = pd.DataFrame([{
        'oilPressure': oilPressure,
        'coolantTemperature': coolantTemperature,
        'engineRPM': engineRPM,
        'engineVibration': engineVibration,
        'batteryVoltageDC': batteryVoltageDC,
        'gensetVoltageAC': gensetVoltageAC,
        'gensetCurrentAC': gensetCurrentAC,
        'gensetFrequencyAC': gensetFrequencyAC,
        'gensetPowerAC': gensetPowerAC
    }])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    label = le.inverse_transform([prediction])[0]

    st.success(f"✅ Status Genset: **{label}**")

    st.markdown("---")
    st.subheader("📈 Data yang Dimasukkan")
    st.dataframe(input_data)