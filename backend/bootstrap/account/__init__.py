from fastapi import FastAPI

from app.Http.Middleware.AuthMiddleware import AuthMiddleware
from bootstrap import SubApp
from bootstrap.SubAppVersion import SubAppVersion
from bootstrap.account.versions.Version0 import AccountVersion0
from routes.account import AccountRoutes


class AccountApp(SubApp):

    def __init__(self):
        super().__init__()
        self.versions: list[id(SubAppVersion)] = [AccountVersion0]
        now_version: SubAppVersion = self.versions[0](app_config=self._configure(), now_version=True)
        self.now_version = now_version
        self.routes = now_version.routes
        self.config = now_version.config
        self.debug = now_version.config.debug
        self.add_middleware(AuthMiddleware)

    def _configure(self):
        this = super()._configure()
        this.title = "Account API"
        return this



