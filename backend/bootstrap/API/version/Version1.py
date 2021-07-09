from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig


class APIVersion1(SubAppVersion):

    def __init__(self, app_config: AppConfig):
        super().__init__(app_config)


