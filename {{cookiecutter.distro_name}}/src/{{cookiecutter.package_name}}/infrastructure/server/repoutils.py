from starlette.requests import Request

from {{cookiecutter.package_name}}.application.interfaces import Factory, UOWService


def uow_service_from_request(
    request: Request,
) -> UOWService:
    """Get UOWService from FastAPI request.

    Args:
        request: HTTP Request.

    Returns:
        UOWService.
    """
    factory: Factory = request.app.state.factory
    uow_service = factory.make_uow_service()
    return uow_service
