from rest_framework import status
from rest_framework.exceptions import APIException

from webdev.common import(
    messages as glob_messages
)

class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = glob_messages.INTERNAL_SERVER_ERROR
    default_code = 'internal_server_error'


class VersionNotSupported(APIException):
    status_code = status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    default_detail = glob_messages.VERSION_NOT_SUPPORTED
    default_code = 'version_not_supported'


class ValidationFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = glob_messages.VALIDATION_FAILED
    default_code = 'validation_failed'

