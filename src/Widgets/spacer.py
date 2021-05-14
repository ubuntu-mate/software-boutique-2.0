from PyQt5.QtWidgets import QSizePolicy, QWidget


class Spacer(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
