import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

# --- Cargar recursos con caché ---
@st.cache_resource
def cargar_modelo():
    return load_model("modelo_penguins.keras")

@st.cache_data
def cargar_clases():
    return pd.read_csv("clases.csv", header=None)[0].tolist()

@st.cache_resource
def cargar_scaler():
    return joblib.load("scaler.pkl")

@st.cache_data
def cargar_columnas():
    return pd.read_csv("columnas.csv", header=None)[0].tolist()

# --- Cargar archivos ---
model = cargar_modelo()
clases = cargar_clases()
scaler = cargar_scaler()
columnas = cargar_columnas()

# --- Título de la app ---
st.title("Predicción de Especie de Pingüino 🐧")
st.write("""
Ingresa las características físicas de un pingüino y descubre su especie según nuestro modelo de Machine Learning entrenado con Keras.
""")

# --- Inputs del usuario ---
culmen_length = st.number_input("Longitud del culmen (mm)", min_value=30.0, max_value=60.0, value=45.0)
culmen_depth = st.number_input("Profundidad del culmen (mm)", min_value=13.0, max_value=22.0, value=17.0)
flipper_length = st.number_input("Longitud de la aleta (mm)", min_value=170, max_value=240, value=200)
body_mass = st.number_input("Masa corporal (g)", min_value=2700, max_value=6300, value=4000)
island = st.selectbox("Isla", ["Biscoe", "Dream", "Torgersen"])
sex = st.selectbox("Sexo", ["Male", "Female"])

# --- Construir DataFrame con variables dummy ---
input_dict = {
    "culmen_length_mm": culmen_length,
    "culmen_depth_mm": culmen_depth,
    "flipper_length_mm": flipper_length,
    "body_mass_g": body_mass,
    "island_Biscoe": 1 if island == "Biscoe" else 0,
    "island_Dream": 1 if island == "Dream" else 0,
    "sex_Male": 1 if sex == "Male" else 0,
}
input_df = pd.DataFrame([input_dict])

# --- Asegurar todas las columnas esperadas ---
for col in columnas:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[columnas]  # Reordenar columnas

# --- Escalado y predicción ---
input_scaled = scaler.transform(input_df)

if st.button("Predecir especie"):
    pred = model.predict(input_scaled)
    clase_predicha = clases[np.argmax(pred)]

    st.success(f"### Especie predicha: **{clase_predicha}** 🎉")
    st.write(f"Según los datos ingresados, el modelo predice que el pingüino pertenece a la especie **{clase_predicha}**.")
