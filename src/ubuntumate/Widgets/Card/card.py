from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from ubuntumate.system_state import SystemState
from .info_panel import InfoPanel

from .package_icon import PackageIcon


class Card(QWidget):
    def __init__(self, package: dict, systemState: SystemState, parent: QWidget) -> None:
        super().__init__(parent)
        self.package = package
        self.createComponents(package, systemState)
        self.addListeners()
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

    def createComponents(self, package: dict, systemState: SystemState) -> None:

        package_name = package["name"]
        description = package["description"]
        icon = package["icon"]

        icon_widget = PackageIcon(icon, 20, self)
        self.info_panel = InfoPanel(package, description, systemState, self)

        card_layout = QHBoxLayout()
        card_layout.addWidget(icon_widget, 0, Qt.AlignTop)
        card_layout.addWidget(self.info_panel, 0, Qt.AlignTop)

        self.setLayout(card_layout)

    def addListeners(self) -> None:
        def install():
            print(f"Adding {self.package['name']} to the install queue")

        self.info_panel.package_buttons.install_button.clicked.connect(install)
