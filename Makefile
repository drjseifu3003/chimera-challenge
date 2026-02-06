.PHONY: setup test clean spec-check dev-setup check lint secure all

IMAGE := chimera-governor

setup:
	docker build -t $(IMAGE) .

# Run the container image (it will run tests by default inside the image)
test: setup
	docker run --rm $(IMAGE)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + || true
	find . -name "*.pyc" -delete || true
	rm -rf build/ dist/ *.egg-info .pytest_cache || true

# Placeholder spec check
spec-check:
	docker run --rm -v "$(PWD)":/app -w /app python:3.11-slim bash -lc "echo 'SPEC CHECK: placeholder — implement verification script to compare repo files with specs/'; exit 0"

# Local uv-based developer setup
dev-setup:
	uv sync

# Run tests locally via uv
check:
	uv run pytest

# Linting (code quality)
lint:
	uv run ruff check .

# Security checks (static analysis)
secure:
	uv run bandit -r src/

# Run lint, security, and tests in sequence
all: lint secure test