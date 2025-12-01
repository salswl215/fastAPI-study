## HTTP Response

- Client Request에 따른 server에서 내려 보내는 메시지
- 요청 Request의 처리 상태, 여러 메타 정보 그리고 contect 데이터 담고 있음

~~~
HTTP/1.1 200 OK
Date: Mon, 01 Dec 2025 08:30:00 GMT
Content-Type: application/json
Content-Length: 30

{
  "message": "사용자 등록 완료"
}
~~~

1. status-line(상태 라인): HTTP Version과 Response 상태 코드
2. Response Headers: Content Type, 서버 정보등의 다양한 메타 정보
3. Blank Line : Header와 Body 구분
4. Response Body: HTML이나 Json, Image 등의 client에게 전달되는 실질 데이터


## FastAPI Response Class 유형

- JSONResponse : Json 타입 content 전송. Python object을 json format으로 자동 변환
- HTMLResponse : HTML Content 전송
- RedirectResponse : 요청 처리 후 다른 url로 client를 다른 url로 redirect 하기 위해 사용
- PlainTextResponse : 일반 text content 전송
- FileResponse : 파일을 download 하는데 주로 사용
- StreamingResponse : 대용량 파일의 streaming 이나 chat message 등에 사용

## HTTP Status Code 개요

## HTTP Status Code 정리

| Status 계열 | 내용 | 코드 | 설명 |
|-------------|-------|------|------|
| **2xx** | 성공적으로 요청 수행 | **200 OK** | 일반적인 성공 응답 |
|  |  | **201 Created** | 새로운 리소스 생성 성공(POST) |
|  |  | **204 No Content** | 성공했지만 응답 본문 없음 (DELETE 등) |
| **3xx** | Redirection | **301 Moved Permanently** | 요청된 resource가 새로운 url로 영구 이동 |
|  |  | **302 Found** | 일시적 리다이렉션 |
|  |  | **303 See Other** | POST/PUT 이후 다른 GET URL로 이동 지시 |
|  |  | **307 Temporary Redirect** | 일시적 리다이렉션(HTTP 메서드 유지) |
| **4xx** | 클라이언트 오류 | **400 Bad Request** | 요청 형식/파라미터 오류 |
|  |  | **401 Unauthorized** | 인증 실패(토큰 없음/만료) |
|  |  | **404 Not Found** | 요청한 Request 자원 없음 |
|  |  | **405 Method Not Allowed** | 지원하지 않는 HTTP 메서드로 요청함 |
|  |  | **422 Unprocessable Entity** | 요청은 valid but 의미적으로 처리 불가(FastAPI 검증 실패) |
| **5xx** | 서버 오류 | **500 Internal Server Error** | 서버 내부 오류 |
|  |  | **503 Service Unavailable** | 서버 과부하/점검으로 서비스 불가 |
