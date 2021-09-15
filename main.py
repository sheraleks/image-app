from aiohttp import web

from image_app.web.app import create_app
from image_app.config import config


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, port=config["server"]["port"])
