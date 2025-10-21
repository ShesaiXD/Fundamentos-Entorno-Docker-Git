# Imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del microservicio
COPY . .

# Expone el puerto en el que corre tu app (ajústalo según tu servicio)
EXPOSE 8000

# Comando por defecto para ejecutar el microservicio
CMD ["python", "app.py"]