import uvicorn
from fastapi import FastAPI
from starlette.middleware import Middleware

from {{cookiecutter.package_name}}.infrastructure.adapters.config import (
    ENV_TYPE,
    # BE_SERVER_NAME,
    BE_SERVER_HOST,
    BE_SERVER_PORT,
)
from {{cookiecutter.package_name}}.infrastructure.adapters.factory import get_factory

# from {{cookiecutter.package_name}}.infrastructure.adapters.logger import init_logging
from {{cookiecutter.package_name}}.infrastructure.server.exception_handlers import add_exception_handlers
from {{cookiecutter.package_name}}.infrastructure.server.health_router import router as health_router


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
    env_type = env_type if env_type is not None else ENV_TYPE
    factory = get_factory(env_type)
    # init_logging(ENV_TYPE, BE_SERVER_NAME)
    # init_sentry()
    # init_otel()
    # init_db()

    middlewares: list[Middleware] = []

    # create app
    app = FastAPI(middlewares=middlewares)
    app.state.factory = factory

    include_routers(app)
    add_exception_handlers(app)

    return app


def main() -> None:
    """Run server directly from this module, for testing purposes."""
    app = create_app()
    uvicorn.run(app, host=BE_SERVER_HOST, port=BE_SERVER_PORT)


if __name__ == "__main__":
    main()
