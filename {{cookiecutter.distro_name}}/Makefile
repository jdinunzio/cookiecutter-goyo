.PHONY: help test-unit test-integration tests lint typecheck black-check black-fix coverage docs
.PHONY: report-test-unit report-test-integration report-test report-lint

# Sphinx Configuration
SPHINXOPTS          =
SPHINXBUILD         = sphinx-build
SPHINXPROJ          = cookiecutterpackage_name
SPHINXSOURCEDIR     = docs
SPHINXBUILDDIR      = docs/_build

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
	@pylint src

typecheck:                 ## Typecheck
	@mypy src/

black-check:               ## Code checking with black
	@black --line-length 100 --check --skip-string-normalization --diff src tests

black-fix:                 ## Code formatting with black
	@black --line-length 100 --skip-string-normalization src tests

coverage:                  ## Code coverage
	@green --run-coverage test/unit

docs:                      ## Build documentation
	@$(SPHINXBUILD) -M html "$(SPHINXSOURCEDIR)" "$(SPHINXBUILDDIR)" $(SPHINXOPTS) $(O)

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

