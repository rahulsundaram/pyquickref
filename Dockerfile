FROM python:3.10-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen 2>/dev/null || uv sync

COPY pyquickref/ pyquickref/
COPY tests/ tests/

CMD ["uv", "run", "pyquickref"]
