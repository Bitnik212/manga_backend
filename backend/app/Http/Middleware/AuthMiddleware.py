from starlette.types import Scope, Receive, Send, ASGIApp

from app.Http.Middleware.CustomMiddleware import CustomMiddleware


class AuthMiddleware(CustomMiddleware):

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.auth = AuthResponder()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        await super().__call__(scope, receive, send)
        exclude_list = self.exclude_list
        if scope['type'] == "http" and (scope['path'] in exclude_list) is False:
            if self.auth.is_valid_token(""):
                print(scope['path'])


class AuthResponder:

    def is_valid_token(self, token: str) -> bool:
        return True
