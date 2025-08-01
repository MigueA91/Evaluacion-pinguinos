# Clasificador de Especies de Pingüinos

Este proyecto utiliza técnicas de aprendizaje automático para clasificar las especies de pingüinos en el dataset de **Palmer Penguins**. El modelo fue entrenado utilizando **Keras** y desplegado con **Streamlit**. La aplicación permite predecir la especie de un pingüino basándose en sus características físicas.

## Descripción

El objetivo del proyecto es entrenar un modelo de clasificación para predecir la especie de un pingüino utilizando datos de características como el tamaño de las aletas, el peso y otros parámetros. El modelo entrenado se guarda y se puede reutilizar para hacer predicciones sobre nuevas muestras de datos.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal utilizado para el desarrollo de la aplicación.
- **TensorFlow (Keras)**: Framework utilizado para construir y entrenar el modelo de aprendizaje automático.
- **Seaborn**: Para cargar y visualizar el dataset de pingüinos.
- **Pandas**: Para manipulación de datos.
- **Scikit-learn**: Para preprocesamiento de datos y división en conjuntos de entrenamiento y prueba.
- **Matplotlib**: Para graficar la evolución de la precisión y la pérdida del modelo durante el entrenamiento.
- **Joblib**: Para guardar y cargar el scaler.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
