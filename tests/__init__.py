from aiohttp.test_utils import AioHTTPTestCase
from image_app.web.app import create_app


class AppTestCase(AioHTTPTestCase):

    async def get_application(self):
        return create_app()
