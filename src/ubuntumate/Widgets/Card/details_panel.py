from typing import Dict

from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QWidget
import qtawesome as qta

from ubuntumate.system_state import SystemState

class DetailsPanelLayout(QGridLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setVerticalSpacing(0)
        self.setHorizontalSpacing(0)
        self.setColumnStretch(1, 1)
        self.row = 0

    def addDetails(self, label: QWidget, value: QWidget) -> None:
        first_row_item = " first-row-item" if self.row == 0 else ""
        odd_even_row_item = " even-row-item" if self.row % 2 == 0 else " odd-row-item"
        css_class = f"row-item{first_row_item}{odd_even_row_item}"

        label.setProperty("class", f"row-item-label {css_class}")
        label.setFont(qta.font('fa', 14))
        self.addWidget(label, self.row, 0)
        
        value.setProperty("class", f"row-item-value {css_class}")
        value.setFont(qta.font('fa', 14))
        self.addWidget(value, self.row, 1)

        self.row += 1


class DetailsPanel(QWidget):
    def __init__(self, package: Dict, systemState: SystemState, parent: QWidget = None) -> None:
        super().__init__(parent=parent)

        self.package = package

        self.createComponents(systemState)
        self.addListeners()

    def createComponents(self, systemState: SystemState) -> None:
        lic = "Proprietary" if self.package['proprietary'] else "Open Source"
        url = self.package['urls']['info']
        
        layout = DetailsPanelLayout()

        label = QLabel("License")
        value = QLabel(lic)
        layout.addDetails(label, value)

        label = QLabel("Platform")
        value = QWidget()
        sublayout = QHBoxLayout()
        for arch in self.package['arch']:
            if arch in ["i386", "amd64"]:
                icon = QLabel(chr(0xf109) + f' {arch}')
            elif arch in ["armhf", "arm64"]:
                icon = QLabel(chr(0xf109) + f' {arch}')
            else:
                icon = QLabel(arch)
            if arch == systemState.arch:
                icon.setProperty("class", "current-arch")
            sublayout.addWidget(icon)
        sublayout.addWidget(QWidget(), 1)
        value.setLayout(sublayout)
        layout.addDetails(label, value)

        label = QLabel("Website")
        value = QLabel(f'<a href="{url}">{url}</a>')
        value.setOpenExternalLinks(True)
        layout.addDetails(label, value)

        sources = []
        for method in self.package['methods']:
            if "apt" == method:
                method_arch = systemState.codename if systemState.codename in self.package['apt'] else 'default'
                method_details: Dict = self.package['apt'][method_arch]
                method_source: str = method_details['source']
                if method_source == "universe" or method_source == "main":
                    sources.append("Ubuntu Repository")
                elif "ppa:" == method_source[:4]:
                    user, project = method_source[4:].split("/")
                    link = f'https://launchpad.net/~{user}/+archive/ubuntu/{project}'
                    print(f"link : {link}")
                    sources.append(f'<a href="{link}">{method_source}</a>')
                else:
                    sources.append(f"Unknown source {method_source} for method apt/{method_arch}")
            else:
                sources.append(f"Unknown method {method}")

        label = QLabel("Source")
        value = QLabel(", ".join(sources))
        value.setOpenExternalLinks(True)
        layout.addDetails(label, value)

        self.setLayout(layout)
        self.setVisible(False)

    def addListeners(self) -> None:
        pass


        j = {
            "alternate-to": None,
            "apt": {
                "default": {
                    "install-packages": ["caffeine"],
                    "main-package": "caffeine",
                    "remove-packages": ["caffeine"],
                    "source": "main",
                }
            },
            "arch": ["i386", "amd64", "armhf", "arm64"],
            "description": "Prevents the desktop from becoming idle when an application is running full-screen. A desktop indicator <code>caffeine-indicator</code> supplies a manual toggle, and the command <code>caffeinate</code> can be used to prevent idleness for the duration of any command.",
            "developer-name": "Caffeine Developers",
            "developer-url": "https://launchpad.net/~caffeine-developers",
            "icon": "assets/caffeine.png",
            "launch-cmd": "caffeine-indicator",
            "listed": True,
            "methods": ["apt"],
            "name": "Caffeine",
            "proprietary": False,
            "releases": ["xenial", "zesty", "artful"],
            "screenshots": [],
            "snap": {"name": None},
            "summary": "Temporarily prevent the screensaver from activating or the system from suspending.",
            "urls": {
                "android-app": None,
                "info": "https://launchpad.net/caffeine",
                "ios-app": None,
            },
        }
