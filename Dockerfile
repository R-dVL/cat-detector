FROM python:3.9-buster
#Crear directorios
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/cat_detector/data
#Copiar archivos
COPY requirements.txt /opt/app/
COPY app /opt/app/cat_detector/
WORKDIR /opt/app
#Instalar dependencias
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
#Config
#Permisos script de inicio
#RUN chmod 777 /opt/app/start.sh
#Arrancar app
CMD ["python3", "/opt/app/cat_detector/app/main.py"]