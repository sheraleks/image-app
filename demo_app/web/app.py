from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from image_app.config import config
from image_app.web.middlewares import error_middleware
from image_app.web.routes import setup_routes


def create_app():
    app = web.Application(
        middlewares=[error_middleware, validation_middleware],
        client_max_size=config["file_max_size"],
    )
    setup_routes(app)
    setup_aiohttp_apispec(
        app=app,
        title="Image APP",
        version="v1",
        url="/api/docs/json",
        swagger_path="/api/docs",
    )
    return app

