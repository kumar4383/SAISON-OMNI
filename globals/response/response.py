from typing import Any

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK




class PkHttpResponse(Response):
    def __init__(
        self,
        data: Any,
        status: int,
        message: str = "OK",
        meta: dict = None,
        content_type: str = "application/json",
    ):
        super().__init__(
            data={
                "code": status,
                "message": message,
                "data": data,
            },
            status=status,
            content_type=content_type,
        )

