from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QWidget


class SearchField(QLineEdit):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents()

        self.setAttribute(QtCore.Qt.WA_StyledBackground)

    def createComponents(self) -> None:
        self.setMaximumWidth(150)
        self.setClearButtonEnabled(True)
        icon = QIcon.fromTheme("search-symbolic")
        self.addAction(icon, QLineEdit.LeadingPosition)
        self.setPlaceholderText("Search...")        

    def onReturnPressed(self, listener) -> None:
        self.returnPressed.connect(listener)
