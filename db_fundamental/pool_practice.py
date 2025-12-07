from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from db_config import get_database_url

# database connection URL
DATABASE_CONN = get_database_url()

# engine = create_engine(DATABASE_CONN)
engine = create_engine(DATABASE_CONN, 
                       #poolclass=NullPool, # Connection Pool 사용하지 않음. 
                       pool_size=5, max_overflow=2
                       )
print("#### engine created")

def direct_execute_sleep(is_close: bool = False):
    conn = engine.connect()
    query = "select sleep(5)"
    result = conn.execute(text(query))
    # rows = result.fetchall()
    # print(rows)
    result.close()

    # 인자로 is_close가 True일 때만 connection close()
    if is_close:
        conn.close()
        print("conn closed")

for ind in range(10):
    print("loop index:", ind)
    direct_execute_sleep(is_close=True)


print("end of loop")

    
