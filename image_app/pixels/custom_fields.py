from aiohttp.web_request import FileField
from marshmallow import fields, ValidationError, pre_load

from image_app.web.utils import load_image


class Image(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, FileField):
            raise ValidationError("Must be a file.")
        return load_image(value.file)

    def _validate(self, value):
        if value is None:
            raise ValidationError("Not a valid image.")
