.DEFAULT_GOAL := help
SHELL := /bin/sh
ENV ?= dev
SERVICE ?= app

DC ?= COMPOSE_PROFILES=${COMPOSE_PROFILES} docker compose -f stack/docker/docker-compose.y*ml -f stack/docker/docker-compose.${ENV}.y*ml

help: ## Show this help
	@echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\1:\2/' | column -c2 -t -s :)"

whereami: ## Show current environment
	@echo ${ENV}

push: ## Push docker containers
	${DC} push ${SERVICE}

build: ## Build docker containers
	${DC} build

up: ## Start docker containers
	${DC} up -d --remove-orphans

run: ## Start docker containers attached
	${DC} run --remove-orphans ${SERVICE} poetry run python -m advent_of_code_2024.main

down: ## Shutdown docker containers
	${DC} down --remove-orphans

ps: ## List docker containers
	${DC} ps

logs: ## Show docker containers logs
	${DC} logs ${SERVICE}

tail: ## Tail on docker containers logs
	${DC} logs --follow ${SERVICE}

exec: ## Open shell in docker container
	${DC} exec ${SERVICE} sh

shell: ## Open shell in docker container
	${DC} run --rm ${SERVICE} sh

context: ## Show docker contexts
	docker context ls

generate-dist: ## Generate Dist from .env file
	cat ${FILE} | grep -o '.*=' > ${FILE}.dist

repl: build run ## Start a read-eval-print-loop

test: ## Run tests

cs: ## Run code style checks
	${DC} run --rm ${SERVICE} poetry run black --check .

format: ## Format code
	${DC} run --rm ${SERVICE} poetry run black .

type-check: ## Run type checks
	${DC} run --rm ${SERVICE} poetry run pyright .

lint: ## Run linting
	${DC} run --rm ${SERVICE} poetry run pylint -d duplicate-code .

unit: ## Run code coverage
	${DC} run --rm ${SERVICE} poetry run coverage run -a -m pytest -vvv

functional: ## Run code coverage
	${DC} run --rm ${SERVICE} poetry run coverage run -a -m behave

coverage: ## Run code coverage
	${DC} run --rm ${SERVICE} poetry run coverage report

coverage-html: ## Run code coverage
	${DC} run --rm ${SERVICE} poetry run coverage html

check: down cs lint type-check unit functional coverage ## Run all checks

cicd: ## Run cicd pipeline
	${DC} run --rm ${SERVICE} poetry run invoke cicd
