from types import FunctionType
from typing import Type
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QApplication, QGroupBox, QLabel, QLineEdit, QMainWindow, QScrollArea, QSizePolicy, QToolBar, QVBoxLayout, QWidget
from libboutique.services.packagekit.packagekit_service import PackageKitService
from libboutique.services.snap.snap_service import SnapService

from Widgets import MainWindow


if "__main__" == __name__:
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
