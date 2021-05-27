from typing import Dict
from PyQt5.QtWidgets import QGridLayout, QLabel, QVBoxLayout, QWidget

import qtawesome as qta

from Widgets.package_buttons import PackageButtons


class InfoPanel(QWidget):

    def __init__(self, package: Dict, description: str, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents(package, description)
        self.addListeners()

    def createComponents(self, package: Dict, description: str) -> None:
        name_widget = QLabel(package['name'], self)
        name_widget.setProperty("class", "package-name")

        description_widget = QLabel(description, self)
        description_widget.setWordWrap(True)

        self.package_buttons = PackageButtons(self)

        lic = "Propietary" if package['proprietary'] else "Open Source"
        url = package['urls']['info']

        layout = QGridLayout()
        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)
        l = QLabel("License :")
        l.setContentsMargins(0, 10, 0, 10)
        layout.addWidget(l, 0, 0)
        layout.addWidget(QLabel(lic), 0, 1)
        layout.addWidget(QLabel("Website :"), 1, 0)
        layout.addWidget(QLabel(url), 1, 1)

        self.details_panel = QWidget(self)
        self.details_panel.setVisible(False)
        self.details_panel.setLayout(layout)
        
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