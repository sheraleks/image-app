from aiohttp.web import Application

from image_app.pixels.views import BlackWhiteView, CustomColorView


def setup_routes(app: Application) -> None:
    app.router.add_view("/black_white", BlackWhiteView)
    app.router.add_view("/custom_color", CustomColorView)