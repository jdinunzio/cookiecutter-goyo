from starlette.config import Config

# NOTE: We are using `starlette.config` just for convenience. This code is not web-dependent.
# Config will be read from environment variables and `.env` file, if present

config = Config(".env")

# general configuration
ENV_TYPE = config("ENV_TYPE", default="localtest")  # change me, once "deployment" is done
LOG_LEVEL = config("LOG_LEVEL", default=None)

{%- if cookiecutter.add_fastapi_application | fix_boolean %}
# FAST API
BE_SERVER_NAME = "{{cookiecutter.package_name}}"
BE_SERVER_HOST = config("BE_SERVER_PORT", default="0.0.0.0")
BE_SERVER_PORT = config("BE_SERVER_PORT", cast=int, default=3380)
BE_SERVER_WORKERS = config("BE_SERVER_WORKERS", cast=int, default=1)
{%- endif %}
