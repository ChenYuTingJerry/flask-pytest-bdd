from pytest import fixture

from app import create_app
from config import test_config


@fixture
def client():
    app = create_app(test_config)
    with app.test_client() as client:
        yield client


@fixture
def context():
    class objdict(dict):
        def __getattr__(self, name):
            if name in self:
                return self[name]
            else:
                raise AttributeError("No such attribute: " + name)

        def __setattr__(self, name, value):
            self[name] = value

        def __delattr__(self, name):
            if name in self:
                del self[name]
            else:
                raise AttributeError("No such attribute: " + name)

    yield objdict()
