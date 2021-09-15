import os

import numpy as np
from cv2 import imread
from webcolors import hex_to_rgb
from aiohttp import BodyPartReader


def count_pixels(image_path: str, hex_color: str) -> int:
    image = imread(image_path)
    rgb_color = hex_to_rgb(hex_color)
    bgr_color = rgb_color[::-1]
    return np.count_nonzero(np.all(image == bgr_color, axis=2))


async def download_file(part: BodyPartReader, download_folder: str, filename: str) -> None:
    size = 0
    with open(os.path.join(os.path.abspath(download_folder), filename), 'wb') as f:
        while True:
            chunk = await part.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)
        f.close()
