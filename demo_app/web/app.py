import jinja2
from aiohttp import web
import aiohttp_jinja2

from demo_app.web.routes import setup_routes


def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("demo_app/templates"))
    return app

