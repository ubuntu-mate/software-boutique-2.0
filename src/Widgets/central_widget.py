from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget


class CentralWidget(QScrollArea):
    def __init__(self) -> None:
        super().__init__()

        self.createComponents()

    def createComponents(self) -> None:
        self.scroll_widget_layout = QVBoxLayout()

        scroll_widget = QWidget()
        scroll_widget.setLayout(self.scroll_widget_layout)

        self.setWidgetResizable(True)
        self.setWidget(scroll_widget)
        self.setBackgroundRole(QPalette.Light)

    def clear(self) -> None:
        while self.scroll_widget_layout.count():
            item = self.scroll_widget_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()
                self.scroll_widget_layout.removeWidget(item.widget())

    def addWidget(self, widget: QWidget) -> None:
        self.scroll_widget_layout.addWidget(widget)
