from aiohttp import web

from image_app.web.routes import setup_routes


def create_app():
    app = web.Application()
    setup_routes(app)
    return app

