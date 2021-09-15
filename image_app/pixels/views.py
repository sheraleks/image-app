import os

from aiohttp import MultipartReader
from aiohttp.web import View, json_response, HTTPBadRequest

from image_app.web.utils import download_file


class BlackWhiteView(View):
    async def post(self):
        try:
            reader: MultipartReader = await self.request.multipart()
        except AssertionError as exc:
            raise HTTPBadRequest(reason=exc.args[0])

        async for part in reader:
            if part.name == "image":
                await download_file(part, "image_files", part.filename)

        return json_response()


class CustomColorView(View):
    async def post(self):
        return json_response()