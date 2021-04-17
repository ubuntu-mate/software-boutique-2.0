import argh

from ..common import BaseCommand

from libboutique.services.packagekit.packagekit_service import PackageKitService


class AptCommands(BaseCommand):

    def __init__(self):
        super().__init__()
        self.service = PackageKitService(self)

    @argh.named("apt")
    @argh.arg("action", choices=["list", "info", "install", "remove"])
    def handler(self, action, package_name=None):
        super()._handler(action, package_name)
