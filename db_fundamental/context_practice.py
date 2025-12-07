from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from db_config import get_database_url

# database connection URL
DATABASE_CONN = get_database_url()

engine = create_engine(DATABASE_CONN, pool_size=10, max_overflow=0)

def context_execute_sleep():
    # with 절 밖으로 나가면 connection close됨
    with engine.connect() as conn:
        query = "select sleep(5)"
        result = conn.execute(text(query))
        result.close()
        #conn.close()

for ind in range(15):
    print("loop index:", ind)
    context_execute_sleep()

print("end of loop")