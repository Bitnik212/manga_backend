from starlette.exceptions import HTTPException
from fastapi import Request
from starlette.responses import JSONResponse
from app.Http.Helpers import ResponceBuilder

class ResponceException:

    def not_found(self, r: Request, e: HTTPException) -> JSONResponse:
        return ResponceBuilder().not_found()

    def not_impl(self, r: Request, e: HTTPException) -> JSONResponse:
        return ResponceBuilder().not_impl()

    def handle(self, r: Request, e: HTTPException) -> JSONResponse:
        try:
            data = dict(e.args)
        except:
            data = r.body()
        return ResponceBuilder().result(info=str(e.detail), data=data, status=e.status_code)
        # return JSONResponse(status_code=500, content=e.detail)
