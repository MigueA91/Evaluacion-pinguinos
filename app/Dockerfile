# Imagen base liviana con Python 3.10
FROM python:3.10-slim

# Variables de entorno para evitar mensajes interactivos
ENV PIP_NO_CACHE_DIR=yes \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.2

# Instalar Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios de tu proyecto
COPY . .

# Instalar dependencias usando Poetry (sin instalar proyecto como paquete)
RUN poetry install --no-root

# Exponer puerto que usa Streamlit
EXPOSE 8501

# Comando para ejecutar app.py con Poetry + Streamlit
CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
