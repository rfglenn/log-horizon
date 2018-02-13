from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

	
engine = create_engine('sqlite:///study.db', echo=False)

Session = sessionmaker(bind=engine)

