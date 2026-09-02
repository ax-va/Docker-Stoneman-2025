FROM python:3.13-alpine

WORKDIR /app/src

COPY app/src/ .
COPY app/data /data

VOLUME /data

CMD ["python", "main.py"]
