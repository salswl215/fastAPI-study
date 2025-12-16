from sqlalchemy import text
from db.database import direct_get_conn, engine
import asyncio


async def execute_query():
    conn = await direct_get_conn()
    print("conn type:", type(conn))
    query = "select * from blog"
    stmt = text(query)
    # SQL 호출하여 CursorResult 반환.
    # Eventloop에 던져놓고, 결과 반환 전까지 다른 request 처리
    result = await conn.execute(stmt)

    rows = result.fetchall()
    print(rows)
    result.close()
    await conn.rollback()
    await conn.close()
    await engine.dispose()

async def main():
    await execute_query()

if __name__ == "__main__":
    asyncio.run(main())
