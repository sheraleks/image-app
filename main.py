from aiohttp import web

from image_app.web.app import create_app
from image_app.config import config
from demo_app.web.app import create_app as create_demo_app


if __name__ == "__main__":
    app = create_app()
    app.add_subapp("/demo", create_demo_app())
    web.run_app(app, port=config["port"])
