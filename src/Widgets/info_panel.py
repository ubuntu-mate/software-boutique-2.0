from typing import Dict
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QGridLayout, QLabel, QPlainTextDocumentLayout, QVBoxLayout, QWidget

import qtawesome as qta

from Widgets.package_buttons import PackageButtons


class InfoPanel(QWidget):

    def __init__(self, package: Dict, description: str, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents(package, description)
        self.addListeners()

    def createComponents(self, package: Dict, description: str) -> None:
        p = self.palette()
        bg_color = p.color(QPalette.Background)
        print(bg_color.name())
        light_bg_color = bg_color.lighter(102)
        print(light_bg_color.name())
        dark_bg_color = bg_color.darker(110)
        print(dark_bg_color.name())
        
        name_widget = QLabel(package['name'], self)
        name_widget.setProperty("class", "package-name")

        description_widget = QLabel(description, self)
        description_widget.setWordWrap(True)

        self.package_buttons = PackageButtons(self)

        lic = "Propietary" if package['proprietary'] else "Open Source"
        url = package['urls']['info']

        layout = QGridLayout()
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)
        layout.setColumnStretch(1, 1)

        l = QLabel("License")
        l.setProperty("class", "row-item first-row-item")
        l.setStyleSheet(f"background-color: {dark_bg_color.name()};")
        layout.addWidget(l, 0, 0)

        l = QLabel(lic)
        l.setProperty("class", "row-item first-row-item")
        l.setStyleSheet(f"background-color: {dark_bg_color.name()};")
        layout.addWidget(l, 0, 1)

        l = QLabel("Website")
        l.setProperty("class", "row-item")
        l.setStyleSheet(f"background-color: {light_bg_color.name()};")
        layout.addWidget(l, 1, 0)

        l = QLabel(url)
        l.setProperty("class", "row-item")
        l.setStyleSheet(f"background-color: {light_bg_color.name()};")
        layout.addWidget(l, 1, 1)

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