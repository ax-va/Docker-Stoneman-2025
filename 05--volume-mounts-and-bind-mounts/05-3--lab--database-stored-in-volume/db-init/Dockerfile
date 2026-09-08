FROM python:3.12-alpine

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY app/pyproject.toml app/poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

RUN mkdir /data

COPY app/alembic.ini .
COPY app/alembic ./alembic
COPY app/src ./src

RUN alembic revision \
    --autogenerate \
    -m "create fake-users table"

CMD ["alembic", "upgrade", "head"]