from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from contextlib import contextmanager
from fastapi import status
from fastapi.exceptions import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로딩

def get_database_url():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    driver = os.getenv("DB_ASYNC_DRIVER")

    return f"{driver}://{user}:{password}@{host}:{port}/{dbname}"

# database connection URL
DATABASE_CONN = get_database_url()
print("database_conn:", DATABASE_CONN)

engine: AsyncEngine= create_async_engine(DATABASE_CONN, echo=True,
                       #poolclass=NullPool, # Connection Pool 사용하지 않음. 
                       pool_size=10, max_overflow=0,
                       pool_recycle=300)

async def direct_get_conn():
    conn = None
    try:
        conn = await engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detial = "요청하신 서비스가 잠시 내부적으로 문제가 발생하였습니다.")
    

def context_get_conn():
    conn = None
    try:
        conn = engine.connect()
        yield conn
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detial = "요청하신 서비스가 잠시 내부적으로 문제가 발생하였습니다.")

    finally:
        if conn:
            conn.close()

