import os

import numpy as np
from cv2 import imread
from webcolors import hex_to_rgb
from aiohttp import BodyPartReader


# TODO: ловить эксепшн при некорректном изображении
def load_image_np(image_path: str) -> np.ndarray:
    return imread(image_path)


def count_pixels(image: np.ndarray, hex_color: list[str]) -> int:
    rgb_color = hex_to_rgb(hex_color)
    bgr_color = rgb_color[::-1]
    return np.count_nonzero(np.all(image == bgr_color, axis=2))


async def download_file(part: BodyPartReader, download_path: str, filename: str) -> None:
    size = 0
    with open(os.path.join(download_path, filename), 'wb') as f:
        while True:
            chunk = await part.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)
        f.close()
