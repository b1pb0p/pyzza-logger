from PyQt6.QtWidgets import QWidget, QVBoxLayout

from ....utilities import EntryListWidget, TabItem


class RecipeFlourTab(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._layout.addWidget(EntryListWidget(self._get_entry_context()))
        self.setLayout(self._layout)

    def _get_entry_context(self):
        return {
            "prefix": TabItem.flour.value,
            "stylesheet": "assets/styles/pages/add/style_recipe_page.qss",
            "min_bound": 0,
            "max_bound": 10000,
            "default_value": 500,
            "fetch_values": self._fetch_values
        }

    @staticmethod
    def _fetch_values():
        # MOCK, TODO: FETCH ACTUAL DATA FROM DB
        return ['One', 'Two', 'Three', 'Four']
