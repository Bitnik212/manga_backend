from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

from app.Exceptions import ResponseException
from bootstrap.MainApp import MainApp
from bootstrap.SubApp import SubApp
from bootstrap.API import API as APIClass

# AppMain = App()
# ConfigMain = AppMain.config
# RoutesMain = AppMain.routes
#
# V0 = RoutesMain.api.v0
# app = AppMain.get_instance()
#
# AppV0 = App(version=0)
# ConfigV0 = AppV0.config
# RoutesV0 = AppV0.routes
# appv0 = AppV0.get_instance()
app_class = MainApp()
app = app_class.get_instance()
app_routes = app_class.routes
app_class.config = app_class.config

# print(app_class.config.subclass_name)

api = APIClass()
api_i = api.get_instance()


def add_validation_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(r: Request, e: RequestValidationError):
        return ResponseException().validation_error(r, e)


add_validation_exception_handler(api_i)
add_validation_exception_handler(app)



#
# appv0.include_router(
#     V0.about,
# )
api_i.include_router(
    api.routes.latest.basics,
)


@api_i.get("/")
def read_root():
    return {"Hello": "World main"}


#
@app.get("/")
def read_root():
    return {"Hello": "World v0"}

app.mount(api.config.mount_path, api_i)

