from starlette.responses import JSONResponse


class ResponseBuilder:

    @staticmethod
    def __get_schema(status_code: int, message: str, data: dict or None or str) -> dict:
        return {
            "message": message,
            "statusCode": status_code,
            "data": data
        }

    def success(self, message: str = "Все хорошо", data: dict or None or str = None) -> JSONResponse:
        """
        Когда все хорошо
        """
        return JSONResponse(
            status_code=200,
            content=self.__get_schema(
                status_code=200,
                message=message,
                data=data
            )
        )

    def error(
            self,
            status_code: int = 500,
            message: str = "Все плохо",
            data: dict or None or str = None
    ) -> JSONResponse:
        """
        Когда все плохо
        """
        return JSONResponse(
            status_code=status_code,
            content=self.__get_schema(
                status_code=status_code,
                message=message,
                data=data
            )
        )

    def not_found(self, status_code: int = 404, message: str = "Не нашел(", data: dict or None or str = None) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content=self.__get_schema(
                status_code=status_code,
                message=message,
                data=data
            )
        )

    def not_implemented(self, message: str = "Метод еще не реализован(", data: dict or None or str = None) -> JSONResponse:
        return JSONResponse(
            status_code=501,
            content=self.__get_schema(
                status_code=501,
                message=message,
                data=data
            )
        )
