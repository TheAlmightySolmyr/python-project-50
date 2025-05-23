install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

lint_fix:
	uv run ruff check --fix

build:
	uv build