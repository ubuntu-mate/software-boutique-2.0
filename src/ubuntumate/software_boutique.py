from PyQt5.QtWidgets import QApplication
from ubuntumate.Widgets.main_window import MainWindow
from ubuntumate.system_state import SystemState

class SoftwareBoutique(QApplication):

    systemState: SystemState = SystemState()

    def __init__(self) -> None:
        super().__init__([])
        self.window = MainWindow()
        self.window.show()
