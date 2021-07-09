from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request

from app.Exceptions import ResponseException
from bootstrap.SubAppVersion import SubAppVersion
from config import AppConfig
from routes.SubAppRoutes import SubAppRoutes


class SubApp:

    def __init__(self):
        self.__subclass_name: str = ""
        self.config: AppConfig or None = None
        self.routes: SubAppRoutes or None = None
        self.versions: list = []
        self.now_version: SubAppVersion or None = None

    def _instance(self) -> FastAPI:
        if self.config is None:
            config = AppConfig()
        else:
            config = self.config
        app = FastAPI(
            title=config.title,
            version=config.version,
            openapi_prefix=config.openapi_prefix,
            description=config.description,
            debug=config.debug,
            servers=config.servers,
            root_path=config.root_path,
            exception_handlers=config.exception_handlers
        )
        self.add_validation_exception_handler(app)
        return app

    def get_instance(self) -> FastAPI:
        return self._instance()

    def add_validation_exception_handler(self, app: FastAPI):
        @app.exception_handler(RequestValidationError)
        async def validation_exception_handler(r: Request, e: RequestValidationError):
            return ResponseException().validation_error(r, e)

    def select_now_version(self, versionn: id(SubAppVersion)) -> None:
        """
        Это нужно чтобы создавать экземпляры с разными версиями

        :param versionn: ссылка на версию
        """
        self.now_version: SubAppVersion = versionn(app_config=self._configure(), now_version=True)

    def __get_subclass_name(self):
        name = str(self.__class__.__name__).replace("App", '').lower()
        self.__subclass_name = name
        return self.__subclass_name

    # getter
    @property
    def subclass_name(self) -> str:
        """
        Отформатированное название класса. Форматирует AppNameApp убирая посленйю App и делает все остальное в ниэнем регистре

        :return: Отформатированное название класса подприложения
        """
        return self.__get_subclass_name()

    # setter
    @subclass_name.setter
    def subclass_name(self, name: str):
        self.__subclass_name = name

    def _configure(self) -> AppConfig:
        """
        Сделать свою конфигурацию подприлжения(SubApp)

        :return: AppConfig
        """
        app = AppConfig()
        app.title = "Default docs"
        app.mount_path = "/"+self.subclass_name
        return app

