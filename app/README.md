Miguel Acuña Gaete

# Aplicación de Clasificación de Pingüinos 🐧

Esta aplicación fue desarrollada como parte de la Evaluación Práctica 2 del curso de Plataformas para Machine Learning. Utiliza un modelo entrenado con Keras para predecir la especie de un pingüino en base a características físicas.

---

## 📦 Requisitos

Para ejecutar esta aplicación dockerizada, asegúrese de tener instalado Docker.

---

## ▶️ Instrucciones para ejecución en Docker

### 1️⃣ Construir la imagen Docker:
```bash
docker build -t miguel-app .

### 2️⃣ Ejecutar el contenedor Docker:
```bash
docker run -p 8501:8501 -d miguel-app

### 🔗 Acceder a la aplicación:
Una vez ejecutado el contenedor, abra en su navegador:
http://localhost:8501

## 🔎 Ejecución local alternativa (opcional)

Si desea ejecutar la aplicación localmente (sin Docker), puede hacerlo activando el entorno de Poetry y ejecutando:

Se recomienda instalar previamente:
```bash
poetry install

Luego ejecutar:
```bash
poetry run streamlit run app.py