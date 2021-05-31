from typing import List
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QWidget

from ubuntumate.Widgets.Card.card import Card


class CentralWidget(QScrollArea):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents()

    def createComponents(self) -> None:
        self.scroll_widget_layout = QVBoxLayout()

        self.scroll_widget = QWidget(self)
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        self.setWidgetResizable(True)
        self.setWidget(self.scroll_widget)

    def addCards(self, cards: List[Card]) -> None:
        while self.scroll_widget_layout.count():
            item = self.scroll_widget_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()
                self.scroll_widget_layout.removeWidget(item.widget())
        for card in cards:
            self.scroll_widget_layout.addWidget(card)
        self.scroll_widget_layout.addStretch()
