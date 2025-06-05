from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt

from functools import partial

from src.configuration import HomePageConfiguration
from src.ui.utilities import load_stylesheet


class HomePage(QWidget):

    def __init__(self, callback):
        super().__init__()

        self._callback = callback
        self._configuration = HomePageConfiguration(ratio=0.5)

        self._button_size = self._configuration.get_button_size()

        self._background = self._set_background()
        self._buttons = []

        self._create_home_layout()
        self.setStyleSheet(load_stylesheet("assets/styles/pages/home/style_home_page.qss"))

    def _create_home_layout(self):
        home_layout = QVBoxLayout()
        home_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.setSpacing(0)

        button = self.__add_mock_button_stub("Query", self._test)
        # button = self._add_button("Query", 185, 413, partial(print, "query"))
        # button = self._add_button("Query", 185, 413, partial(self._proceed_to_page, "query"))
        self._buttons.append(button)
        home_layout.addWidget(button)

        button = self._add_button("Add")
        self._buttons.append(button)
        home_layout.addWidget(button)

    @staticmethod
    def _test():
        print("Query")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._background)

    def set_buttons_visibility(self, show=True):
        [btn.show() for btn in self._buttons] if show else [btn.hide() for btn in self._buttons]

    def _proceed_to_page(self, destination):
        self.set_buttons_visibility(show=False)
        self._callback(destination)

    def _add_button(self, label):
        button = QPushButton(label.capitalize(), self)
        button.setFixedSize(*self._button_size)
        button.move(*self._configuration.get_button_positions(label.lower()))
        button.clicked.connect(partial(self._proceed_to_page, label.lower()))
        font = button.font()
        font.setPointSize(int(40 * self._configuration.ratio()))
        button.setFont(font)
        return button

    def __add_mock_button_stub(self, label, callback):
        button = QPushButton(label.capitalize(), self)
        button.setFixedSize(*self._button_size)
        button.move(*self._configuration.get_button_positions(label.lower()))
        button.clicked.connect(callback)
        font = button.font()
        font.setPointSize(int(40 * self._configuration.ratio()))
        button.setFont(font)
        return button

    def _set_background(self):
        background = QPixmap(str(self._configuration.get_background_image_path()))
        factor = self._configuration.ratio()

        background = background.scaled(
            int(background.width() * factor),
            int(background.height() * factor),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.setFixedSize(background.size())

        return background
