from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "mysql+pymysql://root:developer@mysql:3306/demo?charset=utf8"
db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base = declarative_base()


def get_db():
    with db_session() as session:
        yield session
