from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QFrame, QGroupBox, QHBoxLayout, QLabel, QLayout, QLineEdit, QPushButton, QScrollArea, QVBoxLayout, QWidget
from libboutique.services.packagekit.packagekit_service import PackageKitService
from libboutique.services.snap.snap_service import SnapService

class BoutiqueWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout = QVBoxLayout()
        top_row = self.build_top_row()
        layout.addWidget(top_row)
        
        scroll_area = self.build_scroll_area()
        layout.addWidget(scroll_area)

        self.setLayout(layout)
        self.setMinimumSize(800, 450)

    def build_top_row(self) -> QWidget:
        layout = QHBoxLayout()
        label = QLabel("Package :")
        layout.addWidget(label)
        self.text_field = QLineEdit()
        self.text_field.returnPressed.connect(self.button_clicked)
        layout.addWidget(self.text_field)
        button = QPushButton("Search")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(button)

        group = QGroupBox()
        group.setLayout(layout)

        return group

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

    def button_clicked(self) -> None:
        package_name = self.text_field.text()

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
        self.text_field.setText("")

if "__main__" == __name__:
    app = QApplication([])
    window = BoutiqueWindow()
    window.show()
    app.exec()
