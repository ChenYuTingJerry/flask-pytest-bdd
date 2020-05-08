import traceback

from flask import jsonify, Flask
from werkzeug.exceptions import HTTPException

from .models.exception import RouteNotFound, ServerError
from .models.response import ErrorResponse


def handle_http_exception(error):
    print()
    status_code = error.status
    response = ErrorResponse(error)
    return jsonify(response), status_code


def handle_unexpected_exception(error):
    traceback.print_exc()
    response = ErrorResponse(ServerError())
    return jsonify(response), 500


def init(app: Flask):
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(Exception, handle_unexpected_exception)
