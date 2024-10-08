# -- General
SHELL := /bin/bash

# -- Docker
COMPOSE              = bin/compose
COMPOSE_RUN          = $(COMPOSE) run --rm --no-deps
COMPOSE_RUN_CPO      = $(COMPOSE_RUN) cpo
POETRY_RUN_CPO       = $(COMPOSE_RUN_CPO) poetry run

# ==============================================================================
# RULES

default: help

# -- Docker/compose
bootstrap: ## bootstrap the project for development
bootstrap: \
  build
.PHONY: bootstrap

build: ## build the app container(s)
	$(COMPOSE) build
.PHONY: build

logs: ## display OCPI server logs (follow mode)
	@$(COMPOSE) logs -f
.PHONY: logs

run: ## run the whole stack
	$(COMPOSE) up -d
.PHONY: run

status: ## an alias for "docker compose ps"
	@$(COMPOSE) ps
.PHONY: status

stop: ## stop all servers
	@$(COMPOSE) stop
.PHONY: stop

# -- OCPI
lint: ## lint api python sources
lint: \
  lint-black \
  lint-ruff \
  lint-mypy
.PHONY: lint

lint-black: ## lint api python sources with black
	@echo 'lint:black started…'
	@$(POETRY_RUN_CPO) black playground tests
.PHONY: lint-black

lint-ruff: ## lint api python sources with ruff
	@echo 'lint:ruff started…'
	@$(POETRY_RUN_CPO) ruff check playground tests
.PHONY: lint-ruff

lint-ruff-fix: ## lint and fix api python sources with ruff
	@echo 'lint:ruff-fix started…'
	@$(POETRY_RUN_CPO) ruff check --fix playground tests
.PHONY: lint-ruff-fix

lint-mypy: ## lint api python sources with mypy
	@echo 'lint:mypy started…'
	@$(POETRY_RUN_CPO) mypy playground tests
.PHONY: lint-mypy

test: ## run tests
	bin/pytest
.PHONY: test

# -- Misc
help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

