import argh

from ..common import BaseCommand

from libboutique.services.snap.snap_service import SnapService


class SnapCommands(BaseCommand):

    def __init__(self):
        super().__init__()
        self.service = SnapService(self)

    @argh.named("snap")
    @argh.arg("action", choices=["list", "info", "install", "remove"])
    def handler(self, action, package_name=None):
        super()._handler(action, package_name)
