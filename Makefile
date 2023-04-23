format:
	@poetry run black src
	@poetry run isort src
	@poetry run autoflake --remove-all-unused-imports --recursive src

run:
	@poetry run uvicorn src.app:app --reload

test:
	@poetry run pytest tests/
