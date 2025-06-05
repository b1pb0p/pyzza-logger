from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QComboBox, QDoubleSpinBox,
    QLineEdit, QPushButton, QSpinBox
)

from ...utilities import ItemType


class AddItemPage(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout(self)
        self._form_layout = QFormLayout()

        self._item_type_combo = self._add_item_type_combo()
        self._fields = self._initialize_item_fields()
        self._nutrition_fields = self._initialize_nutrition_fields()

        self._add_item_button()

        self._current_item = ItemType.flour
        self._update_fields(ItemType.flour)

    def _add_item_type_combo(self):
        widget = QComboBox()
        widget.addItems([item.value for item in ItemType])
        widget.currentTextChanged.connect(self._update_fields)

        self._layout.addWidget(widget)

        return widget

    def _initialize_item_fields(self):
        fields = {
            "manufacturer": QLineEdit(),
            "type": QLineEdit(),
            "grind_level": QLineEdit(),
            "name": QLineEdit(),
            "weight": QDoubleSpinBox(),
            "notes": QLineEdit()
        }

        fields["weight"].setMaximum(500)   # TODO: GET FROM CONFIG

        for label, widget in fields.items():
            self._form_layout.addRow(label.capitalize(), widget)

        self._layout.addLayout(self._form_layout)

        return fields

    def _initialize_nutrition_fields(self):
        nutrition_fields = {
            "calories": QSpinBox(),
            "protein": QDoubleSpinBox(),
            "fiber": QDoubleSpinBox(),
            "carbs": QDoubleSpinBox(),
            "fat": QDoubleSpinBox()
        }

        nutrition_fields["calories"].setMaximum(2000)  # TODO: GET FROM CONFIG
        nutrition_fields["calories"].setSingleStep(1)

        for key, widget in nutrition_fields.items():
            if key != "calories":
                widget.setDecimals(1)
                widget.setSingleStep(0.1)
                widget.setMaximum(1000)
            self._form_layout.addRow(key.capitalize(), widget)

        return nutrition_fields

    def _add_item_button(self):
        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.callback)
        self._layout.addWidget(self.add_button)

    def callback(self):
        print("Item fields:")
        item_data = {}
        visible_keys = self._get_visible_keys()

        for key, widget in self._fields.items():
            if key not in visible_keys:
                continue
            if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                print(f"  {key}: {widget.value()}")
                item_data[key] = widget.value()
                widget.setValue(widget.minimum())
            else:
                print(f"  {key}: {widget.text()}")
                item_data[key] = widget.text()
                widget.clear()

        print("Nutritional context:")

        print(f"Nutrition Item Name: {self._create_nutrition_item_name(item_data)}")

        for key, widget in self._nutrition_fields.items():
            if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                print(f"  {key}: {widget.value()}")
                widget.setValue(widget.minimum())
            else:
                print(f"  {key}: {widget.text()}")
                widget.clear()

    def _create_nutrition_item_name(self, item_data):
        if self._current_item == ItemType.flour.value:
            nutrition_name = f"{item_data.get('manufacturer', '')} {item_data.get('type', '')}".strip()
        elif self._current_item == ItemType.topping.value:
            nutrition_name = f"{item_data.get('name', '')} {item_data.get('manufacturer', '')}".strip()
        elif self._current_item == ItemType.sauce.value:
            nutrition_name = item_data.get("name", "")
        else:
            nutrition_name = ""

        return nutrition_name

    def _get_visible_keys(self):
        if self._current_item == ItemType.sauce.value:
            visible_keys = ["name", "weight", "notes"]
        elif self._current_item == ItemType.topping.value:
            visible_keys = ["name", "weight", "manufacturer"]
        else:  # Flour
            visible_keys = ["manufacturer", "type", "grind_level"]

        return visible_keys

    def _update_fields(self, item_type):
        self._current_item = item_type
        visible_keys = self._get_visible_keys()

        for key in self._fields:
            widget = self._fields[key]
            label = self._form_layout.labelForField(widget)
            widget.setVisible(False)
            if label:
                label.setVisible(False)

        for key in visible_keys:
            widget = self._fields[key]
            label = self._form_layout.labelForField(widget)
            widget.setVisible(True)
            if label:
                label.setVisible(True)
