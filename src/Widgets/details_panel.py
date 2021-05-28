import typing
from typing import Dict

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QWidget

class DetailsPanelLayout(QGridLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setVerticalSpacing(0)
        self.setHorizontalSpacing(0)
        self.setColumnStretch(1, 1)
        self.row = 0

    def addDetails(self, label: QWidget, value: QWidget) -> None:
        first_row_item = " first-row-item" if self.row == 0 else ""
        css_class = f"row-item{first_row_item}"

        label.setProperty("class", css_class)
        self.addWidget(label, self.row, 0)
        
        value.setProperty("class", css_class)
        self.addWidget(value, self.row, 1)

        self.row += 1


class DetailsPanel(QWidget):
    def __init__(self, package: Dict, parent: QWidget = None) -> None:
        super().__init__(parent=parent)

        self.package = package

        self.createComponents()
        self.addListeners()

    def createComponents(self) -> None:
        lic = "Proprietary" if self.package['proprietary'] else "Open Source"
        url = self.package['urls']['info']
        
        layout = DetailsPanelLayout()

        label = QLabel("License")
        value = QLabel(lic)
        layout.addDetails(label, value)

        label = QLabel("Website")
        value = QLabel(url)
        layout.addDetails(label, value)

        self.setLayout(layout)
        self.setVisible(True)

    def addListeners(self) -> None:
        pass
