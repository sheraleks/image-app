import json
from typing import Callable

from aiohttp import web
from aiohttp.web_exceptions import HTTPRequestEntityTooLarge, HTTPUnprocessableEntity, HTTPNotFound, \
    HTTPMethodNotAllowed
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from image_app.web.utils import error_json_response


@web.middleware
async def error_middleware(request: Request, handler: Callable) -> Response:
    try:
        response = await handler(request)
        return response
    except HTTPNotFound as e:
        return error_json_response(
            http_status=404,
            status="not_found",
        )
    except HTTPMethodNotAllowed as e:
        return error_json_response(
            http_status=405,
            status="not_allowed",
        )
    except HTTPRequestEntityTooLarge as e:
        return error_json_response(
            http_status=413,
            status="entity_too_large",
            message=e.text,
        )
    except HTTPUnprocessableEntity as e:
        return error_json_response(
            http_status=422,
            status="unprocessable_entity",
            data=json.loads(e.text),
        )
    except Exception as e:
        return error_json_response(
            http_status=500,
            status="internal_server_error",
            message=str(e),
        )
