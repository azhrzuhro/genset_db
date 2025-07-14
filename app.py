import streamlit as st
import pandas as pd
import mysql.connector
import joblib

# Load model & tools
model = joblib.load('model/random_forest_genset.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')

# Streamlit UI
st.set_page_config(page_title="Prediksi Status Genset", layout="centered")
st.title("⚡ Prediksi Status Genset Otomatis dari Database")
st.markdown("Ambil data sensor terbaru dari database dan prediksi status genset (Normal, Anomaly, Failure).")

# Koneksi ke database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Ganti kalau ada password
        database="genset"
    )
    cursor = db.cursor()
except:
    st.error("❌ Gagal konek ke database.")
    st.stop()

# Ambil 1 data sensor terbaru
cursor.execute("""
SELECT oil_pressure, coolant_temp, engine_RPM, vibration,
       baterei, genset_voltage, genset_current,
       genset_frekuensi, genset_power
FROM sensor
ORDER BY timestamp DESC
LIMIT 1
""")
row = cursor.fetchone()

if row:
    # Label kolom untuk model
    columns = ['oilPressure', 'coolantTemperature', 'engineRPM', 'engineVibration',
               'batteryVoltageDC', 'gensetVoltageAC', 'gensetCurrentAC',
               'gensetFrequencyAC', 'gensetPowerAC']

    df_input = pd.DataFrame([row], columns=columns)
    st.subheader("📥 Data Sensor Terbaru")
    st.dataframe(df_input)

    # Prediksi
    input_scaled = scaler.transform(df_input)
    pred = model.predict(input_scaled)[0]
    label = le.inverse_transform([pred])[0]

    st.success(f"✅ Prediksi Status Genset: **{label}**")

    # Simpan hasil prediksi ke tabel sensor_prediksi
    insert_query = """
    INSERT INTO sensor_prediksi (
        oilPressure, coolantTemperature, engineRPM, engineVibration,
        batteryVoltageDC, gensetVoltageAC, gensetCurrentAC,
        gensetFrequencyAC, gensetPowerAC, status_prediksi
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row) + (label,))
    db.commit()

    st.info("📝 Hasil prediksi telah disimpan ke tabel `sensor_prediksi`.")

    # Menampilkan riwayat prediksi
    cursor.execute("SELECT * FROM sensor_prediksi ORDER BY waktu DESC LIMIT 5")
    result = cursor.fetchall()
    columns_display = [i[0] for i in cursor.description]
    df_history = pd.DataFrame(result, columns=columns_display)

    st.markdown("---")
    st.subheader("🕓 Riwayat Prediksi")
    st.dataframe(df_history)
else:
    st.warning("⚠️ Tidak ada data sensor di database.")

cursor.close()
db.close()
