## MVC Architecture (Model–View–Controller)

- MVC(Model–View–Controller)는 애플리케이션의 **관심사 분리(Separation of Concerns)** 를 목적으로 한 소프트웨어 아키텍처 패턴이다.  
- 비즈니스 로직, 사용자 인터페이스, 입력 제어 로직을 각각 분리하여 **유지보수성**, **확장성**, **테스트 용이성**을 높인다.


### Model
- **역할**
  - 애플리케이션의 핵심 데이터와 비즈니스 로직을 담당
  - 데이터 상태를 관리하고 규칙을 적용
- **특징**
  - View나 Controller에 대해 알지 못함 (독립적)
  - DB 접근, 도메인 로직, 검증 로직 포함
- **예시**
  - Entity, DTO, Repository, Service 계층


### View
- **역할**
  - 사용자에게 데이터를 화면(UI)으로 표현
  - Controller로부터 전달받은 데이터를 렌더링
- **특징**
  - 비즈니스 로직을 포함하지 않음
  - Model의 상태를 직접 변경하지 않음
- **예시**
  - HTML, JSP, Thymeleaf
  - React, Vue 컴포넌트


### Controller
- **역할**
  - 사용자 요청(Request)을 처리하고 전체 흐름을 제어
  - Model과 View를 연결하는 중개자 역할
- **특징**
  - 요청 파라미터 검증 및 분기 처리
  - 비즈니스 로직을 직접 수행하지 않고 Model에 위임
- **예시**
  - REST API Controller
  - Web Controller 클래스


## Web Application MVC Architecture


```text
Browser ↔ Controller ↔ Service ↔ DAO ↔ DB
            ↕ 
Browser ← View (JSP / Thymeleaf)
```

- Controller : 웹 애플리케이션의 진입점 / 요청을 해석하고 전체 흐름 제어 / Service 호출 및 View 선택 담당
- Service : 비즈니스 로직 계층 / 여러 DAO를 조합하여 하나의 기능 수행
- DAO(Repository) : 데이터 접근 계층 / DB와 직접 통신
- View : 사용자에게 보여줄 화면 (UI) / Controller가 전달한 데이터를 기반으로 HTML 생성 / Browser로 응답 전송







