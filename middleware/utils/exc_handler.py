from fastapi import Request, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError

# routes에서 template 엔진 띄우고 있음 >> main에서 엔진을 routes에서 쓰게하는 방법도 있음!
# but 해당 엔진이 크게 성능 상 영향 없기에 일단 그냥 씀
templates = Jinja2Templates(directory="templates")


async def custom_http_exception_handler(request:Request, exc: StarletteHTTPException):
    return templates.TemplateResponse(
        request=request,
        name="http_error.html",
        context={
            "status_code": exc.status_code,
            "title_message": "불편을 드려 죄송합니다.",
            "detail": exc.detail
        },
        status_code=exc.status_code
    )

async def validation_exception_handler(request:Request, exc: RequestValidationError):
    return templates.TemplateResponse(
        request=request,
        name="validation_error.html",
        context={
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "title_message": "잘못된 값을 입력하였습니다. 제목은 최소 2자 이상, 200자 미만. 내용은 최소 2자 이상 4000자 미만입니다.",
            "detail": exc.errors()
        },
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )