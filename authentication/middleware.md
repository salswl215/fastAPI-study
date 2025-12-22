## FastAPI Middleware

### Middleware 개념
- 미들웨어는 각 HTTP 요청이 라우터(엔드포인트)로 전달되기 전과, 응답이 클라이언트로 나가기 직전에 항상 실행되는 함수/클래스이다.
- 공통 로직(로그 기록, 인증/인가 검사, 처리 시간 측정, 공통 헤더 추가 등)을 한 곳에 모아서 처리할 때 사용한다.


### Middleware 동작
- 클라이언트가 요청을 보내면, 먼저 미들웨어가 요청 객체를 받아 필요한 작업을 수행한다.
- 이어서 `call_next(request)`를 호출해 실제 FastAPI 라우터로 요청을 전달하고, 라우터에서 생성된 응답을 다시 미들웨어가 받아 후처리를 한 뒤 클라이언트로 반환한다.


### FastAPi Middleware
- FastAPI는 Custom Middleware를 생성하고 등록 가능
- Pure ASGI Middleware를 구현하는 방법과 BaseHTTPMiddleware를 상속받아 구현하는 방법이 있음
- BaseHTTPMiddleware 클래스를 상속받고 `dispath()`를 오버라이드 해주는 방법이 훨씬 간단
- `dispath()` 매소드에서 필요한 선처리 작업 수행 후 `call_next()`를 불러서 API 수행함수를 수행 후 Response를 return


```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # 전처리 (예: 로깅, 인증 체크 등)
        response = await call_next(request)
        # 후처리 (예: 공통 헤더 추가)
        response.headers["X-Custom-Header"] = "CustomValue"
        return response

app.add_middleware(CustomMiddleware)

```



## CORS (Cross-Origin Resource Sharing)

### CORS 개념
- 서로 다른 Origin(출처)를 가진 리소스에 대한 접근을 허용할지에 대한 절차 및 정책
- Client는 초기 접속 Orgin(site)이 아닌 다른 서드 파티 API 접근이나 리소스를 참조할 때 브라우저와 해당 서버 간 리소스 허용에 대한 메커니즘을 관리할 수 있도록 해줌.
- Origin은 `프로토콜 + 도메인 + 포트` 조합이고, URL에서 프로토콜, 도메인(Hostname), 포트 중 하나라도 다르면 동일한 Origin이 아닌 것으로 간주


### CORS 동작
- 브라우저는 서버 접속 시 Header에 Origin 정보를 기재하여 접속
- 처음 접속한 서버에서 받은 HTML/Javascript에서 다른 서버로의 리소스 접속을 요청하는 코드가 있을 경우 브라우저는 Header Origin에 처음 접속한 Origin 정보를 담아 해당 서버로 보냄
- 리소스 접속 요청을 받은 타 서버에서 브라우저가 보낸 Origin을 허용할 것인지를 CORS 기반으로 판단하여 허용 가능한 Origin에 대한 리스트를 응답으로 보내고, 브라우저는 이 리스트에 해당 Origin이 있을 경우 Response를 출력


### CORS Preflight Request
- 브라우저는 일부 요청에 대해 먼저 OPTIONS 메서드로 “preflight request”를 보내서, 이 출처/메서드/헤더를 서버가 허용하는지 확인한다.
- 서버가 `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers` 같은 헤더로 허용을 표시하면, 그때 실제 요청을 다시 보내고 응답도 사용할 수 있다.


### FastAPI CORS적용
- CORSMiddleware 클래스를 기본 제공 > Middleware로 등록하여 적용

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://my-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # 허용할 출처 목록
    allow_credentials=True,     # 쿠키/인증정보 허용 여부
    allow_methods=["*"],        # 허용 HTTP 메서드
    allow_headers=["*"],        # 허용 요청 헤더
)
```