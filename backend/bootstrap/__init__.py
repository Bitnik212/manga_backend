from typing import Optional

from fastapi import FastAPI
from config import APIConfig
# from routes.v0.About import router as about
from routes.v0 import APIV0

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
    # root_path_in_servers=False
)

app.include_router(
    V0.about,
    prefix=Config.version_prefix,
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


