from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QToolButton, QFormLayout,
    QWidget, QComboBox, QSpinBox
)

from PyQt6.QtCore import Qt

from .style_manager import load_stylesheet


class ExpandableEntryBox(QFrame):
    def __init__(self, context):
        super().__init__()

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setContentsMargins(0, 0, 0, 0)

        self._context = context

        self._prefix = self._context["prefix"]
        self._remove_callback = self._context["callback"]
        self._index = self._context["index"]
        self._stylesheet = load_stylesheet(self._context["stylesheet"])

        self._layout = QVBoxLayout(self)
        self._form = QFormLayout()
        self._header_layout = QHBoxLayout()
        self._toggle_button = self._initialize_toggle_button()
        self._max_height = self._toggle_button.height()

        if self._context["removable"]:
            self._initialize_remove_button()

        self._item_type = self._set_item_type_widget()
        self._item_weight = self._set_item_weight_widget()

        self._content = self._set_layout_content()

    def _initialize_toggle_button(self):
        button = QToolButton()
        button.setText("▼")
        button.setCheckable(True)
        button.setChecked(True)
        button.clicked.connect(self.toggle_view)
        button.setStyleSheet(self._stylesheet)
        self._header_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)

        return button

    def _initialize_remove_button(self):
        button = QToolButton()
        button.setText("−")
        button.clicked.connect(self._request_removal)
        button.setToolTip("Remove this flour entry")
        button.setStyleSheet(self._stylesheet)
        self._header_layout.addStretch()    # TODO: TRY WITHOUT IT
        self._header_layout.addWidget(button)

    def _set_item_type_widget(self):
        item_type = QComboBox()
        item_type.addItems(self._context["fetch_values"]())
        self._form.addRow(f"{self._prefix} {self._index} Type:", item_type)

        return item_type

    def _set_item_weight_widget(self):
        weight = QSpinBox()
        weight.setRange(self._context["min_bound"], self._context["max_bound"])
        weight.setValue(self._context["default_value"])
        self._form.addRow(f"{self._prefix} {self._index} Weight:", weight)

        return weight

    def _set_layout_content(self):
        content = QWidget()
        content.setLayout(self._form)

        self._layout.addLayout(self._header_layout)
        self._layout.addWidget(content)
        self.setLayout(self._layout)

        return content

    def toggle_view(self):
        is_checked = self._toggle_button.isChecked()
        self._toggle_button.setText("▼" if is_checked else "▲")
        self._toggle_button.setStyleSheet(self._stylesheet)
        self._content.setVisible(is_checked)

        if not is_checked:
            self.setMaximumHeight(self._toggle_button.sizeHint().height() + 10)
        else:
            self.setMaximumHeight(self._max_height)
        self.adjust_size_to_contents()

    def adjust_size_to_contents(self):
        self.adjustSize()
        if self.window():
            self.window().adjustSize()

    def _request_removal(self):
        if self._remove_callback:
            self._remove_callback(self)

    def update_labels(self):
        self._form.labelForField(self._item_type).setText(f"{self._prefix} {self._index} Type:")
        self._form.labelForField(self._item_weight).setText(f"{self._prefix} {self._index} Weight:")
