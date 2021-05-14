from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from Widgets.package_buttons import PackageButtons


class InfoPanel(QWidget):

    def __init__(self, package_name: str, description: str) -> None:
        super().__init__()

        self.createComponents(package_name, description)

    def createComponents(self, package_name: str, description: str) -> None:
        name_widget = QLabel(package_name)
        name_widget.setObjectName("package-name")

        description_widget = QLabel(description)
        description_widget.setWordWrap(True)

        self.package_buttons = PackageButtons()

        info_layout = QVBoxLayout()
        info_layout.addWidget(name_widget)
        info_layout.addWidget(description_widget)
        info_layout.addWidget(self.package_buttons)

        self.setLayout(info_layout)
