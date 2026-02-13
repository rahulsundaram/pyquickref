.PHONY: help lint format format-check typecheck test check all clean run list \
       docker-build docker-check docker-test docker-lint docker-format docker-run docker-list

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

lint: ## Run ruff linter
	uv run ruff check .

format: ## Run ruff formatter (auto-fix)
	uv run ruff format .

format-check: ## Check ruff formatting (no changes)
	uv run ruff format --check .

typecheck: ## Run ty type checker
	uv run ty check .

test: ## Run pytest
	uv run pytest tests -v

check: lint format-check typecheck test ## Run all checks (lint + format + typecheck + test)
	@echo "All checks passed!"

all: format check ## Format code then run all checks

run: ## Run all examples
	uv run pyquickref

list: ## List all examples with doc links
	uv run pyquickref --list

clean: ## Remove build artifacts
	rm -rf build/ dist/ *.egg-info .pytest_cache .ruff_cache __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

IMAGE := pyquickref

docker-build: ## Build Docker image
	docker build -t $(IMAGE) .

docker-check: docker-build ## Run all checks in Docker
	docker run --rm $(IMAGE) make check

docker-test: docker-build ## Run tests in Docker
	docker run --rm $(IMAGE) make test

docker-lint: docker-build ## Run linting in Docker
	docker run --rm $(IMAGE) make lint

docker-format: docker-build ## Run formatting in Docker
	docker run --rm $(IMAGE) make format

docker-run: docker-build ## Run all examples in Docker
	docker run --rm $(IMAGE)

docker-list: docker-build ## List all examples in Docker
	docker run --rm $(IMAGE) uv run pyquickref --list
