from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton, QHBoxLayout

from .add_item_page import AddItemPage
from .add_nutrition_page import AddNutritionPage
# from .add_recipe_page import AddRecipePage

from .recipe import RecipePage as AddRecipePage


class AdditionHandler(QWidget):
    def __init__(self, callback):
        super().__init__()

        self._callback = callback

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._tabs = self._add_tabs()
        self._home_button = self._add_home_button()
        self.setLayout(self._layout)

    def _add_tabs(self):
        tabs = QTabWidget()
        tabs.addTab(AddItemPage(), "Add Item")
        tabs.addTab(AddNutritionPage(), "Add Nutritional value")
        tabs.addTab(AddRecipePage(), "Add Recipe")
        tabs.setTabEnabled(1, False)

        self._layout.addWidget(tabs)

        return tabs

    def _add_home_button(self):
        btn_recipe = QPushButton("Home")
        btn_recipe.clicked.connect(lambda: self._callback("home"))

        button_layout = QHBoxLayout()
        button_layout.addWidget(btn_recipe)

        self._layout.addLayout(button_layout)

        return btn_recipe

    def move_to_tab(self, index):
        self._tabs.setCurrentIndex(index)
