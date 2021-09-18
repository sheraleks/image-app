from marshmallow import fields, ValidationError, pre_load

from image_app.web.utils import load_image


class Image(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        a = load_image(value.file)
        return a

    def _validate(self, value):
        if value is None:
            raise ValidationError("Not a valid image")
