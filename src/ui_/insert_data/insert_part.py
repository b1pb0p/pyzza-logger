from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QSpinBox,
    QVBoxLayout, QPushButton, QDateEdit, QDoubleSpinBox, QFormLayout, QComboBox
)
from PyQt6.QtCore import QDate


class InsertDataPart(QWidget):  # TODO: RENAME IT
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.form = QFormLayout()

        self.flour1_type, self.flour1_weight = self._add_flours_widget("1")
        self.flour2_type, self.flour2_weight = self._add_flours_widget("2")
        self.yeast_type, self.yeast_expiry = self._add_yeast_widget()
        self.yeast_weight = self._add_yeast_weight_widget()
        self.sauce_name, self.sauce_weight = self._add_sauce_widget()
        self.water = self._add_water_widget()
        self.salt = QSpinBox()
        self.form.addRow("Salt (g):", self.salt)
        self.ball_weight, self.num_balls = self._dough_widget()
        self.topping1_name, self.topping1_weight = self._add_toppings_widget("1")
        self.topping2_name, self.topping2_weight = self._add_toppings_widget("2")

        layout.addLayout(self.form)
        self.add_button = QPushButton("Add Recipe")
        self.add_button.clicked.connect(self.print_recipe)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setMinimumWidth(400)

    def _add_flours_widget(self, number):
        flour_type = QComboBox()
        flour_type.addItems(['One', 'Two', 'Three', 'Four'])  # TODO: ADD REAL VALUES, FROM DB
        flour_weight = QSpinBox()
        flour_weight.setValue(500)
        flour_weight.setMaximum(10000)
        self.form.addRow(f"Flour {number} Type:", flour_type)
        self.form.addRow(f"Flour {number} Weight:", flour_weight)

        return flour_type, flour_weight

    def _add_yeast_widget(self):
        yeast_type = QLineEdit()
        yeast_expiry = QDateEdit()
        yeast_expiry.setDate(QDate.currentDate())

        self.form.addRow("Yeast Type:", yeast_type)
        self.form.addRow("Yeast Expiry:", yeast_expiry)

        return yeast_type, yeast_expiry

    def _add_yeast_weight_widget(self):
        yeast_weight = QDoubleSpinBox()
        yeast_weight.setDecimals(2)
        yeast_weight.setMaximum(100)

        self.form.addRow("Yeast (g):", yeast_weight)

        return yeast_weight

    def _add_water_widget(self):
        water = QSpinBox()
        water.setMaximum(1000)

        self.form.addRow("Water (g):", water)

        return water

    def _add_sauce_widget(self):
        sauce_name = QLineEdit()
        sauce_weight = QSpinBox()
        sauce_weight.setMaximum(1000)

        self.form.addRow("Sauce Name:", sauce_name)
        self.form.addRow("Sauce Weight:", sauce_weight)

        return sauce_name, sauce_weight

    def _dough_widget(self):
        ball_weight = QSpinBox()
        ball_weight.setMaximum(1000)
        num_balls = QSpinBox()

        self.form.addRow("Ball Weight (g):", ball_weight)
        self.form.addRow("Number of Balls:", num_balls)

        return ball_weight, num_balls

    def _add_toppings_widget(self, number):
        name = QLineEdit()
        weight = QSpinBox()
        weight.setMaximum(300)

        self.form.addRow(f"Topping {number} Name:", name)
        self.form.addRow(f"Topping {number} Weight:", weight)

        return name, weight

    def add_button(self, label, x, y, callback):
        button = QPushButton(label, self)
        button.setFixedSize(120, 30)
        button.move(x, y)
        button.clicked.connect(callback)

    @staticmethod
    def on_button_clicked(text):
        print(f"{text} button was clicked!")

    def print_recipe(self):
        print("---- Recipe Data ----")
        print(f"Flour 1: {self.flour1_type.currentText()} - {self.flour1_weight.value()}g")
        print(f"Flour 2: {self.flour2_type.currentText()} - {self.flour2_weight.value()}g")
        print(f"Yeast: {self.yeast_type.text()}, Expiry: {self.yeast_expiry.date().toString()}")
        print(f"Sauce: {self.sauce_name.text()} - {self.sauce_weight.value()}g")
        print(f"Topping 1: {self.topping1_name.text()} - {self.topping1_weight.value()}g")
        print(f"Topping 2: {self.topping2_name.text()} - {self.topping2_weight.value()}g")
        print(f"Water: {self.water.value()}g")
        print(f"Salt: {self.salt.value()}g")
        print(f"Yeast weight: {self.yeast_weight.value()}g")
        print(f"Ball weight: {self.ball_weight.value()}g")
        print(f"Num balls: {self.num_balls.value()}")
        print("----------------------")
