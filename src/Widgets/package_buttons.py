from PyQt5.QtCore import QWaitCondition, pyqtSignal
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget
import qtawesome as qta

class PackageButtons(QWidget):

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        text_button_color = QPalette().buttonText().color().name()
        self.up_arrow_icon = qta.icon("fa.angle-double-up", color=text_button_color)
        self.down_arrow_icon = qta.icon("fa.angle-double-down", color=text_button_color)
        self.createComponents()
        self.addListeners()


    def createComponents(self) -> None:
        
        self.details_button = QPushButton(self.up_arrow_icon, "Details", self)
        self.details_button.setProperty("class", "details-button package-button")
        self.details_button.setCheckable(True)

        self.install_button = QPushButton("Install", self)
        self.install_button.setProperty("class", "install-button package-button")

        buttons_box_layout = QHBoxLayout()
        buttons_box_layout.addStretch()
        buttons_box_layout.addWidget(self.details_button)
        buttons_box_layout.addWidget(self.install_button)

        self.setLayout(buttons_box_layout)

    def addListeners(self) -> None:
        self.details_button.clicked.connect(self.toggleDetailsButton)

    def toggleDetailsButton(self) -> None:
        if self.details_button.isChecked():
            print("Showing details")
            self.details_button.setIcon(self.down_arrow_icon)
            self.details_button.setText("Hide")
        else:
            print("Hiding details")
            self.details_button.setIcon(self.up_arrow_icon)
            self.details_button.setText("Details")
