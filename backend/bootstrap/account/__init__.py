from fastapi import FastAPI

from bootstrap import SubApp
from bootstrap.SubAppVersion import SubAppVersion


class AccountApp(SubApp):

    def __init__(self):
        super().__init__()
        self.versions: list[id(SubAppVersion)] = [SubAppVersion] #TODO
        now_version: SubAppVersion = self.versions[0](app_config=self._configure(), now_version=True)
        self.now_version = now_version
        self.routes = now_version.routes
        self.config = now_version.config
        self.debug = now_version.config.debug

    def _configure(self):
        this = super()._configure()
        return this



