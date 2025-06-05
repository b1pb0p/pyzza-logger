from .base import Configuration


class HomePageConfiguration(Configuration):

    def __init__(self, ratio=0.5):
        super().__init__("home_page_configuration.json")

        self._ratio = ratio
        self._scale_ratio = self._ratio / self.get_image_factor_ratio()
        self._half_scale_button_positions = self._data["half_scale_button_positions"]

    def get_window_title(self):
        return self._data["window_title"]

    def get_window_icon_path(self):
        return self._ASSETS_ROOT / self._data["window_icon_path"]

    def get_background_image_path(self):
        return self._ASSETS_ROOT / self._data["background_image_path"]

    def get_image_factor_ratio(self):
        return self._data["image_factor_ratio"]

    def get_button_positions(self, button: str):
        x, y = self._half_scale_button_positions[f"{button}_button_positions"]
        return int(x * self._scale_ratio), int(y * self._scale_ratio)

    def get_button_size(self):
        width, height = self._half_scale_button_positions["button_size"]
        return int(width * self._scale_ratio), int(height * self._scale_ratio)

    def scale_ratio(self):
        return self._scale_ratio

    def ratio(self):
        return self._ratio
