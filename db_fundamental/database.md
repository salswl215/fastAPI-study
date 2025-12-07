## Database Handling in FastAPI


### SQL 수행을 위한 Client와 DB 서버 간 주요 프로세스
- Client App (DB Client Driver)
    1) DB Connection 요청
    2) 생성된 Connection을 이용하여 SQL 요청
    3) Cursor에서 결과 데이터 Fetch 요청
    4) Conneciton 종료 요청

- RDBMS
    1) Client의 connection을 위한 세션 생성 및 connection 허용
    2) 해당 SQL이 적절한 SQL인지 확인. SQL을 파싱하여 실행 계획 수립. SQL 수행 후 결과를 반환할 수 있는 Cursor 생성
    3) CUrsor에서 결과 데이터 Fetch 후 Client에 전송
    4) 해당 Connection의 세션을 종료. 세션이 점유한 자원도 같이 정리


### DB 자원 관리를 위한 필수 Client 코드 구성 요소

1. **Connection 관리**
    - DB 연결 생성 및 유지
    - 커넥션 풀 관리
    - idle/stale connection 정리
    - 재연결 및 retry 처리
    - pool 옵션 관리 (pool_size, max_overflow, pool_recycle, pool_pre_ping 등)

2. **Session 관리**
    - 트랜잭션 범위 관리 (Begin, Commit, Rollback)
    - 요청 단위 세션 유지
    - ORM 엔티티 상태 관리
    - context manager 또는 try/except/finally 로 세션 종료 처리

3. **SQL 파싱 및 실행계획 관리**
    - SQL 파싱 및 문법 검증
    - 실행 계획 생성 및 Plan Cache 활용
    - Prepared Statement 활용
    - Parameter binding 사용 (:id, %s, ? 등)
    - 반복 SQL의 문자열 재생성 최소화

4. **데이터 Access & Fetching**
    - fetchone, fetchmany, streaming 조회 방식
    - ORM 매핑 처리
    - Lazy/Eager loading 관리
    - Pagination 및 batch 처리
    - 대용량 조회 시 streaming 방식 사용

5. **Caching Layer**
    - DB 내부 캐시(buffer pool, plan cache)
    - 애플리케이션 캐시(Redis, Memcached, local LRU)
    - read-through, write-through 패턴
    - TTL 기반 캐시 만료 관리

6. **Resource Cleanup**
    - 커넥션 close 또는 pool 반환
    - 세션 종료
    - 트랜잭션 종료 처리
    - idle-in-transaction 방지
    - Connection leak 방지


### Connection Poooling
- Database 서버에서 Connection을 생성하는 작업은 DB 자원을 소모
    - 사용자/패스워드 검증
    - 사용자 권한 확인 및 설정
    - 세션 메모리 할당
- 빈번한 OLTP 성 작업의 요청마다(초당 수십건) DB Connection을 생성하고 종료하는 작업은 많은 자원을 소모하여 안정적인 DB 운영에 큰 영향을 미칠 수 있음
- 일정 수의 Connection을 미리 Pool에서 생성하고, 이를 가져다 sql을 수행 후 Connection을 종료시키지 않고 다시 Pool에 반환하는 기법이 Connection Pooling

