FROM python:latest
# Env variables
ENV BOT_TOKEN=YOUR_BOT_TOKEN
ENV CHAT_ID=YOUR_CHAT_ID
# OpenCv dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Create folder
RUN mkdir /app
# Copy code and requirements
COPY requirements.txt app /app/
# Define working directory
WORKDIR /app
# Intall dependencies
RUN pip install -r requirements.txt
# Expose flask port
EXPOSE 8888
# Start app
CMD ["python3", "main.py"]