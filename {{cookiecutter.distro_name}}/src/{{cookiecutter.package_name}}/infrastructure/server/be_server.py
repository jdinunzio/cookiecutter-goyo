from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI

from {{cookiecutter.package_name}}.infrastructure.adapters.config import (
    BE_SERVER_HOST,
    BE_SERVER_NAME,
    BE_SERVER_PORT,
    ENV_TYPE,
    LOG_LEVEL,
)
from {{cookiecutter.package_name}}.infrastructure.adapters.factory import get_factory
from {{cookiecutter.package_name}}.infrastructure.adapters.logger import init_logging
from {{cookiecutter.package_name}}.infrastructure.server.exception_handlers import add_exception_handlers
from {{cookiecutter.package_name}}.infrastructure.server.health_router import router as health_router

if TYPE_CHECKING:
    from starlette.middleware import Middleware


API_PREFIX = "/api/v1"


def include_routers(app: FastAPI) -> None:
    """Add routers to the given FastAPI application.

    Args:
        app: FastAPI application to add routers to.
    """
    routers = [
        health_router,
    ]
    for router in routers:
        app.include_router(router, prefix=API_PREFIX)


def create_app(env_type: str | None = None) -> FastAPI:
    """Create a FastAPI instance with PaymentGateway application.

    Args:
        env_type: Optional name of the factory to use to create concrete instances of the
            interfaces required by use cases.

    Returns:
        FastAPI instance.
    """
    # init main logger
    logger = init_logging(LOG_LEVEL or "debug")
    logger.info(
        "logging initialised",
        extra={"server_name": BE_SERVER_NAME, "log_level": LOG_LEVEL},
    )

    # get factory
    env_type = env_type if env_type is not None else ENV_TYPE
    factory = get_factory(env_type)

    # instrumentation
    # init_sentry()  # noqa: ERA001
    # init_otel()  # noqa: ERA001

    # db init
    uow_service = factory.make_uow_service()
    uow_service.init_db()

    # define fastapi middlewares
    middlewares: list[Middleware] = []

    # create fastapi app, and add services to its state
    app = FastAPI(middlewares=middlewares)
    app.state.factory = factory
    app.state.uow_service = uow_service

    include_routers(app)
    add_exception_handlers(app)
    logger.info(
        "server started",
        extra={"host": BE_SERVER_HOST, "port": BE_SERVER_PORT, "env_type": ENV_TYPE},
    )

    return app


def main() -> None:
    """Run server directly from this module, for testing purposes."""
    app = create_app()
    uvicorn.run(app, host=BE_SERVER_HOST, port=BE_SERVER_PORT)


if __name__ == "__main__":
    main()
