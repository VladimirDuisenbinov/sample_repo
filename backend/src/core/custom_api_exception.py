from django.http import Http404
from rest_framework import exceptions
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import set_rollback


class CustomApiException(APIException):
    detail = None
    status_code = None

    def __init__(self, status_code, message, err_type="INTERNAL_SERVER_ERROR"):
        CustomApiException.status_code = status_code
        CustomApiException.detail = message
        CustomApiException.err_type = err_type


def custom_exception_handler(exc, context): # noqa: C901

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
        exc.err_type = "NOT_AUTHORIZED"

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header

        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        if isinstance(exc.detail, (list, dict)):
            stack = []
            for key, value in exc.detail.items():
                stack.append((key, value))

            result = []
            while stack:
                cur = stack.pop()
                if isinstance(cur[1], dict):
                    for key, val in cur[1].items():
                        stack.append((key, val))
                elif isinstance(cur[1], list):
                    for item in cur[1]:
                        result.append(str((cur[0])) + ": " + str(item))
                elif isinstance(cur[1], str):
                    result.append(str((cur[0])) + ": " + cur[1])

            data = {"error": {"message": result[0]}}
        else:
            data = {"error": {"message": exc.detail}}

        err_type = "INTERNAL_SERVER_ERROR"
        if hasattr(exc, "err_type"):
            err_type = exc.err_type

        data["error"]["type"] = err_type
        data["status"] = "error"
        set_rollback()

        return Response(data, status=exc.status_code, headers=headers)

    return None


class Exception():
    NOT_FOUND = {
        'message': 'Not found.',
        'type': 'NOT_FOUND'
    }
