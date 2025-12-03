## FastAPI 비동기, 멀티 쓰레드, 멀티 프로세스


### FastAPI 동기/비동기 프로세싱
- 동기(Synchronous) 프로세싱
    - 한 번에 하나의 작업만 처리
    - 작업 A 실행
        → 작업 B 호출
        → 작업 B가 끝날 때까지 작업 A는 반드시 기다림(blocking)
        → 작업 B 응답을 받은 후에 작업 A가 계속 진행됨

- 비동기(Asynchronous) 프로세싱
    - 한 작업이 I/O를 기다리는 동안, 같은 스레드에서 다른 작업을 병렬로 처리
    - 작업 A 실행
        → 작업 B 호출
        → 작업 B가 I/O 대기 상태에 들어가면 바로 A로 제어권 반환
        → 이벤트 루프가 B 작업 완료를 감지하면 A 또는 다른 작업에 결과 전달


- 클라이언트-서버 동기/비동기 처리
    - 동기 : 개별 Client의 Request 처리를 서버가 순차 수행. 먼저 요청된 request 처리가 완료되어야 다음 client의 reqeust 처리 시작
        - 동기 처리의 경우 multi-thread를 이용 but python의 경우 이슈(GIL) 등이 있지...
    - 비동기 : 먼저 들어온 Client의 request 처리를 완료하지 않고도 다음 client의 request 처리를 받아 들일 수 잇음. 단, request 내의 프로세스가 비동기 호출이 되어야 함


### Async 여부에 따른 Event Loop와 ThreadPool 적용
- async def 수행 함수는 비동기 Event Loop를 적용
    - 이벤트 루프에서 직접 실행
    - await 사용 가능
    - I/O 작업에 매우 효율적
    - 이벤트 루프를 블로킹하지 않음

```python
@app.get("/task")
async def run_task():
    result = await long_running_task()
    return result
```

- def 수행 함수는 ThreadPool을 적용
    - FastAPI가 ThreadPoolExecutor(스레드 풀) 에서 실행
    - 이벤트 루프 블로킹 방지
    - CPU-bound 작업에 적합

```python
@app.get("/task")
def run_task():
    time.sleep(20)
    return {"status":"long_running task completed"}
```


### FastAPI에서 멀티 쓰레드/멀티 프로세스

- 멀티스레드 (Multi-thread)
    - 하나의 프로세스 안에서 여러 스레드가 메모리를 공유하며 실행
    - 가볍고 전환 비용이 낮아 빠름
    - 하나의 스레드 오류 → 전체 프로세스 영향
    - I/O bound 작업에 적합 (DB, 파일, 네트워크)
    - Python은 GIL 때문에 CPU 작업 병렬화 X


- 멀티프로세스 (Multi-process)
    - 여러 프로세스를 만들어 메모리를 독립적으로 사용
    - 무겁고 전환 비용이 높음
    - 한 프로세스가 죽어도 다른 프로세스 영향 없음
    - CPU bound 작업에 적합
    - Python은 GIL 영향 없음 → 진짜 병렬 처리 가능


### Uvicorn, Starlette, FastAPI 역할
1. Uvicorn
- Python 기반의 ASGI 웹서버
- ASGI(Asynchronous Server Gateway Interface)는 웹서버와 파이썬 애플리케이션 간의 연동규약이며, 특히 비동기 프로그래밍 수행에 초점
- ASGI 서버는 HTTP(또는 WebSocket) Request를 처리하는 웹서버의 역할을 수행함과 동시에 ASGI 규약을 준수하는 파이썬 애플리케이션을 구동. 비동기적 요청 처리로 많은 동시 접속을 효율적 처리


2. Starlette
- ASGI 기반의 Lightweight, Framework/toolkit
- 웹 애플리케이션 구현을 위한 많은 기반 컴포넌트 제공
- Routing, Middleware, Cookie 등 FastAPI 에 사용되는 많은 기능들이 Starlette 기반하고 있음


3. FastAPI
- 모던, 고성능 웹 Framework. Starlette의 기능에 보다 다양한 편의 기능 추가
- 편리한 Request 처리, Dependency ingestion, Pydantic 통합, 문서 자동화 등의 기능으로 좀 더 편리하게 웹 및 API 애플리케이션 구현을 가능하게 함


4. 구조
```
Client
   ↓
HTTP Request
   ↓
[ Uvicorn (ASGI 서버) ]
   ↓
[ FastAPI ]
   ↓
[ Starlette 기능 기반 라우팅/미들웨어 ]
   ↓
Application Logic → Response
```
