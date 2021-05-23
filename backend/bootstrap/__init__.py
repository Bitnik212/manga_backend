from fastapi import FastAPI, Request
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError

from config import APIConfig
from routes.v0 import APIV0
from app.Exceptions import ResponseException

V0 = APIV0()
Config = APIConfig()
app = FastAPI(
    title=Config.title,
    version=Config.version,
    openapi_prefix=Config.openapi_prefix,
    description=Config.description,
    debug=Config.debug,
    servers=Config.servers,
    root_path=Config.root_path,
    exception_handlers=Config.exception_handlers
    # root_path_in_servers=False
)

# Фикс на обработку валидации
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(r: Request, e: RequestValidationError):
    return ResponseException().validation_error(r, e)

app.include_router(
    V0.about,
    prefix=Config.version_prefix,
)
app.include_router(
    V0.basics,
    prefix=Config.version_prefix,
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


