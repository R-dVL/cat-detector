FROM python:latest
#Dependencias de OpenCV
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
#Crear directorios
RUN mkdir /app
#Copiar archivos
COPY requirements.txt /app/
COPY app /app/
WORKDIR /app
#Instalar dependencias
RUN pip install -r requirements.txt
#Arrancar app
ENTRYPOINT ["python3", "main.py"]