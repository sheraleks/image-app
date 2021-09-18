from aiohttp.web import Application

from image_app.pixels.views import BlackWhiteView, CustomColorView


def setup_routes(app: Application) -> None:
    app.router.add_view("/api/black_white", BlackWhiteView)
    app.router.add_view("/api/custom_color", CustomColorView)