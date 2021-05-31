import locale as l18n
from typing import SupportsFloat
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QLabel
from pkg_resources import resource_exists, resource_stream, resource_string
import json

class LoadIndexWorker(QObject):

    finished = pyqtSignal(dict)
    progress = pyqtSignal(str)

    def run(self) -> None:
        try:
            locale = l18n.getlocale()[0]
        except Exception:
            print("Could not get system locale information! Falling back to 'en_US'.")
            locale = "en_US"
        print(f"System locale is {locale}")
        if not resource_exists('apps', f'application-{locale}.json'):
            full_locale = locale
            locale = locale.split('_')[0]
            print(f"Could not find applications-{full_locale}.json, trying applications-{locale}.json")
            
        if not resource_exists('apps', f'application-{locale}.json'):
            print(f"Could not find applications-{locale}.json, falling back to 'applications-en.json'.")
            locale = "en"

        index_file = f'applications-{locale}.json'
        self.progress.emit(f"Loading {index_file}") #type: ignore
        print(f"Loading {index_file}")

        json_file = resource_stream('apps', index_file)
        tmp_index = json.load(json_file)

        self.progress.emit(f"Reorganizing {index_file}") #type: ignore

        index = {
            'metadata': {
                'distro': tmp_index['distro'],
                'supported': tmp_index['supported']
            },
            'stats': tmp_index['stats'],
            'categories': {key:value for (key,value) in tmp_index.items() if key not in ['stats', 'distro', 'supported']}
        }

        self.finished.emit(index) #type: ignore
