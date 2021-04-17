class BaseCommand:

    def publish(self, client, object):
        print(f"client: {client}")
        print(f"object: {object}")

    def _handler(self, action, package_name=None):
        func = getattr(self, action)
        func(package_name)

    def list(self, _):
        packages = self.service.list_installed_packages()
        for package in packages:
            print(package)

    def info(self, package_name):
        if package_name is None:
            raise Exception
        packages = self.service.retrieve_package_information_by_name(package_name)
        for package in packages:
            print(package)

    def install(self, package_name):
        if package_name is None:
            raise Exception
        self.service.install_package(package_name)

    def remove(self, package_name):
        if package_name is None:
            raise Exception
        self.service.remove_package(package_name)
