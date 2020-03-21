SHELL := /bin/sh

doc:
	snowboard html -o docs/core.html docs/core.coreb
	vanadia --input docs/.core --output docs/core.postman_collection.json

clean:
	@rm -f .coverage 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete

format:
	@black core

sort:
	@isort --skip .venv

lint:
	@flake8 core

test: clean lint
	@black --check core
	@isort --skip .venv -c
	python -m pytest --cov=core

dump_data:
	python manage.py load_data --all  