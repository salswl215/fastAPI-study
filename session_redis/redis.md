## FastAPI : Redis Middleware

### 1. Redis 개요
- RAM(메모리)에 데이터 액세스를 빠르게 수행하는 Database(Cache) 솔루션 (메모리(RAM) 기반의 In-Memory Data Store)
- 주로 Key=Value 형태로 다양한 데이터 타입(문자열, Set, List, Hash등)들에 대해 데이터 액세스/수정/삭제/저장 등을 수행
- 메모리의 데이터를 File로 Persistent 저장 가능
- 마이크로 second 단위의 빠른 처리 성능으로 매우 빈번한 데이터 액세스가 발생할 경우 자주 활용
    - Caching: 데이터베이스의 부하를 감소시키기 위해 자주 사용되는 데이터 Caching
    - 사용자 Session: 웹 애플리케이션의 사용자 세션 저장소로 사용
    - 실시간 분석: 실시간으로 데이터 분석을 빠르게 수행


### 2. Redis 특징

#### 2.1 In-Memory 기반 구조
- 모든 데이터를 메모리(RAM)에 저장
- 디스크 기반 DB 대비 매우 빠른 읽기/쓰기 성능 제공
- 평균 응답 속도는 sub-millisecond 수준

#### 2.2 다양한 자료구조 지원
| 자료구조 | 설명 | 활용 예시 |
|--------|------|---------|
| String | 단일 값 저장 | 토큰, 카운터 |
| Hash | 필드-값 구조 | 사용자 정보, Session |
| List | 순서 있는 목록 | Queue |
| Set | 중복 없는 집합 | 태그, 방문자 중복 제거 |
| Sorted Set | 점수 기반 정렬 | 랭킹 시스템 |
| Stream | 로그/이벤트 스트림 | 메시지 큐 |
| Bitmap / HyperLogLog | 비트/통계 구조 | 사용자 통계 |


#### 2.3 Cache/Database 역할
- Cache
    - TTL(Time To Live) 기반 데이터 만료 지원
    - 자주 조회되는 데이터 캐싱
    - 원본 DB 부하 감소

- Database
    - Key 기반 데이터 조회/수정
    - 제한적인 트랜잭션 지원 (MULTI / EXEC)
    - 영속성(Persistence) 옵션 제공


#### 2.4 Redis 영속성(Persistence)
- RDB (Snapshot)
    - 일정 주기로 메모리 상태를 디스크에 저장
    - 빠른 재시작 및 복구 가능
    - Snapshot 시점 이후 데이터 유실 가능


- AOF (Append Only File)
    - 모든 쓰기 명령을 로그로 저장
    - 데이터 안정성이 높음
    - 디스크 I/O 증가
    - 실무에서는 RDB + AOF를 함께 사용하는 경우가 많음


### 3. Redis 아키텍처

#### Single Thread 모델
- 명령 처리 로직은 단일 스레드 기반
- I/O Multiplexing 사용
- Lock 경합이 없어 예측 가능한 성능 제공


#### 메모리 관리 및 Eviction 정책
- 최대 메모리 크기 설정 가능 (`maxmemory`)
- 메모리 초과 시 Eviction 정책 적용

| 정책 | 설명 |
|----|----|
| noeviction | 메모리 초과 시 쓰기 요청 거부 |
| allkeys-lru | 가장 적게 사용된 키 제거 |
| volatile-lru | TTL 설정된 키 중 LRU 제거 |
| volatile-ttl | 만료 시간이 임박한 키 제거 |
