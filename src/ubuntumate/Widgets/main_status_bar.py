from PyQt5.QtWidgets import QLabel, QStatusBar, QWidget


class MainStatusBar(QStatusBar):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents()

    def createComponents(self) -> None:
        self.status_label = QLabel("Initializing...")
        self.addWidget(self.status_label)
        self.setContentsMargins(10, 10, 10, 10)

    def setStatus(self, status: str) -> None:
        self.status_label.setText(status)
