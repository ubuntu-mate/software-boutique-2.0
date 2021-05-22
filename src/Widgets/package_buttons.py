from PyQt5.QtCore import QWaitCondition, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget


class PackageButtons(QWidget):

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents()

    def createComponents(self) -> None:
        self.details_button = QPushButton("Details", self)

        self.install_button = QPushButton("Install", self)
        self.install_button.setProperty("class", "install-button")

        buttons_box_layout = QHBoxLayout()
        buttons_box_layout.addStretch()
        buttons_box_layout.addWidget(self.details_button)
        buttons_box_layout.addWidget(self.install_button)

        self.setLayout(buttons_box_layout)
