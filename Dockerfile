FROM python:latest
#Env variables
ENV BOT_TOKEN=YOUR_BOT_TOKEN
ENV CHAT_ID=YOUR_CHAT_ID
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