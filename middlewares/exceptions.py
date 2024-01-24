from base.exception_handler.base_exception import APIException


class MissingHeaderTokenException(APIException):
    message = "MISSING_HEADER_TOKEN"
    error_code = "AUTH401"
    status_code = 401


class InvalidTokenException(APIException):
    message = "MISSING_HEADER_TOKEN"
    error_code = "AUTH402"
    status_code = 401
