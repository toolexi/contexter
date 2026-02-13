.PHONY: format
format:
	ruff check --fix
	black .