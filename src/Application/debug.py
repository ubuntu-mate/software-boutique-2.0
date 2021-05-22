
from json import dump
from PyQt5.QtWidgets import QWidget


def dump_widget(w: QWidget, spacer: str = '') -> None:
    print(f"{spacer}{w}")
    for w in w.children():
        dump_widget(w, f"{spacer}  ")
