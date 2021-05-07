from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QSizePolicy, QToolBar, QWidget


class MainToolBar(QToolBar):
    def __init__(self) -> None:
        super().__init__("main")
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.addWidget(spacer)
        self.search_field = QLineEdit()
        #self.search_field.returnPressed.connect(self.button_clicked)
        self.search_field.setMaximumWidth(150)
        self.search_field.setClearButtonEnabled(True)
        icon = QIcon.fromTheme("search-symbolic")
        self.search_field.addAction(icon, QLineEdit.LeadingPosition)
        self.search_field.setPlaceholderText("Search...")
        self.addWidget(self.search_field)
    
    def add_listener(self, listener) -> None:
        self.search_field.returnPressed.connect(listener)
