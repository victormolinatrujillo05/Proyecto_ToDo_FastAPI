# Usamos una imagen oficial de Python ligera
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requisitos primero (si tuviéramos uno) 
# o instalamos directamente las librerías necesarias
RUN pip install --no-cache-dir fastapi uvicorn

# Copiamos todos los archivos de nuestra carpeta a la carpeta /app del contenedor
COPY . .

# Exponemos el puerto 8000 que es donde corre FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]