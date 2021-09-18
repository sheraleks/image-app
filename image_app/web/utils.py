import io

import numpy as np
from cv2 import imdecode
from webcolors import hex_to_rgb


def count_pixels(image: np.ndarray, hex_color: list[str]) -> int:
    rgb_color = hex_to_rgb(hex_color)
    bgr_color = rgb_color[::-1]
    return np.count_nonzero(np.all(image == bgr_color, axis=2))


def load_image(img_file: io.BufferedRandom):
    return imdecode(np.frombuffer(img_file.read(), np.uint8), 1)
