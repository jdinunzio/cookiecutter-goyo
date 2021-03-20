# {{cookiecutter.distro_name}}

{{cookiecutter.description}}

FIXME: provide a two paragraphs summary of this package

## Development

### Install and Initialization

This package uses `poetry` to handle its dependencies. To use it, you'll need a python installation
with `pip` and `virtualenv`. The recommended way to install it is

```bash
git clone {url of the project}
cd {{cookiecutter.distro_name}}
make project-init
```

### Common Task

Every time you work with this package, you'll need to activate the virtual environment. If
you followed `Install and Initialization` section, you'll need to do:

```bash
source .venv/bin/activate
```

#### Adding New Dependencies

You can use Poetry to manage dependencies:

```bash
# install dev dependencies
poetry add --dev colorama

# install dependencies
poetry add pandas

# update dependencies
poetry update
```

#### Makefile Goodies

`Makefile` offers you a lot of commonly used task:

	help:                       Show this help
	test-unit:                  Run unit tests
	test-integration:           Run integration tests
	tests:                      Run all tests
	lint:                       Code Linting
	flake:                      Flake-8
	pydocstyle:                 Check Style of docstrings
	typecheck:                  Typecheck
	safety:                     Check for security vulnerabilities in current environment
	black-check:                Code checking with black
	black-fix:                  Code formatting with black
	dev-check:                  Run common development checks
	coverage:                   Code coverage
	docs:                       Build documentation
	report-test-unit:           Generate junit report for unit tests
	report-test-integration:    Generate junit report for integration tests
	report-test:                Generate junit report for tests
	report-lint:                Generate text and junit report for linting
	project-init:               Initializes virtual environment for this project


# Links
-----

Project home page

  https://git.ivxs.uk/{{cookiecutter.distro_name}}

Issues tracker

  https://git.ivxs.uk/{{cookiecutter.distro_name}}/issue
