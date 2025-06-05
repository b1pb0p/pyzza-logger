from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget


class RecipeQuantitiesTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel("Quantities Page")
        layout.addWidget(label)
        self.setLayout(layout)
