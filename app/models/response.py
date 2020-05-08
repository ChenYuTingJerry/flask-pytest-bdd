from ..utils.converter import StringConverter


class SuccessResponse(dict):
    def __init__(self, data=None):
        super().__init__()
        if data:
            self.update(data)


class ErrorResponse(dict):
    def __init__(self, error=None):
        super().__init__()
        error_code = error.error_code if hasattr(error, "error_code") else error.status
        self.update(
            self.to_payload(error.__class__.__name__, error_code) if error else {}
        )

    @staticmethod
    def to_payload(error_type, error_code=""):
        payload = dict(code=error_code, type=StringConverter.to_snake_case(error_type))
        return payload
