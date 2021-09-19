from aiohttp.test_utils import unittest_run_loop

from tests import AppTestCase


class BlackWhiteTestCase(AppTestCase):

    @unittest_run_loop
    async def test_black_image(self):
        black_image = open('tests/test_files/black_image.jpg', 'rb')
        response = await self.client.post(
            "/api/black_white",
            data={
                "image": black_image,
            })
        assert response.status == 200
        response_body = await response.json()
        assert response_body["data"]["major_color"] == "black"

    @unittest_run_loop
    async def test_white_image(self):
        white_image = open('tests/test_files/white_image.png', 'rb')
        response = await self.client.post(
            "/api/black_white",
            data={
                "image": white_image,
            })
        assert response.status == 200
        response_body = await response.json()
        assert response_body["data"]["major_color"] == "white"

    @unittest_run_loop
    async def test_green_image(self):
        green_image = open('tests/test_files/green_image.png', 'rb')
        response = await self.client.post(
            "/api/black_white",
            data={
                "image": green_image,
            })
        assert response.status == 200
        response_body = await response.json()
        assert response_body["data"]["major_color"] == "neither"
