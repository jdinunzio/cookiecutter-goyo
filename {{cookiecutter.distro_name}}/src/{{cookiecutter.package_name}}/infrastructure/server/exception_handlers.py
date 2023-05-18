from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from {{cookiecutter.package_name}}.application.exceptions import UseCaseException


def request_validation_handler(request: Request, error: RequestValidationError) -> JSONResponse:
    """Handle FastAPI/pydantic RequestValidationErrors during FastAPI request processing.

    Args:
        request: HTTP Request that caused the error.
        error: RequestValidationError.

    Returns:
        JSONResponse representing the error.
    """
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={"request_url": str(request.url), "message": str(error)},
    )


def use_case_exception_handler(request: Request, error: UseCaseException) -> JSONResponse:
    """Handle Use Case during FastAPI request processing.

    Args:
        request: HTTP Request that caused the error.
        error: Use Case Exception.

    Returns:
        JSONResponse representing the error.
    """
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"request_url": str(request.url), "message": error.message},
    )


def generic_exception_handler(request: Request, error: Exception) -> JSONResponse:
    """Handle generic exceptions during FastAPI request processing.

    Args:
        request: HTTP Request that caused the error.
        error: Exception.

    Returns:
        JSONResponse representing the error.
    """
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"request_url": str(request.url), "message": str(error), "errors": []},
    )


def add_exception_handlers(app: FastAPI) -> None:
    """Add exception handlers to the given FastAPI application.

    Args:
        app: FastAPI application to add routers to.
    """
    app.add_exception_handler(RequestValidationError, request_validation_handler)
    app.add_exception_handler(UseCaseException, use_case_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
