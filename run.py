from app import create_app
from config import config


app = create_app(config)

if __name__ == "__main__":
    app.run()
