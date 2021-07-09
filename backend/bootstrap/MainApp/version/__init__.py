from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.main import MainRoutes


class MainVersion0(SubAppVersion):
    def __init__(self, app_config: AppConfig = AppConfig(), now_version: bool = False):
        super().__init__(app_config=app_config, now_version=now_version)
        self.config = self._configure(app_config, now_version)
        self.routes = MainRoutes()

