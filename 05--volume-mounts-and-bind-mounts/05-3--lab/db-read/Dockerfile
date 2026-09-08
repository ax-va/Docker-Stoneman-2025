FROM python:3.12-alpine

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY app/pyproject.toml app/poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

COPY app/src ./src

CMD ["python", "src/main.py"]