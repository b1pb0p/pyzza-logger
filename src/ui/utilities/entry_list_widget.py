from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from functools import partial

from .expandable_entry_box import ExpandableEntryBox


class EntryListWidget(QWidget):
    def __init__(self, context):
        super().__init__()

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._context = context

        self._prefix = self._context["prefix"]
        self._stylesheet = self._context["stylesheet"]
        self._min_bound = self._context["min_bound"]
        self._max_bound = self._context["max_bound"]
        self._default_value = self._context["default_value"]
        self._fetch_values = self._context["fetch_values"]

        self._number_of_entries = 0

        self._entries = []
        self.add_entry(removable=False)

        self.add_button = self._initialize_add_button()

        self.setLayout(self._layout)

    def _get_entry_context(self, removable):
        return {
            "prefix": self._prefix,
            "index": self._number_of_entries,
            "stylesheet": self._stylesheet,
            "min_bound": self._min_bound,
            "max_bound": self._max_bound,
            "default_value": self._default_value,
            "removable": removable,
            "fetch_values": self._fetch_values,
            "callback": self.remove_entry
        }

    def add_entry(self, removable=True):
        self._number_of_entries += 1
        entry = ExpandableEntryBox(self._get_entry_context(removable))

        self._entries.append(entry)
        self._layout.insertWidget(self._layout.count() - 1, entry)
        self.adjust_size_to_contents()

    def _initialize_add_button(self):
        button = QPushButton(f"+ Add {self._prefix}")
        button.clicked.connect(partial(self.add_entry, True))
        self._layout.addWidget(button)

        return button

    def remove_entry(self, entry):
        self._entries.remove(entry)
        entry.setParent(None)
        entry.deleteLater()
        self._number_of_entries -= 1
        self.reindex_entries()
        self.adjust_size_to_contents()

    def reindex_entries(self):
        for i, entry in enumerate(self._entries, start=1):
            entry.number = i
            entry.update_labels()

    def adjust_size_to_contents(self):
        self.adjustSize()
        if self.window():
            self.window().adjustSize()
