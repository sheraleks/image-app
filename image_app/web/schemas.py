from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    http_status = fields.Int(required=True)
    status = fields.Str(required=True)
    message = fields.Str()
    data = fields.Dict()
