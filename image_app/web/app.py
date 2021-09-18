from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from image_app.web.routes import setup_routes


def create_app():
    app = web.Application(
        middlewares=[validation_middleware],
    )
    setup_routes(app)
    setup_aiohttp_apispec(
        app=app,
        title="Image APP",
        version="v1",
        url="/docs/json",
        swagger_path="/docs",
    )
    return app

