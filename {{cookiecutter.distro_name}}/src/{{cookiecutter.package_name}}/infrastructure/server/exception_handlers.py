from http import HTTPStatus
from typing import cast

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from {{cookiecutter.package_name}}.application.exceptions import UseCaseError


def request_validation_handler(request: Request, error: Exception) -> Response:
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


def use_case_exception_handler(request: Request, error: Exception) -> Response:
    """Handle Use Case exception during FastAPI request processing.

    Args:
        request: HTTP Request that caused the error.
        error: Use Case Exception.

    Returns:
        JSONResponse representing the error.
    """
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"request_url": str(request.url), "message": cast("UseCaseError", error).message},
    )


def generic_exception_handler(request: Request, error: Exception) -> Response:
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
    app.add_exception_handler(UseCaseError, use_case_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
