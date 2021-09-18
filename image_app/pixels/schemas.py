from marshmallow import Schema, fields
from marshmallow.validate import Regexp, OneOf

from image_app.pixels.custom_fields import Image


class BlackWhiteSchema(Schema):
    image = Image(
        required=True,
        type="file",
        description="image file",
    )


class BlackWhiteOkResponseSchema(Schema):
    major_color = fields.Str(required=True, validate=OneOf(["neither", "white", "black", "equal"]))


class CustomColorSchema(BlackWhiteSchema):
    hex_color = fields.Str(
        required=True,
        validate=Regexp(r"^#[a-fA-F0-9]{6}$"),
        description="hex color code",
    )


class CustomColorOkResponseSchema(Schema):
    major_color = fields.Int(required=True)