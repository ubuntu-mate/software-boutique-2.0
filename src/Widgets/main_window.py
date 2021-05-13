from PyQt5.QtWidgets import QLabel, QMainWindow
from libboutique.services.packagekit.packagekit_service import PackageKitService
from libboutique.services.snap.snap_service import SnapService
from Widgets import MainToolBar
from Widgets.central_widget import CentralWidget

import json


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setMinimumSize(800, 450)

        self.create_components()
        self.addListeners()
        self.loadIndex()

    def create_components(self) -> None:
        self.toolbar = MainToolBar()
        self.addToolBar(self.toolbar)

        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

    def addListeners(self) -> None:
        self.toolbar.onReturnPressed(self._startSearch)

    def loadIndex(self) -> None:
        with open('applications.json') as json_file:
            self.index = json.load(json_file)

    def _startSearch(self) -> None:
        package_name = self.toolbar.search_field.text()

        snap_service = SnapService()
        package_kit_service = PackageKitService()
        snaps = snap_service.search_packages_by_name(package_name)
        debs = package_kit_service.search_packages_by_name(package_name)
        packages = sorted(debs + snaps)

        self.central_widget.clear()

        for package in packages:
            print(package)
            label = QLabel(f"{package.name} {package.version}")
            self.central_widget.addWidget(label)
