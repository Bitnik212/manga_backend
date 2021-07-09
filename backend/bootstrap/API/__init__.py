from bootstrap import SubApp
from bootstrap.API.version import APIVersion0, APIVersions
from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.api import APIRoutes


class APIApp(SubApp):

    def __init__(self):
        super().__init__()

        self.versions: list[id(SubAppVersion)] = APIVersions().versions
        now_version: SubAppVersion = self.versions[0](app_config=self._configure(), now_version=True)
        self.now_version = now_version
        self.routes = now_version.routes
        self.config = now_version.config
        self.debug = now_version.config.debug

    def _configure(self):
        this = super()._configure()
        this.title = "API service"
        this.mount_path = "/"+self.subclass_name
        return this



