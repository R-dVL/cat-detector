FROM python:latest
#Dependencias de OpenCV
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
#Crear directorios
RUN mkdir /app
#Copiar archivos
COPY requirements.txt start.sh /app/
COPY app /app/
WORKDIR /app
#Instalar dependencias
RUN pip install -r requirements.txt
#Config
#Permisos script de inicio
RUN chmod 755 /app/start.sh
#Arrancar app
CMD ["/app/start.sh"]