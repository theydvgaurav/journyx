from flask import jsonify, Blueprint

from base.exception_handler.base_exception import APIException

error_handler_blueprint = Blueprint('error_handlers', __name__)


@error_handler_blueprint.app_errorhandler(APIException)
def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
