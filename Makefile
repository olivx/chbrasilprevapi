SHELL := /bin/sh


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
	python -m pytest --cov=core --cov=account

down:
	docker-compose down

compose:
	docker-compose up --build

build:
	docker build -t brasilprev . 

run:
	docker container run  \
	-e DEBUG="True" \
	-e LOG_LEVEL="INFO" \
	-e ALLOWED_HOSTS="127.0.0.1, .localhost, *" \
	-e SECRET_KEY="eb*xnd%dbcj*u0q^y75s!mz9)87(_i@vz&i@w4r-pc3rp1duf1" \
	-p 8000:8000 --rm --name container_brasilprev brasilprev