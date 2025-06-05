from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from PyQt6.QtGui import QIcon

from src.ui.pages import HomePage, AdditionHandler
from src.configuration import HomePageConfiguration


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self._configuration = HomePageConfiguration()

        self.setWindowTitle(self._configuration.get_window_title())
        self.setWindowIcon(QIcon(str(self._configuration.get_window_icon_path())))

        self._stacked = QStackedWidget()
        self._pages = self._load_pages()

        self._layout = QVBoxLayout()
        self._set_layout()
        self.proceed_to_page("home")

    def proceed_to_page(self, destination):
        widget = self._pages[destination]
        self._stacked.setCurrentWidget(widget)

        if destination == "home":
            widget.set_buttons_visibility(show=True)

    def _load_pages(self):
        pages = {
            "home": HomePage(self.proceed_to_page),
            "add": AdditionHandler(self.proceed_to_page)
        }

        for page in pages.values():
            self._stacked.addWidget(page)

        return pages

    def _set_layout(self):
        self._layout.addWidget(self._stacked)
        self.setLayout(self._layout)
        self._layout.setContentsMargins(0, 0, 0, 0)
