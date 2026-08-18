FROM python:3.12-slim

WORKDIR /app/src

COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src .

CMD ["python", "main.py"]