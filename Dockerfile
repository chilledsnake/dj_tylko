FROM python:3.13-slim

RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install poetry

ENV POETRY_HOME="/root/.poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=core.settings

EXPOSE 8000
