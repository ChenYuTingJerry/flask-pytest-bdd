from flask_restx import Resource, Namespace

from ..models.response import SuccessResponse

api = Namespace("Health", path="/health")


@api.route("")
class Health(Resource):
    def get(self):
        return SuccessResponse({"status": "OK"}), 200
