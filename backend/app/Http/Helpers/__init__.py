from starlette.responses import JSONResponse

class ResponseBuilder:

    @staticmethod
    def _get_response_schema(data: dict, status: int, info: str = "Все хорошо") -> dict:
        """
        Получение шаблона ответа сервера
        :param data:
        :param status:
        :param info:
        :return: dict
        """
        success = False
        if status == 200 or status == 404:
            success = True
        data = {
            "success": success,
            "data": data,
            "info": info
        }
        return data

    def result(self, data: dict, info: str = "Все хорошо", status: int = 200) -> JSONResponse:
        """
        Билдер запроса по шаблону
        :param data: Данные запроса
        :param info: Дополнительная информация
        :param status: статус
        :return: JSONResponse
        """
        data = self._get_response_schema(data=data, status=status, info=info)
        return JSONResponse(status_code=status, content=data)

    def success(self, info: str = "Все хорошо") -> JSONResponse:
        """
        Готовый запрос, когда все хорошо
        :param info: Дополнительная информация
        :return: JSONResponse
        """
        status = 200
        data = self._get_response_schema(data={}, status=status, info=info)
        return JSONResponse(status_code=status, content=data)

    def server_error(self, info: str = "Внутрняя ошибка сервера") -> JSONResponse:
        """
        Готовый запрос, когда все плохо
        :param info: Дополнительная информация
        :return: JSONResponse
        """
        status = 500
        data = self._get_response_schema(data={}, status=status, info=info)
        return JSONResponse(status_code=status, content=data)

    def not_found(self, info: str = "Не нашел") -> JSONResponse:
        """

        :param info: Дополнительная информация
        :return: JSONResponse
        """
        status = 404
        data = self._get_response_schema(data={}, status=status, info=info)
        return JSONResponse(status_code=status, content=data)

    def not_impl(self, info: str = "Метод не готов") -> JSONResponse:
        """

        :param info: Дополнительная информация
        :return: JSONResponse
        """
        status = 501
        data = self._get_response_schema(data={}, status=status, info=info)
        return JSONResponse(status_code=status, content=data)

