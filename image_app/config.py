import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "config" / "config.yml"


def get_config(path: str) -> dict:
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
    return parsed_config


config = get_config(config_path)
config["file_max_size"] *= 1024**2
