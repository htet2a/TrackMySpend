from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIRECTORY = PROJECT_ROOT / "config"


def load_yaml(filename: str) -> dict:
    """
    Load a YAML file from the project's config directory.
    """

    config_file = CONFIG_DIRECTORY / filename

    with config_file.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}