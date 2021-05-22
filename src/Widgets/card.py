from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget
from Widgets.info_panel import InfoPanel

from Widgets.pacakge_icon import PackageIcon


class Card(QWidget):

    def __init__(self, package: dict, parent: QWidget) -> None:
        super().__init__(parent)
        self.package = package
        self.createComponents(package)
        self.addListeners()
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

    def createComponents(self, package: dict) -> None:

        package_name = package['name']
        description = package['description']
        icon = package['icon']

        icon_widget = PackageIcon(icon, 20, self)
        self.info_panel = InfoPanel(package_name, description, self)

        card_layout = QHBoxLayout()
        card_layout.addWidget(icon_widget, 0, Qt.AlignTop)
        card_layout.addWidget(self.info_panel, 0, Qt.AlignTop)

        self.setLayout(card_layout)

    def addListeners(self) -> None:
        def install():
            print(f"Adding {self.package['name']} to the install queue")

        self.info_panel.package_buttons.install_button.clicked.connect(install)

        def showDetails():
            print(f"Showing details for {self.package['name']}")

        self.info_panel.package_buttons.details_button.clicked.connect(
            showDetails)
