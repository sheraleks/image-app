import os
import io

import numpy as np
from cv2 import imread, imdecode
from webcolors import hex_to_rgb
from aiohttp import BodyPartReader


def count_pixels(image: np.ndarray, hex_color: list[str]) -> int:
    rgb_color = hex_to_rgb(hex_color)
    bgr_color = rgb_color[::-1]
    return np.count_nonzero(np.all(image == bgr_color, axis=2))


# TODO: ловить эксепшн при некорректном изображении
async def load_image(part: BodyPartReader):
    size = 0
    img_stream = io.BytesIO()
    while True:
        chunk = await part.read_chunk()
        if not chunk:
            break
        size += len(chunk)
        img_stream.write(chunk)
    img_stream.seek(0)
    return imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
