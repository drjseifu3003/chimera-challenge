FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app:$PYTHONPATH

WORKDIR /app

# Install exact dependencies from lockfile
COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen

# Copy project files
COPY . /app

# Default: run the test suite using uv's runner
CMD ["uv", "run", "pytest", "-q"]
