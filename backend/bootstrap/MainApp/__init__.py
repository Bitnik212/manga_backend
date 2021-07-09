from bootstrap.MainApp.version import MainVersion0
from bootstrap.SubApp import SubApp
from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.SubAppRoutes import SubAppRoutes


class MainApp(SubApp):

    def __init__(self):
        super().__init__()
        self.subclass_name: str = "app" # здесь не имеет смылса так как это главный класс
        self.versions: list[id(SubAppVersion)] = [MainVersion0]
        now_version: SubAppVersion = self.versions[0](app_config=self._config(), now_version=True)
        self.now_version = now_version
        self.routes = now_version.routes
        self.config = now_version.config
        self.debug = now_version.config.debug

    def _config(self) -> AppConfig:
        app = AppConfig()
        app.title = "Main App"
        # app.subclass_name = "ff"
        app.mount_path = "/"+self.subclass_name
        return app

