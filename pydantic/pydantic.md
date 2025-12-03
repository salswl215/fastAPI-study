## Pydantic


### Pydantic 개요
- Python에서 type annotation을 활용해 데이터 검증과 설정 관리를 해주는 라이브러리
- 특징
    - 다양하고 빠른 Validation 수행
        - Schema/데이터 타입 검증 및 데이터 값에 대한 검증 수행
        - 정규식 지원 및 다양한 내장 검증 로직 제공
        - Core 검증 로직은 Rust로 제작되어 가장 빠른 파이썬 데이터 검증 라이브러리
    - Serialization 지원 (쉽게 Json이나 Dict 형태로 Serialization 수행)
    - 다양한 Echo 시스템에서 활용되며, 문서화 시스템에서 지원 (FastAPI, HuggingFace, LangChain)


### Pydantic Model 선언 및 생성
- Pydantic 객체는 BaseModel을 상속한 Pydantic Model 클래스에 기반하여 생성. Pydantic Model은 클래스 속성들의 type hint, optional, default 값 등의 schema 구조 및 validation 로직을 선언함
- Pydantic 객체 생성은 해당 클래스 속성값을 생성 인자로 입력하여 생성


```python
class User(BaseModel):
    id: int, 
    name: str,
    email: str,
    age: int | None = None

user = User(id = 10, name="Kim", email = "kim@gmail.com", age = 30)
```


### Pydantic 사용 이유
- Schema 구조, Optional/Mandatory, 데이터 검증 등이 함꼐 통합되어 있으므로 데이터 값 자체만 담는 역할이라던가, 보다 유연한 구조체 성격이 필요할 경우 사용하지 않는 것이 오히려 더 적합
- Client 입력 데이터는 Pydantic으로, RDBMS의 데이터 추출을 담는 경우는 dataclass 가 보다 더 적절