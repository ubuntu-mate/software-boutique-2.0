from typing import Optional
from PyQt5.QtWidgets import QAction, QWidget
import qtawesome as qta

class ToolbarAction(QAction):

    def __init__(self, label: str, category: str, char: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(chr(char), parent)
        self.label = label
        self.category = category
        self.setCheckable(True)
        self.setData(category)
        self.setFont(qta.font('fa', 24))
        self.setToolTip(label)

    ACCESSORIES = lambda: ToolbarAction("Accessories", "accessories", 0xf0c4)
    EDUCATION = lambda: ToolbarAction("Education", "education", 0xf19d)
    GAMES = lambda: ToolbarAction("Games", "games", 0xf11b)
    GRAPHICS = lambda: ToolbarAction("Graphics", "graphics", 0xf03e)
    INTERNET = lambda: ToolbarAction("Internet", "internet", 0xf0ac)
    OFFICE = lambda: ToolbarAction("Office", "office", 0xf080)
    PROGRAMMING = lambda: ToolbarAction("Programming", "development", 0xf121)
    SOUND_VIDEO = lambda: ToolbarAction("Sound & Video", "multimedia", 0xf008)
    SYSTEM_TOOLS = lambda: ToolbarAction("System Tools", "system", 0xf013)
    UNIVERSAL_ACCESS = lambda: ToolbarAction("Universal Access", "accessibility", 0xf193)
    SERVERS = lambda: ToolbarAction("Servers", "server", 0xf233)
    MORE_SOFTWARE = lambda: ToolbarAction("More Software", "more-software", 0xf019)
    FIXES = lambda: ToolbarAction("Fixes", "fixes", 0xf046)
