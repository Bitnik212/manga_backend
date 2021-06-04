from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.api import APIRoutes


class APIVersion0(SubAppVersion):

    def __init__(self, app_config: AppConfig = AppConfig(), now_version: bool = False):
        super().__init__(app_config=app_config, now_version=now_version)
        self.config = self._configure(app_config, now_version)
        self.routes = APIRoutes()

    def _configure(self, app_config: AppConfig, now_version: bool = False) -> AppConfig:
        app = app_config
        app.version = "0.0.0"
        if now_version is False:
            app.version = "0.0.1"
            app.mount_path += "/v0"
        return app
