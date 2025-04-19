FROM python:3.10-slim

# Instala dependencias del sistema necesarias para numpy y pybullet
RUN apt update && apt install -y \
    libgl1-mesa-glx \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crea carpeta de trabajo
WORKDIR /app

# Copia todos los archivos de la app (asegúrate de estar en la misma carpeta al hacer build)
COPY . /app

# Instala numpy y pybullet
RUN pip install --no-cache-dir numpy pybullet

# Ejecuta el script
CMD ["python", "brazo_robotico.py"]


