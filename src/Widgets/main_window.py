from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QGroupBox, QLabel, QMainWindow, QScrollArea, QVBoxLayout
from libboutique.services.packagekit.packagekit_service import PackageKitService
from libboutique.services.snap.snap_service import SnapService

from Widgets import MainToolBar



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.create_components()
        self.setMinimumSize(800, 450)
    
    def create_components(self) -> None:
        self.toolbar = MainToolBar()
        self.toolbar.add_listener(self.start_search)
        self.addToolBar(self.toolbar)

        scroll_area = self.build_scroll_area()
        self.setCentralWidget(scroll_area)

    def build_scroll_area(self) -> QScrollArea:
        self.scroll_layout = QVBoxLayout()

        for x in range(30):
            label = QLabel(f"Line {x}")
            self.scroll_layout.addWidget(label)
        scroll_group = QGroupBox()
        scroll_group.setLayout(self.scroll_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_group)
        scroll_area.setBackgroundRole(QPalette.Light)     

        return scroll_area

    def start_search(self) -> None:
        package_name = self.toolbar.search_field.text()

        snap_service = SnapService()
        package_kit_service = PackageKitService()
        snaps = snap_service.search_packages_by_name(package_name)
        debs = package_kit_service.search_packages_by_name(package_name)
        packages = sorted(debs + snaps)

        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()
                self.scroll_layout.removeWidget(item.widget())
        
        for package in packages:
            print(package)
            label = QLabel(f"{package.name} {package.version}")
            self.scroll_layout.addWidget(label)

