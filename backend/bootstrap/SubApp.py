from fastapi import FastAPI

from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.SubAppRoutes import SubAppRoutes


class SubApp:

    def __init__(self):
        self.config: AppConfig or None = None
        self.routes: SubAppRoutes or None = None
        self.versions: list = []
        self.now_version: SubAppVersion or None = None

    def _instance(self) -> FastAPI:
        if self.config is None:
            config = AppConfig()
        else:
            config = self.config
        return FastAPI(
            title=config.title,
            version=config.version,
            openapi_prefix=config.openapi_prefix,
            description=config.description,
            debug=config.debug,
            servers=config.servers,
            root_path=config.root_path,
            exception_handlers=config.exception_handlers
        )

    def get_instance(self) -> FastAPI:
        return self._instance()
