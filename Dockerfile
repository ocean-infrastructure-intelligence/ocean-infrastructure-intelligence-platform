FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install \
    fastapi \
    uvicorn \
    sqlalchemy \
    alembic \
    psycopg[binary] \
    geoalchemy2 \
    pydantic-settings \
    python-dotenv

CMD [
    "uvicorn",
    "backend.app.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]