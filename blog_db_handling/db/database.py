from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from contextlib import contextmanager
from fastapi import status
from fastapi.exceptions import HTTPException
from db_config import get_database_url

# database connection URL
DATABASE_CONN = get_database_url()

engine = create_engine(DATABASE_CONN, #echo=True,
                       #poolclass=NullPool, # Connection Pool 사용하지 않음. 
                       pool_size=10, max_overflow=0,
                       pool_recycle=300)

def direct_get_conn():
    conn = None
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise e
    

def context_get_conn():
    conn = None
    try:
        conn = engine.connect()
        yield conn
    except SQLAlchemyError as e:
        print(e)
        raise e
    finally:
        if conn:
            conn.close()

