import os

from aiohttp import MultipartReader
from aiohttp.web import View, json_response, HTTPBadRequest

from image_app.web.utils import download_file, load_image_np, count_pixels


class BlackWhiteView(View):
    # TODO: поле image обязательно
    async def post(self):
        try:
            reader: MultipartReader = await self.request.multipart()
        except AssertionError as exc:
            raise HTTPBadRequest(reason=exc.args[0])

        download_path = os.path.abspath("image_files")
        async for part in reader:
            if part.name == "image":
                await download_file(part, download_path, part.filename)
                image_path = os.path.join(download_path, part.filename)
        image_np = load_image_np(image_path)
        white_pixels_count = count_pixels(image_np, "#FFFFFF")
        black_pixels_count = count_pixels(image_np, "#000000")
        if white_pixels_count > black_pixels_count:
            major_color = "white"
        elif white_pixels_count < black_pixels_count:
            major_color = "black"
        else:
            major_color = "equal"
        return json_response(
            data={
                "major_color": major_color,
            }
        )


class CustomColorView(View):
    # TODO: поля image и hex_color обязательны
    # TODO: валидация поля hex_color
    async def post(self):
        try:
            reader: MultipartReader = await self.request.multipart()
        except AssertionError as exc:
            raise HTTPBadRequest(reason=exc.args[0])

        download_path = os.path.abspath("image_files")
        async for part in reader:
            if part.name == "image":
                await download_file(part, download_path, part.filename)
                image_path = os.path.join(download_path, part.filename)
            elif part.name == "hex_color":
                hex_color = (await part.read()).decode()
        image_np = load_image_np(image_path)
        pixels_count = count_pixels(image_np, hex_color)
        return json_response(
            data={
                "pixels_count": pixels_count
            }
        )