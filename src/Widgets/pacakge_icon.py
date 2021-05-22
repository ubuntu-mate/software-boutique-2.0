from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget


class PackageIcon(QLabel):
    def __init__(self, fileName: str, margin: int, parent: QWidget) -> None:
        super().__init__(parent)

        icon_pixmap = QPixmap(f"software-boutique-curated-apps/dist/{fileName}")
        self.setPixmap(icon_pixmap)
        self.setFixedWidth(2 * margin + icon_pixmap.width())
        self.setContentsMargins(margin, margin, margin, margin)