from werkzeug.exceptions import HTTPException


class CustomException(HTTPException):
    def __init__(self, description, status, error_code, message=None):
        self.description = description
        self.status = status
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return self.description


class RouteNotFound(CustomException):
    def __init__(self, description="", **kwargs):
        kwargs["error_code"] = "404.route"
        kwargs["status"] = 400
        kwargs["description"] = description
        super().__init__(**kwargs)


class InvalidQueryParameter(CustomException):
    def __init__(self, name, description="", **kwargs):
        kwargs["error_code"] = f"001524.4.1.400-{name}"
        kwargs["status"] = 400
        kwargs["description"] = description
        super().__init__(**kwargs)


class ServerError(CustomException):
    def __init__(self, description="", **kwargs):
        kwargs["error_code"] = "001524.4.500"
        kwargs["status"] = 500
        kwargs["description"] = description
        super().__init__(**kwargs)
