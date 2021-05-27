from functools import partial
from typing import List

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QToolBar, QWidget

from Widgets.search_field import SearchField
from Widgets.spacer import Spacer
from Widgets.toolbar_action import ToolbarAction


class MainToolBar(QToolBar):

    actionTriggered = pyqtSignal(bool, str)

    def __init__(self, parent: QWidget) -> None:
        super().__init__("main", parent)

        self.createComponents()
        self.addListeners()

        self.onReturnPressed = self.search_field.onReturnPressed

        self.setMovable(False)
        self.setFloatable(False)
        self.setObjectName("main-toolbar")

    def createComponents(self) -> None:

        self._actions: List[ToolbarAction] = []

        def createAction(action: ToolbarAction) -> None:
            self._actions.append(action)
            self.addAction(action)

        createAction(ToolbarAction.ACCESSORIES())
        createAction(ToolbarAction.EDUCATION())
        createAction(ToolbarAction.GAMES())
        createAction(ToolbarAction.GRAPHICS())
        createAction(ToolbarAction.INTERNET())
        createAction(ToolbarAction.OFFICE())
        createAction(ToolbarAction.PROGRAMMING())
        createAction(ToolbarAction.SOUND_VIDEO())
        createAction(ToolbarAction.SYSTEM_TOOLS())
        createAction(ToolbarAction.UNIVERSAL_ACCESS())
        createAction(ToolbarAction.SERVERS())
        createAction(ToolbarAction.MORE_SOFTWARE())
        createAction(ToolbarAction.FIXES())

        spacer = Spacer(self)
        self.addWidget(spacer)

        self.search_field = SearchField(self)
        self.addWidget(self.search_field)

    def addListeners(self) -> None:
        for action in self._actions:
            action.triggered.connect(
                partial(self._toolbarActionTriggered, action))

    def _toolbarActionTriggered(self, action: ToolbarAction, checked: bool) -> None:
        self.actionTriggered.emit(checked, action.category)

    def uncheckButtonsExcept(self, exception: str) -> None:
        for action in self._actions:
            if exception != action.data():
                action.setChecked(False)
