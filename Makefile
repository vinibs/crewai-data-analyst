PROJECT_NAME=ai-data-analysis-crew-poc

build:
	@echo "Building Image..."
	docker image rm ${PROJECT_NAME} || true
	docker build -t ${PROJECT_NAME} .

run:
	@echo "Running Container..."
	docker rm ${PROJECT_NAME} || true
	docker run --name ${PROJECT_NAME} --env-file ./.env -v ./src:/app ${PROJECT_NAME}

stop:
	@echo "Stopping Container..."
	docker stop ${PROJECT_NAME}

rerun:
	@echo "Re-Running Container..."
	make stop
	make build
	make run

install:
	pip install -r requirements/requirements.txt

install-dev:
	pip install -r requirements/requirements-dev.txt

lint:
	black . && isort --profile black .