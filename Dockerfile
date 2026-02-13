FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends make && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen 2>/dev/null || uv sync

COPY pyquickref/ pyquickref/
COPY tests/ tests/
COPY Makefile ./

CMD ["uv", "run", "pyquickref"]
