# -- General
SHELL := /bin/bash

# -- Docker
COMPOSE              = bin/compose
COMPOSE_RUN          = $(COMPOSE) run --rm --no-deps

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
	@$(COMPOSE) logs -f cpo
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
test: ## run tests
	bin/pytest
.PHONY: test

# -- Misc
help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

