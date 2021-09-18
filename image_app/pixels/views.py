from aiohttp.web import View
from aiohttp_apispec import docs, form_schema

from image_app.pixels.schemas import BlackWhiteSchema, CustomColorSchema
from image_app.web.utils import count_pixels, json_response


class BlackWhiteView(View):
    @docs(
        tags=["image"],
        summary="Black or white",
        description="Determines the major pixel color between black and white in the picture",
    )
    @form_schema(BlackWhiteSchema)
    async def post(self):
        image = self.request["form"]["image"]
        white_pixels_count = count_pixels(image, "#FFFFFF")
        black_pixels_count = count_pixels(image, "#000000")
        if not white_pixels_count and not black_pixels_count:
            major_color = "neither"
        elif white_pixels_count > black_pixels_count:
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
    @docs(
        tags=["image"],
        summary="Custom color count",
        description="Counts pixels of color hex_color",
    )
    @form_schema(CustomColorSchema)
    async def post(self):
        form = self.request["form"]
        image = form["image"]
        hex_color = form["hex_color"]
        pixels_count = count_pixels(image, hex_color)
        return json_response(
            data={
                "pixels_count": pixels_count
            }
        )
