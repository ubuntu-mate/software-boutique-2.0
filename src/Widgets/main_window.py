import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QTextBlock
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from libboutique.services.packagekit.packagekit_service import PackageKitService
from libboutique.services.snap.snap_service import SnapService
from Widgets.card import Card
from Widgets.main_tool_bar import MainToolBar
from Widgets.central_widget import CentralWidget

import json


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setMinimumSize(800, 450)

        self.createComponents()
        self.addListeners()
        self.loadIndex()
        self.setWindowTitle("Software Boutique")
        self.setStyleSheet(open(os.path.join(os.path.dirname(
            __file__), '../../assets/css/boutique.css')).read())

    def createComponents(self) -> None:
        self.toolbar = MainToolBar()
        self.addToolBar(self.toolbar)

        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

    def addListeners(self) -> None:
        self.toolbar.onReturnPressed(self._search)

    def loadIndex(self) -> None:
        with open('software-boutique-curated-apps/dist/applications-en.json') as json_file:
            self.index = json.load(json_file)

    def _search(self) -> None:
        search_term = self.toolbar.search_field.text()

        self.central_widget.clear()

        def matches(haystack, needle):
            return haystack.lower().find(needle.lower()) > -1

        packages = [
            package
            for _, packages
            in self.index['categories'].items()
            for _, package
            in packages.items()
            if
            matches(package['name'], search_term)
            or matches(package['description'], search_term)
        ]

        for package in packages:
            card = Card(package)
            self.central_widget.addWidget(card)
