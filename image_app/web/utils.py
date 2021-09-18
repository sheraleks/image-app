import io
from typing import Any, Optional

import numpy as np
from aiohttp.web_response import Response
from aiohttp.web import json_response as aiohttp_json_response
from cv2 import imdecode
from webcolors import hex_to_rgb


def count_pixels(image: np.ndarray, hex_color: list[str]) -> int:
    rgb_color = hex_to_rgb(hex_color)
    bgr_color = rgb_color[::-1]
    return np.count_nonzero(np.all(image == bgr_color, axis=2))


def load_image(img_file: io.BufferedRandom):
    return imdecode(np.frombuffer(img_file.read(), np.uint8), 1)


def json_response(data: Any = None, status: str = "ok") -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(
        data={
            "status": status,
            "data": data,
        }
    )


def error_json_response(
    http_status: int,
    status: str = "error",
    message: Optional[str] = None,
    data: Optional[dict] = None,
):
    response_data = {
        "status": status,
    }
    if message:
        response_data["message"] = message
    if data:
        response_data["data"] = data
    return aiohttp_json_response(
        status=http_status,
        data=response_data,
    )
