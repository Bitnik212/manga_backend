from bootstrap import SubApp
from bootstrap.API.version import APIVersion0
from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.api import APIRoutes


class API(SubApp):

    def __init__(self):
        super().__init__()
        self.subclass_name: str = "api"
        self.versions: list[id(SubAppVersion)] = [APIVersion0]
        now_version: SubAppVersion = self.versions[0](app_config=self._configure(), now_version=True)
        self.now_version = now_version
        self.routes = now_version.routes
        self.config = now_version.config
        self.debug = now_version.config.debug

    def _configure(self):
        app = AppConfig()
        app.title = "API api"
        app.mount_path = "/"+self.subclass_name
        return app
