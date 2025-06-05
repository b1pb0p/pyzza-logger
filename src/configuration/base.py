import json
from pathlib import Path

from abc import ABC  # , abstractmethod

from .singleton import SingletonMeta


class Configuration(ABC, metaclass=SingletonMeta):

    _ROOT = Path(__file__).resolve()
    _ASSETS_ROOT = _ROOT.parents[2] / "assets"
    _CONFIGURATION_PATH = "configuration"

    def __init__(self, relative_path):
        self._relative_path = relative_path
        self._data = self._load_config()

    def _load_config(self):
        path = self._ASSETS_ROOT / self._CONFIGURATION_PATH / self._relative_path
        if not path.is_file():
            raise FileNotFoundError(f"Config file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
