# {{cookiecutter.distro_name}}

{{cookiecutter.description}}

FIXME: provide a two paragraphs summary of this package

## Install and Initialization

This package uses `uv` to handle its dependencies. To use it, you'll need a python installation
with `pip` and `venv` (included in python 3.11 and later). Alternatively, and preferably, you can use
[devenv](https://devenv.sh/) and [direnv](https://direnv.net/).

### Installation with devenv and direnv

If you have `devenv` and `direnv` installed and configured, you just need to `cd` to this directory
and all dependencies will be installed.

### Installation without devenv and direnv

Provided you have `pip`, `venv`, and `just` installed.

```bash
git clone {url of the project}
cd {{cookiecutter.distro_name}}
just project-init
```

## Development

### Common Task

To interact with the development environment you have three options:

1. Use `just` and any of the predefined targets (see below for more details).
2. Use `uv run ...` where `...` stands for the tool you want to run.
3. Enable the virtual environment you used with uv. You'll need to do this every time you
   use a new console.

If you chose (3) and set up your environment using `just project-init`, the way to activate your
virtual environment is:

```bash
source .venv/bin/activate
```

#### Adding New Dependencies

You can use uv to manage dependencies:

```bash
# install dev dependencies
uv add --group dev colorama

# install dependencies
uv add pandas

# update dependencies
uv sync
```

You can create multiple dependency groups. This projects used `dev`, `test`, and the default group.

#### justfile Goodies

`justfile` offers you a lot of commonly used task:
Development and CI set of task. Use `just <<task>>`, where tasks is:


  Available recipes:
      help                    # This help.

      [dev]
      dep-check               # Check the project for dependency relationships.
      dev-check               # Run common development checks.
      docstyle                # Check the project for docstring documentation.
      lint-check              # Check the project for linting issues.
      lint-fix                # Fix linting issues.
      type-check              # Check the project for typing issues.

      [testing]
      coverage                # Run all tests with coverage.
      report-test-integration # Generate junit report for integration tests.
      report-test-unit        # Generate junit report for unit tests.
      report-tests            # Generate junit report for all tests.
      test-integration        # Run integration tests.
      test-unit               # Run unit tests.
      tests                   # Run all tests.
    
    help:                       Show this help


# Links
-----

Project home page

  https://github.com/your-github-user/{{cookiecutter.distro_name}}

Issues tracker

  https://github.com/your-github-user/{{cookiecutter.distro_name}}/issue
