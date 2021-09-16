from aiohttp import MultipartReader
from aiohttp.web import View, json_response, HTTPBadRequest

from image_app.web.utils import count_pixels, load_image


class BlackWhiteView(View):
    # TODO: поле image обязательно
    async def post(self):
        try:
            reader: MultipartReader = await self.request.multipart()
        except AssertionError as exc:
            raise HTTPBadRequest(reason=exc.args[0])

        async for part in reader:
            if part.name == "image":
                image_np = await load_image(part)
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
        async for part in reader:
            if part.name == "image":
                image_np = await load_image(part)
            elif part.name == "hex_color":
                hex_color = (await part.read()).decode()
        pixels_count = count_pixels(image_np, hex_color)
        return json_response(
            data={
                "pixels_count": pixels_count
            }
        )