from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit


class SearchField(QLineEdit):
    def __init__(self) -> None:
        super().__init__()

        self.createComponents()

    def createComponents(self) -> None:
        self.setMaximumWidth(150)
        self.setClearButtonEnabled(True)
        icon = QIcon.fromTheme("search-symbolic")
        self.addAction(icon, QLineEdit.LeadingPosition)
        self.setPlaceholderText("Search...")        

    def onReturnPressed(self, listener) -> None:
        self.returnPressed.connect(listener)
