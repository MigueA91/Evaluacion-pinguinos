Miguel Acuña Gaete

# Parte 0: Entrenamiento del modelo 🐧

Este script entrena un modelo de clasificación de especies de pingüinos y guarda los siguientes archivos que deberán ser utilizados por la aplicación en la Parte 1:

- `modelo_penguins.keras`: Modelo Keras entrenado
- `scaler.pkl`: Scaler `StandardScaler` ajustado
- `clases.csv`: Clases codificadas del `LabelEncoder`
- `columnas.csv`: Columnas después de aplicar `get_dummies`

---

## 📦 Requisitos

- Python 3.10
- [Poetry](https://python-poetry.org/docs/)

---

## ▶️ Instrucciones de ejecución

**Instalar dependencias:**
```bash
poetry install

**Ejecutar el script**
```bash
poetry run python train.py