import pyodbc
from collections.abc import Generator
import urllib
from sqlalchemy import create_engine, text
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

# database info
server = settings.SERVER_URI
database = settings.DATABASE_NAME
username = settings.DATABASE_USERNAME
password = settings.DATABASE_PASSWORD

driver = pyodbc.drivers()[-1]

# define the connection string to the SQL Server
connection_string = f'Driver={driver};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
connection_string = connection_string.replace('\r', '').replace('\n', '') # for some reason some special charactors are added and causes errors without this line of code.

# connctor engine 
try:
    odbc_connect = urllib.parse.quote_plus(connection_string)
    engine = create_engine('mssql+pyodbc:///?odbc_connect=' + odbc_connect)
    
    # create session which will be used in crud.py
    session_factory = sessionmaker(bind=engine)
except Exception as e:
    logger.info(f"DB connection error. detail={e}")

# Base class which will be used in model.py
# Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """endpointからアクセス時に、Dependで呼び出しdbセッションを生成する
    エラーがなければ、commitする
    エラー時はrollbackし、いずれの場合も最終的にcloseする.
    """
    db = None
    try:
        db = session_factory()
        yield db
        db.commit()
    except Exception:
        if db:
            db.rollback()
    finally:
        if db:
            db.close()

if __name__ == '__main__':
    # connection test
    with engine.connect() as conn:
        rs = conn.execute(text('SELECT @@VERSION as version'))
        for row in rs:
            logger.info(row)