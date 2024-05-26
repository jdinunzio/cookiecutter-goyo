.PHONY: help lint flake docstyle typecheck black-check black-fix
.PHONY: test-unit test-integration tests coverage
.PHONY: report-test-unit report-test-integration report-test report-lint project-init

# General Configuration
#SHELL               := /bin/bash
TEST_LOG_LEVEL       := error
INTEG_DB_NAME        := integ.db

help:                      ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


##
##Run Services
##

run-be-dev:                ## Run backend in foreground, in development mode
	@UVICORN_EXTRA_PARAMS="--reload" poetry run src/{{cookiecutter.package_name}}/presentation/be_server.sh

run-be:                    ## Run backend in foreground
	poetry run src/{{cookiecutter.package_name}}/presentation/be_server.sh


##
##Development
##

lint:                      ## Code Linting
	@echo -en '\033[33m'
	@poetry run pylint --version
	@echo -en '\033[0m'
	@poetry run pylint src tests

flake:                     ## Flake-8 and ruff
	@echo -en '\033[33m'
	@poetry run ruff --version
	@echo -en '\033[0m'
	@poetry run ruff check src tests
	@echo -e '\033[33m'
	@echo -n "flake " && poetry run flake8 --version
	@echo -en '\033[0m'
	@poetry run flake8 --config=.flake8 src tests && echo "All checks passed!"

docstyle:                  ## Check Style of docstrings
	@echo -en '\033[33m'
	@echo -n "pydocstyle " && poetry run pydocstyle --version
	@echo -en '\033[0m'
	@poetry run pydocstyle src/ tests/ && echo "All checks passed!"

typecheck:                 ## Typecheck
	@echo -en '\033[33m'
	@poetry run mypy --version
	@echo -en '\033[0m'
	@poetry run mypy src tests

black-check:               ## Code checking with black
	@echo -en '\033[33m'
	@poetry run black --version
	@echo -en '\033[0m'
	@poetry run black --check --diff src tests

black-fix:                 ## Code formatting with black
	@poetry run isort src tests
	@poetry run black src tests

dev-check:                 ## Run common development checks
	@echo -e '\033[34m**** Linting...\033[0m'
	@make --no-print-directory lint
	@echo -e '\033[34m\n**** Flaking...\033[0m'
	@make --no-print-directory flake
	@echo -e '\033[34m\n\n**** Blacking...\033[0m'
	@make --no-print-directory black-check
	@echo -e '\033[34m\n\n**** Docstyling...\033[0m'
	@make --no-print-directory docstyle
	@echo -e '\033[34m\n\n**** Type checking...\033[0m'
	@make --no-print-directory typecheck
	@echo -e '\033[34m\n\n**** Unit Testing...\033[0m'
	@make --no-print-directory test-unit
	@echo -e '\033[34m\n\n**** Integration Testing...\033[0m'
	@make --no-print-directory test-integration
	@echo -e '\n'

##
##Testing
##

test-unit:                 ## Run unit tests
	@LOG_LEVEL=${TEST_LOG_LEVEL} poetry run green -vvvq tests/unit

test-integration:          ## Run integration tests
	@rm -f ${INTEG_DB_NAME}
	@LOG_LEVEL=${TEST_LOG_LEVEL} SQLITE_DB_NAME=${INTEG_DB_NAME} poetry run green -vvvq -s 1 tests/integration

tests:                     ## Run all tests
	@make --no-print-directory test-unit
	@make --no-print-directory test-integration

coverage:                  ## Code coverage
	@rm -f ${INTEG_DB_NAME}
	@LOG_LEVEL=${TEST_LOG_LEVEL} SQLITE_DB_NAME=${INTEG_DB_NAME} poetry run green -vvvq -s 1 --run-coverage tests/

report-test-unit:          ## Generate junit report for unit tests
	@LOG_LEVEL=${TEST_LOG_LEVEL} poetry run python -m xmlrunner discover -o ./reports/junit/tests/unit tests/unit/

report-test-integration:   ## Generate junit report for integration tests
	@LOG_LEVEL=${TEST_LOG_LEVEL} poetry run python -m xmlrunner discover -o ./reports/junit/tests/integration tests/integration/

report-test:               ## Generate junit report for tests
	@make report-test-unit
	@make report-test-integration

report-lint:               ## Generate text and junit report for linting
	@poetry run flake8 . --output-file=reports/flake8.txt
	@poetry run flake8_junit reports/flake8.txt reports/junit/lint/flake8_junit.xml

# #
# #Docker
# #

#docker-build:              # # Build docker image
#	@docker build -t {{cookiecutter.package_name}}:latest .

#docker-run-be-dev:         # # Run backend in foreground using docker, in development mode
#	@UVICORN_EXTRA_PARAMS="--reload" docker run --rm -it -p 3380:3380 {{cookiecutter.package_name}}:latest run-be-dev

##
##CI Related and Bootstrapping
##

project-init:              ## Initializes virtual environment for this project
	@python -m venv .venv
	@source .venv/bin/activate && pip install -U pip && pip install "poetry>1.8" && poetry install
