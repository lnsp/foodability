FROM python:buster

WORKDIR /app

ENV FLASK_PORT=5000
ENV DOWNLOAD_PICKLE=yes

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "app.py"]

