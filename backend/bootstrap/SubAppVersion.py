from config import AppConfig
from routes.SubAppRoutes import SubAppRoutes


class SubAppVersion:
    """
    Класс для версии подприложения
    """
    def __init__(self, app_config: AppConfig, now_version: bool = False):
        self.version_code: int = 0
        self.version: str = "0.0.0"
        self.version_name: str = "Some version name"
        self.config: AppConfig or None = None
        self.routes: SubAppRoutes or None = None

    def _configure(self, app_config: AppConfig, now_version: bool = False) -> AppConfig:
        return app_config
