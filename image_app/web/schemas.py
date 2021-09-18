from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    status = fields.Str(required=True)
    message = fields.Str()
    data = fields.Dict()


error_docs = {
    413: {"description": "Image is too large", "schema": ErrorResponseSchema},
    422: {"description": "Params values are not as expected", "schema": ErrorResponseSchema},
    500: {"description": "Server error", "schema": ErrorResponseSchema},
}


