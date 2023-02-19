format:
	@poetry run black src frontend
	@poetry run isort src frontend
	@poetry run autoflake --remove-all-unused-imports --recursive src frontend

run-backend:
	@poetry run uvicorn src.app:app --reload

run-frontend:
	@poetry run streamlit run frontend/app.py

test:
	@poetry run pytest tests/
