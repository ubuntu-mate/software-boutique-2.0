import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QTextBlock
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from libboutique.services.packagekit.packagekit_service import PackageKitService
from libboutique.services.snap.snap_service import SnapService
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
        self.setStyleSheet(open(os.path.join(os.path.dirname(__file__), '../../assets/css/boutique.css')).read())

    def createComponents(self) -> None:
        self.toolbar = MainToolBar()
        self.addToolBar(self.toolbar)

        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

    def addListeners(self) -> None:
        self.toolbar.onReturnPressed(self._startSearch)

    def loadIndex(self) -> None:
        with open('software-boutique-curated-apps/dist/applications-en.json') as json_file:
            self.index = json.load(json_file)
            self.index.pop('stats', None)
            self.index.pop('supported', None)
            self.index.pop('distro', None)

    def _startSearch(self) -> None:
        search_term = self.toolbar.search_field.text()

        self.central_widget.clear()

        packages = [
            package
            for _, packages
            in self.index.items()
            for _, package
            in packages.items()
            if 
                package["name"].lower().find(search_term.lower()) > -1 
                or package["description"].lower().find(search_term.lower()) > -1
        ]

        for package in packages:
            package_name = package['name']
            description = package['description']
            icon = package['icon']

            icon_widget = QLabel()
            icon_pixmap = QPixmap(f"software-boutique-curated-apps/dist/{icon}")
            icon_widget.setPixmap(icon_pixmap)
            icon_widget.setFixedWidth(40 + icon_pixmap.width())
            icon_widget.setContentsMargins(20, 20, 20, 20)

            name_widget = QLabel(package_name)
            name_widget.setStyleSheet("font-weight: 700;")

            description_widget = QLabel(description)
            description_widget.setWordWrap(True)

            details_button = QPushButton("Details")

            install_button = QPushButton("Install")
            install_button.setObjectName("install-button")

            buttons_box_layout = QHBoxLayout()
            buttons_box_layout.addStretch()
            buttons_box_layout.addWidget(details_button)
            buttons_box_layout.addWidget(install_button)

            buttons_box_widget = QWidget()
            buttons_box_widget.setLayout(buttons_box_layout)

            info_layout = QVBoxLayout()
            info_layout.addWidget(name_widget)
            info_layout.addWidget(description_widget)
            info_layout.addWidget(buttons_box_widget)

            info_group = QWidget()
            info_group.setLayout(info_layout)

            card_layout = QHBoxLayout()
            card_layout.addWidget(icon_widget, 0, QtCore.Qt.AlignTop)
            card_layout.addWidget(info_group, 0, QtCore.Qt.AlignTop)

            card_widget = QWidget()
            card_widget.setLayout(card_layout)

            self.central_widget.addWidget(card_widget)
