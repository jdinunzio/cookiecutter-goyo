# cookiecutter-goyo

Cookiecutter template to create new, modern python projects.

## Features

* Use of `pyproject.toml` for package configuration.
* Minimum use of `setup.py` for installing in editable mode.
* Unit and integration tests with `unittest` and `green`.
* Linting with `flake8` and `pylint`.
* Typechecking with `mypy`.
* Code coverage with `coverage`.
* Code reformating with `black`.
* Documentation with `sphinx` using rst and markdown.
* Reporting of test and linting results in `junit`.
* Sane `.gitignore`.

## Pre-Requisits

Install `cookiecutter`

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
