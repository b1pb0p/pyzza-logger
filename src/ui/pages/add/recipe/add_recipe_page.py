from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from ....utilities import load_stylesheet, TabItem

from .add_recipe_flour import RecipeFlourTab
from .add_recipe_quantities import RecipeQuantitiesTab
from .add_recipe_doughs import RecipeDoughsTab


class RecipePage(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._widgets = self._initialize_tabs_widgets()
        self._tabs = self._initialize_tabs()

        self.setLayout(self._layout)

    @staticmethod
    def _initialize_tabs_widgets():
        return {
            TabItem.flour: RecipeFlourTab(),
            TabItem.quantities: RecipeQuantitiesTab(),
            TabItem.balls: RecipeDoughsTab()
        }

    def _initialize_tabs(self):
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)

        for index, (key, widget) in enumerate(self._widgets.items()):
            tabs.addTab(widget, key.value)
            tabs.setTabEnabled(index, False)
        tabs.setTabEnabled(0, True)

        tabs.setStyleSheet(load_stylesheet("assets/styles/pages/add/style_recipe_page.qss"))
        tabs.tabBar().setTabToolTip(1, "This tab will be enabled when all required data is entered.")

        self._layout.addWidget(tabs)

        return tabs
