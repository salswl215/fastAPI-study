## Async DB in SQLAlchemy

### MySQL용 Async DB Driver
- pymysql + aiomysql
    - aiomysql은 pymysql 기반에서 동작하며, native DB Driver의 Async 처리 지원.
    - Connection Pooling 기능 지원

- Async Engine 생성
    - `create_async_engine()` 함수를 사용하여 생성
    - Connection Pooling은 QueuePool을 사용하지 않으며, AsyncAdaptedQueuePool을 사용함

    ```python
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

    engine: AsyncEngine = create_async_engine(DATABASE_CONN, pool_size = 10, max_overflow = 0, pool_recycle = 300)
    ``` 
