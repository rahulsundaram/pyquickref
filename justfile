# list available recipes
default:
    @just --list

# run ruff linter
lint:
    uv run ruff check .

# run ruff formatter (auto-fix)
format:
    uv run ruff format .

# check ruff formatting (no changes)
format-check:
    uv run ruff format --check .

# run ty type checker
typecheck:
    uv run ty check .

# run pytest
test:
    uv run pytest tests -v

# run all checks (lint + format + typecheck + test)
check: lint format-check typecheck test
    @echo "All checks passed!"

# format code then run all checks
all: format check

# run all examples
run:
    uv run pyquickref

# list all examples with doc links
list:
    uv run pyquickref --list

# remove build artifacts
clean:
    rm -rf build/ dist/ *.egg-info .pytest_cache .ruff_cache __pycache__
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

image := "pyquickref"

# build Docker image
docker-build:
    docker build -t {{image}} .

# run all examples in Docker
docker-run: docker-build
    docker run --rm {{image}}

# list all examples in Docker
docker-list: docker-build
    docker run --rm {{image}} uv run pyquickref --list
