from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class AddNutritionPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        label = QLabel("Nutrition Page")
        layout.addWidget(label)

    # def __init__(self, go_to_callback):
    #     super().__init__()
    #
    #     layout = QVBoxLayout()
    #     label = QLabel("Nutrition Page")
    #     layout.addWidget(label)
