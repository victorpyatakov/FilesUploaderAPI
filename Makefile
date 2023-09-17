
build:
	docker-compose up --build -d

lint:
	flake8 app/

types:
	mypy app/

black:
	black app/

isort:
	isort app/

test:
	docker-compose up pytest