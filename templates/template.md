## Jinja2 Template 엔진


### Template 엔진
- 표현을 위한 Frontend와 로직과 데이터 핸들링을 위한 Backend 처리를 쉽게 분리할 수 있게 해줌
- 유연한 동적 Content 생성, 개발팀과 Designer의 역할을 분리, 소스코드 모듈화 및 재사용성 증대 등의 다양한 장점 지원


### Jinja2 Template
- Python 기반의 가장 대표적인 Template 엔진, FastAPI에서는 내장되어 제공
- Python과 유사한 자신만의 구문을 가짐
- 뛰어난 변환 성능. 첫 변환 시 python bytecode로 변환되고, 비동기 수행을 지원하여 빠른 성능을 가짐.
- 자체적으로 다양한 기능을 지원

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory = "templates")
```

- 주요 구문
    - {{ ... }} : 변수나 표힌식
    - {% ... %} : if 나 for
    - {# ... #} : 주석


### StaticFiles
- 결과값을 동적으로 반환하는 endpoint path와 달리, CSS, JavaScript, Image, 정적 HTML 파일들은 그 내용이 변경되지 않는 정적 파일임
- FastAPI는 이들 Static File들은 Endpoint로 별도로 관리하지 않으며 정적 파일들을 위한 별도의 ASGI 서버를 생성하여 관리하며, 이를 위해 StaticFiles 클래스를 제공

```python
from fastapi.staticfiles import StaticFiles

# url path, StaticFiles의 directory는 물리적인 directory 명, name은 url_for 등에서 참조하는 이름
app.mount("/static", StaticFiles(directory="static"), name = "static") 

```