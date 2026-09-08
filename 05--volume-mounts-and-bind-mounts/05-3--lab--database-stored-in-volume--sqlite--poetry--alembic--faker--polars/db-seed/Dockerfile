FROM python:3.12-alpine

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY db-seed/app/pyproject.toml db-seed/app/poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

COPY db-init/app/src/models.py ./src/models.py
COPY db-seed/app/src ./src

CMD ["python", "src/main.py"]