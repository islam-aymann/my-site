import json

from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.views import exception_handler as drf_exception_handler


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    args = ", ".join(map(str, args))
    kwargs = ", ".join(map(str, kwargs.items()))
    data = {
        "error_code": "server_error",
        "message": _("Server Error (500)"),
        "additional_info": {
            "basic": "server couldn't get the required information",
            "request": str(request),
            "args": args,
            "kwargs": kwargs,
        },
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def bad_request(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    args = ", ".join(map(str, args))
    kwargs = ", ".join(map(str, kwargs.items()))

    data = {
        "error_code": "bad_request",
        "message": _("Bad Request (400)"),
        "additional_info": {
            "basic": "request has bad information or None",
            "request": str(request),
            "exception": str(exception),
            "args": args,
            "kwargs": kwargs,
        },
    }
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


def not_found(*args, **kwargs):
    """
    Generic 404 error handler.
    """
    args = ", ".join(map(str, args))
    kwargs = ", ".join(map(str, kwargs.items()))

    data = {
        "error_code": "not_found",
        "message": _("Not found (404)"),
        "additional_info": {
            "basic": "requested object/url doesn't exist",
            "args": args,
            "kwargs": kwargs,
        },
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        try:
            error_code = exc.default_code
        except AttributeError:
            error_code = response.status_text.replace(" ", "_").lower()

        try:
            message = exc.message
        except AttributeError:
            try:
                message = exc.default_detail
            except AttributeError:
                message = _("Server Error (500)")

        try:
            additional_info = json.dumps(exc.additional_info, ensure_ascii=False)
        except AttributeError:
            try:
                additional_info = json.dumps(exc.detail, ensure_ascii=False)
            except AttributeError:
                additional_info = json.dumps(response.data, ensure_ascii=False)

        response.data = {
            "error_code": error_code,
            "message": message,
            "additional_info": additional_info,
        }
    return response
