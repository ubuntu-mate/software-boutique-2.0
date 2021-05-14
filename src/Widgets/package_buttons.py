from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget


class PackageButtons(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.createComponents()

    def createComponents(self) -> None:
        self.details_button = QPushButton("Details")

        self.install_button = QPushButton("Install")
        self.install_button.setObjectName("install-button")

        buttons_box_layout = QHBoxLayout()
        buttons_box_layout.addStretch()
        buttons_box_layout.addWidget(self.details_button)
        buttons_box_layout.addWidget(self.install_button)

        self.setLayout(buttons_box_layout)
