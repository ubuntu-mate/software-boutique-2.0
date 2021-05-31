from typing import Dict

from pkg_resources import resource_string
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QLabel, QMainWindow, QStatusBar
from ubuntumate.Widgets.Card.card import Card
from ubuntumate.Widgets.central_widget import CentralWidget
from ubuntumate.Widgets.MainToolbar.main_tool_bar import MainToolBar
from ubuntumate.Widgets.main_status_bar import MainStatusBar
from ubuntumate.Workers.load_index_worker import LoadIndexWorker
from ubuntumate.system_state import SystemState


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.systemState = SystemState()

        self.createComponents()
        self.addListeners()

        self.currentCategory = None
        self.search_term = ""

        width = 900
        height = 600

        self.setMinimumSize(width, height)

        self.setWindowTitle("Software Boutique")
        self.setStyleSheet(
            resource_string('assets.css', 'boutique.css').decode('utf8')
        )
        self.loadIndex()

    def createComponents(self) -> None:
        self.toolbar = MainToolBar(self)
        self.addToolBar(self.toolbar)

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

        self.status_bar = MainStatusBar(self)
        self.setStatusBar(self.status_bar)

    def addListeners(self) -> None:
        self.toolbar.onReturnPressed(self.search)
        self.toolbar.action_triggered.connect(self.filter) #type: ignore
        self.toolbar.search_term_edited.connect(self.search)

    def loadIndex(self) -> None:
        self.t = QThread()
        self.w = LoadIndexWorker()
        self.w.moveToThread(self.t)
        self.t.started.connect(self.w.run)
        self.w.progress.connect(self.show_progress) #type: ignore
        self.w.finished.connect(self.index_loaded) #type: ignore
        self.w.finished.connect(self.t.quit) #type: ignore
        self.w.finished.connect(self.w.deleteLater) #type: ignore
        self.t.finished.connect(self.t.deleteLater)
        self.t.start()

    def show_progress(self, progress: str) -> None:
        self.status_bar.setStatus(progress)

    def index_loaded(self, index: Dict) -> None:
        self.status_bar.setStatus("Software boutique loaded")
        self.index = index

    def doSearch(self) -> None:
        def _matches(haystack, needle):
            return haystack.lower().find(needle.lower()) > -1

        if self.currentCategory is None:
            if len(self.search_term) >= 3:
                packages = [
                    package
                    for _, packages in self.index["categories"].items()
                    for _, package in packages.items()
                    if _matches(package["name"], self.search_term)
                    or _matches(package["description"], self.search_term)
                ]
            else:
                packages = []
        else:
            packages = [
                package
                for _, package in self.index["categories"][self.currentCategory].items()
                if _matches(package["name"], self.search_term)
                or _matches(package["description"], self.search_term)
            ]

        nb_package = len(packages)
        if 0 == nb_package:
            status = "No package found"
        elif 1 == nb_package:
            status = "1 package found"
        else:
            status = f"{nb_package} packages found"
            
        self.status_bar.setStatus(status)

        cards = [Card(package, self.systemState, self) for package in packages]
        self.central_widget.addCards(cards)


    def filter(self, checked: bool, category: str) -> None:
        if checked:
            self.toolbar.uncheckButtonsExcept(category)
            self.currentCategory = category
        else:
            self.currentCategory = None
        self.doSearch()

    def search(self) -> None:
        self.search_term = self.toolbar.search_field.text()
        self.doSearch()
