# cookiecutter-goyo

Cookiecutter template to create new, modern python projects.

## Features

* Use of `pyproject.toml` for package configuration.
* Support for clean architecture.
* Developer friendly command invocation with `make`.
* Unit and integration tests with `unittest`, or `green`.
* Linting with `flake8` and `pylint`.
* Typechecking with `mypy`.
* Code coverage with `coverage`.
* Code reformatting with `black`.
* Reporting of test and linting results in `junit`.
* Sane `.gitignore`.

## Pre-Requisites

You can use `pipenv` to install all this packages dependencies:

```bash
pipenv install
```

Alternatively, you can install `cookiecutter` manually:

```bash
pip install cookiecutter
```

## Use

Invoke cookiecutter pointing to this repo, answer some questions, and a new folder
with your project will be created:

```
cookiecutter {path to this project}
```

## Project Structure

This is the structure of your newly created project:

```
+ distro_name
+-- src
| +-- package_name
+-- tests
| +-- unit
| +-- integration
+-- docs
+-- reports
```
