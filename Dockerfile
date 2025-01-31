FROM python:3.13-alpine

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

COPY . .

RUN python -m venv .venv && \
    .venv/bin/pip install uv && \
    .venv/bin/uv pip install -e .

ENV DATABASE_URL=sqlite:///med-scheduling.db

EXPOSE 5000

CMD [".venv/bin/python", "-m", "fastapi", "run", "main.py", "--port", "5000", "--host", "0.0.0.0"]