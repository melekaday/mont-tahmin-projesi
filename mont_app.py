
import streamlit as st
import pandas as pd
from joblib import load

st.title("Mont Tahmin Sistemi 🌦️")
st.write("Sıcaklık, yağmur ve rüzgar değerlerini girerek mont giyip giymeyeceğini tahmin edin.")

temp = st.number_input("Sıcaklık (°C)", value=20)
rain = st.selectbox("Yağmur var mı?", ["Hayır", "Evet"])
wind = st.number_input("Rüzgar Hızı (km/s)", value=10)

if st.button("Tahmin Et"):
    model = load("mont_model.joblib")
    input_df = pd.DataFrame([{
        "temp_c": temp,
        "rain": 1 if rain=="Evet" else 0,
        "wind": wind
    }])
    tahmin = "Mont Giy" if model.predict(input_df)[0] == 1 else "Mont Gerek Yok"
    st.success(f"✅ Tahmin: {tahmin}")
