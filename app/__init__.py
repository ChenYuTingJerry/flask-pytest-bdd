from flask import Flask


def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)

    with app.app_context():
        from . import error

        error.init(app)

        from . import apis

        apis.init(app)
        print(app.url_map)
    return app
