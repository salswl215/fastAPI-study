from fastapi import FastAPI, Form, status
from typing import Optional
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    RedirectResponse
)

from pydantic import BaseModel

app = FastAPI()

#response_class는 default가 JSONResponse.
#response_class가 HTMLResponse일 경우 아래 코드는?
@app.get("/resp_json/{item_id}", response_class=JSONResponse)
async def response_json(item_id: int, q: str | None = None):
    # status code 기본값은 200
    return JSONResponse(content = {"message": "Hello World",
                                   "item_id": item_id,
                                   "q":q},
                        status_code=status.HTTP_200_OK)


# HTML Response
@app.get("/resp_html/{item_id}", response_class=HTMLResponse)
async def response_html(item_id: int, item_name:Optional[str] = None):
    # status code 기본값은 200
    html_str = f'''
    <html>
    <body>
        <h2>HTML Response</h2>
        <p>item_id: {item_id}</p>
        <p>item_name: {item_name}</p>
    </body>
    </html>
    '''
    return HTMLResponse(html_str, status_code=status.HTTP_200_OK)


# Redirect(Get -> Get)
@app.get("/redirect")
async def redirect_only(comment: str | None = None):
    print(f"redirect {comment}")
    # status code : 307 (temporary redirect)
    return RedirectResponse(url=f"/resp_html/3?item_name={comment}")

# Redirect(Post -> Get)
# 예를 들어 로그인! 로그인 창 > 메인 화면으로
@app.post("/create_redirect")
async def create_item(item_id: int = Form(), item_name: str = Form()):
    print(f"item_id: {item_id} item name: {item_name}")
    # status code : 302 명시 필요
    # 302는 HTTP 스펙 상 GET Method로의 전환을 명시하고 있지 않으나 대부분 302에 대해 GET Method로 전환
    # 303은 HTTP 스펙 상 명확히 GET Method로의 전환을 명시
    # 303을 사용하는 것이 스펙에 따른 정확한 적용 (but 302 써도 무방)
    return RedirectResponse(url=f"/resp_html/{item_id}?item_name={item_name}"
                            , status_code=status.HTTP_303_SEE_OTHER)
