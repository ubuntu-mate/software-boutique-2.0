from PyQt5.QtWidgets import QToolBar
from Widgets.search_field import SearchField

from Widgets.spacer import Spacer


class MainToolBar(QToolBar):
    def __init__(self) -> None:
        super().__init__("main")

        self.createComponents()

        self.onReturnPressed = self.search_field.onReturnPressed

    def createComponents(self) -> None:
        spacer = Spacer()
        self.addWidget(spacer)

        self.search_field = SearchField()
        self.addWidget(self.search_field)
