from PyQt5.QtWidgets import QApplication
from Widgets import MainWindow

class SoftwareBoutique(QApplication):
    def __init__(self) -> None:
        super().__init__([])
        self.window = MainWindow()
        self.window.show()
