from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget
from pkg_resources import resource_stream, resource_filename


class PackageIcon(QLabel):
    def __init__(self, fileName: str, margin: int, parent: QWidget) -> None:
        super().__init__(parent)

        icon_pixmap = QPixmap(resource_filename('apps', fileName))
        self.setPixmap(icon_pixmap)
        self.setFixedWidth(2 * margin + icon_pixmap.width())
        self.setContentsMargins(margin, margin, margin, margin)