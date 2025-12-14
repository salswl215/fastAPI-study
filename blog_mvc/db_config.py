import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로딩

def get_database_url():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    driver = os.getenv("DB_DRIVER", "mysql+mysqlconnector")

    return f"{driver}://{user}:{password}@{host}:{port}/{dbname}"
