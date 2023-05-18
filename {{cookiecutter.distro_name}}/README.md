# {{cookiecutter.distro_name}}

{{cookiecutter.description}}

FIXME: provide a two paragraphs summary of this package

## Development

### Install and Initialization

This package uses `poetry` to handle its dependencies. To use it, you'll need a python installation
with `pip` and `venv` (included in python 3.11). The recommended way to install it is

```bash
git clone {url of the project}
cd {{cookiecutter.distro_name}}
make project-init
```

### Common Task

To interact with the development environment you have three options:

1. Use `make` and any of the predefined targets (see below for more details).
2. Use `poetry run ...` where `...` stands for the tool you want to run.
3. Enable the virtual environment you used with poetry. You'll need to do this every time you
   use a new console.

If you chose (3) and set up your environment using `make project-init`, the way to activate your
virtual environment is:

```bash
source .venv/bin/activate
```

#### Adding New Dependencies

You can use Poetry to manage dependencies:

```bash
# install dev dependencies
poetry add --group dev colorama

# install dependencies
poetry add pandas

# update dependencies
poetry update
```

You can create multiple dependency groups. This projects used `dev`, `test`, and the default group.

#### Makefile Goodies

`Makefile` offers you a lot of commonly used task:

    help:                       Show this help

    Development

    lint:                       Code Linting
    flake:                      Flake-8 and ruff
    docstyle:                   Check Style of docstrings
    typecheck:                  Typecheck
    black-check:                Code checking with black
    black-fix:                  Code formatting with black
    dev-check:                  Run common development checks

    Testing

    test-unit:                  Run unit tests
    test-integration:           Run integration tests
    tests:                      Run all tests
    coverage:                   Code coverage
    report-test-unit:           Generate junit report for unit tests
    report-test-integration:    Generate junit report for integration tests
    report-test:                Generate junit report for tests
    report-lint:                Generate text and junit report for linting

    CI Related and Bootstrapping

    project-init:               Initializes virtual environment for this project


# Links
-----

Project home page

  https://github.com/your-github-user/{{cookiecutter.distro_name}}

Issues tracker

  https://github.com/your-github-user/{{cookiecutter.distro_name}}/issue
