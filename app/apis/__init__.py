import pkgutil
from importlib import import_module
from pathlib import Path

from flask import Flask, Blueprint
from flask_restx import Api


def init(app: Flask):
    root_pkg = Path(__file__).parent
    blueprint = _scan_namespace(root_pkg)
    app.register_blueprint(blueprint)


def _scan_namespace(root_pkg):
    result = Blueprint("api", __name__, url_prefix="/")
    api = Api(result)
    for (file_finder, name, _) in pkgutil.iter_modules([root_pkg]):
        module = import_module(__name__ + "." + name)
        api.add_namespace(module.api)
    return result
