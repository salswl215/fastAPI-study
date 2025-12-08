### FastAPI Dependency Injection

#### 1) Dependency Ingestion 개요

- 개발된 함수 또는 객체의 호출을 개발자가 만든 로직내에서 수행하지 않고, FastAPI 가 직접 수행
- 정교한 모듈화로 코드내에서 인프라/프레임워크 전용의 로직과 업무처리 로직을 더 편리하게 분리할 수 있도록 함
- FastAPI는 이를 위해 `Depends()` 함수를 제공하여 `Depends()` 함수는 인자로 함수 또는 Callable Object를 입력 받음
- FastAPI는 내부적으로 Dependency Ingestion을 잘 활용하는 Framework
    - Form(), Query(), Path(), Cookie() 등은 FastAPI가 내부적으로 지원하는 DI object들


```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_message():
    return "Hello Dependency!"

@app.get("/hello")
def read_hello(message: str = Depends(get_message)):
    return {"msg": message}
```


#### 2) Dependency Ingestion 반드시 사용?
- Custom 함수 / Callable Object를 Depends를 이용하여 DI 적용 시, Endpoint 수행 함수들에 반복 적용 필요
- Endpoint 수행 함수내에서 개발 코드로 직접 함수를 호출하는 것과 큰 차이가 없을 수 있음.
- Depends는 Context Manager 기능을 함께 가지고 있으므로 DB 자원의 해제(Release) 등의 적용을 보다 간결히 할 수 있으므로 이 경우는 Depends를 사용하는 것이 보다 효율적임