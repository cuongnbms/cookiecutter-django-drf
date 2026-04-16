FROM python:3.12-slim AS builder

ENV PYTHONUNBUFFERED=1

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential libpq-dev git && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . .

RUN STAGE=build uv run python3 manage.py collectstatic --noinput

# ── Runtime ──────────────────────────────────────────────
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV LANG=en_US.UTF-8

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libpq5 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /app /app
RUN chmod +x ./entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
