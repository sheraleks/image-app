from marshmallow import Schema, fields, pre_load
from marshmallow.validate import Regexp

from image_app.pixels.custom_fields import Image


class BlackWhiteSchema(Schema):
    image = Image(
        required=True,
        type="file",
        description="image file",
    )


class CustomColorSchema(BlackWhiteSchema):
    hex_color = fields.Str(
        required=True,
        validate=Regexp(r"^#[a-fA-F0-9]{6}$"),
        description="hex color code",
    )
