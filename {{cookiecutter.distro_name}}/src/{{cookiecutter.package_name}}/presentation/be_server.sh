#! /bin/bash

exec /usr/bin/env uvicorn --log-level ${LOG_LEVEL:-warning} \
     ${UVICORN_EXTRA_PARAMS} \
     --workers ${BE_SERVER_WORKERS:-1} \
     --host ${BE_SERVER_HOST:-0.0.0.0} \
     --port ${BE_SERVER_PORT:-3380} \
     --factory "{{cookiecutter.package_name}}.infrastructure.server.be_server:create_app"
