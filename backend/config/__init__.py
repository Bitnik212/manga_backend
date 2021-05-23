from typing import Optional

from fastapi.exceptions import HTTPException

from app.Exceptions import ResponseException

class APIConfig:

    def __init__(self):
        self.title = "GG"
        self.description = "GG"
        self.debug = True
        self.version = "0.1.0"
        self.version_prefix = "/v"+self.version[0:1]
        self.servers = [
                      # {"url": "https://stag.example.com", "description": "Staging environment"},
                      {"url": "http://0.0.0.0:8000/v0", "description": "Development server. Version "+self.version},
                      # {"url": "http://0.0.0.0:8000/", "description": "Now server. Version "+self.version}
                  ]
        self.root_path = ""
        self.openapi_prefix = ""
        self.exception_handlers = {
                422: ResponseException().validation_error, # Не работает (((((
                404: ResponseException().not_found,
                501: ResponseException().not_impl,
            }


