from starlette.config import Config

# NOTE: We are using `starlette.config` just for convenience. This code is not web-dependent.
# Config will be read from environment variables and `.env` file, if present

config = Config(".env")

# general configuration
ENV_TYPE = config("ENV_TYPE", default="simple")  # default: simple env, sqlite instead of PG
LOG_LEVEL = config("LOG_LEVEL", default=None)  # throws if not defined
{%- if cookiecutter.add_fastapi_application %}

# FAST API
BE_SERVER_NAME = "{{cookiecutter.package_name}}"
BE_SERVER_HOST = config("BE_SERVER_PORT", default="0.0.0.0")  # noqa: S104
BE_SERVER_PORT = config("BE_SERVER_PORT", cast=int, default=3380)
BE_SERVER_WORKERS = config("BE_SERVER_WORKERS", cast=int, default=1)
{%- endif %}
{%- if cookiecutter.add_repository_and_sqlalchemy %}

# DB
SQLITE_DB_FILE_NAME = config("SQLITE_DB_NAME", default="local.db")  # used only for "simple" env
{%- endif %}
