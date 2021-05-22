import json
import os

from PyQt5.QtWidgets import QMainWindow, QWidget

from Widgets.card import Card
from Widgets.central_widget import CentralWidget
from Widgets.main_tool_bar import MainToolBar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.currentCategory = None
        self.search_term = ''

        self.setMinimumSize(800, 450)

        self.createComponents()
        self.addListeners()
        self.loadIndex()
        self.setWindowTitle("Software Boutique")
        self.setStyleSheet(open(os.path.join(os.path.dirname(
            __file__), '../../assets/css/boutique.css')).read())

    def createComponents(self) -> None:
        self.toolbar = MainToolBar(self)
        self.addToolBar(self.toolbar)

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

    def addListeners(self) -> None:
        self.toolbar.onReturnPressed(self._search)
        self.toolbar.actionTriggered.connect(self._filter)

    def loadIndex(self) -> None:
        with open('software-boutique-curated-apps/dist/applications-en.json') as json_file:
            self.index = json.load(json_file)

    def _doSearch(self) -> None:
        _matches = lambda haystack, needle: haystack.lower().find(needle.lower()) > -1

        if self.currentCategory is None:
            packages = [
                package
                for _, packages
                in self.index['categories'].items()
                for _, package
                in packages.items()
                if
                _matches(package['name'], self.search_term)
                or _matches(package['description'], self.search_term)
            ]
        else:
            packages = [
                package
                for _, package
                in self.index['categories'][self.currentCategory].items()
                if _matches(package['name'], self.search_term)
                or _matches(package['description'], self.search_term)
            ]

        #self.central_widget.clear()

        # for package in packages:
        #     card = Card(package, None)
        #     self.central_widget.addCard(card)
        # self.central_widget.addStretch()

        cards = [Card(package, self) for package in packages]
        self.central_widget.addCards(cards)

    def _filter(self, checked: bool, category: str) -> None:
        if checked:
            self.toolbar.uncheckButtonsExcept(category)
            self.currentCategory = category
        else:
            self.currentCategory = None
        self._doSearch()

    def _search(self) -> None:
        self.search_term = self.toolbar.search_field.text()
        self._doSearch()
