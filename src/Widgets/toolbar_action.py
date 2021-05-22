from PyQt5.QtWidgets import QAction, QWidget
import qtawesome as qta

class ToolbarAction(QAction):

    def __init__(self, label: str, category: str, char: int, parent: QWidget) -> None:
        super().__init__(chr(char), parent)
        self.label = label
        self.category = category
        self.setCheckable(True)
        self.setData(category)
        self.setFont(qta.font('fa', 24))
        self.setToolTip(label)

    ACCESSORIES = lambda: ToolbarAction("Accessories", "accessories", 0xf0c4, None)
    EDUCATION = lambda: ToolbarAction("Education", "education", 0xf19d, None)
    GAMES = lambda: ToolbarAction("Games", "games", 0xf11b, None)
    GRAPHICS = lambda: ToolbarAction("Graphics", "graphics", 0xf03e, None)
    INTERNET = lambda: ToolbarAction("Internet", "internet", 0xf0ac, None)
    OFFICE = lambda: ToolbarAction("Office", "office", 0xf080, None)
    PROGRAMMING = lambda: ToolbarAction("Programming", "development", 0xf121, None)
    SOUND_VIDEO = lambda: ToolbarAction("Sound & Video", "multimedia", 0xf008, None)
    SYSTEM_TOOLS = lambda: ToolbarAction("System Tools", "system", 0xf013, None)
    UNIVERSAL_ACCESS = lambda: ToolbarAction("Universal Access", "accessibility", 0xf193, None)
    SERVERS = lambda: ToolbarAction("Servers", "server", 0xf233, None)
    MORE_SOFTWARE = lambda: ToolbarAction("More Software", "more-software", 0xf019, None)
    FIXES = lambda: ToolbarAction("Fixes", "fixes", 0xf046, None)
