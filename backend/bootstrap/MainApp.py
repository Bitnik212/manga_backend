from bootstrap.SubApp import SubApp
from config import AppConfig
from routes.SubAppRoutes import SubAppRoutes


class MainApp(SubApp):

    def __init__(self):
        super().__init__()
        self.config = self._config()

    def _config(self) -> AppConfig:
        app = AppConfig()
        app.title = "Main App"
        app.subclass_name = "ff"
        # app.root_path = "ff"
        return app

