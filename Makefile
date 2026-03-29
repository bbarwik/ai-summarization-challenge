.PHONY: help install install-dev test test-cov lint format typecheck clean pre-commit docker-build docker-setup docker-run docker-test docker-clean docker-restore

help:
	@echo "Available commands:"
	@echo "  install       Install package in production mode"
	@echo "  install-dev   Install package with development dependencies"
	@echo "  test          Run tests"
	@echo "  test-cov      Run tests with coverage"
	@echo "  lint          Run linting checks"
	@echo "  format        Format code with ruff"
	@echo "  typecheck     Run type checking with basedpyright"
	@echo "  clean         Remove build artifacts and cache files"
	@echo "  pre-commit    Run pre-commit hooks on all files"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

test-cov:
	pytest --cov=ai_summarization --cov-report=html --cov-report=term

lint:
	ruff check .

format:
	ruff format .
	ruff check --fix .

typecheck:
	basedpyright --level warning

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

pre-commit:
	pre-commit run --all-files

docker-build:
	@if [ ! -f .env.docker ]; then \
		echo "Error: .env.docker not found"; \
		exit 1; \
	fi
	@export $$(grep -v '^#' .env.docker | xargs) && docker compose build

docker-setup:
	rm -rf workspace_isolated
	cp -a workspace workspace_isolated

docker-run:
	@if [ ! -f .env.docker ]; then \
		echo "Error: .env.docker not found"; \
		exit 1; \
	fi
	export $$(grep -v '^#' .env.docker | xargs) && docker compose run --rm pipeline

docker-test:
	@if [ ! -f .env.docker ]; then \
		echo "Error: .env.docker not found"; \
		exit 1; \
	fi
	export $$(grep -v '^#' .env.docker | xargs) && docker compose run --rm --entrypoint /app/scripts/docker-test.sh pipeline

docker-clean:
	rm -rf workspace_isolated/output

docker-restore:
	rm -rf workspace
	cp -a workspace_isolated workspace
