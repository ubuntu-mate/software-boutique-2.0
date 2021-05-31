from typing import Dict
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QGridLayout, QLabel, QPlainTextDocumentLayout, QVBoxLayout, QWidget

import qtawesome as qta

from ubuntumate.system_state import SystemState
from .details_panel import DetailsPanel

from .package_buttons import PackageButtons


class InfoPanel(QWidget):

    def __init__(self, package: Dict, description: str, systemState: SystemState, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents(package, description, systemState)
        self.addListeners()

    def createComponents(self, package: Dict, description: str, systemState: SystemState) -> None:
        name_widget = QLabel(package['name'], self)
        name_widget.setProperty("class", "package-name")

        description_widget = QLabel(description, self)
        description_widget.setWordWrap(True)

        self.package_buttons = PackageButtons(self)

        self.details_panel = DetailsPanel(package, systemState, self)
        
        info_layout = QVBoxLayout()
        info_layout.addWidget(name_widget)
        info_layout.addWidget(description_widget)
        info_layout.addWidget(self.package_buttons)
        info_layout.addWidget(self.details_panel)
        self.setLayout(info_layout)

    def addListeners(self) -> None:
        self.package_buttons.details_button.clicked.connect(self.toggleDetailsButton)

    def toggleDetailsButton(self) -> None:
        if self.package_buttons.details_button.isChecked():
            self.details_panel.setVisible(True)
        else:
            self.details_panel.setVisible(False)