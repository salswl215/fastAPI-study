# Cookie


## Stateless Web

- Web은 Client의 HTML 리소스 요청에 대해서 해당 HTML을 빠르고 안정적으로 전달하는 목적을 가지고 설계됨.
- 서버는 개별 Client 접속을 지속적으로 유지하지 않고, 리소스의 전송이 완료되면 Client의 연결을 종료 시킴
    - Client가 개인화된 특정 정보를 서버와 지속적으로 유지할 수 없음(Stateless)
- 웹은 태생이 Stateless(상태 관리를 하지 않음)임. 즉 서버는 연속적인 Transaction으로 특정 Client에게 특화된 정보만을 제공하지 않음.
- 웹이 Enterprise 환경에서 사용되기 위해서는 상태 관리가 필요해 졌고, 이를 위해 `Cookie`가 도입됨
- Cookie가 사용자 특화된 정보를 Brower에 저장하면서 Browser와 서버간 상태관리(인식)이 가능해졌으며, Cookie에서 많은 특화 정보를 가지고 있는 것은 보안상 이슈가 있을 수 있으므로 Browser는 특정 Session 키만 가지고 있고, 서버에서 사용자 특화 정보를 메모리/DB등으로 저장/관리하는 Session 방식이 널리 사용됨.


## Cookie

### Cookie 개념 및 특징

-  Cookie는 개인화된 특정 정보를 Browser와 Server간에 유지하기 위해 만들어짐.
- (사용자의 (Login)등) 요청시에 서버는 Cookie 정보를 Header로 보내주고, Browser는 이 Cookie의 정보를 인식하면서 개별화된 정보를 전달 및 공유
    - 상업용 애플리케이션으로 확장하는데 기폭제 역할을 수행 (개인화/트랙킹)
- 서버는 Header에 Set-Cookie를 설정하며, 여기에 Cookie 이름(key), 값, 만료기한, 도메인등의 정보를 설정하여 Brower로 내려 보내주고, Browser는 이를 Cookie 정보로 저장
- 브라우저는 여러 개의 Cookie들을 가질 수 있으며 개별 Cookie는 고유한 Key값으로 구분되고, Value값을 가질 수 있음. 하나에 최대 4KB까지 저장
    - 보통은 하나의 Cookie에 value값을 하나씩 할당하지 않고, Json같은 포맷으로 여러 개의 별도 정보들을 할당함.
    - 브라우저는 최대 300개까지 Cookie를 저장하되, 하나의 도메인당 최대 20개까지만 허용.


### Cookie와 보안
- Cookie는 태생적으로 보안에 취약함에 따라 Cookie에는 가급적 최소한의 정보를 가지되, 민감정보(패스워드, 주민번호, 전화번호등)를 담지 않아야 함.
- Cookie 정보를 암호화할 수는 있지만, 서버쪽에서 복호화 하는데 시간이 소요되며, 특히나 Cookie 정보는 빈번하게 확인되는데, 이때마다 복호화를 할 경우 서버 자원이 크게 소모되어서 일반적으로 암호화 하지 않음.
- 대신 Cookie에 정보를 담아야 할 경우는 서버가 Cookie를 읽어 들일 때 Cookie 정보가 수정/변조가 되었는지 확인이 가능하도록 Signed Key기반으로 Cookie를 Encoding한 Signed Cookie가 주로 활용됨(복호화 보다 덜 자원 소모). 하지만 Signed Cookie 역시 Cookie 정보를 Decoding 해서 알아낼 수 있음.
- Cookie에 정보 자체는 담지 않고, Cookie를 식별할 Cookie id(session id)만 Cookie로 전송하고, 해당 Cookie id로 가지는 상세 정보는 서버의 DB, Memory, Redis등에 저장하는 Session 메커니즘이 기업에서 가장 많이 활용됨.
- 브라우저와 서버는 보다 안전한 Cookie 활용을 위해 domain, httponly, secure, samesite 등의 다양한 파라미터들을 발전시켜옴.


### Cookie 유형

#### 1. 도메인 구분
- First Party Cookie
    - 사용자가 직접 URL을 입력하여 방문한 사이트에서 발행된 Cookie. Cookie 도메인이 방문한 사이트의 도메인과 동일
    - 사용자 세션 관리 / 개인화 / 사용자 분석

- Third Party Cookie
    - 사용자가 직접 URL을 입력하여 방문한 사이트가 아닌 다른 사이트에서 생성된 Cookie. Cookie 도메인이 직접 방문 사이트의 도메인이 아닌 다른 사이트의 도메인을 가짐
    - 개인화 광고 / 소셜 미디어 통합 / 사용자 분석 솔루션


#### 2. 수명 주기
- Session Cookie
    - 브라우저가 종료되면 사라지는 Cookie 
- Permanent Cookie
    - 브라우저가 종료되어도 사라지지 않고 max age나 expiration에 지정된 시간동안 계속 유지되는 Cookie


### Cookie 주요 Meta Parameters

| 파라미터 | 설명 |
|---------|------|
| max_age | Cookie 유지 시간. 초 단위이며 정수형 값으로 설정.<br>서버에서 Cookie의 `max_age`를 3600으로 설정하면 브라우저는 cookie를 받은 후 3600초까지 유지시키고, 이후에는 삭제함.<br>예: `3600` |
| expires | Cookie를 유지할 일시(일자 + 시분초).<br>`max_age`와 유사하지만, 유지할 **절대 일시**를 설정하며 datetime 형태 또는 문자열을 입력값으로 받음.<br>예: `Wed, 21 Oct 2024 07:28:00 GMT` |
| path | Cookie가 적용되는 서버의 path.<br>Cookie는 해당 서버의 지정된 Path(하위 path 포함)에 접속 시에만 전송됨.<br>예: `/` (전체 path에 전송) |
| domain | Cookie가 유효한 Domain.<br>Cookie는 해당 Domain에 접속 시에만 전송됨.<br>예: `example.com` |
| secure | `true`이면 HTTPS 접속 시에만 Cookie가 전송됨. |
| httponly | `true`이면 JavaScript에서는 cookie에 접근하거나 전송할 수 없도록 함. |
| samesite | Cookie가 Cross-origin(초기 접속과 다른 Origin) 요청 시 전송될지 여부를 설정함.<br><br>**Strict**: 원 접속과 다른 origin에는 Cookie를 전송하지 않음.<br>**Lax**: 기본적으로 Strict와 같으나, 링크 클릭 등 GET 요청의 경우 전송됨.<br>&nbsp;&nbsp;&nbsp;&nbsp;- iframe, image, JavaScript call로는 전송되지 않음.<br>**None**: 서로 다른 Origin이라도 Cookie 전송됨. |
