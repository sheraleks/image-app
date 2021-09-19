from aiohttp.test_utils import unittest_run_loop

from tests import AppTestCase


class CustomColorTestCase(AppTestCase):

    @unittest_run_loop
    async def test_black_image(self):
        black_image = open('tests/test_files/black_image.jpg', 'rb')
        response = await self.client.post(
            "/api/custom_color",
            data={
                "image": black_image,
                "hex_color": "#000000",
            })
        assert response.status == 200
        response_body = await response.json()
        assert response_body["data"]["pixels_count"] == 29103

    @unittest_run_loop
    async def test_white_image(self):
        white_image = open('tests/test_files/white_image.png', 'rb')
        response = await self.client.post(
            "/api/custom_color",
            data={
                "image": white_image,
                "hex_color": "#ffffff",
            })
        assert response.status == 200
        response_body = await response.json()
        assert response_body["data"]["pixels_count"] == 228960

    @unittest_run_loop
    async def test_green_image(self):
        green_image = open('tests/test_files/green_image.png', 'rb')
        response = await self.client.post(
            "/api/custom_color",
            data={
                "image": green_image,
                "hex_color": "#30ac36",
            })
        assert response.status == 200
        response_body = await response.json()
        assert response_body["data"]["pixels_count"] == 18480
