.PHONY: help test-unit test-integration tests lint typecheck black-check black-fix coverage
.PHONY: report-test-unit report-test-integration report-test report-lint project-init

# General Configuration
SHELL               := /bin/bash

help:                      ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test-unit:                 ## Run unit tests
	@green tests/unit

test-integration:          ## Run integration tests
	@green tests/integration

tests:                     ## Run all tests
	@make test-unit
	@make test-integration

lint:                      ## Code Linting
	@pylint --rcfile=.pylintrc src tests

flake:                     ## Flake-8
	@flake8 --config=.flake8 src tests

pydocstyle:                ## Check Style of docstrings
	@pydocstyle --config=./.pydocstylerc src/ tests/

typecheck:                 ## Typecheck
	@mypy --config-file .mypy.ini src tests

safety:                    ## Check for security vulnerabilities in current environment
	@safety check

black-check:               ## Code checking with black
	@black --line-length 100 --check --diff src tests

black-fix:                 ## Code formatting with black
	@black --line-length 100 src tests

dev-check:                 ## Run common development checks
	@echo '**** Linting....'
	@make --no-print-directory lint
	@echo -e '\n\n**** Flaking...'
	@make --no-print-directory flake
	@echo -e '\n\n**** Blacking...'
	@make --no-print-directory black-check
	@echo -e '\n\n**** Docstyling...'
	@make --no-print-directory pydocstyle
	@echo -e '\n\n**** Type checking...'
	@make --no-print-directory typecheck
	@echo -e '\n\n**** Unit Testing...'
	@make --no-print-directory test-unit
	@echo -e '\n\n'

coverage:                  ## Code coverage
	@green --run-coverage test/unit

report-test-unit:          ## Generate junit report for unit tests
	@python -m xmlrunner discover -o ./reports/junit/tests/unit tests/unit/

report-test-integration:   ## Generate junit report for integration tests
	@python -m xmlrunner discover -o ./reports/junit/tests/integration tests/integration/

report-test:               ## Generate junit report for tests
	@make report-test-unit
	@make report-test-integration

report-lint:               ## Generate text and junit report for linting
	@flake8 . --output-file=reports/flake8.txt
	@flake8_junit reports/flake8.txt reports/junit/lint/flake8_junit.xml

project-init:              ## Initializes virtual environment for this project
	@python -m venv .venv
	@source .venv/bin/activate && pip install -U pip && pip install poetry && poetry install
